import pymel.core as pm
import gc
import os
yeti = pm.ls(type='pgYetiMaya')
path = []
for each in yeti:
    textureNodes = pm.pgYetiGraph(each, listNodes=True, type='texture')
    for every in textureNodes:
        #get node path
        path.append(os.path.dirname(pm.pgYetiGraph(each, node=every, param='file_name', getParamValue=True)).replace('\\','/'))
        #file = os.path.basename(pm.pgYetiGraph(each, node=every, param='file_name', getParamValue=True))
        #set node path
        #pm.pgYetiGraph(each, node=every, param='file_name', setParamValueString='NEW_PATH')
list(set(path))


del(list)
gc.collect()