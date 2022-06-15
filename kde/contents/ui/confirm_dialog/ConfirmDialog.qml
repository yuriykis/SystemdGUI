import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3


Dialog {
    id : confirmDialog
    visible : true
    title : "Confirm Action"
    property string actionName
    property string serviceName
    property string functionToCall
    standardButtons : StandardButton.Ok | StandardButton.Cancel

    PlasmaComponents3.Label {
        id : label
        text : "Are you sure you want to " + confirmDialog.actionName.toLowerCase() + " " + confirmDialog.serviceName + "?"
    }

    onAccepted : serviceActionButton.performAction(functionToCall)
}
