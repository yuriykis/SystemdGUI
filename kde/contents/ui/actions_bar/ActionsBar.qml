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
        anchors.fill : parent
        spacing : 5
        AddNewServiceButton {}
        RemoveServiceButton {}
        ReloadServicesButton {}
    }
}
