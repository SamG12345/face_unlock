import cv2 as cv
import face_recognition
import matplotlib.pyplot as plt
import threading

lock = threading.Lock()
saved_image = face_recognition.load_image_file("C://im.jpg")
known_faces = face_recognition.face_encodings(face_image = saved_image,
                                                num_jitters=7,
                                                model='small')[0]
run = 0
def b():
    
    global known_faces
    saved_image = face_recognition.load_image_file("C://abc.png")
    known_faces = face_recognition.face_encodings(face_image = saved_image,
                                                num_jitters=7,
                                                model='small')[0]
    print("another image")
def a(f):
    global run
    try:
        frame = f
        
        face_encoding = face_recognition.face_encodings(face_image = frame,
                                                        num_jitters=7,
                                                        model='small')[0]
        results = face_recognition.compare_faces([known_faces], face_encoding)

        if results[0]:
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.putText(img, 'abc', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1,
                            (255,0,0), 2, cv.LINE_AA)
            print('ABC Enter....')
            
            run = 1
        else:
            run = -1
            raise Exception("Errrrrrrrrrrr")
    except:
        pass
def cam():
    video = cv.VideoCapture(0)

    if not video:
        print("Error capture")
        exit()

    while True:
        ret, frame = video.read()

        face_locations = face_recognition.face_locations(frame)
        print(face_locations)
        for face_location in face_locations:
                top, right, bottom, left = face_location
                #Draw a rectangle with blue line borders of thickness of 2 px
                frame = cv.rectangle(frame,  (right,top), (left,bottom), color = (0,0, 255), thickness=2)
            # Check the each faces location in each frame
        
        cv.imshow('Frame', frame)
        
        
        t1 = threading.Thread(target=a, args=(frame,))
        t1.start()
        t1.join()

        if run==1:
            print("Matched")
            break
        if run == -1:
            print("changing")
            t2 = threading.Thread(target=b)
            t2.start()
            t2.join()

        if cv.waitKey(1) == ord('q'):
            break
        
    video.release()


if __name__ == "__main__":
    print("start")
    cam()
    
    cv.destroyAllWindows()