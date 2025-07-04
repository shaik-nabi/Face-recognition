import cv2
face_cap = cv2.CascadeClassifier("file_path = "path/to/your/file.xml"" ) # Replace this with your actual file
video_cap = cv2.VideoCapture(0)
while True :
    ret , video_data = video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10) == ord("e"):
        break
video_cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1) 
