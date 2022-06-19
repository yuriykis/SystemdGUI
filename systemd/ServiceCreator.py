import subprocess
import getpass as gp
from pystemd.systemd1 import Manager, Unit
from SystemdManager import SystemdManager


class ServiceCreator():

    def create_service(service_name, service_description, service_exec_start):
        try:
            subprocess.run([
                "sudo", "touch",
                "/lib/systemd/system/%s.service" % service_name
            ])
            user_name = gp.getuser()
            subprocess.run([
                "sudo", "chown", user_name,
                "/lib/systemd/system/%s.service" % service_name
            ])
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
            ServiceCreator.enable_service(service_name)
            return (True, "Service %s created" % service_name)
        except Exception as e:
            print("Error: %s" % e)
            return (False, "Failed to create service %s" % service_name)

    def enable_service(service_name):
        try:
            SystemdManager.enable_unit(service_name + ".service")
        except Exception as e:
            print("Error: %s" % e)
