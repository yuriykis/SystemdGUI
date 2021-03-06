import gi

from Language.Language import Language

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ServicesList(Gtk.ScrolledWindow):

    def __init__(self, main_window, info_text):
        super().__init__()

        self._info_text = info_text
        self.liststore = Gtk.ListStore(str, str, str, str, str)
        self.treeview = Gtk.TreeView(model=self.liststore)
        self.treeview.set_hexpand(True)
        self.treeview.set_vexpand(True)
        self.add(self.treeview)

        firstColumnName = Gtk.CellRendererText()
        self.systemdUnitsColorPoint = Gtk.TreeViewColumn("",
                                                         firstColumnName,
                                                         text=0,
                                                         foreground=4)
        self.treeview.append_column(self.systemdUnitsColorPoint)

        secondColumnName = Gtk.CellRendererText()
        self.systemdUnitsNames = Gtk.TreeViewColumn(
            self._info_text.get_service_name_text(), secondColumnName, text=1)
        self.treeview.append_column(self.systemdUnitsNames)

        thirdColumnName = Gtk.CellRendererText()
        self.systemdUnitsStatus = Gtk.TreeViewColumn(
            self._info_text.get_load_state_text(), thirdColumnName, text=2)
        self.treeview.append_column(self.systemdUnitsStatus)

        forthColumnName = Gtk.CellRendererText()
        self.systemdUnitsDescription = Gtk.TreeViewColumn(
            self._info_text.get_active_state_text(), forthColumnName, text=3)
        self.treeview.append_column(self.systemdUnitsDescription)

        self.treeview.connect("button-press-event",
                              main_window.on_double_unit_click)
        self.tree_selection = self.treeview.get_selection()
        self.tree_selection.connect("changed",
                                    main_window.on_service_selection)
