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
        print('XGen Substrate Name: ' + xgen_substrate + ' with cbId: ' + xgen_substrate.cbId.get())
        
        #composing the query key for searching
        #search in MDL grp only, ignoring PROXY grp, for anything that has scalp_GEO and replace search string with just GEO
        #because each.inputs() returns [namespace]:xxx_GEO or [namespace]:xxx_GRP|[namespace]:xxx_GEO
        #replacing namespace as ".*" can make ".*MDL_GRP\|.*xxx_GRP\|.*xxx_GEO" and ".*MDL_GRP\|.*xxx_GEO" both searchable key
        queryKey = '.*MDL_GRP\|' + xgen_substrate.name().replace('scalp_GEO', 'GEO').replace(currentNS, '.*').replace('|', '\|')
        print('Query Keyword is: ' + queryKey)
        
        #search the binding target with queryKey
        asset_substrate = pm.ls(regex=queryKey, type = 'transform')
    
        #warrning message for exceptions
        if (len(asset_substrate)!=1):
            pm.warning("There are " + str(len(asset_substrate)) + " result(s) match with regex " + queryKey + ":")
            continue
        else:
            #create blendshape, and set the weight as 1
            pm.blendShape(asset_substrate[0], xgen_substrate, w=(0,1))
            print('Asset Substrate Name: ' + asset_substrate[0] + ' with cbId: ' + asset_substrate[0].cbId.get())
            
    print('\n')