import gi
import os

from ServiceAction import ServiceAction
from systemd.ServiceCreator import ServiceCreator

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

from systemd.SystemdManager import SystemdManager
from PropsWindow import PropsWindow
from AddServiceWindow import AddServiceWindow


class MainWindow(Gtk.Window):
    def __init__(self):

        Gtk.init_check()
        super().__init__(title="Systemd GUI")
        self.set_border_width(10)
        self.set_default_size(1000, 500)
        grid = Gtk.Grid()
        scrolledwindow = Gtk.ScrolledWindow()

        self.liststore = Gtk.ListStore(str, str, str)
        self.treeview = Gtk.TreeView(model=self.liststore)
        self.treeview.set_hexpand(True)
        self.treeview.set_vexpand(True)
        scrolledwindow.add(self.treeview)
        grid.attach(scrolledwindow, 0, 0, 1, 1)

        # Add new service button
        add_service_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'assets/green-plus-sign-icon-6.jpg', 25, 25)
        img = Gtk.Image()
        img.set_from_pixbuf(add_service_icon)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        add_new_service_button = Gtk.Button(label="Add service")
        add_new_service_button.connect("clicked",
                                       self.on_add_new_service_clicked)
        add_new_service_button.set_image(img)
        add_new_service_button.set_image_position(Gtk.PositionType.TOP)
        add_new_service_button.set_always_show_image(True)
        box.pack_start(add_new_service_button, False, True, 1)
        grid.attach_next_to(box, scrolledwindow, Gtk.PositionType.RIGHT, 1, 1)

        firstColumnName = Gtk.CellRendererText()
        systemdUnitsNames = Gtk.TreeViewColumn("Service Name",
                                               firstColumnName,
                                               text=0)
        self.treeview.append_column(systemdUnitsNames)

        secondColumnName = Gtk.CellRendererText()
        systemdUnitsStatus = Gtk.TreeViewColumn("Load State",
                                                secondColumnName,
                                                text=1)
        self.treeview.append_column(systemdUnitsStatus)

        thirdColumnName = Gtk.CellRendererText()
        systemdUnitsDescription = Gtk.TreeViewColumn("Active State",
                                                     thirdColumnName,
                                                     text=2)
        self.treeview.append_column(systemdUnitsDescription)

        self.treeview.connect("button-press-event", self.on_double_unit_click)

        self.add(grid)
        self.refresh_services_view()

    def decodeUnit(self, unit):
        return os.path.basename(unit.decode('UTF-8'))

    def decodeTuple(self, tuple):
        return self.decodeUnit(tuple[0]), self.decodeUnit(
            tuple[1]), self.decodeUnit(tuple[2])

    def refresh_services_view(self):
        self.liststore = Gtk.ListStore(str, str, str)
        self.systemdUnitsList = SystemdManager.getUnitsList()

        # only service unit should remain
        self.systemdUnitsList = map(self.decodeTuple, self.systemdUnitsList)

        self.systemdUnitsList = list(
            filter(lambda unit: "service" in unit[0], self.systemdUnitsList))
        self.systemdUnitsList.sort()
        for unit in self.systemdUnitsList:
            serivce_name = unit[0]
            is_loaded_field = unit[1]
            is_active_field = unit[2]

            self.liststore.append(
                [serivce_name, is_loaded_field, is_active_field])
        self.treeview.set_model(self.liststore)

    def on_double_unit_click(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            mouse_x, mouse_y = self.treeview.get_pointer()
            row_number = int(str(widget.get_path_at_pos(mouse_x, mouse_y)[0]))
            clicked_service = self.systemdUnitsList[row_number - 1][0]
            propsWindow = PropsWindow(self, clicked_service)
            propsWindow.run()
            propsWindow.destroy()

    def on_service_action_performed(self, serice_action):
        if (serice_action == ServiceAction.SERVICE_START_OK):
            print("Service started")
        elif (serice_action == ServiceAction.SERVICE_START_FAILED):
            print("Service start failed")
        elif (serice_action == ServiceAction.SERVICE_STOP_OK):
            print("Service stopped")
        elif (serice_action == ServiceAction.SERVICE_STOP_FAILED):
            print("Service stop failed")
        elif (serice_action == ServiceAction.SERVICE_RESTART_OK):
            print("Service restarted")
        elif (serice_action == ServiceAction.SERVICE_RESTART_FAILED):
            print("Service restart failed")
        self.refresh_services_view()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

    def on_add_new_service_clicked(self, button):
        addServiceWindow = AddServiceWindow(self)
        addServiceWindow.run()
        service_name = addServiceWindow.getServiceName()
        service_description = addServiceWindow.getServiceDescription()
        service_extec_start = addServiceWindow.getServiceExecStart()
        service_creator = ServiceCreator()
        service_name = service_creator.createService(service_name,
                                                     service_description,
                                                     service_extec_start)
        SystemdManager.enableUnit(service_name + ".service")
        addServiceWindow.destroy()
        self.refresh_services_view()