import cv2 # See video 1 for installation

# Replace "0" with a file path to work with a saved video
stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

# list of FourCC video codes: https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs
output = cv2.VideoWriter("assets/4_stream.mp4",
            cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
            fps=fps, frameSize=(width, height))

while True:
    ret, frame = stream.read()
    if not ret: # if no frames are returned
        print("No more stream :(")
        break
    
    frame = cv2.resize(frame, (width, height))
    output.write(frame)
    cv2.imshow("Webcam!", frame)
    if cv2.waitKey(1) == ord('q'): # press "q" to quit
        break

stream.release()
cv2.destroyAllWindows() #!