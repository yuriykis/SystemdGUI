import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3
import "../python_api"

PlasmaComponents3.Button {
    id : removeServiceButton
    icon.name : "package-remove"
    text : language.getRemoveServiceText()
    height : parent.height * 0.1
    width : parent.width
    property string serviceName
    onClicked : {
        serviceName = root.getCurrentService();
        showConfirmDialog(serviceName);
    }
    function performAction() {
        removeService();
    }
    function removeService() {
        const removeServicePython = function () {
            python.call('SystemdManager.remove_unit', [serviceName], function (res) {
                python.call('str', [res], function (result) {
                    if (result == "ServiceAction.SERVICE_REMOVE_OK") {
                        showServiceActionStatusDialog("Info", language.getServiceRemovedSuccessfullyText());
                        contentArea.loadUnitsList();
                    } else {
                        showServiceActionStatusDialog(language.getErrorText(), result[1]);
                    }
                });
            });
        }
        python.importNames('SystemdManager', ['SystemdManager'], removeServicePython);
    }
    function showServiceActionStatusDialog(title, text) {
        var component = Qt.createComponent("../service_action_dialog/ServiceActionStatusDialog.qml");
        var dialog = component.createObject(root, {
            title: title,
            text: text
        });
    }
    function showConfirmDialog() {
        var component = Qt.createComponent("../confirm_dialog/ConfirmDialog.qml");
        var dialog = component.createObject(root, {
            actionName: "Remove",
            serviceName: serviceName,
            caller: removeServiceButton
        });
    }
    PythonApi {
        id : python
    }
}
