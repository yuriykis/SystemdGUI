import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from SystemdManager import SystemdManager


class LogsWindow(Gtk.Dialog):

    def __init__(self, parent, info_text, service_name):
        self._info_text = info_text
        self._service_name = service_name
        Gtk.init_check()
        super().__init__(title=self._info_text.get_logs_window_title())
        self.add_buttons(self._info_text.get_close_text(), Gtk.ResponseType.CLOSE)
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

        # get current service logs
        logs = SystemdManager.get_service_logs(self._service_name)
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
