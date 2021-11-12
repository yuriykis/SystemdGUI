import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ConfirmWindow(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Confirm action", transient_for=parent, flags=0)
        self.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                         Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.get_action_area().get_children()[0].set_label("Cancel")
        ok_button = self.get_action_area().get_children()[1]
        ok_button.set_label("OK")
        ok_button.connect("clicked", self.on_info_clicked)
        self.set_default_size(200, 100)

        vbox = Gtk.VBox()

        label = Gtk.Label("Are you sure you want restart the service?")
        label.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label, False, False, 0)

        self.get_content_area().add(vbox)

        self.show_all()

    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Error",
        )
        dialog.format_secondary_text(
            "You need a sudo privileges to restart the service")
        dialog.run()

        dialog.destroy()