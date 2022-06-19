import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3


Row {
    spacing : 15
    width : parent.width
    property string fieldName
    property string fieldText
    PlasmaComponents3.Label {
        topPadding : 5
        text : fieldName
        width : parent.width * addServiceDialog.firstColumnWidthPercent
    }
    PlasmaComponents3.TextField {
        placeholderText : qsTr(fieldName)
        onTextEdited : {
            parent.fieldText = text
        }
    }
}
