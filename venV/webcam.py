import cv2

# Initialize the webcam (0 refers to the default camera)
# The VideoCapture object will capture the video stream from the webcam
webcam = cv2.VideoCapture(0)

# Loop to continuously capture frames from the webcam
while True:
    # Read the next frame from the webcam
    # 'ret' is True if the frame was successfully captured, False otherwise
    # 'frame' contains the current image frame from the webcam
    ret, frame = webcam.read()

    # Display the current frame in a window named 'frame'
    cv2.imshow('frame', frame)

    # Wait for 40 milliseconds for a key event
    # If the user presses the 'q' key (ASCII value for 'q' is 113), break the loop
    if cv2.waitKey(40) & 0xFF == ord('q'): # q to cose the window
        break

# Release the webcam to free up resources
webcam.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
