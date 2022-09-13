import QtQuick 2.3
import QtQuick.Controls 2.3 as Controls
import QtQuick.Dialogs 1.3
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3


Controls.Dialog {
    id : confirmDialog
    visible : true
    title : language.getConfirmActionText()
    property string actionName
    property string serviceName
    property string functionToCall
    property var caller
    standardButtons : StandardButton.Ok | StandardButton.Cancel
    x : (parent.width - width) / 2
    y : (parent.height - height) / 2

    PlasmaComponents3.Label {
        id : label
        text : language.getAreYouSureToPerfActionText(confirmDialog.actionName.toLowerCase(), confirmDialog.serviceName)
    }
    Component.onCompleted : {
        standardButton(Dialog.Ok).text = language.getOKText();
        standardButton(Dialog.Cancel).text = language.getCancelText();
    }
    onAccepted : {
        caller.performAction(functionToCall)
    }
}
