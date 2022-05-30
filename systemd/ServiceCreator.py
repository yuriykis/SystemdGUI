from pystemd.systemd1 import Manager, Unit
from .SystemdManager import SystemdManager


class ServiceCreator():

    def createService(self, service_name, service_description,
                      service_exec_start):
        try:
            with open("/lib/systemd/system/%s.service" % service_name,
                      "w") as f:
                f.write("[Unit]\n")
                f.write("Description=%s\n" % service_description)
                f.write("\n")
                f.write("[Service]\n")
                f.write("ExecStart=%s\n" % service_exec_start)
                f.write("\n")
                f.write("[Install]\n")
                f.write("WantedBy=multi-user.target\n")
            self.enableService(service_name)
        except Exception as e:
            print("Error: %s" % e)

    def enableService(self, service_name):
        try:
            SystemdManager.enable_unit(service_name + ".service")
        except Exception as e:
            print("Error: %s" % e)
