import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3


Dialog {
    id : serviceActionStatusDialog
    visible : true
    title : ""
    property string text

    standardButtons : StandardButton.Ok

    PlasmaComponents3.Label {
        id : serviceActionStatusDialogLabel
        text : ""
    }
    Component.onCompleted : {
        serviceActionStatusDialogLabel.text = text
    }
}
