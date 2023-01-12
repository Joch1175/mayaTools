# createYetiTextureTemp.py

# Powered by: Joseph Chen
# Date 2 Nov 2022
# Version 1.0
# Contact: joseph@hellohornet.com

import pymel.core as pm
import os
yeti = pm.ls(type='pgYetiMaya')

if pm.ls('yetiTextureTemp_*'):
    pm.delete('yetiTextureTemp_*')

# Search all yeti texture nodes in the scene and collect the texture file names
yetiTextures = []
for each in yeti:
    textureNodes = pm.pgYetiGraph(each, listNodes=True, type='texture')
    for every in textureNodes:
        texture = os.path.basename(pm.pgYetiGraph(each, node=every, param='file_name', getParamValue=True)).replace('<UDIM>','1001')
        yetiTextures.append(texture)

# Create temp file nodes for yeti textures so it will be submitted to aws with the project
# If any yetiShaderTemp_* node exists in the scene then don't create temp file nodes again
for index, item in enumerate(yetiTextures):
    shaderName = 'yetiTextureTemp_' + str(index)
    pm.shadingNode('file', name = shaderName, asTexture = True)
    pm.setAttr(shaderName+'.fileTextureName', 'lib\\char\\yetiTexture\\' + item)