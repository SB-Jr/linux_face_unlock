dbus-monitor --session "type='signal',interface='org.freedesktop.ScreenSaver'" |
  while read x; do
    case "$x" in
      *"boolean true"*) python script.py;;
      *"boolean false"*) echo SCREEN_UNLOCKED;;  
    esac
  done