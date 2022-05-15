import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from systemd.SystemdManager import SystemdManager
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as
                                                 FigureCanvas)
import numpy as np


class CpuUtilizationGraphWindow(Gtk.Dialog):
    def __init__(self, infoText):
        self._infoText = infoText
        Gtk.init_check()
        super().__init__(
            title=self._infoText.getCpuUtilizationGraphWindowTitle())
        self.add_buttons(Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        self.set_border_width(10)
        self.set_default_size(800, 600)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.cos(2 * np.pi * t)
        ax.plot(t, s)

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

        sw = Gtk.ScrolledWindow()
        # A scrolled selfdow border goes outside the scrollbars and viewport
        sw.set_border_width(10)

        canvas = FigureCanvas(fig)  # a Gtk.DraselfgArea
        canvas.set_size_request(800, 600)
        sw.add(canvas)
        self.grid.attach(sw, 0, 0, 1, 1)
        self.whole_screen.pack_start(self.grid, True, True, 0)
        self.show_all()
