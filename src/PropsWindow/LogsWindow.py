import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from systemd.SystemdManager import SystemdManager


class LogsWindow(Gtk.Dialog):
    def __init__(self, parent, infoText, serviceName):
        self._infoText = infoText
        self._serviceName = serviceName
        Gtk.init_check()
        super().__init__(title=self._infoText.getLogsWindowTitle())
        self.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.set_default_size(800, 600)

        content_area = self.get_content_area()
        self.whole_screen = Gtk.VBox(spacing=6)
        self.whole_screen.set_orientation(Gtk.Orientation.VERTICAL)
        self.whole_screen.set_hexpand(True)
        self.whole_screen.set_vexpand(True)
        content_area.add(self.whole_screen)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.grid.set_border_width(5)

        # load current service logs
        logs = SystemdManager.getServiceLogs(self._serviceName)
        textbuffer = Gtk.TextBuffer()
        textbuffer.set_text(logs)

        self.logs_textview = Gtk.TextView(buffer=textbuffer)
        self.logs_textview.set_editable(False)
        self.logs_textview.set_cursor_visible(False)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.logs_textview)
        self.grid.attach(scrolled_window, 0, 0, 1, 1)
        self.whole_screen.pack_start(self.grid, True, True, 0)
        self.show_all()
