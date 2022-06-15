import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import io.thp.pyotherside 1.4
Python {
    id : python

    Component.onCompleted : {
        addImportPath(Qt.resolvedUrl('/home/yuriy/GTK/SystemdGUI/systemd'));
    }
    onError : {
        console.log('python error: ' + traceback);
    }

    onReceived : {
        console.log('got message from python: ' + data);
    }
}
