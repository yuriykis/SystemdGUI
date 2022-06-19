import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2

MessageDialog {
    id : fieldsEmptyErrorDialog
    visible : true
    title : "Error"
    text : "Fields cannot be empty"
    width : 300
}
