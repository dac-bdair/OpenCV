import cv2
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


    #No Comment