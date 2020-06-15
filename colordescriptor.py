import numpy as np
import cv2
import imutils

class ColorDescriptor:
    def __init__(self,bins): 
        #numarul de bins pentru histograma
        self.bins = bins

    def describe(self, image):
        #transforma din RGB in HSV
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []
        

        (h,w) = image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))

        #impartirea imaginii in 4 parti (stanga-sus, dreapta-sus, dreapta-jos, 
        # stanga-jos)
        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),             (0, cX,cY,h)]

        #construim o elipsa care sa reprezinte centrul imaginii
        (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)


        for(startX, endX, startY, endY) in segments:
            #construim o masca pentru fiecare colt al imaginii
            cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)

        #extragem o histograma pentru elipsa din imagine
        hist = self.histogram(image, cornerMask)
        features.extend(hist)
            

        return features
    
    def histogram(self, image, mask):
        #extragem o histograma pentru partea mascata a imaginii folosind numarul de "bins"
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])

        #se normalizeaza histograma
        hist = cv2.normalize(hist, hist).flatten()
        
        return hist
    


