import gi

from Language.Language import Language

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class SideMenu(Gtk.Box):

    def __init__(self, main_window, info_text):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self._info_text = info_text
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.pack_start(listbox, True, True, 0)

        # Add new service button
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        row.add(hbox)

        add_service_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'gnome/assets/green-plus-sign-icon-6.jpg', 25, 25)
        img = Gtk.Image()
        img.set_from_pixbuf(add_service_icon)
        self.add_new_service_button = Gtk.Button(
            label=self._info_text.get_add_new_service_text())
        self.add_new_service_button.connect(
            "clicked", main_window.on_add_new_service_clicked)
        self.add_new_service_button.set_image(img)
        self.add_new_service_button.set_image_position(Gtk.PositionType.TOP)
        self.add_new_service_button.set_always_show_image(True)
        hbox.pack_start(self.add_new_service_button, True, True, 0)
        listbox.add(row)

        # Remove service button
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        row.add(hbox)
        remove_service_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'gnome/assets/red-minus-sign-icon-6.png', 25, 25)
        img = Gtk.Image()
        img.set_from_pixbuf(remove_service_icon)

        self.remove_service_button = Gtk.Button(
            label=self._info_text.get_remove_service_text())
        self.remove_service_button.connect(
            "clicked", main_window.on_remove_service_clicked)
        self.remove_service_button.set_image(img)
        self.remove_service_button.set_image_position(Gtk.PositionType.TOP)
        self.remove_service_button.set_always_show_image(True)
        self.remove_service_button.set_sensitive(True)
        hbox.pack_start(self.remove_service_button, True, True, 0)
        listbox.add(row)

        # Reload list of services
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        row.add(hbox)
        reload_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'gnome/assets/reload-icon-6.png', 25, 25)
        img = Gtk.Image()
        img.set_from_pixbuf(reload_icon)
        self.reload_button = Gtk.Button(
            label=self._info_text.get_reload_text())
        self.reload_button.connect("clicked",
                                   main_window.refresh_services_view)
        self.reload_button.set_image(img)
        self.reload_button.set_image_position(Gtk.PositionType.TOP)
        self.reload_button.set_always_show_image(True)
        self.reload_button.set_sensitive(True)
        hbox.pack_start(self.reload_button, True, True, 0)
        listbox.add(row)
