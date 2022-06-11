import QtQuick 2.0
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.0

import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.components 3.0 as PlasmaComponents3
import Qt.labs.qmlmodels 1.0
import io.thp.pyotherside 1.4

PlasmaComponents3.Page {
    implicitWidth : 80
    Layout.fillHeight : true
    Layout.fillWidth : true
    ListModel {
        id : libraryModel
    }
    TableView {
        id : libraryView
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
        onDoubleClicked : {
            console.log(libraryModel.get(libraryView.currentRow)['service_name']);
            var component = Qt.createComponent("../props_window/PropsWindow.qml");
            var win = component.createObject(root, {
                serviceName: libraryModel.get(libraryView.currentRow)['service_name']
            });
            win.show();
        }
        model : libraryModel
    }

    Python {
        id : python

        Component.onCompleted : {

            addImportPath(Qt.resolvedUrl('/home/yuriy/GTK/SystemdGUI/systemd'));
            // Function to call after python module is loaded
            const processItems = function () {
                python.call('SystemdManager.get_units_list', [], function (result) {
                    var tmpArray = [];
                    for (var i = 0; i < result.length; i++) { // only services unit should remain
                        if (result[i]['0'].toString().endsWith('service')) {
                            tmpArray.push({service_name: result[i]['0'].toString(),
                                load_state: result[i]['1'].toString(),
                                active_state: result[i]['2'].toString()
                            });
                        }
                    }
                    tmpArray.sort((a, b) => a.service_name.localeCompare(b.service_name));
                    tmpArray.forEach(function (item) {
                        libraryModel.append(item);
                    });
                });
            }
            importNames('SystemdManager', ['SystemdManager'], processItems);

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
