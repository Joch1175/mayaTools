import maya.cmds as cmds
import maya.OpenMaya as om
import random as random
import math as math

UDIM_num = 3

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

meshList = cmds.ls(sl=True)

for mesh in meshList:
	meshShellDict = getUvShelList(mesh)
	meshShellDict = meshShellDict[0]['map1']
	meshShellNum = len(meshShellDict)
	
	for key in meshShellDict:
	    intNumber =  int(math.floor(random.random()*UDIM_num))
	    cmds.select(meshShellDict[key][0])
	    cmds.polyEditUVShell(uValue = intNumber, relative = True)
	    progress = float(key+1)/ float(meshShellNum)*100.0
	    print ("%s -> UDIM_100%s, %d/%d (%d%%)" %(meshShellDict[key][0], intNumber+1, key+1, meshShellNum, progress))