import gi

from src.Language.Language import Language

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainMenuBar(Gtk.MenuBar):

    def __init__(self, main_window, info_text):
        super().__init__()
        self._info_text = info_text
        file_menu = Gtk.Menu()
        self.file_menu_item = Gtk.MenuItem(
            label=self._info_text.get_file_text())
        self.file_menu_item.set_submenu(file_menu)
        acgroup_file = Gtk.AccelGroup()
        main_window.add_accel_group(acgroup_file)
        self.new = Gtk.ImageMenuItem.new_from_stock(
            self._info_text.get_new_service_text(), acgroup_file)
        self.new.connect("activate", main_window.on_add_new_service_clicked)
        file_menu.append(self.new)
        separator = Gtk.SeparatorMenuItem()
        file_menu.append(separator)
        self.quit = Gtk.ImageMenuItem.new_from_stock(
            self._info_text.get_exit_text(), acgroup_file)
        self.quit.connect("activate", main_window.on_close_clicked)
        file_menu.append(self.quit)

        self.append(self.file_menu_item)
        view_menu = Gtk.Menu()
        self.view_menu_item = Gtk.MenuItem(
            label=self._info_text.get_view_text())
        self.view_menu_item.set_submenu(view_menu)
        self.append(self.view_menu_item)
        acgroup_view = Gtk.AccelGroup()
        main_window.add_accel_group(acgroup_view)
        self.language = Gtk.ImageMenuItem.new_from_stock(
            self._info_text.get_language_text(), acgroup_view)
        self.language.set_sensitive(False)
        view_menu.append(self.language)
        separator = Gtk.SeparatorMenuItem()
        view_menu.append(separator)
        language_pl = Gtk.RadioMenuItem("Polski")
        language_pl.connect("activate", main_window.on_language_pl_clicked)
        view_menu.append(language_pl)
        language_en = Gtk.RadioMenuItem("English", group=language_pl)
        language_en.connect("activate", main_window.on_language_en_clicked)
        view_menu.append(language_en)
        if (self._info_text.get_current_language() == Language.PL):
            language_pl.set_active(True)
        else:
            language_en.set_active(True)

        about_menu = Gtk.Menu()
        self.about_menu_item = Gtk.MenuItem(
            label=self._info_text.get_about_text())
        self.about_menu_item.set_submenu(about_menu)
        self.view_program_info = Gtk.ImageMenuItem.new_from_stock(
            self._info_text.get_view_program_info(), acgroup_view)
        self.view_program_info.connect(
            "activate", main_window.on_view_program_info_clicked)
        about_menu.append(self.view_program_info)
        self.append(self.about_menu_item)