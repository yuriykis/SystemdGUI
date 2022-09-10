import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3

PlasmaComponents3.Button {
    id : serviceActionButton
    width : parent.width
    property int buttonsInset : 5
    property string serviceName
    topInset : buttonsInset
    bottomInset : buttonsInset
    rightInset : buttonsInset

    onClicked : {
        if (serviceActionButton.text == language.getStartText()) {
            showConfirmDialog('start_unit');
        } else if (serviceActionButton.text == language.getStopText()) {
            showConfirmDialog('stop_unit');
        } else if (serviceActionButton.text == language.getRestartText()) {
            showConfirmDialog('restart_unit');
        } else if (serviceActionButton.text == language.getEditConfigFileText()) {
            console.log("Edit config file is not implemented yet")
        } else if (serviceActionButton.text == language.getShowLogsText()) {
            showLogsWindow();
        }
    }
    function showConfirmDialog(functionToCall) {
        var component = Qt.createComponent("../confirm_dialog/ConfirmDialog.qml");
        var dialog = component.createObject(root, {
            actionName: serviceActionButton.text,
            serviceName: serviceActionButton.serviceName,
            functionToCall: functionToCall,
            caller: serviceActionButton
        });
    }
    function showLogsWindow() {
        var component = Qt.createComponent("../logs_window/LogsWindow.qml");
        var logsWindow = component.createObject(root, {serviceName: serviceActionButton.serviceName});
        logsWindow.show();
    }
    function performAction(functionToCall) {
        const obtainUnitDetails = function () {
            python.call('SystemdManager.' + functionToCall, [serviceActionButton.serviceName], function (result) {});
        }
        python.importNames('SystemdManager', ['SystemdManager'], obtainUnitDetails);
        contentArea.loadUnitsList();
    }
}
