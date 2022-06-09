import QtQuick 2.0
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.0

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import io.thp.pyotherside 1.4

Item {
    implicitWidth : 80
    Layout.fillHeight : true
    Layout.fillWidth : true
    ListModel {
        id : libraryModel
    }
    TableView {
        anchors.fill : parent
        TableViewColumn {
            role : "service_name"
            title : "Service Name"
            width : 300
        }
        TableViewColumn {
            role : "load_state"
            title : "Load State"
            width : 100
        }
        TableViewColumn {
            role : "active_state"
            title : "Active State"
            width : 100
        }
        model : libraryModel
    }

    Python {
        id : python

        Component.onCompleted : { // Print version of plugin and Python interpreter
            console.log('PyOtherSide version: ' + pluginVersion());
            console.log('Python version: ' + pythonVersion());

            addImportPath(Qt.resolvedUrl('.'));
            // Asynchronous module importing
            importModule('systemd.SystemdManager', function () {
                console.log('Python module "systemd" is now imported');
                python.call('systemd.SystemdManager.SystemdManager.get_units_list', [], function (result) { // Load the received data into the list model
                    for (var i = 0; i < result.length; i++) { // console.log(result[i]['0'].toString());
                        libraryModel.append({service_name: result[i]['0'].toString(),
                            load_state: result[i]['1'].toString(),
                            active_state: result[i]['2'].toString()
                        });
                    }
                });
            });

        }

        onError : { // when an exception is raised, this error handler will be called
            console.log('python error: ' + traceback);
        }

        onReceived : {
            // asychronous messages from Python arrive here
            // in Python, this can be accomplished via pyotherside.send()
            console.log('got message from python: ' + data);
        }
    }
}
