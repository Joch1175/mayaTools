# autoAiStandard.py

# Powered by: Joseph Chen
# Date 10 Oct 2022
# Version 3.0
# Contact: joseph@hellohornet.com / joseph50422@gmail.com

import maya.cmds as cmds
from functools import partial

def createBaseColor(S_Name, UV_Name, sourecPath,fileFormat):
	# S_Name = Shader Name, T_Name = Texture Name, CC_Name = ColorCorrect Node Name
	T_Name = S_Name + "_BaseColor"
	createUVTex(UV_Name, T_Name)
	cmds.setAttr('%s.fileTextureName' %T_Name, '%s%s.%s' %(sourecPath, T_Name, fileFormat), type="string")

	CC_Name = cmds.shadingNode("aiColorCorrect", asUtility = True, n = T_Name + "_CC" )

	cmds.connectAttr('%s.outColor' %T_Name, '%s.input' %CC_Name, f = True)
	cmds.connectAttr('%s.outColor' %CC_Name, '%s.baseColor' %S_Name, f = True)

	cmds.setAttr('%s.base' %S_Name, 1.0)

def createRoughness(S_Name, UV_Name, sourecPath,fileFormat):
	# S_Name = Shader Name, T_Name = Texture Name, CC_Name = ColorCorrect Node Name
	T_Name = S_Name + "_Roughness"
	createUVTex(UV_Name, T_Name)
	cmds.setAttr('%s.fileTextureName' %T_Name, '%s%s.%s' %(sourecPath, T_Name, fileFormat), type="string")
	cmds.setAttr('%s.ignoreColorSpaceFileRules' %T_Name, 1)
	cmds.setAttr('%s.alphaIsLuminance' %T_Name, 1)
	cmds.setAttr('%s.colorSpace' %T_Name, 'Utility - Raw', type="string")

	CC_Name = cmds.shadingNode("aiColorCorrect", asUtility = True, n = T_Name + "_CC" )

	cmds.connectAttr('%s.outColor' %T_Name, '%s.input' % CC_Name, f = True)
	cmds.connectAttr('%s.outColorR' %CC_Name, '%s.specularRoughness' %S_Name, f = True)
	
def createMetalness(S_Name, UV_Name, sourecPath,fileFormat):
	# S_Name = Shader Name, T_Name = Texture Name, CC_Name = ColorCorrect Node Name
	T_Name = S_Name + "_Metalness"
	createUVTex(UV_Name, T_Name)
	cmds.setAttr('%s.fileTextureName' %T_Name, '%s%s.%s' %(sourecPath, T_Name, fileFormat), type="string")
	cmds.setAttr('%s.ignoreColorSpaceFileRules' %T_Name, 1)
	cmds.setAttr('%s.alphaIsLuminance' %T_Name, 1)
	cmds.setAttr('%s.colorSpace' %T_Name, 'Utility - Raw', type="string")

	CC_Name = cmds.shadingNode("aiColorCorrect", asUtility = True, n = T_Name + "_CC" )

	cmds.connectAttr('%s.outColor' %T_Name, '%s.input' %CC_Name, f = True)
	cmds.connectAttr('%s.outColorR' %CC_Name, '%s.metalness' %S_Name, f = True)
    
def createSubsurface(S_Name, UV_Name, sourecPath,fileFormat):
	# S_Name = Shader Name, T_Name = Texture Name, CC_Name = ColorCorrect Node Name
	T_Name = S_Name + "_SSS"

	createUVTex(UV_Name, T_Name)
	cmds.setAttr('%s.fileTextureName' %T_Name, '%s%s.%s' %(sourecPath, T_Name, fileFormat), type="string")
	cmds.setAttr('%s.ignoreColorSpaceFileRules' %T_Name, 1)
	cmds.setAttr('%s.alphaIsLuminance' %T_Name, 1)
	cmds.setAttr('%s.colorSpace' %T_Name, 'Utility - Raw', type="string")

	Color_Name = cmds.shadingNode("aiColorCorrect", asUtility = True, n = S_Name + "_SSSColor_CC" )
	Radius_Name = cmds.shadingNode("aiColorCorrect", asUtility = True, n = S_Name + "SSSRadius_CC" )

	cmds.connectAttr('%s.outColor' %T_Name, '%s.input' %Radius_Name, f = True)
	cmds.connectAttr('%s.outColor' %Radius_Name, '%s.subsurfaceRadius' %S_Name, f = True)
    
	cmds.connectAttr('%s_BaseColor.outColor' %S_Name, '%s.input' %Color_Name, f = True)
	cmds.connectAttr('%s.outColor' %Color_Name, '%s.subsurfaceColor' %S_Name, f = True)

	cmds.setAttr('%s.subsurface' %S_Name, 1.0)

def createNormal(S_Name, UV_Name, sourecPath,fileFormat):
	# S_Name = Shader Name, T_Name = Texture Name, N_Name = aiNormalMap Node Name
	T_Name = S_Name + "_Normal"
	createUVTex(UV_Name, T_Name)
	cmds.setAttr('%s.fileTextureName' %T_Name, '%s%s.%s' %(sourecPath, T_Name, fileFormat), type="string")
	cmds.setAttr('%s.ignoreColorSpaceFileRules' %T_Name, 1)
	cmds.setAttr('%s.colorSpace' %T_Name, 'Utility - Raw', type="string")

	N_Name = cmds.shadingNode("aiNormalMap", asUtility = True, n = S_Name + "_aiNormalMap" )

	cmds.connectAttr('%s.outColor' %T_Name, '%s.input' %N_Name, f = True)
	cmds.connectAttr('%s.outValue' %N_Name, '%s.normalCamera' %S_Name, f = True)

