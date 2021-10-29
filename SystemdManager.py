
from pystemd.systemd1 import Manager

class SystemdManager():

    def getUnitsList():
        with Manager() as manager:

            unitList = []
            for unit, state in manager.Manager.ListUnitFiles():
                unit_element = (unit, state)
                unitList.append(unit_element)

            return unitList