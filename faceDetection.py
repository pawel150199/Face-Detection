import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To use videa from webcam
cap = cv2.VideoCapture(0)

# To import video from file
#cap = cv2.VideoCapture('filename.mp4')

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle aroud faces to highlight them
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    
    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()


