import os
import time
import cv2
import pickle
import subprocess
import face_recognition


def get_encodings():
    with open('/home/sbjr/my_workspace/plasma_face_unlock/encodings.pkl', 'rb') as f:
        encodings = pickle.load(f)
        return encodings


def is_screen_locked():
    is_locked = subprocess.check_output(
        'qdbus org.kde.screensaver /org/freedesktop/ScreenSaver org.freedesktop.ScreenSaver.GetActive',
        shell=True
    ).decode()
    if 'false' in is_locked:
        return False
    else:
        return True
    

def unlock(encodings):
    while(is_screen_locked()):
        cap = cv2.VideoCapture(0)
        # check for 10 images continuously with 1 second of gap in between
        for i in range(10):
            _, frame = cap.read()
            face_loc = face_recognition.face_locations(frame, model='cnn')
            if len(face_loc) < 1:
                continue
            encoding = face_recognition.face_encodings(frame, face_loc)

            if len(encoding) >= 1:
                result = face_recognition.compare_faces(encodings, encoding[0])
                if True in result:
                    print('face matched successfully')
                    os.system('loginctl unlock-session')
                    break
                else:
                    print('face mismatch')
            time.sleep(1)
        cap.release()
        
        # if screen is unlocked by user or by the script then end the loop
        if not is_screen_locked():
            break

        # sleep for some time (10 seconds)
        time.sleep(10)


if __name__ == '__main__':
    if is_screen_locked():
        encodings = get_encodings()
        print('encodings loaded')
        # making sure that the screen is not unlocked just after being locked
        time.sleep(10)
        unlock(encodings)
        print('closing the app')

