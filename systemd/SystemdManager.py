from distutils import command
from pystemd.systemd1 import Manager, Unit
from systemd.ServiceAction import ServiceAction
import subprocess
import pathlib


class SystemdManager():
    def getUnitsList():
        with Manager() as manager:
            unitList = []
            for unit in manager.Manager.ListUnits():
                unit_element = (unit[0], unit[2], unit[3])
                unitList.append(unit_element)
            return unitList

    def getUnitDetails(unitName):
        unit = Unit(unitName)
        unit.load()
        return unit

    def stopUnit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            unit.Unit.Stop(b'replace')
            return ServiceAction.SERVICE_STOP_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_STOP_FAILED

    def restartUnit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            unit.Unit.Restart(b'replace')
            return ServiceAction.SERVICE_RESTART_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_RESTART_FAILED

    def startUnit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            unit.Unit.Start(b'replace')
            return ServiceAction.SERVICE_START_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_START_FAILED

    def enableUnit(unitName):
        try:
            unit = Unit(unitName)
            unit.load()
            subprocess.run(["sudo", "systemctl", "enable", unitName])
            return ServiceAction.SERVICE_ENABLE_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_ENABLE_FAILED

    def reloadDaemon():
        try:
            subprocess.run(["systemctl", "daemon-reload"])
        except Exception as e:
            print(e)

    def removeUnit(serviceName):
        print("Remove unit" + serviceName)

    def loadServiceLogs(serviceName):
        try:
            unit = Unit(serviceName)
            unit.load()
            command = ["sudo", "journalctl", "-eu", serviceName]
            with open(
                    str(pathlib.Path().resolve()) +
                    "/systemd/logs/service.log", "w") as f:
                subprocess.run(command, stdout=f)
            return ServiceAction.SERVICE_LOGS_LOAD_OK
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_LOGS_LOAD_FAILED

    def getServiceLogs(serviceName):
        try:
            SystemdManager.loadServiceLogs(serviceName)
            with open(
                    str(pathlib.Path().resolve()) +
                    "/systemd/logs/service.log", "r") as f:
                return f.read()
        except Exception as e:
            print(e)
            return ServiceAction.SERVICE_LOGS_LOAD_FAILED
