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

        service_name_label = Gtk.Label(serviceName, xalign=2)
        box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box1.pack_start(service_name_label, True, True, 0)

        unit_details = SystemdManager.getUnitDetails(serviceName)
        main_area.pack_start(box1, True, True, 0)

        box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        restart_button = Gtk.Button.new_with_label("Restart")
        edit_config_file_button = Gtk.Button.new_with_label("Edit config file")
        edit_config_file_button.connect("clicked",
                                        self.on_edit_config_file_clicked)
        restart_button.connect("clicked", self.on_restart_clicked)
        box2.pack_start(restart_button, True, True, 0)
        box2.pack_start(edit_config_file_button, True, True, 0)
        main_area.pack_end(box2, True, True, 0)

        self.show_all()

    def on_restart_clicked(self, widget):
        confirmWindow = ConfirmWindow(self)
        response = confirmWindow.run()

        confirmWindow.destroy()

    def on_edit_config_file_clicked(self, widget):
        pass
