from pystemd.systemd1 import Manager, Unit


class ServiceCreator():
    def createService(self):
        self.unit = Unit()
        self.unit.load()
        self.unit.set("Unit", "Description", "Created by SystemdGUI")
        self.unit.set("Unit", "Documentation", "Created by SystemdGUI")
