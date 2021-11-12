import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from MainWindow import MainWindow

settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", True)

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
