import gi
import os
import sys
from MainWindow.ServicesList import ServicesList

from MainWindow.SideMenu import SideMenu
from AboutWindow.AboutWindow import AboutWindow
from .MainMenuBar import MainMenuBar

sys.path.append("/home/yuriy/GTK/SystemdGUI/systemd")
from ServiceAction import ServiceAction
from ServiceCreator import ServiceCreator

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from SystemdManager import SystemdManager
from PropsWindow.PropsWindow import PropsWindow
from AddServiceWindow.AddServiceWindow import AddServiceWindow
from InfoText.InfoText import InfoText
from Language.Language import Language

from ConfirmWindow.ConfirmWindow import ConfirmWindow


class MainWindow(Gtk.Window):

    def __init__(self):
        self._info_text = InfoText(Language.EN)
        Gtk.init_check()
        super().__init__(title="Systemd GUI")
        self.set_border_width(5)
        self.set_default_size(1000, 500)
        self.grid = Gtk.Grid()

        self.menu_bar = MainMenuBar(self, self._info_text)
        self.grid.attach(self.menu_bar, 0, 0, 1, 1)

        self.services_list = ServicesList(self, self._info_text)
        self.grid.attach_next_to(self.services_list, self.menu_bar,
                                 Gtk.PositionType.BOTTOM, 1, 1)

        self.side_menu = SideMenu(self, self._info_text)

        self.grid.attach_next_to(self.side_menu, self.services_list,
                                 Gtk.PositionType.RIGHT, 1, 1)

        self.add(self.grid)
        self.refresh_services_view()

    def decode_unit(self, unit):
        return os.path.basename(unit.decode('UTF-8'))

    def decode_tuple(self, tuple):
        return self.decode_unit(tuple[0]), self.decode_unit(
            tuple[1]), self.decode_unit(tuple[2])

    def refresh_services_view(self, button=None):
        self.liststore = Gtk.ListStore(str, str, str, str, str)
        self.systemd_units_list = SystemdManager.get_units_list()

        # only service unit should remain
        self.systemd_units_list = map(self.decode_tuple,
                                      self.systemd_units_list)

        self.systemd_units_list = list(
            filter(lambda unit: "service" in unit[0], self.systemd_units_list))
        self.systemd_units_list.sort()
        for unit in self.systemd_units_list:
            color_point = "●"
            serivce_name = unit[0]
            is_loaded_field = unit[1]
            is_active_field = unit[2]
            if is_active_field == "active":
                status_color = "green"
            elif (is_active_field == "inactive"
                  and is_loaded_field == "loaded") or (is_active_field
                                                       == "activating"):
                status_color = "yellow"
            else:
                status_color = "red"

            self.liststore.append([
                color_point, serivce_name, is_loaded_field, is_active_field,
                status_color
            ])
            a = self.liststore[len(self.liststore) - 1]
            # self.liststore.set(iter, COL_COLOR, "red")
        self.services_list.treeview.set_model(self.liststore)

    def set_all_widgets_labels(self):
        self.menu_bar.file_menu_item.set_label(self._info_text.get_file_text())
        self.menu_bar.new.set_label(self._info_text.get_new_service_text())
        self.menu_bar.quit.set_label(self._info_text.get_exit_text())
        self.menu_bar.view_menu_item.set_label(self._info_text.get_view_text())
        self.menu_bar.language.set_label(self._info_text.get_language_text())
        self.menu_bar.about_menu_item.set_label(
            self._info_text.get_about_text())
        self.menu_bar.view_program_info.set_label(
            self._info_text.get_view_program_info())
        self.side_menu.add_new_service_button.set_label(
            self._info_text.get_add_new_service_text())
        self.side_menu.remove_service_button.set_label(
            self._info_text.get_remove_service_text())
        self.side_menu.reload_button.set_label(
            self._info_text.get_reload_text())
        self.services_list.systemdUnitsNames.set_title(
            self._info_text.get_service_name_text())
        self.services_list.systemdUnitsStatus.set_title(
            self._info_text.get_load_state_text())
        self.services_list.systemdUnitsDescription.set_title(
            self._info_text.get_active_state_text())

    def on_double_unit_click(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            mouse_x, mouse_y = self.services_list.treeview.get_pointer()
            row_number = int(str(widget.get_path_at_pos(mouse_x, mouse_y)[0]))
            clicked_service = self.systemd_units_list[row_number - 1][0]
            propsWindow = PropsWindow(self, clicked_service, self._info_text)
            propsWindow.run()
            propsWindow.destroy()

    def on_service_action_performed(self, serice_action):
        if (serice_action == ServiceAction.SERVICE_START_OK):
            print("Service started")
        elif (serice_action == ServiceAction.SERVICE_START_FAILED):
            print("Service start failed")
        elif (serice_action == ServiceAction.SERVICE_STOP_OK):
            print("Service stopped")
        elif (serice_action == ServiceAction.SERVICE_STOP_FAILED):
            print("Service stop failed")
        elif (serice_action == ServiceAction.SERVICE_RESTART_OK):
            print("Service restarted")
        elif (serice_action == ServiceAction.SERVICE_RESTART_FAILED):
            print("Service restart failed")
        elif (serice_action == ServiceAction.SERVICE_REMOVE_OK):
            print("Service removed")
        elif (serice_action == ServiceAction.SERVICE_REMOVE_FAILED):
            print("Service remove failed")
        self.refresh_services_view()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

    def on_add_new_service_clicked(self, button):
        addServiceWindow = AddServiceWindow(self, self._info_text)
        addServiceWindow.run()
        service_name = addServiceWindow.getservice_name()
        service_description = addServiceWindow.getServiceDescription()
        service_extec_start = addServiceWindow.getServiceExecStart()
        service_name = ServiceCreator.create_service(service_name,
                                                      service_description,
                                                      service_extec_start)
        addServiceWindow.destroy()
        self.refresh_services_view()

    def on_remove_service_clicked(self, button):
        _service_name = self.current_selected_service
        confirmWindow = ConfirmWindow(self, "remove", self._info_text,
                                      _service_name)
        response = confirmWindow.run()
        if response == Gtk.ResponseType.OK:
            service_action_result = SystemdManager.remove_unit(_service_name)
            if service_action_result == ServiceAction.SERVICE_START_FAILED:
                self.show_required_privileges_dialog()

            self.on_service_action_performed(service_action_result)
        confirmWindow.destroy()

    def on_service_selection(self, selection):
        (model, pathlist) = selection.get_selected_rows()
        for path in pathlist:
            tree_iter = model.get_iter(path)
            value = model.get_value(tree_iter, 1)
            self.current_selected_service = value

    def on_view_program_info_clicked(self, button):
        aboutWindow = AboutWindow(self, self._info_text)
        aboutWindow.run()
        aboutWindow.destroy()

    def on_language_pl_clicked(self, button):
        self._info_text.set_language(Language.PL)
        self.set_all_widgets_labels()

    def on_language_en_clicked(self, button):
        self._info_text.set_language(Language.EN)
        self.set_all_widgets_labels()