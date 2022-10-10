import maya.cmds as cmds
import random as random
import math as math
from functools import partial

def connectButtonPush(udimfield, checkUnpack, *args):
	udimNum = cmds.intField(udimfield, query=True, value=True) 
	meshList = cmds.ls(sl=True)

	if (cmds.checkBox(checkUnpack, query=True, value=True)):
		for mesh in meshList:
			meshParent = cmds.listRelatives(mesh, parent=True)
			meshParentChildNum = len(cmds.listRelatives(meshParent, children=True))
			print (meshParentChildNum)
			if(meshParentChildNum == 1):
				temp = cmds.spaceLocator(name='tempLocator')
				cmds.parent(temp, meshParent)
			cmds.polySeparate(mesh, name = 'comp_#', constructionHistory=False)
			compList = cmds.listRelatives(mesh, children=True)
			
			for comp in compList:
				intNumber = int(math.floor(random.random()*udimNum))
				compFace = comp + '.f[*]'
				cmds.polyEditUV(compFace, uValue = intNumber, relative = True)
				print ('%s moved to UDIM_100%s' %(comp, intNumber + 1))
		
			cmds.polyUnite(mesh, name=mesh, constructionHistory=False, mergeUVSets=True)
			cmds.parent(mesh, meshParent)

			if(meshParentChildNum == 1):
				cmds.delete(temp)

			print ("%s UDIM randomized successfully" %mesh)
			
	else:
		for mesh in meshList:
			intNumber =  int(math.floor(random.random()*udimNum))
			meshFace = mesh + '.f[*]'
			cmds.polyEditUV(meshFace, uValue = intNumber, relative = True)
			print ("%s moved to UDIM_100%s" %(mesh, intNumber + 1))

def randUDIM():

	window = cmds.window( title = 'randomUDIM', iconName = 'randUDIM', widthHeight = (250, 150), sizeable = False)
	cmds.frameLayout('Randomize settings', labelAlign ='top', borderStyle ='in')
	cmds.rowColumnLayout(numberOfColumns = 2, columnWidth = [(1, 80), (2, 120)], columnSpacing = [(1,10), (2,10)] )
	cmds.text(label = 'UDIM number', align = 'right')
	udimfield = cmds.intField(value = 3)
	cmds.setParent('..')

	cmds.columnLayout(adjustableColumn=True)
	checkUnpack = cmds.checkBox( label = 'Unpack combined meshes.\n(Cannot work with referenced object)', value = False)
	cmds.setParent('..')

	cmds.button( label = 'Randomize UDIM', command = partial(connectButtonPush, udimfield, checkUnpack))
	cmds.showWindow()
	
if __name__=='__main__':
    randUDIM()