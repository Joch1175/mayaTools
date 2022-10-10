# swapYetiTexturePath.py

# Powered by: John Kalaigian / Joseph Chen
# Date 10 Oct 2022
# Version 1.0
# Contact: joseph@hellohornet.com / joseph50422@gmail.com

import pymel.core as pm
import os
yeti = pm.ls(type='pgYetiMaya')
for each in yeti:
    textureNodes = pm.pgYetiGraph(each, listNodes=True, type='texture')
    for every in textureNodes:
        #get node path
        path = os.path.dirname(pm.pgYetiGraph(each, node=every, param='file_name', getParamValue=True)).replace('\\','/')
        #set node path
        pm.pgYetiGraph(each, node=every, param='file_name', setParamValueString=path.replace('P:/','/mnt/prod/'))