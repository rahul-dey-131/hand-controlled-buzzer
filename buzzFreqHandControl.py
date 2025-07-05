import cv2
import numpy as np
import time
import handTrackingModule as htm  # Importing the hand tracking module
import math
import serial  # Importing the serial module for communication with Arduino

###################
wCam, hCam = 640, 480  # Width and height of the camera feed
pTime = 0  # Previous time for FPS calculation (Initialized to 0)
###################

arduinoData = serial.Serial('com3', 9600)  # Initialize serial communication with Arduino
time.sleep(2)  # Wait for the connection to establish

cap = cv2.VideoCapture(0)  # Open the first camera
cap.set(3, wCam)  # Set the width of the camera feed
cap.set(4, hCam)  # Set the height of the camera feed

detector = htm.handDetector(detectionCon=0.75)  # Create an instance of the hand detector class

while True:
    success, img = cap.read()  # Read a frame from the camera
    if not success:
        break  # Exit if the frame is not read successfully
    
    img = cv2.flip(img, 1)  # Flip the image horizontally for a mirror effect
    img = detector.findHands(img)  # Detect hands in the image
    lmList = detector.findPosition(img, draw=False)  # Get the positions of the landmarks without drawing them
    if len(lmList):
        thumblm, indexlm = lmList[4], lmList[8]  # Print the list of landmarks to the console
        midpoint = ((thumblm[1] + indexlm[1]) // 2, (thumblm[2] + indexlm[2]) // 2)  # Calculate the midpoint between thumb and index finger
        
        length = math.hypot(thumblm[1] - indexlm[1], thumblm[2] - indexlm[2])  # Calculate the distance between thumb and index finger
        
        arduinoData.write((str(int(length)) + '\r').encode())  # Send the length to Arduino
        
        print(length)  # Print the length to the console
        
        cv2.circle(img, (thumblm[1], thumblm[2]), 10, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (indexlm[1], indexlm[2]), 10, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, midpoint, 10, (0, 255, 255), cv2.FILLED)  # Draw a circle at the midpoint
        cv2.line(img, (thumblm[1], thumblm[2]), (indexlm[1], indexlm[2]), (255, 0, 255), 3)  # Draw a line between the thumb and index finger
    
        if length < 30 or length > 240:
            cv2.circle(img, midpoint, 10, (0, 0, 255), cv2.FILLED)  # Draw a circle at the midpoint

    
    cTime = time.time()  # Get the current time
    fps = 1 / (cTime - pTime)  # Calculate frames per second
    # cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Display FPS on the image
    pTime = cTime   # Update previous time

    # Display the image in a window
    cv2.imshow("Camera Feed", img)
    time.sleep(0.05)  # Sleep for a short duration to control the frame rate
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break