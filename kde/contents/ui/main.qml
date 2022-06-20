// import related modules
import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import "menu_bar"
import "actions_bar"
import "content_area"
import "language"

ApplicationWindow {
    id : root
    visible : true

    title : qsTr("SystemdGUI")
    width : 800
    height : 600

    menuBar : MenuBar {}

    ColumnLayout {
        anchors.fill : parent

        RowLayout {

            Layout.preferredHeight : 200
            ContentArea {
                id : contentArea
            }

            ActionsBar {}
        }
    }
    function reloadServices() {
        contentArea.loadUnitsList();
    }

    function getCurrentService() {
        return contentArea.getCurrentlySelectedServiceName();
    }
    Language {
        id : language
    }
}
