import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from SystemdManager import SystemdManager
from ConfirmWindow import ConfirmWindow

class MainWindow(Gtk.Window):

    def __init__(self):
        
        Gtk.init_check()
        super().__init__(title="Systemd GUI")
        self.set_border_width(10)
        self.set_default_size(1000, 500)

        scrolledwindow = Gtk.ScrolledWindow()
        self.add(scrolledwindow)
        
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        scrolledwindow.add(box_outer)

        lbox = Gtk.ListBox()
        lbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(lbox, True, True, 0)

        systemdUnitsList = SystemdManager.getUnitsList()

        # only service unit should remain
        def decodeUnit(unit):
            return os.path.basename(unit.decode('UTF-8'))
        def decodeTuple(tuple):
            return decodeUnit(tuple[0]), decodeUnit(tuple[1]), decodeUnit(tuple[2])


        systemdUnitsList = map(decodeTuple, systemdUnitsList)

        systemdUnitsList = filter(lambda unit: "service" in unit[0], systemdUnitsList)

        for unit in systemdUnitsList:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            serivce_name = Gtk.Label(label=unit[0], xalign=0)
            is_loaded_button = Gtk.Label(label=unit[1], xalign=0)
            is_active_button = Gtk.Label(label=unit[2], xalign=0)
            restart_button = Gtk.Button.new_with_label("Restart")
            restart_button.connect("clicked", self.on_restart_clicked)

            hbox.pack_start(serivce_name, True, True, 0)
            hbox.pack_start(is_loaded_button, False, True, 0)
            hbox.pack_start(is_active_button, False, True, 0)
            hbox.pack_start(restart_button, False, True, 0)
            lbox.add(row)

    def on_restart_clicked(self, button):
        confirmWindow = ConfirmWindow(self)
        response = confirmWindow.run()

        confirmWindow.destroy()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()


