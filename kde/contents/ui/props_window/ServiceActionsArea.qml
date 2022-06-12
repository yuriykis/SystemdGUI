import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import io.thp.pyotherside 1.4

PlasmaComponents3.Page {
    id : serviceActionsArea
    implicitWidth : 30
    Layout.fillHeight : true
    Layout.fillWidth : true
    property string serviceName
    property var serviceActions: [
        "Start",
        "Stop",
        "Restart",
        "Edit config file",
        "Show logs"
    ]
    Column {
        topPadding : 10
        width : parent.width
        Repeater {
            model : serviceActionsArea.serviceActions
            delegate : ServiceActionButton {
                text : modelData
                serviceName : serviceActionsArea.serviceName
            }
        }
    }
}
