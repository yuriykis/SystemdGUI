from pystemd.systemd1 import Manager


class SystemdManager():
    def getUnitsList():
        with Manager() as manager:

            unitList = []
            for unit in manager.Manager.ListUnits():
                unit_element = (unit[0], unit[2], unit[3])
                unitList.append(unit_element)
            return unitList

    def getUnitDetails(unitName):
        with Manager() as manager:
            unit = manager.Manager.GetUnit(unitName)
            return unit
