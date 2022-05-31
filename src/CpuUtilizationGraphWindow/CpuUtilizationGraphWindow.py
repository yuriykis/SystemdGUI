import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from systemd.SystemdManager import SystemdManager
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as
                                                 FigureCanvas)
import numpy as np


class CpuUtilizationGraphWindow(Gtk.Dialog):

    def __init__(self, service_name, info_text):
        self._info_text = info_text
        self._service_name = service_name
        self._values_number = 300
        Gtk.init_check()
        super().__init__(
            title=self._info_text.get_cpu_utilization_graph_window_title())
        self.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.set_border_width(10)
        self.set_default_size(1500, 1000)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot()
        ax.title.set_text(
            self._info_text.get_cpu_utilization_graph_window_title())

        logs_list = SystemdManager.get_service_logs(
            self._service_name).split("\n")
        logs = list(map(lambda x: x.split(" "), logs_list))
        system_utilization_values = []
        system_utilization_times = []
        for log in logs:
            log[:] = [x for x in log if x != ""]
            if (len(log) >= 9):
                system_utilization_values.append(log[9])
                system_utilization_times.append(log[2])
        system_utilization_values = system_utilization_values[:self.
                                                              _values_number]
        # replace commas with dots
        system_utilization_values = list(
            map(lambda x: x.replace(",", "."), system_utilization_values))
        # map to float
        system_utilization_values = list(
            map(lambda x: float(x), system_utilization_values))
        system_utilization_times = system_utilization_times[:self.
                                                            _values_number]
        ax.set_xticks(np.arange(0, len(system_utilization_times),
                                self._values_number / 10),
                      minor=False)
        ax.plot(system_utilization_times, system_utilization_values)

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
