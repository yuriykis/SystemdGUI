import gi
import os
from src.MainWindow.ServicesList import ServicesList

from src.MainWindow.SideMenu import SideMenu
from ..AboutWindow.AboutWindow import AboutWindow
from .MainMenuBar import MainMenuBar

from systemd.ServiceAction import ServiceAction
from systemd.ServiceCreator import ServiceCreator

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from systemd.SystemdManager import SystemdManager
from ..PropsWindow.PropsWindow import PropsWindow
from ..AddServiceWindow.AddServiceWindow import AddServiceWindow
from ..InfoText.InfoText import InfoText
from src.Language.Language import Language

from ..ConfirmWindow.ConfirmWindow import ConfirmWindow


class MainWindow(Gtk.Window):
    def __init__(self):
        self._infoText = InfoText(Language.EN)
        Gtk.init_check()
        super().__init__(title="Systemd GUI")
        self.set_border_width(5)
        self.set_default_size(1000, 500)
        self.grid = Gtk.Grid()

        self.menu_bar = MainMenuBar(self, self._infoText)
        self.grid.attach(self.menu_bar, 0, 0, 1, 1)

        self.services_list = ServicesList(self, self._infoText)
        self.grid.attach_next_to(self.services_list, self.menu_bar,
                                 Gtk.PositionType.BOTTOM, 1, 1)

        self.side_menu = SideMenu(self, self._infoText)

        self.grid.attach_next_to(self.side_menu, self.services_list,
                                 Gtk.PositionType.RIGHT, 1, 1)

        self.add(self.grid)
        self.refresh_services_view()

    def decodeUnit(self, unit):
        return os.path.basename(unit.decode('UTF-8'))

    def decodeTuple(self, tuple):
        return self.decodeUnit(tuple[0]), self.decodeUnit(
            tuple[1]), self.decodeUnit(tuple[2])

    def refresh_services_view(self):
        self.liststore = Gtk.ListStore(str, str, str, str, str)
        self.systemdUnitsList = SystemdManager.getUnitsList()

        # only service unit should remain
        self.systemdUnitsList = map(self.decodeTuple, self.systemdUnitsList)

        self.systemdUnitsList = list(
            filter(lambda unit: "service" in unit[0], self.systemdUnitsList))
        self.systemdUnitsList.sort()
        for unit in self.systemdUnitsList:
            color_point = "● "
            serivce_name = unit[0]
            is_loaded_field = unit[1]
            is_active_field = unit[2]
            if is_active_field == "active":
                status_color = "green"
            elif is_active_field == "inactive" and is_loaded_field == "loaded":
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

    def setAllWidgetsLabels(self):
        self.menu_bar.file_menu_item.set_label(self._infoText.getFileText())
        self.menu_bar.new.set_label(self._infoText.getNewServiceText())
        self.menu_bar.quit.set_label(self._infoText.getExitText())
        self.menu_bar.view_menu_item.set_label(self._infoText.getViewText())
        self.menu_bar.language.set_label(self._infoText.getLanguageText())
        self.menu_bar.about_menu_item.set_label(self._infoText.getAboutText())
        self.menu_bar.view_program_info.set_label(
            self._infoText.getViewProgramInfo())
        self.side_menu.add_new_service_button.set_label(
            self._infoText.getAddNewServiceText())
        self.side_menu.remove_service_button.set_label(
            self._infoText.getRemoveServiceText())
        self.services_list.systemdUnitsNames.set_title(
            self._infoText.getServiceNameText())
        self.services_list.systemdUnitsStatus.set_title(
            self._infoText.getLoadStateText())
        self.services_list.systemdUnitsDescription.set_title(
            self._infoText.getActiveStateText())

    def on_double_unit_click(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            mouse_x, mouse_y = self.services_list.treeview.get_pointer()
            row_number = int(str(widget.get_path_at_pos(mouse_x, mouse_y)[0]))
            clicked_service = self.systemdUnitsList[row_number - 1][0]
            propsWindow = PropsWindow(self, clicked_service, self._infoText)
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
        addServiceWindow = AddServiceWindow(self, self._infoText)
        addServiceWindow.run()
        service_name = addServiceWindow.getServiceName()
        service_description = addServiceWindow.getServiceDescription()
        service_extec_start = addServiceWindow.getServiceExecStart()
        service_creator = ServiceCreator()
        service_name = service_creator.createService(service_name,
                                                     service_description,
                                                     service_extec_start)
        addServiceWindow.destroy()
        self.refresh_services_view()

    def on_remove_service_clicked(self, button):
        _serviceName = self.current_selected_service
        confirmWindow = ConfirmWindow(self, "remove", self._infoText,
                                      _serviceName)
        response = confirmWindow.run()
        if response == Gtk.ResponseType.OK:
            service_action_result = SystemdManager.removeUnit(_serviceName)
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
        aboutWindow = AboutWindow(self, self._infoText)
        aboutWindow.run()
        aboutWindow.destroy()

    def on_language_pl_clicked(self, button):
        self._infoText.setLanguage(Language.PL)
        self.setAllWidgetsLabels()

    def on_language_en_clicked(self, button):
        self._infoText.setLanguage(Language.EN)
        self.setAllWidgetsLabels()