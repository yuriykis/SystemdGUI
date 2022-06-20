import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import "../python_api"

ApplicationWindow {
    id : root
    visible : true
    title : language.getServiceLogsText()
    width : 900
    height : 500
    property string serviceName

    PlasmaComponents3.ScrollView {
        id : scrollView
        anchors.fill : parent
        property string serviceLogs
        PlasmaComponents3.TextArea {
            anchors.fill : parent
            text : scrollView.serviceLogs
        }
    }

    function obtainServiceLogs() {
        const obtainUnitLogs = function () {
            python.call('SystemdManager.get_service_logs', [root.serviceName], function (result) {
                scrollView.serviceLogs = result;
            });
        }
        python.importNames('SystemdManager', ['SystemdManager'], obtainUnitLogs);
    }
    PythonApi {
        Component.onCompleted : obtainServiceLogs()
    }
}
