# http://docs.qtile.org/en/latest/manual/config/gnome.html
import subprocess
import os

from libqtile import hook

@hook.subscribe.startup
def dbus_register():
    id = os.environ.get('DESKTOP_AUTOSTART_ID')
    if not id:
        return
    subprocess.Popen(['dbus-send',
                      '--session',
                      '--print-reply',
                      '--dest=org.gnome.SessionManager',
                      '/org/gnome/SessionManager',
                      'org.gnome.SessionManager.RegisterClient',
                      'string:qtile',
                      'string:' + id])


FILES = {
    '/usr/share/xsessions/qtile_gnome.desktop': '''
[Desktop Entry]
Name=Qtile GNOME
Comment=Tiling window manager
TryExec=/usr/bin/gnome-session
Exec=gnome-session --session=qtile
Type=XSession
'''.strip(),
    '/usr/share/gnome-session/sessions/qtile.session': '''
[GNOME Session]
Name=Qtile session
RequiredComponents=qtile;gnome-settings-daemon;
'''.strip(),
    '/usr/share/applications/qtile.desktop': '''
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Qtile
Exec=qtile
NoDisplay=true
X-GNOME-WMName=Qtile
X-GNOME-Autostart-Phase=WindowManager
X-GNOME-Provides=windowmanager
X-GNOME-Autostart-Notify=false
'''.strip(),
}


def main():
    for path, content in FILES.items():
        if not os.path.exists(path):
            with open(path, 'w+') as f:
                f.write(content)
