import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3
import "../python_api"

PlasmaComponents3.Button {
    icon.name : "package-remove"
    text : i18n("Remove service")
    height : parent.height * 0.1
    width : parent.width
    property string serviceName
    onClicked : {
        serviceName = root.getCurrentService();
        removeService();
    }
    function removeService() {
        const removeServicePython = function () {
            python.call('SystemdManager.remove_unit', [serviceName], function (res) {
                python.call('str', [res], function (result) {
                    if (result == "ServiceAction.SERVICE_REMOVE_OK") {
                        showServiceActionStatusDialog("Info", "Service removed successfully");
                        contentArea.loadUnitsList();
                    } else {
                        showServiceActionStatusDialog("Error", result[1]);
                    }
                });
            });
        }
        python.importNames('ServiceCreator', ['ServiceCreator'], removeServicePython);
    }
    function showServiceActionStatusDialog(title, text) {
        var component = Qt.createComponent("../service_action_dialog/ServiceActionStatusDialog.qml");
        var dialog = component.createObject(root, {
            title: title,
            text: text
        });
    }
    PythonApi {
        id : python
    }
}
