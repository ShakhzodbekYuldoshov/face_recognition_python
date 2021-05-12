import face_recognition
import numpy as np
import cv2 as cv

#all informations necessary for training
img = face_recognition.load_image_file('image1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
faceloc = face_recognition.face_locations(img)[0]
encode_img = face_recognition.face_encodings(img)[0]

#capture the video
capture = cv.VideoCapture(0)

#loop through the every frame of captured video
while True:

    # Get the frame
    ret, frame = capture.read()

    #Convert BGR to RGB for comparing with training image
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # get face location from the frame
    faceloc = face_recognition.face_locations(frame)[0]

    #encode the frame to binary
    encode_frame = face_recognition.face_encodings(frame)[0]

    #draw rectangle around the face
    cv.rectangle(frame, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 255, 0), 4)

    # Compare the detected face and the training image's face
    results = face_recognition.compare_faces([encode_img], encode_frame)
    print(results)

    #converting back RGB to BGR for opencv
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    #print all the frames
    cv.imshow('Video', frame)

    #exit the loop
    if cv.waitKey(20) & 0xFF==ord('q'):
        break


capture.release()
cv.destroyAllWindows()
