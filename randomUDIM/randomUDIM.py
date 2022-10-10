import maya.cmds as cmds
import random as random
import math as math

meshList = cmds.ls(sl=True)
UDIM_num = 3

for mesh in meshList:
	meshParent = cmds.listRelatives(parent=True)
	
	cmds.polySeparate(mesh, constructionHistory=False)
	compList = cmds.listRelatives(mesh, children=True)
	
	for comp in compList:
		intNumber = 0
		intNumber = int(math.floor(random.random()*UDIM_num))
		CompFace = comp + ".f[*]"
		cmds.polyEditUV(CompFace, uValue = intNumber, relative = True)
		print ("%s moved to UDIM_100%s" %(comp, intNumber + 1))
	    
	cmds.polyUnite(mesh, constructionHistory=False, mergeUVSets=True, name=mesh)
	cmds.parent(mesh, meshParent)
	
	print ("%s UDIM randomized successfully" %mesh)