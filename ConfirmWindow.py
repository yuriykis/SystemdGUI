import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ConfirmWindow(Gtk.Dialog):
    def __init__(self, parent, action, infoText):
        self._infoText = infoText
        super().__init__(title=self._infoText.getComfirmActionText(),
                         transient_for=parent,
                         flags=0)
        self.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                         Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.get_action_area().get_children()[0].set_label(
            self._infoText.getCancelText())
        ok_button = self.get_action_area().get_children()[1]
        ok_button.set_label("OK")
        self.set_default_size(200, 100)

        vbox = Gtk.VBox()

        label = Gtk.Label(self._infoText.getAreYouSurePerfActionText(action))
        label.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label, False, False, 0)

        self.get_content_area().add(vbox)

        self.show_all()
