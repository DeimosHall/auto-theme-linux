import subprocess
import os


class Theme:
    
    def set_dark(self):
        result = subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "ZorinBlue-Dark"])
        return result.returncode

    def set_light(self):
        result = subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "ZorinBlue-Light"])
        return result.returncode

    def get(self):
        command = 'gsettings list-recursively org.gnome.desktop.interface | grep "gtk-theme"'
        result = os.popen(command).read()
        return result.split()[2]