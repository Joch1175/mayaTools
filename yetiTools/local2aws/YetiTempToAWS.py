# YetiTempToAWS.py

import pymel.core as pm
import time

#get all yeti nodes in scene, not including groom nodes as they have no cache i/o functionality
yeti = pm.ls(type='pgYetiMaya')

#selecting all yeti nodes before caching is the easiest way to cached based on the Concurrent Caching docs https://support.peregrinelabs.com/support/solutions/articles/66000481611-working-with-caches#Concurrent-Caching
pm.select(yeti, r = True)

#replace the Windows path with Linux path
for each in yeti:
    try:
        each.fileMode.set(1)
        path = each.cacheFileName.get()
        each.cacheFileName.set(path.replace('P:/','/mnt/prod/'))
    except Exception, e:
        continue

for each in yeti:
    path = each.cacheFileName.get()
    print path