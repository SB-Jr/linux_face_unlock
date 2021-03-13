import os
import time
import cv2
import pickle
import face_recognition


def get_encodings():
    with open('encodings.pkl', 'rb') as f:
        encodings = pickle.load(f)
        return encodings


def unlock(encodings):
    cap = cv2.VideoCapture(0)
    for i in range(5):
        _, frame = cap.read()
        face_loc = face_recognition.face_locations(frame, model='cnn')
        encoding = face_recognition.face_encodings(frame, face_loc)
        
        if len(encoding) >= 1:
            result = face_recognition.compare_faces(encodings, encoding[0])
            if True in result:
                print('found')
                os.system('loginctl unlock-session')
                break
            else:
                print('mismatch')
        time.sleep(1)
    cap.release()


if __name__ == '__main__':
    encodings = get_encodings()
    print('ready')
    time.sleep(10)
    unlock(encodings)
    print('done')

