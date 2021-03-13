import os
import pickle
import face_recognition


def get_encodings(db_path):
    print('genrating encdings from ', db_path)
    encodings = []
    for file in os.listdir(db_path):
        file_path = os.path.join(db_path, file)
        image = face_recognition.load_image_file(file_path)
        face_loc = face_recognition.face_locations(image, model='cnn')
        encoding = face_recognition.face_encodings(image, face_loc)
        encodings.append(encoding[0])
    print('done generating encodings')
    return encodings


def write_to_file(encodings):
    with open('encodings.pkl', 'wb') as f:
        pickle.dump(encodings, f)


if __name__ == '__main__':
    encodings = get_encodings('test_images/db')
    write_to_file(encodings)