def from_rgb_to_yuv(rgb):
    #rgb[0] --> Red
    #rgb[1] --> Green
    #rgb[2] --> Blue

    YUV = [0,0,0] #Vector on guardarem els resultats

    #Utilitzem la fórmula per obtenir Y
    YUV[0] = 0.257 * rgb[0] + 0.504 * rgb[1] + 0.098 * rgb[2] + 16
    #Utilitzem la fórmula per obtenir Cb = U
    YUV[1] = -0.148 * rgb[0] - 0.291 * rgb[1] + 0.439 * rgb[2] + 128
    #Utilitzem la fórmula per obtenir Cr = V
    YUV[2] = 0.439 * rgb[0] - 0.368 * rgb[1] - 0.071 * rgb[2] + 128

    return YUV

def from_yuv_to_rgb(YUV):
    #YUV[0] --> Y
    #YUV[1] --> U
    #YUV[2] --> V

    rgb = [0,0,0] #Vector on guardarem els resultats

    #Utilitzem la fórmula per obtenir R
    rgb[0] = 1.164 * (YUV[0] - 16) + 1.596 * (YUV[2] - 128)
    #Utilitzem la fórmula per obtenir G
    rgb[1] = 1.164 * (YUV[0] - 16) - 0.813 * (YUV[2] - 128) - 0.391 * (YUV[1] - 128)
    #Utilitzem la fórmula per obtenir B
    rgb[2] = 1.164 * (YUV[0] - 16) + 2.018 * (YUV[1] - 128)

    return rgb

def main():
    rgb = [0,0,0]
    yuv = [0,0,0]

    #Demanem els valors a l'usuari i els guardem en la variable pertinent
    rgb[0] = float(input('Valor R'))
    while (rgb[0]<0 or rgb[0]>255):
        print('El valor introduït està fora dels límits, torna a introduir-ho')
        rgb[0] = float(input('Valor R'))

    rgb[1] = float(input('Valor G'))
    while (rgb[1]<0 or rgb[1]>255):
        print('El valor introduït està fora dels límits, torna a introduir-ho')
        rgb[1] = float(input('Valor G'))

    rgb[2] = float(input('Valor B'))
    while (rgb[2]<0 or rgb[2]>255):
        print('El valor introduït està fora dels límits, torna a introduir-ho')
        rgb[2] = float(input('Valor B'))

    yuv[0] = float(input('Valor Y'))
    while (yuv[0]<0 or yuv[0]>255):
        print('El valor introduït està fora dels límits, torna a introduir-ho')
        yuv[0] = float(input('Valor Y'))

    yuv[1] = float(input('Valor U'))
    while (yuv[1]<0 or yuv[1]>255):
        print('El valor introduït està fora dels límits, torna a introduir-ho')
        yuv[1] = float(input('Valor U'))

    yuv[2] = float(input('Valor V'))
    while (yuv[2]<0 or yuv[2]>255):
        print('El valor introduït està fora dels límits, torna a introduir-ho')
        yuv[2] = float(input('Valor V'))

    rgb_to_yuv = [0,0,0]
    yuv_to_rgb = [0,0,0]

    #Cridem a les funcions perquè facin la transformació
    rgb_to_yuv = from_rgb_to_yuv(rgb)
    print("El valor YUV és:", rgb_to_yuv)

    yuv_to_rgb = from_yuv_to_rgb(yuv)
    print("El valor RGB és:", yuv_to_rgb)

if __name__=="__main__":
    main()