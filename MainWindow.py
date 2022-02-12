from tokenize import group
import gi
import os
from AboutWindow import AboutWindow

from ServiceAction import ServiceAction
from systemd.ServiceCreator import ServiceCreator

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf

from systemd.SystemdManager import SystemdManager
from PropsWindow import PropsWindow
from AddServiceWindow import AddServiceWindow
from InfoText import InfoText
from Language import Language
from ConfirmWindow import ConfirmWindow


class MainWindow(Gtk.Window):
    def __init__(self):
        self._infoText = InfoText(Language.PL)
        Gtk.init_check()
        super().__init__(title="Systemd GUI")
        self.set_border_width(5)
        self.set_default_size(1000, 500)
        grid = Gtk.Grid()
        scrolledwindow = Gtk.ScrolledWindow()

        menu_bar = Gtk.MenuBar()
        file_menu = Gtk.Menu()
        file_menu_item = Gtk.MenuItem(label=self._infoText.getFileText())
        file_menu_item.set_submenu(file_menu)
        acgroup_file = Gtk.AccelGroup()
        self.add_accel_group(acgroup_file)
        new = Gtk.ImageMenuItem.new_from_stock(
            self._infoText.getNewServiceText(), acgroup_file)
        file_menu.append(new)
        separator = Gtk.SeparatorMenuItem()
        file_menu.append(separator)
        quit = Gtk.ImageMenuItem.new_from_stock(self._infoText.getExitText(),
                                                acgroup_file)
        file_menu.append(quit)

        menu_bar.append(file_menu_item)
        view_menu = Gtk.Menu()
        view_menu_item = Gtk.MenuItem(label=self._infoText.getViewText())
        view_menu_item.set_submenu(view_menu)
        menu_bar.append(view_menu_item)
        acgroup_view = Gtk.AccelGroup()
        self.add_accel_group(acgroup_view)
        language = Gtk.ImageMenuItem.new_from_stock(
            self._infoText.getLanguageText(), acgroup_view)
        language.set_sensitive(False)
        view_menu.append(language)
        separator = Gtk.SeparatorMenuItem()
        view_menu.append(separator)
        language_pl = Gtk.RadioMenuItem("Polski")
        view_menu.append(language_pl)
        language_en = Gtk.RadioMenuItem("English", group=language_pl)
        view_menu.append(language_en)
        if (self._infoText.getCurrentLanguage() == Language.PL):
            language_pl.set_active(True)
        else:
            language_en.set_active(True)

        about_menu = Gtk.Menu()
        about_menu_item = Gtk.MenuItem(label=self._infoText.getAboutText())
        about_menu_item.set_submenu(about_menu)
        view_program_info = Gtk.ImageMenuItem.new_from_stock(
            self._infoText.getViewProgramInfo(), acgroup_view)
        view_program_info.connect("activate",
                                  self.on_view_program_info_clicked)
        about_menu.append(view_program_info)
        menu_bar.append(about_menu_item)
        grid.attach(menu_bar, 0, 0, 1, 1)

        self.liststore = Gtk.ListStore(str, str, str)
        self.treeview = Gtk.TreeView(model=self.liststore)
        self.treeview.set_hexpand(True)
        self.treeview.set_vexpand(True)
        scrolledwindow.add(self.treeview)
        grid.attach_next_to(scrolledwindow, menu_bar, Gtk.PositionType.BOTTOM,
                            1, 1)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        # Add new service button
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        row.add(hbox)

        add_service_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'assets/green-plus-sign-icon-6.jpg', 25, 25)
        img = Gtk.Image()
        img.set_from_pixbuf(add_service_icon)
        add_new_service_button = Gtk.Button(
            label=self._infoText.getAddNewServiceText())
        add_new_service_button.connect("clicked",
                                       self.on_add_new_service_clicked)
        add_new_service_button.set_image(img)
        add_new_service_button.set_image_position(Gtk.PositionType.TOP)
        add_new_service_button.set_always_show_image(True)
        hbox.pack_start(add_new_service_button, True, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        row.add(hbox)
        remove_service_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
            'assets/red-minus-sign-icon-6.png', 25, 25)
        img = Gtk.Image()
        img.set_from_pixbuf(remove_service_icon)

        remove_service_button = Gtk.Button(
            label=self._infoText.getRemoveServiceText())
        remove_service_button.connect("clicked",
                                      self.on_remove_service_clicked)
        remove_service_button.set_image(img)
        remove_service_button.set_image_position(Gtk.PositionType.TOP)
        remove_service_button.set_always_show_image(True)
        remove_service_button.set_sensitive(True)
        hbox.pack_start(remove_service_button, True, True, 0)
        listbox.add(row)

        grid.attach_next_to(box_outer, scrolledwindow, Gtk.PositionType.RIGHT,
                            1, 1)

        firstColumnName = Gtk.CellRendererText()
        systemdUnitsNames = Gtk.TreeViewColumn(
            self._infoText.getServiceNameText(), firstColumnName, text=0)
        self.treeview.append_column(systemdUnitsNames)

        secondColumnName = Gtk.CellRendererText()
        systemdUnitsStatus = Gtk.TreeViewColumn(
            self._infoText.getLoadStateText(), secondColumnName, text=1)
        self.treeview.append_column(systemdUnitsStatus)

        thirdColumnName = Gtk.CellRendererText()
        systemdUnitsDescription = Gtk.TreeViewColumn(
            self._infoText.getActiveStateText(), thirdColumnName, text=2)
        self.treeview.append_column(systemdUnitsDescription)

        self.treeview.connect("button-press-event", self.on_double_unit_click)
        self.tree_selection = self.treeview.get_selection()
        self.tree_selection.connect("changed", self.on_service_selection)

        self.add(grid)
        self.refresh_services_view()

    def decodeUnit(self, unit):
        return os.path.basename(unit.decode('UTF-8'))

    def decodeTuple(self, tuple):
        return self.decodeUnit(tuple[0]), self.decodeUnit(
            tuple[1]), self.decodeUnit(tuple[2])

    def refresh_services_view(self):
        self.liststore = Gtk.ListStore(str, str, str)
        self.systemdUnitsList = SystemdManager.getUnitsList()

        # only service unit should remain
        self.systemdUnitsList = map(self.decodeTuple, self.systemdUnitsList)

        self.systemdUnitsList = list(
            filter(lambda unit: "service" in unit[0], self.systemdUnitsList))
        self.systemdUnitsList.sort()
        for unit in self.systemdUnitsList:
            serivce_name = unit[0]
            is_loaded_field = unit[1]
            is_active_field = unit[2]

            self.liststore.append(
                [serivce_name, is_loaded_field, is_active_field])
        self.treeview.set_model(self.liststore)

    def on_double_unit_click(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            mouse_x, mouse_y = self.treeview.get_pointer()
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
            value = model.get_value(tree_iter, 0)
            self.current_selected_service = value

    def on_view_program_info_clicked(self, button):
        aboutWindow = AboutWindow(self, self._infoText)
        aboutWindow.run()
        aboutWindow.destroy()