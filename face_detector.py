from imutils import paths
import face_recognition
import cv2
import os

# Variables

# directories 
input_dir = "input/"
photoset_dir = "photoset/"
output_dir = "output/"

# resize factor
maxEdgeLength = 600 #px


def drawRectangleAroundFaces(face_location, photo):
    for coordinate in face_location:
        cv2.rectangle(photo, ( coordinate[3], coordinate[0]), (coordinate[1], coordinate[2]), color = (0, 0, 255), thickness = 2)
    cv2.imwrite('ROI_{}.png'.format(sum(coordinate)), photo)
    print('[INFO] File ROI_{} was saved.'.format(sum(coordinate)))


def resizePhoto(photo, maxEdgeLength = maxEdgeLength):
    height, width = (photo.shape[:2])
    if height > width:
        resizedPhoto = cv2.resize(photo,(int(maxEdgeLength/height*width), maxEdgeLength))
    else:
        resizedPhoto = cv2.resize(photo, (maxEdgeLength, int(maxEdgeLength/width*height)))
    print('[INFO] Image was resized to {}'.format(imgDirectory, resizedPhoto.shape[:2]))
    return resizedPhoto


def faceEncodings(imgDirectory, model):
    faces_img = face_recognition.load_image_file(imgDirectory, mode='RGB')
    faces_img = resizePhoto(faces_img)
    faces_locations = face_recognition.face_locations(faces_img, model=model)
    faces_encodings = face_recognition.face_encodings(faces_img, known_face_locations=faces_locations, num_jitters=1)
    return faces_encodings


def makeCopy(imgDirectory, output_dir):
    img = face_recognition.load_image_file(imgDirectory, mode='RGB')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    head, tail = os.path.split(imgDirectory) #extracting file name from the path
    cv2.imwrite('{}{}'.format(output_dir, tail), img)


def compareFaces(facesToFind, recognizedFaces):
    rightPhoto = True
    for face in facesToFind:
        if True in face_recognition.compare_faces(face, recognizedFaces, 0.6):
            pass
        else:
            rightPhoto = False
            print('[INFO] None matching.')

    if rightPhoto:
        print('[INFO] Matched photo!')
        makeCopy(imgDirectory, output_dir)


print('####################################')
print('### Temple of the Many-Faced God ###')
print('####################################')

examples_dir = paths.list_images(input_dir)

for imgDirectory in examples_dir:
    facesToFind = faceEncodings(imgDirectory, 'hog')
    print("[INFO] I will look for {} face(s).".format(len(facesToFind)))
    print("-----------")

photos_dirs = paths.list_images(photoset_dir)

if len(facesToFind) > 0:
    for imgDirectory in photos_dirs:
        recognizedFaces = faceEncodings(imgDirectory, 'hog')
        print("[INFO] Found {} face(s).".format(len(recognizedFaces)))
        try:
            compareFaces(facesToFind, recognizedFaces)
        except ValueError:
            print("[WARNING] No faces in the photo.")
else:
    print("[WARNING] No faces to find")