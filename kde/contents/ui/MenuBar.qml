import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3

Item {
    id : topbar
    width : parent.width
    height : parent.height * 0.05

    RowLayout {
        PlasmaComponents3.Button {
            id : fileButton
            text : "File"
            onClicked : menu.open()
            height : topbar.height
            flat : true
            Menu {
                id : menu
                y : fileButton.height
                title : qsTr("File")
                MenuItem {
                    text : qsTr("&New Service")
                    onTriggered : console.log("Open action triggered");
                }
                MenuItem {
                    text : qsTr("Exit")
                    onTriggered : Qt.quit();
                }
            }
        }

        PlasmaComponents3.Button {
            id : viewButton
            text : "View"
            onClicked : menu1.open()
            height : topbar.height
            flat : true
            Menu {
                id : menu1
                y : fileButton.height
                title : qsTr("File")
                MenuItem {
                    text : qsTr("&New Service")
                    onTriggered : console.log("Open action triggered");
                }
                MenuItem {
                    text : qsTr("Exit")
                    onTriggered : Qt.quit();
                }
            }
        }

        PlasmaComponents3.Button {
            id : aboutButton
            text : "About"
            onClicked : menu2.open()
            height : topbar.height
            flat : true
            Menu {
                id : menu2
                y : fileButton.height
                title : qsTr("File")
                MenuItem {
                    text : qsTr("&New Service")
                    onTriggered : console.log("Open action triggered");
                }
                MenuItem {
                    text : qsTr("Exit")
                    onTriggered : Qt.quit();
                }
            }
        }
    }
}
