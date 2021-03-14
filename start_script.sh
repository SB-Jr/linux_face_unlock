dbus-monitor --session "type='signal',interface='org.freedesktop.ScreenSaver'" |
  while read x; do
    case "$x" in
      *"boolean true"*) python script.py;;       # find a way to continually to this until screen unlock
      *"boolean false"*) echo SCREEN_UNLOCKED;;  # track pid of script.py and kill it when screen is unlocked
    esac
  done