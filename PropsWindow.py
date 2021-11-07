import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PropsWindow(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Properties", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(150, 100)
        self.set_border_width(10)
        label = Gtk.Label("Properties")
        box = self.get_content_area()
        box.add(label)
        self.show_all()