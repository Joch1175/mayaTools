import pymel.core as pm
import time
#get frame in and out points from timeline
frameIn = pm.playbackOptions(query=True, min=True)
frameOut = pm.playbackOptions(query=True, max=True)

#get all yeti nodes in scene, not including groom nodes as they have no cache i/o functionality
yeti = pm.ls(type='pgYetiMaya')

#selecting all yeti nodes before caching is the easiest way to cached based on the Concurrent Caching docs https://support.peregrinelabs.com/support/solutions/articles/66000481611-working-with-caches#Concurrent-Caching
pm.select(yeti, r = True)

#define cache path and full file name, splitting for now as it will be useful later on
cachePath = 'P:/directors/yves_geleyn/coke03_year_of_the_rabbit/production/maya/cache/yeti/shots/dummy/SH010'
cacheFilePath = cachePath + '/<NAME>.%04d.fur'

#diagnostic timer setup
startTimer = time.clock()

#disable viewport and extra storage on cache, no added/special subframe calculations for motion blur, just the defaults
pm.pgYetiCommand(writeCache = cacheFilePath, range = [frameIn, frameOut], updateViewport = False, generatePreview = False, storeBoundingBox = False)
print('Total time {totalTime:0.4f} seconds'.format(totalTime = time.clock() - startTimer))

#second part
#updating all yeti nodes to turn on load from cache and setting the cache path based on the files generated above
for each in yeti:
    try:
        each.fileMode.set(1)
        each.cacheFileName.set(cachePath + '/' + each.replace(':','_') + '.%04d.fur')
    except Exception, e:
        continue