import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class AboutWindow(Gtk.AboutDialog):
    def __init__(self, parent, infoText):
        self._infoText = infoText
        Gtk.AboutDialog.__init__(self, parent=parent)

        self.set_program_name("Systemd GUI")
        self.set_version("1.0")
        self.set_copyright("Copyright © 2022")
        self.set_comments(self._infoText.getApplicationName())
        self.set_website("https://github.com/yuriykis/SystemdGUI.git")
        self.set_website_label("SystemdGUI")
        self.set_authors(["Yuriy Kis"])
        self.set_license_type(Gtk.License.GPL_3_0)