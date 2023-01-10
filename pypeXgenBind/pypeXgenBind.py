# xgenBatchBlendShape.py

import maya.cmds as cmds

# List all the GEO node and get its name
xgenlist = cmds.listRelatives(c=True, ad=True, f=True, type="transform") 
scalps = [ x for x in xgenlist if "GEO" in x ]

# Go through all the scalps and find the corresponding mesh
# Make the blendshape connection
for x in scalps:
    # Deconstruct the GEO name and get the keyword for searching
    keyword = x.split(":")[-1]
    key = "*:*" + keyword.replace("scalp_", "") + "*"
    
    # Search corresponding mesh and filter out PROXY and Shape node
    result = cmds.ls(key, ap=True, l=True)
    result = [i for i in result if "Shape" not in i]
    result = [i for i in result if "PROXY" not in i]

    # Show Warning when no corresponding mesh or more than 1
    if len(result) == 0:
        cmds.warning ("[" + keyword + "] No object correspond to the scalp.")
        continue
    elif len(result) > 1 :
        result = [] 
        cmds.warning ("[" + keyword + "] More than 1 object correspond to the scalp.")
        continue
    
    # Create blendshape and set the weight as 1
    blend = cmds.blendShape(result, x, w=(0,1))