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

    Row {
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
                    onTriggered : showAddServiceDialog();
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
                title : qsTr("View")
                MenuItem {
                    text : qsTr("&Language")
                    enabled : false
                    onTriggered : console.log("Open action triggered");
                }
                MenuItem {
                    PlasmaComponents3.RadioButton {
                        text : i18n("Polski")
                        checked : false
                        autoExclusive : true
                        padding : 5
                        ButtonGroup.group : radioGroup
                    }
                }
                MenuItem {
                    PlasmaComponents3.RadioButton {
                        text : i18n("English")
                        checked : true
                        autoExclusive : true
                        padding : 5
                        ButtonGroup.group : radioGroup
                    }
                }
            }
            ButtonGroup {
                id : radioGroup
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
                title : qsTr("About")
                MenuItem {
                    text : qsTr("&View program info")
                    onTriggered : showAboutProgramDialog();
                }
            }
        }
    }

    function showAddServiceDialog() {
        var component = Qt.createComponent("../add_service_window/AddServiceWindow.qml");
        var dialog = component.createObject(root, {});
    }
    function showAboutProgramDialog() {
        var component = Qt.createComponent("../about_dialog/AboutDialog.qml");
        var dialog = component.createObject(root, {});
    }
}
