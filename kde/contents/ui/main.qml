// import related modules
import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3

// window containing the application
ApplicationWindow {

    visible : true

    // title of the application
    title : qsTr("SystemdGUI")
    width : 800
    height : 600

    menuBar : MenuBar {}

    ColumnLayout {
        spacing : 0
        anchors.fill : parent

        RowLayout {
            spacing : 0
            Layout.preferredHeight : 200
            ContentArea {}

            ActionsBar {}
        }
    }

}
