from Language.Language import Language


class InfoText():

    def __init__(self, language):
        self._language = language

    def set_language(self, language):
        self._language = language

    def get_current_language(self):
        return self._language

    def get_add_new_service_text(self):
        if self._language == Language.EN:
            return "Add new service"
        elif self._language == Language.PL:
            return "Dodaj nową usługę"
        else:
            return "Add new service"

    def get_remove_service_text(self):
        if self._language == Language.EN:
            return "Remove Service"
        elif self._language == Language.PL:
            return "Usuń usługę"
        else:
            return "Remove Service"

    def get_service_name_text(self):
        if self._language == Language.EN:
            return "Service Name"
        elif self._language == Language.PL:
            return "Nazwa usługi"
        else:
            return "Service Name:"

    def get_load_state_text(self):
        if self._language == Language.EN:
            return "Load State"
        elif self._language == Language.PL:
            return "Czy załadowana"
        else:
            return "Load State:"

    def get_active_state_text(self):
        if self._language == Language.EN:
            return "Active State"
        elif self._language == Language.PL:
            return "Czy aktywna"
        else:
            return "Active State:"

    def get_service_started_text(self):
        if self._language == Language.EN:
            return "Service started."
        elif self._language == Language.PL:
            return "Usługa została uruchomiona."
        else:
            return "Service started."

    def get_service_stopped_text(self):
        if self._language == Language.EN:
            return "Service stopped."
        elif self._language == Language.PL:
            return "Usługa została zatrzymana."
        else:
            return "Service stopped."

    def get_service_start_failed_text(self):
        if self._language == Language.EN:
            return "Service start failed."
        elif self._language == Language.PL:
            return "Uruchomienie usługi nie powiodło się."
        else:
            return "Service start failed."

    def get_service_stop_failed_text(self):
        if self._language == Language.EN:
            return "Service stop failed."
        elif self._language == Language.PL:
            return "Zatrzymanie usługi nie powiodło się."
        else:
            return "Service stop failed."

    def get_service_restart_text(self):
        if self._language == Language.EN:
            return "Service restarted."
        elif self._language == Language.PL:
            return "Usługa została ponownie uruchomiona."
        else:
            return "Service restarted."

    def get_active_text(self):
        if self._language == Language.EN:
            return "Active"
        elif self._language == Language.PL:
            return "Aktywna"
        else:
            return "Active"

    def get_main_pid_text(self):
        if self._language == Language.EN:
            return "Main PID:"
        elif self._language == Language.PL:
            return "Główny PID:"
        else:
            return "Main PID:"

    def get_start_text(self):
        if self._language == Language.EN:
            return "Start"
        elif self._language == Language.PL:
            return "Uruchom"
        else:
            return "Start"

    def get_stop_text(self):
        if self._language == Language.EN:
            return "Stop"
        elif self._language == Language.PL:
            return "Zatrzymaj"
        else:
            return "Stop"

    def get_restart_text(self):
        if self._language == Language.EN:
            return "Restart"
        elif self._language == Language.PL:
            return "Uruchom ponownie"
        else:
            return "Restart"

    def get_edit_config_file_text(self):
        if self._language == Language.EN:
            return "Edit Config File"
        elif self._language == Language.PL:
            return "Edytuj plik konfiguracyjny"
        else:
            return "Edit Config File"

    def get_sudo_priv_text(self):
        if self._language == Language.EN:
            return "You need a sudo privileges to perform this action"
        elif self._language == Language.PL:
            return "Musisz mieć uprawnienia sudo aby wykonać tę akcję"
        else:
            return "You need to have sudo privileges to run this program."

    def get_cancel_text(self):
        if self._language == Language.EN:
            return "Cancel"
        elif self._language == Language.PL:
            return "Anuluj"
        else:
            return "Cancel"

    def get_close_text(self):
        if self._language == Language.EN:
            return "Close"
        elif self._language == Language.PL:
            return "Zamknij"
        else:
            return "Close"

    def get_are_you_sure_perf_action_text(self, action, service_name):
        if self._language == Language.EN:
            return "Are you sure you want to " + action + " the " + service_name + "?"
        elif self._language == Language.PL:
            if action == "start":
                action_pl = "uruchomić"
            elif action == "stop":
                action_pl = "zatrzymać"
            elif action == "restart":
                action_pl = "ponownie uruchomić"
            elif action == "remove":
                action_pl = "usunąć"
            return "Czy na pewno chcesz " + action_pl + " usługę " + service_name + "?"
        else:
            return "Are you sure you want to " + action + " the " + service_name + "?"

    def get_service_properties_text(self):
        if self._language == Language.EN:
            return "Service Properties"
        elif self._language == Language.PL:
            return "Właściwości usługi"
        else:
            return "Service Properties"

    def get_comfirm_action_text(self):
        if self._language == Language.EN:
            return "Confirm action"
        elif self._language == Language.PL:
            return "Potwierdź czynność"
        else:
            return "Confirm"

    def get_description_text(self):
        if self._language == Language.EN:
            return "Description:"
        elif self._language == Language.PL:
            return "Opis:"
        else:
            return "Description:"

    def get_new_service_text(self):
        if self._language == Language.EN:
            return "New Service"
        elif self._language == Language.PL:
            return "Nowa usługa"
        else:
            return "New Service"

    def get_exit_text(self):
        if self._language == Language.EN:
            return "Exit"
        elif self._language == Language.PL:
            return "Wyjdź"
        else:
            return "Exit"

    def get_language_text(self):
        if self._language == Language.EN:
            return "Language"
        elif self._language == Language.PL:
            return "Język"
        else:
            return "Language"

    def get_file_text(self):
        if self._language == Language.EN:
            return "File"
        elif self._language == Language.PL:
            return "Plik"
        else:
            return "File"

    def get_view_text(self):
        if self._language == Language.EN:
            return "View"
        elif self._language == Language.PL:
            return "Widok"
        else:
            return "View"

    def get_about_text(self):
        if self._language == Language.EN:
            return "About"
        elif self._language == Language.PL:
            return "O programie"
        else:
            return "About"

    def get_view_program_info(self):
        if self._language == Language.EN:
            return "View program info"
        elif self._language == Language.PL:
            return "Wyświetl informacje o programie"
        else:
            return "View program info"

    def get_application_name(self):
        if self._language == Language.EN:
            return "Graphical User Interface for Systemd"
        elif self._language == Language.PL:
            return "Graficzny interfejs użytkownika dla Systemd"
        else:
            return "Graphical User Interface for Systemd"

    def get_reload_text(self):
        if self._language == Language.EN:
            return "Reload list of services"
        elif self._language == Language.PL:
            return "Przeładuj listę usług"
        else:
            return "Reload list of services"

    def get_show_logs_text(self):
        if self._language == Language.EN:
            return "Show logs"
        elif self._language == Language.PL:
            return "Pokaż logi"
        else:
            return "Show logs"

    def get_logs_window_title(self):
        if self._language == Language.EN:
            return "Logs"
        elif self._language == Language.PL:
            return "Logi"
        else:
            return "Logs"

    def get_cpu_utilization_graph_text(self):
        if self._language == Language.EN:
            return "CPU Utilization Graph"
        elif self._language == Language.PL:
            return "Wykres zużycia CPU"
        else:
            return "CPU Utilization Graph"

    def get_cpu_utilization_text(self):
        if self._language == Language.EN:
            return "CPU Utilization"
        elif self._language == Language.PL:
            return "Zużycie CPU"
        else:
            return "CPU Utilization"

    def get_cpu_utilization_graph_window_title(self):
        if self._language == Language.EN:
            return "CPU Utilization Graph"
        elif self._language == Language.PL:
            return "Wykres zużycia CPU"
        else:
            return "CPU Utilization Graph"

    def get_active_text(self):
        if self._language == Language.EN:
            return "Active: "
        elif self._language == Language.PL:
            return "Czy aktywna: "
        else:
            return "Active: "

    def get_path_text(self):
        if self._language == Language.EN:
            return "Path: "
        elif self._language == Language.PL:
            return "Ścieżka: "
        else:
            return "Path: "
    
    def get_main_pid_text(self):
        if self._language == Language.EN:
            return "Main PID: "
        elif self._language == Language.PL:
            return "Główny PID: "
        else:
            return "Main PID: "

    def get_loaded_text(self):
        if self._language == Language.EN:
            return "Loaded: "
        elif self._language == Language.PL:
            return "Czy załadowana: "
        else:
            return "Loaded: "

    def get_type_text(self):
        if self._language == Language.EN:
            return "Type: "
        elif self._language == Language.PL:
            return "Typ: "
        else:
            return "Type: "

    def get_exec_start_text(self):
        if self._language == Language.EN:
            return "ExecStart: "
        elif self._language == Language.PL:
            return "Program startowy: "
        else:
            return "ExecStart: "

    def get_wanted_by_text(self):
        if self._language == Language.EN:
            return "WantedBy: "
        elif self._language == Language.PL:
            return "Wymagane przez: "
        else:
            return "WantedBy: "