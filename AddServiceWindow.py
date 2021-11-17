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

        self.service_name_box = Gtk.Box(spacing=6)
        self.service_name_label = Gtk.Label("Service Name:")
        self.service_name_entry = Gtk.Entry()
        self.service_name_box.pack_start(self.service_name_label, False, True,
                                         0)
        self.service_name_box.pack_end(self.service_name_entry, False, True, 0)
        self.whole_screen.pack_start(self.service_name_box, True, True, 0)

        # Unit statement
        self.unit_statement_box = Gtk.Box(spacing=6)
        self.unit_statement_label = Gtk.Label("[Unit]")
        self.unit_statement_box.pack_start(self.unit_statement_label, False,
                                           False, 0)
        self.whole_screen.pack_start(self.unit_statement_box, False, False, 0)

        self.service_description_box = Gtk.Box(spacing=6)
        self.service_description_label = Gtk.Label("Description:")
        self.service_description_entry = Gtk.Entry()
        self.service_description_box.pack_start(self.service_description_label,
                                                False, True, 0)
        self.service_description_box.pack_end(self.service_description_entry,
                                              False, True, 0)

        self.whole_screen.pack_start(self.service_description_box, True, True,
                                     0)

        # Service statement
        self.service_statement_box = Gtk.Box(spacing=6)
        self.service_statement_label = Gtk.Label("[Service]")
        self.service_statement_box.pack_start(self.service_statement_label,
                                              False, False, 0)
        self.whole_screen.pack_start(self.service_statement_box, False, False,
                                     0)

        self.service_type_box = Gtk.Box(spacing=6)
        self.service_type_label = Gtk.Label("Type:")
        self.service_type_entry = Gtk.Entry()
        self.service_type_box.pack_start(self.service_type_label, False, True,
                                         0)
        self.service_type_box.pack_end(self.service_type_entry, False, True, 0)
        self.whole_screen.pack_start(self.service_type_box, True, True, 0)

        self.service_exec_start_box = Gtk.Box(spacing=6)
        self.service_exec_start_label = Gtk.Label("ExecStart:")
        self.service_exec_start_entry = Gtk.Entry()
        self.service_exec_start_box.pack_start(self.service_exec_start_label,
                                               False, True, 0)
        self.service_exec_start_box.pack_end(self.service_exec_start_entry,
                                             False, True, 0)
        self.whole_screen.pack_start(self.service_exec_start_box, True, True,
                                     0)

        # Install statement
        self.install_statement_box = Gtk.Box(spacing=6)
        self.install_statement_label = Gtk.Label("[Install]")
        self.install_statement_box.pack_start(self.install_statement_label,
                                              False, False, 0)
        self.whole_screen.pack_start(self.install_statement_box, False, False,
                                     0)

        self.service_wanted_by_box = Gtk.Box(spacing=6)
        self.service_wanted_by_label = Gtk.Label("WantedBy:")
        self.service_wanted_by_entry = Gtk.Entry()
        self.service_wanted_by_box.pack_start(self.service_wanted_by_label,
                                              False, True, 0)
        self.service_wanted_by_box.pack_end(self.service_wanted_by_entry,
                                            False, True, 0)
        self.whole_screen.pack_start(self.service_wanted_by_box, True, True, 0)

        self.show_all()

    def getServiceName(self):
        return self.service_name_entry.get_text()

    def getServiceDescription(self):
        return self.service_description_entry.get_text()

    def getServiceType(self):
        return self.service_type_entry.get_text()

    def getServiceExecStart(self):
        return self.service_exec_start_entry.get_text()

    def getServiceWantedBy(self):
        return self.service_wanted_by_entry.get_text()
