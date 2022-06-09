from distutils import command
from pystemd.systemd1 import Manager, Unit
from .ServiceAction import ServiceAction
import subprocess
import pathlib


class SystemdManager():

    def get_units_list():
        with Manager() as manager:
            unitList = []
            for unit in manager.Manager.ListUnits():
                unit_element = (unit[0], unit[2], unit[3])
                unitList.append(unit_element)
            return unitList

    def get_unit_details(unitName):
        unit = Unit(unitName)
        unit.load()
        return unit

    def stop_unit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            unit.Unit.Stop(b'replace')
            return ServiceAction.SERVICE_STOP_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_STOP_FAILED

    def restart_unit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            unit.Unit.Restart(b'replace')
            return ServiceAction.SERVICE_RESTART_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_RESTART_FAILED

    def start_unit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            unit.Unit.Start(b'replace')
            return ServiceAction.SERVICE_START_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_START_FAILED

    def enable_unit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            subprocess.run(["sudo", "systemctl", "enable", unitName])
            return ServiceAction.SERVICE_ENABLE_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_ENABLE_FAILED

    def reload_daemon():
        try:
            subprocess.run(["systemctl", "daemon-reload"])
        except Exception as e:
            print(e)

    def remove_unit(service_name):
        print("Remove unit" + service_name)

    def load_service_logs(service_name):
        try:
            unit = Unit(service_name)
            unit.load()
            command = ["sudo", "journalctl", "-eu", service_name]
            with open(
                    str(pathlib.Path().resolve()) +
                    "/systemd/logs/service.log", "w") as f:
                subprocess.run(command, stdout=f)
            return ServiceAction.SERVICE_LOGS_LOAD_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_LOGS_LOAD_FAILED

    def get_service_logs(service_name):
        try:
            SystemdManager.load_service_logs(service_name)
            with open(
                    str(pathlib.Path().resolve()) +
                    "/systemd/logs/service.log", "r") as f:
                return f.read()
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_LOGS_LOAD_FAILED
