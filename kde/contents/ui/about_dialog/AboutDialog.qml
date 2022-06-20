import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import org.kde.plasma.components 3.0 as PlasmaComponents3

Dialog {
    id : aboutDialog
    visible : true
    title : "About Systemd GUI"
    width : 300

    Column {
        width : parent.width
        spacing : 10
        PlasmaComponents3.Label {
            anchors.horizontalCenter : parent.horizontalCenter
            text : i18n("<b>Systemd GUI</b>")
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter : parent.horizontalCenter
            text : i18n("1.0")
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter : parent.horizontalCenter
            text : i18n("Graphical User Interface for Systemd")
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter : parent.horizontalCenter
            text : i18n("<a href='https://github.com/yuriykis/SystemdGUI.git'>SystemdGUI</a>")
            onLinkActivated : Qt.openUrlExternally(link)
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter : parent.horizontalCenter
            text : i18n("Copyright © 2022")
        }

        PlasmaComponents3.Label {
            anchors.horizontalCenter : parent.horizontalCenter
            text : i18n("Author: Yuriy Kis")
        }
    }


}
