import QtQuick 2.0

Item {
    id : language
    property string currentLanguage : "English"
    property var availableLanguages: ["English", "Polski"]

    function setCurrentLanguage(language) {
        currentLanguage = language;
        console.log("Current language: " + currentLanguage);
    }

    function getAddServiceText() {
        if (currentLanguage == "English") {
            return "Add new service";
        } else if (currentLanguage == "Polski") {
            return "Dodaj nową usługę";
        } else {
            return "Add service";
        }
    }

    function getAboutProgramText() {
        if (currentLanguage == "English") {
            return "About program";
        } else if (currentLanguage == "Polski") {
            return "O programie";
        } else {
            return "About program";
        }
    }

    function getAboutWindowDescriptionText() {
        if (currentLanguage == "English") {
            return "Graphical User Interface for Systemd";
        } else if (currentLanguage == "Polski") {
            return "Graficzny Interfejs Użytkownika dla Systemd";
        } else {
            return "Graphical User Interface for Systemd";
        }
    }
    function getReloadServicesListText() {
        if (currentLanguage == "English") {
            return "Reload services list";
        } else if (currentLanguage == "Polski") {
            return "Przeładuj listę usług";
        } else {
            return "Reload services list";
        }
    }
    function getRemoveServiceText() {
        if (currentLanguage == "English") {
            return "Remove service";
        } else if (currentLanguage == "Polski") {
            return "Usuń usługę";
        } else {
            return "Remove service";
        }
    }
    function getServiceRemovedSuccessfullyText() {
        if (currentLanguage == "English") {
            return "Service removed successfully";
        } else if (currentLanguage == "Polski") {
            return "Usługa została pomyślnie usunięta";
            return "Service removed successfully";
        }
    }

    function getErrorText() {
        if (currentLanguage == "English") {
            return "Error";
        } else if (currentLanguage == "Polski") {
            return "Błąd";
        } else {
            return "Error";
        }
    }

    function getServiceNameText() {
        if (currentLanguage == "English") {
            return "Service name";
        } else if (currentLanguage == "Polski") {
            return "Nazwa usługi";
        } else {
            return "Service name";
        }
    }
    function getServiceDescriptionText() {
        if (currentLanguage == "English") {
            return "Service description";
        } else if (currentLanguage == "Polski") {
            return "Opis usługi";
        } else {
            return "Service description";
        }
    }
    function getServiceCreatedSuccessfullyText() {
        if (currentLanguage == "English") {
            return "Service created successfully";
        } else if (currentLanguage == "Polski") {
            return "Usługa została pomyślnie utworzona";
        } else {
            return "Service created successfully";
        }
    }
    function getFieldsCannotBeEmptyText() {
        if (currentLanguage == "English") {
            return "Fields cannot be empty";
        } else if (currentLanguage == "Polski") {
            return "Pola nie mogą być puste";
        } else {
            return "Fields cannot be empty";
        }
    }
    function getConfirmActionText() {
        if (currentLanguage == "English") {
            return "Confirm action";
        } else if (currentLanguage == "Polski") {
            return "Potwierdź czynność";
        } else {
            return "Confirm action";
        }
    }

    function getAreYouSureToPerfActionText(action, serviceName) {
        if (currentLanguage == "English") {
            return "Are you sure you want to " + action + " the " + serviceName + "?";
        } else if (currentLanguage == "Polski") {
            let action_corrected
            switch (action) {
                case "uruchom": action_corrected = "uruchomić";
                    break;
                case "zatrzymaj": action_corrected = "zatrzymać";
                    break;
                case "uruchom ponownie": action_corrected = "ponownie uruchomić";
                    break;
                case "remove": action_corrected = "usunąć";
                    break;
            }
            return "Czy na pewno chcesz " + action_corrected + " usługę " + serviceName + "?";
        } else {
            return "Are you sure you want to " + action + " the " + serviceName + "?";
        }
    }
    function getLoadStateText() {
        if (currentLanguage == "English") {
            return "Load state";
        } else if (currentLanguage == "Polski") {
            return "Czy załadowana";
        } else {
            return "Load state";
        }
    }
    function getActiveStateText() {
        if (currentLanguage == "English") {
            return "Active state";
        } else if (currentLanguage == "Polski") {
            return "Czy aktywna";
        } else {
            return "Active state";
        }
    }

    function getServiceLogsText() {
        if (currentLanguage == "English") {
            return "Service logs";
        } else if (currentLanguage == "Polski") {
            return "Dziennik usługi";
        } else {
            return "Service logs";
        }
    }

    function getFileText() {
        if (currentLanguage == "English") {
            return "File";
        } else if (currentLanguage == "Polski") {
            return "Plik";
        } else {
            return "File";
        }
    }

    function getNewServiceText() {
        if (currentLanguage == "English") {
            return "New service";
        } else if (currentLanguage == "Polski") {
            return "Nowa usługa";
        } else {
            return "New service";
        }
    }

    function getExitText() {
        if (currentLanguage == "English") {
            return "Exit";
        } else if (currentLanguage == "Polski") {
            return "Wyłącz program";
        } else {
            return "Exit";
        }
    }

    function getViewText() {
        if (currentLanguage == "English") {
            return "View";
        } else if (currentLanguage == "Polski") {
            return "Widok";
        } else {
            return "View";
        }
    }

    function getLanguageText() {
        if (currentLanguage == "English") {
            return "Language";
        } else if (currentLanguage == "Polski") {
            return "Język";
        } else {
            return "Language";
        }
    }

    function getAboutText() {
        if (currentLanguage == "English") {
            return "About";
        } else if (currentLanguage == "Polski") {
            return "O programie";
        } else {
            return "About";
        }
    }
    function getViewProgramInfoText() {
        if (currentLanguage == "English") {
            return "View program info";
        } else if (currentLanguage == "Polski") {
            return "Pokaż informacje o programie";
        } else {
            return "View program info";
        }
    }

    function getServicePropertiesText() {
        if (currentLanguage == "English") {
            return "Service properties";
        } else if (currentLanguage == "Polski") {
            return "Właściwości usługi";
        } else {
            return "Service properties";
        }
    }

    function getStartText() {
        if (currentLanguage == "English") {
            return "Start";
        } else if (currentLanguage == "Polski") {
            return "Uruchom";
        } else {
            return "Start";
        }
    }

    function getStopText() {
        if (currentLanguage == "English") {
            return "Stop";
        } else if (currentLanguage == "Polski") {
            return "Zatrzymaj";
        } else {
            return "Stop";
        }
    }

    function getRestartText() {
        if (currentLanguage == "English") {
            return "Restart";
        } else if (currentLanguage == "Polski") {
            return "Uruchom ponownie";
        } else {
            return "Restart";
        }
    }

    function getEditConfigFileText() {
        if (currentLanguage == "English") {
            return "Edit config file";
        } else if (currentLanguage == "Polski") {
            return "Edytuj plik konfiguracyjny";
        } else {
            return "Edit config file";
        }
    }

    function getShowLogsText() {
        if (currentLanguage == "English") {
            return "Show logs";
        } else if (currentLanguage == "Polski") {
            return "Pokaż dziennik";
        } else {
            return "Show logs";
        }
    }
}
