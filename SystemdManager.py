
from pystemd.systemd1 import Manager

class SystemdManager():

    def getUnitsList():
        with Manager() as manager:

            unitList = []
            for unit, state in manager.Manager.ListUnitFiles():
                unitList.append(unit)

            return unitList