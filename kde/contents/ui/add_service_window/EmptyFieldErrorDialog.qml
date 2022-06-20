import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2

MessageDialog {
    id : fieldsEmptyErrorDialog
    visible : true
    title : language.getErrorText()
    text : language.getFieldsCannotBeEmptyText()
    width : 300
}
