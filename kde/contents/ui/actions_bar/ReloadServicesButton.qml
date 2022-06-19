import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQml.Models 2.1
import QtQuick.Layouts 1.0
import org.kde.plasma.components 3.0 as PlasmaComponents3


PlasmaComponents3.Button {
    icon.name : "package-reinstall"
    text : i18n("Reload list of services")
    height : parent.height * 0.1
    width : parent.width

    onClicked : {
        root.reloadServices();
    }
}
