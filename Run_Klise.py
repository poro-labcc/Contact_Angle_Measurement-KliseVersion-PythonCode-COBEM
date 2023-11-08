"""
Created on Mon Jun  5 15:21:50 2023

author: Christoph Zevenbergen
"""


#Klise code for contact angle measurement
import numpy as np
import Library_Klise as K
import os



radius =   14
plane  = '101'
size   =   80
angle  =   90

directory = '/home/usuario/Documentos/teste'
output_file_name = f'Droplet_R{radius}_P{plane}'
input_file = f'/home/usuario/Documentos/Raw/P{plane}R{radius}x{size}/Droplet_{size}x{size}x{size}_R{radius}_P{plane}_Angulo{angle}.raw'  

npimg = np.fromfile(input_file, dtype=np.uint8)
npimg.astype(int)
imageSize = (size, size, size)
npimg = npimg.reshape(imageSize)

# d  -> Search radius of points for linear regression of the plane
#       d = 4 for radius 7, 14, 28 and d = 5 for radius 56

#Result in radians
theta = K.Klise(npimg, d = 4)

#Convert to degree
theta = theta*180/np.pi

if not os.path.exists(f'{directory}'):       
    os.makedirs(f'{directory}') 
np.save(f"{directory}/{output_file_name}_Results_theta", theta)

