import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class AddServiceWindow(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title="Add Service", parent=parent)
        self.set_border_width(10)

        self.whole_screen = Gtk.Box(spacing=6)
        self.whole_screen.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.whole_screen)

        self.top_box = Gtk.Box(spacing=6)
        self.label1 = Gtk.Label("Service Name:")
        self.entry1 = Gtk.Entry()
        self.top_box.pack_start(self.label1, True, True, 0)
        self.top_box.pack_start(self.entry1, True, True, 0)
        self.whole_screen.pack_start(self.top_box, True, True, 0)

        self.middle_box = Gtk.Box(spacing=6)
        self.label2 = Gtk.Label("Service Description:")
        self.entry2 = Gtk.Entry()
        self.middle_box.pack_start(self.label2, True, True, 0)
        self.middle_box.pack_start(self.entry2, True, True, 0)

        self.whole_screen.pack_start(self.middle_box, True, True, 0)

        self.bottom_box = Gtk.Box(spacing=6)
        self.label3 = Gtk.Label("Service URL:")
        self.entry3 = Gtk.Entry()
        self.bottom_box.pack_start(self.label3, True, True, 0)
        self.bottom_box.pack_start(self.entry3, True, True, 0)
        self.whole_screen.pack_start(self.bottom_box, True, True, 0)

        self.button1 = Gtk.Button(label="Add Service")
        self.whole_screen.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Close")
        self.whole_screen.pack_start(self.button2, True, True, 0)

        self.show_all()
