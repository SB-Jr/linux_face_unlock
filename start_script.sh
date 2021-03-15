dbus-monitor --session "type='signal',interface='org.freedesktop.ScreenSaver'" | while read x; do
    case "$x" in
      *"boolean true"*) python /home/sbjr/my_workspace/plasma_face_unlock/script.py;;
      *"boolean false"*) echo SCREEN_UNLOCKED;;  # track pid of script.py and kill it when screen is unlocked
    esac
  done
