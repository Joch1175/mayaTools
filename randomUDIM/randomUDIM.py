import maya.cmds as cmds
import maya.OpenMaya as om
import random as random
import math as math

from functools import partial

def getUvShelList(name):
	selList = om.MSelectionList()
	selList.add(name)
	selListIter = om.MItSelectionList(selList, om.MFn.kMesh)
	pathToShape = om.MDagPath()
	selListIter.getDagPath(pathToShape)
	meshNode = pathToShape.fullPathName()
	uvSets = cmds.polyUVSet(meshNode, query=True, allUVSets =True)
	allSets = []
	for uvset in uvSets:
		shapeFn = om.MFnMesh(pathToShape)
		shells = om.MScriptUtil()
		shells.createFromInt(0)
		# shellsPtr = shells.asUintPtr()
		nbUvShells = shells.asUintPtr()
 
		uArray = om.MFloatArray()   #array for U coords
		vArray = om.MFloatArray()   #array for V coords
		uvShellIds = om.MIntArray() #The container for the uv shell Ids
 
		shapeFn.getUVs(uArray, vArray)
		shapeFn.getUvShellsIds(uvShellIds, nbUvShells, uvset)
		
		# shellCount = shells.getUint(shellsPtr)
		shells = {}
		for i, n in enumerate(uvShellIds):
			if n in shells:
				# shells[n].append([uArray[i],vArray[i]])
				shells[n].append( '%s.map[%i]' % ( name, i ) )
			else:
				# shells[n] = [[uArray[i],vArray[i]]]
				shells[n] = [ '%s.map[%i]' % ( name, i ) ]
		allSets.append({uvset: shells})
	return allSets

def connectButtonPush(numField, *args):

	UDIM_num = cmds.intField(numField, query=True, value=True)
	meshList = cmds.ls(sl=True)

	for mesh in meshList:
		meshShellDict = getUvShelList(mesh)
		meshShellDict = meshShellDict[0]['map1']
		meshShellNum = len(meshShellDict)
		UDIMList = [[] for i in range(UDIM_num)]

		# random mark
		for key in meshShellDict:
			intNumber =  int(math.floor(random.random()*UDIM_num))
			UDIMList[intNumber].append(key)
		
		# move UDIM
		for i in range(len(UDIMList)):
			cmds.select(clear = True)
			for shellNum in UDIMList[i]:
				cmds.select(meshShellDict[shellNum][0], add=True)
			cmds.polyEditUVShell(uValue = i, relative = True)
			selection = cmds.ls(sl=True)
			udimNum = i+1001
			#print (selection)
			print ("%s shells are moved to %s" %(len(selection), i+1001))

def randomUDIM():
		
	window = cmds.window( title = 'randomUDIM', iconName = 'autoAS', widthHeight = (250, 100), sizeable = False)
	cmds.frameLayout('UDIM', labelAlign ='top', borderStyle ='in')
	cmds.rowColumnLayout(numberOfColumns = 2, columnWidth = [(1, 80), (2, 130)], columnSpacing = [(1,10), (2,10)] )
	cmds.text(label = 'UDIM numbers', align = 'right')
	numField = cmds.intField(value = 3)
	cmds.setParent('..')

	cmds.columnLayout( adjustableColumn=True )
	cmds.setParent('..')

	cmds.button( label = 'random it!', command = partial(connectButtonPush, numField))
	cmds.showWindow()
	
if __name__=='__main__':
    randomUDIM()