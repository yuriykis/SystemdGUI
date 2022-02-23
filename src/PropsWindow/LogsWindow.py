import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class LogsWindow(Gtk.Window):
    def __init__(self, parent, infoText):
        self._infoText = infoText
        Gtk.init_check()
        super().__init__(title=self._infoText.getLogsWindowTitle())

        self.set_default_size(800, 600)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.grid.set_border_width(5)

        textbuffer = Gtk.TextBuffer()
        textbuffer.set_text(
            "GTK+, or the GIMP Toolkit, is a multi-platform toolkit for creating graphical user interfaces. Offering a complete set of widgets, GTK+ is suitable for projects ranging from small one-off tools to complete application suites."
        )

        self.logs_textview = Gtk.TextView(buffer=textbuffer)
        self.logs_textview.set_editable(False)
        self.logs_textview.set_cursor_visible(False)
        self.logs_textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.logs_textview.set_justification(Gtk.Justification.LEFT)
        self.logs_textview.set_left_margin(5)
        self.logs_textview.set_right_margin(5)
        self.logs_textview.set_top_margin(5)
        self.logs_textview.set_bottom_margin(5)
        self.logs_textview.set_border_width(5)
        self.logs_textview.set_pixels_above_lines(5)
        self.logs_textview.set_pixels_below_lines(5)
        self.logs_textview.set_pixels_inside_wrap(5)
        self.logs_textview.set_left_margin(5)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.logs_textview)
        self.grid.attach(scrolled_window, 0, 0, 2, 1)
        self.add(self.grid)
