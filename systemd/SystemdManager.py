from distutils import command
from pystemd.systemd1 import Manager, Unit
from ServiceAction import ServiceAction
import subprocess
import pathlib


class SystemdManager():

    def get_units_list():
        with Manager() as manager:
            unit_list = []
            for unit in manager.Manager.ListUnits():
                unit_element = (unit[0], unit[2], unit[3])
                unit_list.append(unit_element)
            return unit_list

    def get_unit_details_Unit(unit_name):
        unit = Unit(unit_name)
        unit.load()
        return unit.Unit

    def get_unit_details_Service(unit_name):
        unit = Unit(unit_name)
        unit.load()
        return unit.Service

    def stop_unit(unit_name):
        try:
            unit = Unit(unit_name)
            unit.load()
            unit.Unit.Stop(b'replace')
            return ServiceAction.SERVICE_STOP_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_STOP_FAILED

    def restart_unit(unit_name):
        try:
            unit = Unit(unit_name)
            unit.load()
            unit.Unit.Restart(b'replace')
            return ServiceAction.SERVICE_RESTART_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_RESTART_FAILED

    def start_unit(unit_name):
        try:
            unit = Unit(unit_name)
            unit.load()
            unit.Unit.Start(b'replace')
            return ServiceAction.SERVICE_START_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_START_FAILED

    def enable_unit(unit_name):
        try:
            unit = Unit(unit_name)
            unit.load()
            subprocess.run(["sudo", "systemctl", "enable", unit_name])
            return ServiceAction.SERVICE_ENABLE_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_ENABLE_FAILED

    def reload_daemon():
        try:
            subprocess.run(["sudo", "systemctl", "daemon-reload"])
        except Exception as e:
            print(e)

    def reset_failed():
        try:
            subprocess.run(["sudo", "systemctl", "reset-failed"])
        except Exception as e:
            print(e)

    def remove_unit(service_name):
        try:
            subprocess.run(["sudo", "systemctl", "stop", service_name])
            subprocess.run(["sudo", "systemctl", "disable", service_name])
            subprocess.run([
                "sudo", "rm",
                "/lib/systemd/system/%s.service" % service_name
            ])
            subprocess.run([
                "sudo", "rm",
                "/usr/lib/systemd/system/%s.service" % service_name
            ])
            SystemdManager.reload_daemon()
            SystemdManager.reset_failed()
            return ServiceAction.SERVICE_REMOVE_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_REMOVE_FAILED

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
