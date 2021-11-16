import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class AddServiceWindow(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Add Service", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(300, 100)
        self.set_border_width(10)

        content_area = self.get_content_area()
        self.whole_screen = Gtk.Box(spacing=6)
        self.whole_screen.set_orientation(Gtk.Orientation.VERTICAL)
        content_area.add(self.whole_screen)

        self.top_box = Gtk.Box(spacing=6)
        self.label1 = Gtk.Label("Service Name:")
        self.entry1 = Gtk.Entry()
        self.top_box.pack_start(self.label1, False, True, 0)
        self.top_box.pack_end(self.entry1, False, True, 0)
        self.whole_screen.pack_start(self.top_box, True, True, 0)

        self.middle_box = Gtk.Box(spacing=6)
        self.label2 = Gtk.Label("Service Description:")
        self.entry2 = Gtk.Entry()
        self.middle_box.pack_start(self.label2, False, True, 0)
        self.middle_box.pack_end(self.entry2, False, True, 0)

        self.whole_screen.pack_start(self.middle_box, True, True, 0)

        self.bottom_box = Gtk.Box(spacing=6)
        self.label3 = Gtk.Label("Service URL:")
        self.entry3 = Gtk.Entry()
        self.bottom_box.pack_start(self.label3, False, True, 0)
        self.bottom_box.pack_end(self.entry3, False, True, 0)
        self.whole_screen.pack_start(self.bottom_box, True, True, 0)

        self.show_all()
