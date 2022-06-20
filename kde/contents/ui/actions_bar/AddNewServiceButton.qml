import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3

PlasmaComponents3.Button {
    icon.name : "package-install"
    text : language.getAddServiceText()
    height : parent.height * 0.1
    width : parent.width
    onClicked : {
        showAddServiceDialog()
    }

    function showAddServiceDialog() {
        var component = Qt.createComponent("../add_service_window/AddServiceWindow.qml");
        var dialog = component.createObject(root, {});
    }
}
