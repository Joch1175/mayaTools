import maya.cmds as cmds
import random as random
import math as math

UDIM_num = 3
meshList = cmds.ls(sl=True)

for mesh in meshList:
	intNumber =  int(math.floor(random.random()*UDIM_num))
	meshFace = mesh + ".f[*]"
	cmds.polyEditUV(meshFace, uValue = intNumber, relative = True)
	print ("%s moved to UDIM_100%s" %(mesh, intNumber + 1))