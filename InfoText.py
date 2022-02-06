from Language import Language


class InfoText():
    def __init__(self, language):
        self._language = language

    def changeLanguage(self, language):
        self._language = language

    def getAddNewServiceText(self):
        if self._language == Language.EN:
            return "Add new service"
        elif self._language == Language.PL:
            return "Dodaj nową usługę"
        else:
            return "Add new service"

    def getServiceNameText(self):
        if self._language == Language.EN:
            return "Service Name"
        elif self._language == Language.PL:
            return "Nazwa usługi"
        else:
            return "Service Name:"

    def getLoadStateText(self):
        if self._language == Language.EN:
            return "Load State"
        elif self._language == Language.PL:
            return "Czy załadowana"
        else:
            return "Load State:"

    def getActiveStateText(self):
        if self._language == Language.EN:
            return "Active State"
        elif self._language == Language.PL:
            return "Czy aktywna"
        else:
            return "Active State:"

    def getServiceStartedText(self):
        if self._language == Language.EN:
            return "Service started."
        elif self._language == Language.PL:
            return "Usługa została uruchomiona."
        else:
            return "Service started."

    def getServiceStoppedText(self):
        if self._language == Language.EN:
            return "Service stopped."
        elif self._language == Language.PL:
            return "Usługa została zatrzymana."
        else:
            return "Service stopped."

    def getServiceStartFailedText(self):
        if self._language == Language.EN:
            return "Service start failed."
        elif self._language == Language.PL:
            return "Uruchomienie usługi nie powiodło się."
        else:
            return "Service start failed."

    def getServiceStopFailedText(self):
        if self._language == Language.EN:
            return "Service stop failed."
        elif self._language == Language.PL:
            return "Zatrzymanie usługi nie powiodło się."
        else:
            return "Service stop failed."

    def getServiceRestartText(self):
        if self._language == Language.EN:
            return "Service restarted."
        elif self._language == Language.PL:
            return "Usługa została ponownie uruchomiona."
        else:
            return "Service restarted."

    def getActiveText(self):
        if self._language == Language.EN:
            return "Active"
        elif self._language == Language.PL:
            return "Aktywna"
        else:
            return "Active"

    def getMainPIDText(self):
        if self._language == Language.EN:
            return "Main PID:"
        elif self._language == Language.PL:
            return "Główny PID:"
        else:
            return "Main PID:"

    def getStartText(self):
        if self._language == Language.EN:
            return "Start"
        elif self._language == Language.PL:
            return "Uruchom"
        else:
            return "Start"

    def getStopText(self):
        if self._language == Language.EN:
            return "Stop"
        elif self._language == Language.PL:
            return "Zatrzymaj"
        else:
            return "Stop"

    def getRestartText(self):
        if self._language == Language.EN:
            return "Restart"
        elif self._language == Language.PL:
            return "Uruchom ponownie"
        else:
            return "Restart"

    def getEditConfigFileText(self):
        if self._language == Language.EN:
            return "Edit Config File"
        elif self._language == Language.PL:
            return "Edytuj plik konfiguracyjny"
        else:
            return "Edit Config File"

    def getSudoPrivText(self):
        if self._language == Language.EN:
            return "You need a sudo privileges to perform this action"
        elif self._language == Language.PL:
            return "Musisz mieć uprawnienia sudo aby wykonać tę akcję"
        else:
            return "You need to have sudo privileges to run this program."

    def getCancelText(self):
        if self._language == Language.EN:
            return "Cancel"
        elif self._language == Language.PL:
            return "Anuluj"
        else:
            return "Cancel"

    def getAreYouSurePerfActionText(self, action):
        if self._language == Language.EN:
            return "Are you sure you want to " + action + " the service?"
        elif self._language == Language.PL:
            if action == "start":
                action_pl = "uruchomić"
            elif action == "stop":
                action_pl = "zatrzymać"
            elif action == "restart":
                action_pl = "ponownie uruchomić"
            return "Czy na pewno chcesz " + action_pl + " usługę?"
        else:
            return "Are you sure you want to " + action + " the service?"

    def getServicePropertiesText(self):
        if self._language == Language.EN:
            return "Service Properties"
        elif self._language == Language.PL:
            return "Właściwości usługi"
        else:
            return "Service Properties"

    def getComfirmActionText(self):
        if self._language == Language.EN:
            return "Confirm action"
        elif self._language == Language.PL:
            return "Potwierdź czynność"
        else:
            return "Confirm"

    def getDescriptionText(self):
        if self._language == Language.EN:
            return "Description:"
        elif self._language == Language.PL:
            return "Opis:"
        else:
            return "Description:"