import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from ConfirmWindow import ConfirmWindow


class PropsWindow(Gtk.Dialog):
    def __init__(self, parent, serviceName):
        Gtk.Dialog.__init__(self, "Properties", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(150, 100)
        self.set_border_width(10)
        label = Gtk.Label(serviceName)
        box = self.get_content_area()
        box.add(label)
        restart_button = Gtk.Button.new_with_label("Restart")
        restart_button.connect("clicked", self.on_restart_clicked)
        self.show_all()

    def on_restart_clicked(self, widget, event):
        confirmWindow = ConfirmWindow(self)
        response = confirmWindow.run()

        confirmWindow.destroy()
