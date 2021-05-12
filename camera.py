import cv2 as cv


capture = cv.VideoCapture(0)

# Camera is for taking photos without using your phone
while True:
    isTrue, frame = capture.read()

    cv.imshow('Frame', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
    if cv.waitKey(20) & 0xFF == ord('f'):
        cv.imwrite('image.jpg', frame)


capture.release()
cv.destroyAllWindows()
