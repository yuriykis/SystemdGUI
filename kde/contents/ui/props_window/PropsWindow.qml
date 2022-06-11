import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3

ApplicationWindow {
    id : root
    title : "Service Properties"
    width : 600
    height : 400
    visible : true
    property string serviceName
    ColumnLayout {
        anchors.fill : parent

        RowLayout {
            Layout.preferredHeight : 200
            InfoArea {
                serviceName : root.serviceName
            }
            ServiceActionsArea {
                serviceName : root.serviceName
            }
        }
    }
}
