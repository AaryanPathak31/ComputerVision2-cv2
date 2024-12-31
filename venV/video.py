import os
import cv2

# Define the path to the video file
# The video file "monkey.mp4" is located in the "data" directory
video_path = os.path.join('.', 'data', 'monkey.mp4')

# Create a VideoCapture object to read the video
video = cv2.VideoCapture(video_path)

# Initialize a flag to keep the loop running
ret = True

# Loop to read and display each frame of the video
while ret:
    # Read the next frame from the video
    # 'ret' is True if the frame is successfully read, False otherwise
    # 'frame' contains the current frame as an image array
    ret, frame = video.read()
    
    # If 'ret' is False, the video has ended or an error occurred
    if not ret:
        break
    
    # Display the current frame in a window named 'frame'
    cv2.imshow('frame', frame)
    
    # Wait for 40 milliseconds before moving to the next frame
    # This controls the playback speed (~25 frames per second)
    cv2.waitKey(40)

# Release the VideoCapture object to free up resources
video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

video.release() #release the video
cv2.destroyAllWindows() #delete the open window i.e. frame