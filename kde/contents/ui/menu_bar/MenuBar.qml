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
            text : language.getFileText()
            onClicked : fileMenu.open()
            height : topbar.height
            flat : true
            Menu {
                id : fileMenu
                y : fileButton.height
                title : language.getFileText()
                MenuItem {
                    text : language.getNewServiceText()
                    onTriggered : showAddServiceDialog();
                }
                MenuItem {
                    text : language.getExitText()
                    onTriggered : Qt.quit();
                }
            }
        }

        PlasmaComponents3.Button {
            id : viewButton
            text : language.getViewText()
            onClicked : viewMenu.open()
            height : topbar.height
            flat : true
            Menu {
                id : viewMenu
                y : fileButton.height
                title : language.getViewText()
                MenuItem {
                    text : language.getLanguageText()
                    enabled : false
                }
                Repeater {
                    model : language.availableLanguages
                    delegate : MenuItem {
                        PlasmaComponents3.RadioButton {
                            text : language.availableLanguages[index]
                            checked : language.currentLanguage == language.availableLanguages[index]
                            autoExclusive : true
                            padding : 5
                            ButtonGroup.group : radioGroup
                            onClicked : language.setCurrentLanguage(language.availableLanguages[index])
                        }
                    }
                }
            }
            ButtonGroup {
                id : radioGroup
            }
        }

        PlasmaComponents3.Button {
            id : aboutButton
            text : language.getAboutText()
            onClicked : aboutMenu.open()
            height : topbar.height
            flat : true
            Menu {
                id : aboutMenu
                y : fileButton.height
                title : language.getAboutText()
                MenuItem {
                    text : language.getViewProgramInfoText()
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
