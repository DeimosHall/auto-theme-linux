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
        result = result.split()[2]  # The third position contains the name of the theme
        result = result.strip("'")  # Removes the ' from the start and the end
        return result

theme = Theme()