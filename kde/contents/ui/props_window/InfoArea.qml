import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import io.thp.pyotherside 1.4

Item {
    implicitWidth : 70
    Layout.fillHeight : true
    Layout.fillWidth : true
    id : infoArea
    property string serviceName
    property string serviceDescription
    property string serviceLoaded
    property string servicePath
    property string serviceActive
    property string serviceMainPID
    property var viewServiceInfoTexts: [
        "",
        "Loaded:",
        "Path:",
        "Active:",
        "Main PID:"
    ]

    Column {
        padding : 10
        PlasmaExtras.Heading {
            topPadding : 0
            leftPadding : 60
            bottomPadding : 10
            level : 1
            text : infoArea.serviceName
        }
        Repeater {
            id : infoAreaRepeater
            model : [
                infoArea.serviceDescription,
                infoArea.serviceLoaded,
                infoArea.servicePath,
                infoArea.serviceActive,
                infoArea.serviceMainPID
            ]
            delegate : PlasmaExtras.Heading {
                topPadding : 10
                level : 6
                text : i18n("<b>" + infoArea.viewServiceInfoTexts[index] + "</b>" + " " + modelData)
            }
        }
    }
    Python {
        id : python

        Component.onCompleted : {
            addImportPath(Qt.resolvedUrl('/home/yuriy/GTK/SystemdGUI/systemd'));
            const obtainUnitDetails = function () {
                python.call('SystemdManager.get_unit_details_Unit', [infoArea.serviceName], function (result) {
                    infoArea.serviceDescription = getattr(result, 'Description').toString();
                    infoArea.serviceLoaded = getattr(result, 'LoadState').toString();
                    infoArea.servicePath = getattr(result, 'FragmentPath').toString();
                    infoArea.serviceActive = getattr(result, 'ActiveState').toString();
                });
                python.call('SystemdManager.get_unit_details_Service', [infoArea.serviceName], function (result) {
                    infoArea.serviceMainPID = getattr(result, 'MainPID').toString();
                });
            }
            importNames('SystemdManager', ['SystemdManager'], obtainUnitDetails);
        }

        onError : {
            console.log('python error: ' + traceback);
        }

        onReceived : {
            console.log('got message from python: ' + data);
        }
    }
}
