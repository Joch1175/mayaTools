import pymel.core as pm
import re

#find all namespaces
ns = pm.getReferences()
assetNS, xgenNS = [], []

for element in ns.keys():
    xgenNS = [element for element in ns.keys() if 'xgenMain' in element]
    assetNS = [element for element in ns.keys() if 'rigMain' in element] 

#iterate through XGen splines
for each in pm.ls(type="xgmSplineBase"):
    print('SplineBase: ' + each)
    for xgen_substrate in each.inputs():
        print('XGen Substrate Name: ' + xgen_substrate + ' with cbId: ' + xgen_substrate.cbId.get())
        #now search in MDL grp only, ignoring PROXY grp, for anything that has scalp_GEO and replace search string with just GEO
        asset_substrate = pm.ls(regex='.*MDL_GRP\|.*' + xgen_substrate.name().replace('scalp_GEO', 'GEO').split(':')[1])
        #print asset_substrate
        print('Asset Substrate Name: ' + asset_substrate[0] + ' with cbId: ' + asset_substrate[0].cbId.get())
    print('\n')

#experimental
pm.ls(regex='.*MDL_GRP\|.*scalp_\d+_GEO')
pm.selected()[0].cbId.get()