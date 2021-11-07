import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from SystemdManager import SystemdManager
from ConfirmWindow import ConfirmWindow
from PropsWindow import PropsWindow

class MainWindow(Gtk.Window):

    def __init__(self):
        
        Gtk.init_check()
        super().__init__(title="Systemd GUI")
        self.set_border_width(10)
        self.set_default_size(1000, 500)

        scrolledwindow = Gtk.ScrolledWindow()
        self.add(scrolledwindow)

        self.liststore = Gtk.ListStore(str, str, str)
        treeview = Gtk.TreeView(model=self.liststore)
        self.add(treeview)

        scrolledwindow.add(treeview)
    
        firstColumnName = Gtk.CellRendererText()
        systemdUnitsNames = Gtk.TreeViewColumn("Service Name", firstColumnName, text=0)
        treeview.append_column(systemdUnitsNames)

        secondColumnName = Gtk.CellRendererText()
        systemdUnitsStatus = Gtk.TreeViewColumn("Load State", secondColumnName, text=1)
        treeview.append_column(systemdUnitsStatus)

        thirdColumnName = Gtk.CellRendererText()
        systemdUnitsDescription = Gtk.TreeViewColumn("Active State", thirdColumnName, text=2)
        treeview.append_column(systemdUnitsDescription)

        treeview.connect("button-press-event", self.on_double_unit_click)

        systemdUnitsList = SystemdManager.getUnitsList()

        # only service unit should remain
        def decodeUnit(unit):
            return os.path.basename(unit.decode('UTF-8'))
        def decodeTuple(tuple):
            return decodeUnit(tuple[0]), decodeUnit(tuple[1]), decodeUnit(tuple[2])


        systemdUnitsList = map(decodeTuple, systemdUnitsList)

        systemdUnitsList = filter(lambda unit: "service" in unit[0], systemdUnitsList)

        for unit in systemdUnitsList:
            serivce_name = unit[0]
            is_loaded_field = unit[1]
            is_active_field = unit[2]
            restart_button = Gtk.Button.new_with_label("Restart")
            restart_button.connect("clicked", self.on_restart_clicked)

            self.liststore.append([serivce_name, is_loaded_field, is_active_field])
            

    def on_restart_clicked(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            confirmWindow = ConfirmWindow(self)
            response = confirmWindow.run()

            confirmWindow.destroy()

    def on_double_unit_click(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            propsWindow = PropsWindow(self)
            propsWindow.run()
            propsWindow.destroy()


    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()


