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
    #get current namespace from current iterator name
    currentNS = each.split(':')[0] + ':'
    
    for xgen_substrate in each.inputs():
       
        #now search in MDL grp only, ignoring PROXY grp, for anything that has scalp_GEO and replace search string with just GEO
        #because each.inputs() returns [namespace]:xxx_GEO or [namespace]:xxx_GRP|[namespace]:xxx_GEO
        #replacing namespace as ".*" can make ".*MDL_GRP\|.*xxx_GRP\|.*xxx_GEO" and ".*MDL_GRP\|.*xxx_GEO" both searchable key
        queryKey = '.*MDL_GRP\|' + xgen_substrate.name().replace('scalp_GEO', 'GEO').replace(currentNS, '.*').replace('|', '\|')
        asset_substrate = pm.ls(regex=queryKey)
        
        #outputs 
        print('Query Keyword is: ' + queryKey)
        print('XGen Substrate Name: ' + xgen_substrate + ' with cbId: ' + xgen_substrate.cbId.get())
        print('Asset Substrate Name: ' + asset_substrate[0] + ' with cbId: ' + asset_substrate[0].cbId.get())
        
        #create blendshape, and set the weight as 1
        pm.blendShape(asset_substrate[0], xgen_substrate, w=(0,1))

    print('\n')