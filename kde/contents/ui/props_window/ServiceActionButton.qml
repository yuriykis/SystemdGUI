import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import io.thp.pyotherside 1.4

PlasmaComponents3.Button {
    id : serviceActionButton
    width : parent.width
    property int buttonsInset : 5
    property string functionToCall
    property string serviceName
    topInset : buttonsInset
    bottomInset : buttonsInset
    rightInset : buttonsInset

    Component.onCompleted : {
        if (serviceActionButton.text == "Start") {
            serviceActionButton.functionToCall = "start_unit";
        } else if (serviceActionButton.text == "Stop") {
            serviceActionButton.functionToCall = "stop_unit";
        } else if (serviceActionButton.text == "Restart") {
            serviceActionButton.functionToCall = "restart_unit";
        } else if (serviceActionButton.text == "Edit config file") {
            serviceActionButton.functionToCall = "edit_config_file";
        } else if (serviceActionButton.text == "Show logs") {
            serviceActionButton.functionToCall = "show_logs";
        }
    }
    onClicked : { // test
        var component = Qt.createComponent("../confirm_dialog/ConfirmDialog.qml");
        var dialog = component.createObject(root, {});
        const obtainUnitDetails = function () {
            python.call('SystemdManager.remove_unit', [serviceActionButton.serviceName], function (result) {});
        }
        python.importNames('SystemdManager', ['SystemdManager'], obtainUnitDetails);
    }

    Python {
        id : python

        Component.onCompleted : {
            addImportPath(Qt.resolvedUrl('/home/yuriy/GTK/SystemdGUI/systemd'));
        }
        onError : {
            console.log('python error: ' + traceback);
        }

        onReceived : {
            console.log('got message from python: ' + data);
        }
    }
}
