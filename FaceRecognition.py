import cv2
import numpy as np
import face_recognition
from face_recognition import face_locations

imgMJ = face_recognition.load_image_file('Image/MJ.jpeg')
imgMJ = cv2.cvtColor(imgMJ,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Image/MJ2.jpeg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMJ)[0]
encodeMJ = face_recognition.face_encodings(imgMJ)[0]
cv2.rectangle(imgMJ,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeMJ],encodeTest)
faceDist = face_recognition.face_distance([encodeMJ],encodeTest)
print(results,faceDist)
cv2.putText(imgTest,f'{results} {round(faceDist[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)

cv2.imshow("Micheal Jordan", imgMJ)
cv2.imshow("Micheal Jordan Test", imgTest)

cv2.waitKey(0)