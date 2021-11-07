import gi
from MainWindow import MainWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
