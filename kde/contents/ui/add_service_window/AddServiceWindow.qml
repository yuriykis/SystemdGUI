import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import "../python_api"

Dialog {
    id : addServiceDialog
    visible : true
    title : language.getAddServiceText()
    width : 300
    standardButtons : StandardButton.Ok | StandardButton.Cancel
    property double firstColumnWidthPercent : 0.35

    Column {
        spacing : 5
        width : parent.width
        ServiceField {
            id : serviceNameField
            fieldName : language.getServiceNameText()
        }
        PlasmaComponents3.Label {
            topPadding : 5
            text : "[Unit]"
            width : parent.width * firstColumnWidthPercent
        }
        ServiceField {
            id : serviceDescriptionField
            fieldName : language.getServiceDescriptionText()
        }
        PlasmaComponents3.Label {
            topPadding : 5
            text : "[Service]"
            width : parent.width * firstColumnWidthPercent
        }
        ServiceField {
            id : serviceTypeField
            fieldName : language.getTypeText()
        }
        ServiceField {
            id : serviceExecStartField
            fieldName : language.getExecStartText()
        }
        PlasmaComponents3.Label {
            topPadding : 5
            text : "[Install]"
            width : parent.width * firstColumnWidthPercent
        }
        ServiceField {
            id : serviceWantedByField
            fieldName : language.getWantedByText()
        }
    }
    function createNewService(serviceName, serviceDescription, serviceExecStart) {
        if (serviceName == "" || serviceDescription == "" || serviceExecStart == "") {
            var component = Qt.createComponent("EmptyFieldErrorDialog.qml");
            var dialog = component.createObject(root, {});
            return;
        }
        const createNewServicePython = function () {
            python.call('ServiceCreator.create_service', [
                serviceName, serviceDescription, serviceExecStart
            ], function (result) {
                if (result[0].toString() == "true") {
                    showServiceActionStatusDialog("Info", language.getServiceCreatedSuccessfullyText());
                    root.reloadServices();
                } else {
                    showServiceActionStatusDialog(language.getErrorText(), result[1]);
                    root.reloadServices();
                }
            });
        }
        python.importNames('ServiceCreator', ['ServiceCreator'], createNewServicePython);
    }
    function showServiceActionStatusDialog(title, text) {
        var component = Qt.createComponent("../service_action_dialog/ServiceActionStatusDialog.qml");
        var dialog = component.createObject(root, {
            title: title,
            text: text
        });
    }
    onAccepted : {
        createNewService(serviceNameField.fieldText, serviceDescriptionField.fieldText, serviceExecStartField.fieldText);
        addServiceDialog.visible = false
    }
    PythonApi {
        id : python
    }
}
