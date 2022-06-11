import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3

PlasmaComponents3.Page {
    implicitWidth : 20
    Layout.fillHeight : true
    Layout.fillWidth : true
    Column {
        PlasmaComponents3.ToolButton {
            icon.name : "package-install"
            text : i18n("Add new service")
        }
        PlasmaComponents3.ToolButton {
            icon.name : "package-remove"
            text : i18n("Remove service")
        }
        PlasmaComponents3.ToolButton {
            icon.name : "package-reinstall"
            text : i18n("Reload list of services")
        }
    }
}
