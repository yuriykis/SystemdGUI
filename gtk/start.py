import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from MainWindow import MainWindow

settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", True)

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import sys

sys.path.append('/home/yuriy/GTK/SystemdGUI/systemd/')


def main():
    win = MainWindow.MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
