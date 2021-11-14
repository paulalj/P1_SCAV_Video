import os, sys
import cv2
import numpy as np

def main():
    image = 'Ona_tortu.jpg'
    img = cv2.imread(image, 0) #Llegim la imatge en blanc i negre
    img_num = np.float32(img) #La passem a floats
    num_dct = cv2.dct(img_num) #Fem la DCT
    cv2.imwrite('Ona_tortu_DCT.jpg', num_dct) #Guardem la imatge

    num_idct = cv2.idct(num_dct) #Fem la inversa, és a dir, decodifiquem
    cv2.imwrite('Ona_tortu_IDCT.jpg', num_idct) #Guardem la imatge

if __name__=="__main__":
    main()