def createUVnode(S_Name):
	uv = cmds.shadingNode("place2dTexture", asUtility = True, n = S_Name + "_p2t")
	return uv

def createUVTex(UV_Name, T_Name):
	tex = cmds.shadingNode("file", asTexture = True, n = T_Name)

	cmds.connectAttr('%s.coverage' %UV_Name, '%s.coverage' %tex, f = True)
	cmds.connectAttr('%s.translateFrame' %UV_Name, '%s.translateFrame' %tex, f = True)
	cmds.connectAttr('%s.rotateFrame' %UV_Name, '%s.rotateFrame' %tex, f = True)
	cmds.connectAttr('%s.mirrorU' %UV_Name, '%s.mirrorU' %tex, f = True)
	cmds.connectAttr('%s.mirrorV' %UV_Name, '%s.mirrorV' %tex, f = True)
	cmds.connectAttr('%s.stagger' %UV_Name, '%s.stagger' %tex, f = True)
	cmds.connectAttr('%s.wrapU' %UV_Name, '%s.wrapU' %tex, f = True)
	cmds.connectAttr('%s.wrapV' %UV_Name, '%s.wrapV' %tex, f = True)
	cmds.connectAttr('%s.repeatUV' %UV_Name, '%s.repeatUV' %tex, f = True)
	cmds.connectAttr('%s.offset' %UV_Name, '%s.offset' %tex, f = True)
	cmds.connectAttr('%s.rotateUV' %UV_Name, '%s.rotateUV' %tex, f = True)
	cmds.connectAttr('%s.noiseUV' %UV_Name, '%s.noiseUV' %tex, f = True)
	cmds.connectAttr('%s.vertexUvOne' %UV_Name, '%s.vertexUvOne' %tex, f = True)
	cmds.connectAttr('%s.vertexUvTwo' %UV_Name, '%s.vertexUvTwo' %tex, f = True)
	cmds.connectAttr('%s.vertexUvThree' %UV_Name, '%s.vertexUvThree' %tex, f = True)
	cmds.connectAttr('%s.vertexCameraOne' %UV_Name, '%s.vertexCameraOne' %tex, f = True)
	cmds.connectAttr('%s.outUV' %UV_Name, '%s.uv' %tex, f = True)
	cmds.connectAttr('%s.outUvFilterSize' %UV_Name, '%s.uvFilterSize' %tex, f = True)

# UI setup
def connectButtonPush(pathfield, formatfield, checkMap, *args):
	sourecPath = cmds.textField(pathfield, query=True, text=True) + '\\'
	fileFormat = cmds.textField(formatfield, query=True, text=True) 

	shaders = cmds.ls(sl=True)
	
	for i in range (len(shaders)):
		UV_Name = createUVnode(shaders[i])
		if (cmds.checkBox(checkMap[0], query=True, value=True)):
			createBaseColor(shaders[i], UV_Name, sourecPath, fileFormat)
		if (cmds.checkBox(checkMap[1], query=True, value=True)):
			createRoughness(shaders[i], UV_Name, sourecPath, fileFormat)
		if (cmds.checkBox(checkMap[2], query=True, value=True)):
			createMetalness(shaders[i], UV_Name, sourecPath, fileFormat)
		if (cmds.checkBox(checkMap[3], query=True, value=True)):
			createSubsurface(shaders[i], UV_Name, sourecPath, fileFormat)
		if (cmds.checkBox(checkMap[4], query=True, value=True)):
			createNormal(shaders[i], UV_Name, sourecPath, fileFormat)

		cmds.select(shaders[i], r = True)

def autoAiStandard():
		
	window = cmds.window( title = 'autoAiStandard', iconName = 'autoAS', widthHeight = (300, 200), sizeable = False)
	cmds.frameLayout('Texture File Path', labelAlign ='top', borderStyle ='in')
	cmds.rowColumnLayout(numberOfColumns = 2, columnWidth = [(1, 80), (2, 190)], columnSpacing = [(1,10), (2,10)] )
	cmds.text(label = 'Texture Folder', align = 'right')
	pathfield = cmds.textField(text = "sourceimages")
	cmds.text(label='Texture Formet', align = 'right')
	formatfield = cmds.textField(text = "png")
	cmds.setParent('..')

	cmds.columnLayout( adjustableColumn=True )
	checkMap = []
	checkMap.append(cmds.checkBox( label = 'BaseColor', value = True))
	checkMap.append(cmds.checkBox( label = 'Roughness', value = True))
	checkMap.append(cmds.checkBox( label = 'Metalness', value = False))
	checkMap.append(cmds.checkBox( label = 'Subsurface', value = False))
	checkMap.append(cmds.checkBox( label = 'Normal', value = True))
	cmds.setParent('..')

	cmds.button( label = 'I am lazy. Conncet the textures for me.', command = partial(connectButtonPush, pathfield, formatfield, checkMap))
	cmds.showWindow()
	
if __name__=='__main__':
    autoAiStandard()