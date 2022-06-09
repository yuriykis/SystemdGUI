import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3

Item {
    implicitWidth : 20
    Layout.fillHeight : true
    Layout.fillWidth : true
    ColumnLayout {
        PlasmaComponents3.ToolButton {
            icon.name : "view-refresh-symbolic"
            text : i18n("Refresh")
        }
        PlasmaComponents3.ToolButton {
            icon.name : "view-refresh-symbolic"
            text : i18n("Refresh")
        }
        PlasmaComponents3.ToolButton {
            icon.name : "view-refresh-symbolic"
            text : i18n("Refresh")
        }
    }
}
