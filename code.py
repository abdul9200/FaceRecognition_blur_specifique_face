import face_recognition
import cv2

# This is a demo of blurring faces in video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

obama_image=face_recognition.load_image_file("obama.jpg")
obama_visage_signature=face_recognition.face_encodings(obama_image)[0]

 # charger la deuxiéme image de personne est apprendre au système a la reconnaitre  .
biden_image = face_recognition.load_image_file("biden.jpg")
biden_visage_signature = face_recognition.face_encodings(biden_image)[0]

# creer un tableau des signature des visages associés au nom de personnes
reconnu_visage_signatures = [
    obama_visage_signature,
    biden_visage_signature
]

# Initialize some variables
face_locations = []

while True:
    
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = frame

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)
    visage_signatures=face_recognition.face_encodings(small_frame, face_locations)
    print(face_locations)
    # Display the results
    for (top, right, bottom, left),visage_signature in zip(face_locations,visage_signatures):
        matches = face_recognition.compare_faces(reconnu_visage_signatures, visage_signature)
        print('Try it')

	    # Si une correspondance est retrouvé dans les reconne_visage_signatures, seulement prendre le premier!
        if True in matches:
		# Scale back up face locations since the frame we detected in was scaled to 1/4 size
         

            # Extract the region of the image that contains the face
            face_image = frame[top:bottom, left:right]

            # Blur the face image
            face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

            # Put the blurred face region back into the frame image
            frame[top:bottom, left:right] = face_image

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()