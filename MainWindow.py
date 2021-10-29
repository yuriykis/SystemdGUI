import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from SystemdManager import SystemdManager

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
            return os.path.basename(unit[0].decode('UTF-8')), os.path.basename(unit[1].decode('UTF-8'))

        systemdUnitsList = map(decodeUnit, systemdUnitsList)

        systemdUnitsList = filter(lambda unit: "service" in unit[0], systemdUnitsList)

        for unit in systemdUnitsList:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            label1 = Gtk.Label(label=unit[0], xalign=0)
            label2 = Gtk.Label(label=unit[1], xalign=0)
            label3 = Gtk.Button.new_with_label("Restart")
            hbox.pack_start(label1, True, True, 0)
            hbox.pack_start(label2, False, True, 0)
            hbox.pack_start(label3, False, True, 0)
            lbox.add(row)

    def on_click_me_clicked(self, button):
        print('"Click me" button was clicked')

    def on_open_clicked(self, button):
        print('"Open" button was clicked')

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()


