from pystemd.systemd1 import Manager, Unit


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
        unit = Unit(unitName)
        unit.load()
        unit.Unit.Stop(b'replace')

    def restartUnit(unitName):
        unit = Unit(unitName)
        unit.load()
        unit.Unit.Restart(b'replace')

    def startUnit(unitName):
        unit = Unit(unitName)
        unit.load()
        unit.Unit.Start(b'replace')
