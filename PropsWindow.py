import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from ConfirmWindow import ConfirmWindow
from SystemdManager import SystemdManager


class PropsWindow(Gtk.Dialog):
    def __init__(self, parent, serviceName):
        Gtk.Dialog.__init__(self, "Service Properties", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(600, 400)
        self.set_border_width(10)
        content_area = self.get_content_area()
        main_area = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        content_area.add(main_area)

        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        service_name_label = Gtk.Label(xalign=2)
        service_name_label.set_markup("<big>" + serviceName + "</big>")
        vbox_left.pack_start(service_name_label, False, True, 10)

        unit_details = SystemdManager.getUnitDetails(serviceName).Unit
        service_details = SystemdManager.getUnitDetails(serviceName).Service

        serice_description_label = Gtk.Label(
            unit_details.Description.decode('UTF-8'), xalign=0)
        vbox_left.pack_start(serice_description_label, True, True, 0)

        is_service_loaded_label = Gtk.Label(xalign=0)
        is_service_loaded_label.set_markup(
            "<b>Loaded:</b> " + unit_details.LoadState.decode('UTF-8'))
        vbox_left.pack_start(is_service_loaded_label, True, True, 0)

        fragment_path_label = Gtk.Label(xalign=0)
        fragment_path_label.set_markup(
            "<b>Path:</b> " + unit_details.FragmentPath.decode('UTF-8'))
        vbox_left.pack_start(fragment_path_label, True, True, 0)

        is_service_active_label = Gtk.Label(xalign=0)
        is_service_active_label.set_markup(
            "<b>Active:</b> " + unit_details.ActiveState.decode('UTF-8'))
        vbox_left.pack_start(is_service_active_label, True, True, 0)

        main_pid_label = Gtk.Label(xalign=0)
        main_pid_label.set_markup("<b>Main PID:</b> " +
                                  str(service_details.MainPID))
        vbox_left.pack_start(main_pid_label, True, True, 0)
        main_area.pack_start(vbox_left, True, True, 0)

        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        restart_button = Gtk.Button.new_with_label("Restart")
        restart_button.connect("clicked", self.on_restart_clicked)
        stop_button = Gtk.Button.new_with_label("Stop")
        stop_button.connect("clicked", self.on_stop_clicked)
        edit_config_file_button = Gtk.Button.new_with_label("Edit config file")
        edit_config_file_button.connect("clicked",
                                        self.on_edit_config_file_clicked)
        vbox_right.pack_start(restart_button, True, True, 0)
        vbox_right.pack_start(stop_button, True, True, 0)
        vbox_right.pack_start(edit_config_file_button, True, True, 0)
        main_area.pack_end(vbox_right, True, True, 0)

        self.show_all()

    def on_restart_clicked(self, widget):
        confirmWindow = ConfirmWindow(self)
        response = confirmWindow.run()

        confirmWindow.destroy()

    def on_stop_clicked(self, widget):
        confirmWindow = ConfirmWindow(self)
        response = confirmWindow.run()

        confirmWindow.destroy()

    def on_edit_config_file_clicked(self, widget):
        pass
