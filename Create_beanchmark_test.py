import numpy as np
import os.path


def Droplet_P001(I, J, K, raio, angulo):
    D=np.ones((I,J,K),dtype="uint8")
    a: int = K/10
    cx = I/2
    cy = J/2
    cz = a + 0.5 + raio*np.cos(angulo)
    for i in range(0,I):
        for j in range (0, J):
            for k in range (0, K):
                dist = np.sqrt((i-cx)*(i-cx) + (j-cy)*(j-cy) + (k-cz)*(k-cz))
                if (dist <= raio) :
                    D[i,j,k] = 2
                if k <= a:
                    D[i,j,k] = 0
    if(raio<=2):print("raio menor que a distância da parede")
    return D;

def Droplet_P101(I, J, K, raio, angulo):
    D = np.ones((I,J,K),dtype="uint8")
    h = raio*np.cos(angulo)
    ad = h/np.sqrt(2)
    cy = J/2
    cx = cz = (int(2*K/3)-1)/2 +1/4 + ad
    for i in range(0,I):
        for j in range (0, J):
            for k in range (0, K):
                dist = np.sqrt((i-cx)*(i-cx) + (j-cy)*(j-cy) + (k-cz)*(k-cz))
                if (dist <= raio) :
                    D[i,j,k] = 2
                if k < int(2*K/3) - i:
                    D[i,j,k] = 0
    return D;

def Droplet_P111(I, J, K, raio, angulo):
    D = np.ones((I,J,K),dtype="uint8")
    h = raio*np.cos(angulo)
    ad = h/np.sqrt(3)
    cx = cy = cz = (K-0.5)/3 + ad
    for i in range(0,I):
        for j in range (0, J):
            for k in range (0, K):
                dist = np.sqrt((i-cx)*(i-cx) + (j-cy)*(j-cy) + (k-cz)*(k-cz))
                if (dist < raio) :
                    D[i,j,k] = 2
                if k < K - i - j:
                    D[i,j,k] = 0
    return D;


Radius = [  7,  14,  28,  56]
Size   = [ 40,  80,  80, 140]
Plane  = ['001', '101', '111']
Angle  = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]
directory = '/home/usuario/Documentos/Droplets_raw'

for i in range(len(Radius)):
    radius = Radius[i]
    X = Y = Z = Size[i]
    for plane in Plane:
        for angle in Angle:
            angle_rad = angle*np.pi/180
            if plane == '001':
                P = Droplet_P001(X, Y, Z, radius, angle_rad)
            elif plane == '101':
                P = Droplet_P101(X, Y, Z, radius, angle_rad)
            elif plane == '111':
                P = Droplet_P111(X, Y, Z, radius, angle_rad)
            if not os.path.exists(f'{directory}/P{plane}R{radius}x{X}'):
                os.mkdir(f'{directory}/P{plane}R{radius}x{X}')
            P.tofile(f'{directory}/P{plane}R{radius}x{X}/Droplet_{X}x{Y}x{Z}_R{radius}_P{plane}_Angle{angle}.raw')
           





