from vpython import *
import numpy as np
from time import sleep
from numpy import genfromtxt

#definitions
toRad=2*np.pi/360
toDeg=1/toRad

#scene.forward=vector(-1,-1,-1)

#import data
my_data = genfromtxt('ori3.csv', delimiter=';')
nr_row=(my_data.shape[0])

#xarrow=arrow(lenght=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
#yarrow=arrow(lenght=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
#zarrow=arrow(lenght=4, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))

#frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
#upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
#sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

#desigh your gear
distant_light(direction=vec(0, - 1, 0), color=color.magenta)
local_light(pos=vec(- 3, 1, - 2), color=color.red)
board=box(lenght=.9,width=.4,height=.05,color=color.white)
board.opacity=.2
board.pos=vector(0,0,0)
mast=box(lenght=.15,width=.02,height=.76,color=color.white)
mast.length=.15
mast.opacity=.2
mast.pos=vector(.4,-.38,0)
fw=box(lenght=.18,width=1.15,height=.03,color=color.white)
fw.length=.18
fw.opacity=.2
fw.pos=vector(.2,-.8,0)
fuse=box(lenght=.65,width=.05,height=.05,color=color.white)
fuse.length=.65
fuse.opacity=.2
fuse.pos=vector(.5,-.78,0)
rw=box(lenght=.05,width=.36,height=.01,color=color.white)
rw.length=.05
rw.opacity=.2
rw.pos=vector(.8,-.76,0)

myObj=compound([board,mast,fw,fuse,rw])

   
for i in range(nr_row-1):
  x=(my_data[i+1,0])
  y=(my_data[i+1,1])
  z=(my_data[i+1,2])
  roll=float(z)*toRad*(-1)
  pitch=float(y)*toRad
  yaw=float(x)*toRad+np.pi
  #print("Roll=",roll*toDeg," Pitch=",pitch*toDeg,"Yaw=",yaw*toDeg)
  #rate(50)
  k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
  y=vector(0,1,0)
  s=cross(k,y)
  v=cross(s,k)
  vrot=v*cos(roll)+cross(k,v)*sin(roll)
  #frontArrow.axis=k
  #sideArrow.axis=cross(k,vrot)
  #upArrow.axis=vrot
  myObj.axis=k
  myObj.up=vrot
  #sideArrow.length=2
  #frontArrow.length=4
  #upArrow.length=1
  sleep(0.1) # data points 10 per second 

  
