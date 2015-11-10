#!/usr/bin python
'''
<tutorial>
This tutorial:
<br>
<ol>
<li>Imports the detector and the settings file,
<li>Sets the data file, properties, cache size and pool size,
<li>Initialises the provider,
<li>Sets a User-Agent,
<li>Gets a match for the User-Agent. This returns a match object,
<li>Lists all the selected properties for the matched device.
</ol>
<br>
</tutorial>
'''

# // Snippet Start

from FiftyOneDegrees import fiftyone_degrees_mobile_detector_v3_wrapper
from fiftyone_degrees.mobile_detector.conf import settings

dataFile = settings.V3_WRAPPER_DATABASE
properties = 'BrowserName,BrowserVendor,BrowserVersion,DeviceType,HardwareVendor,IsTablet,IsMobile,IsCrawler,ScreenInchesDiagonal,ScreenPixelsWidth'
cacheSize = settings.CACHE_SIZE
poolSize = settings.POOL_SIZE

provider = fiftyone_degrees_mobile_detector_v3_wrapper.Provider(dataFile, properties, cacheSize, poolSize)

userAgent = 'Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG SCH-I545 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36'

device = provider.getMatch(userAgent)

for name in properties.split(','):
	value = device.getValues(name)
	if value:
		sys.stdout.write('   %s: %s\n' % (name, ' '.join(value)))
	else:
		sys.stdout.write('   %s: %s\n' % (name, 'N/A in Lite'))

# // Snippet End

