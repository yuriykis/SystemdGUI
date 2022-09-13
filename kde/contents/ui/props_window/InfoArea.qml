import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import "../python_api"

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
        language.getLoadedText(),
        language.getPathText(),
        language.getActiveText(),
        language.getMainPIDText()
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
    function obtainUnitDetails() {
        const obtainUnitDetailsPython = function () {
            python.call('SystemdManager.get_unit_details_Unit', [infoArea.serviceName], function (result) {
                infoArea.serviceDescription = python.getattr(result, 'Description').toString();
                infoArea.serviceLoaded = python.getattr(result, 'LoadState').toString();
                if (language.currentLanguage == "Polski" && infoArea.serviceLoaded == "loaded") {
                    infoArea.serviceLoaded = "tak"
                }
                infoArea.servicePath = python.getattr(result, 'FragmentPath').toString();
                infoArea.serviceActive = python.getattr(result, 'ActiveState').toString();
                if (language.currentLanguage == "Polski" && infoArea.serviceActive == "active") {
                    infoArea.serviceActive = "tak"
                }
            });
            python.call('SystemdManager.get_unit_details_Service', [infoArea.serviceName], function (result) {
                infoArea.serviceMainPID = python.getattr(result, 'MainPID').toString();
            });
        }
        python.importNames('SystemdManager', ['SystemdManager'], obtainUnitDetailsPython);
    }
    PythonApi {
        Component.onCompleted : obtainUnitDetails()
    }
}
