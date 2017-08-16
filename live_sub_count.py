import urllib2
import time
import sys

subs = 0
views = 0
videos = 0

while 1:
	try:
		stringStat = ''
		result = urllib2.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=YouTubeID&key=APIkey").read()
	
	
		for stat in result:
			stringStat = stringStat + str(stat)
	
	
		for spec in stringStat.split('\n'):
			if 'subscriber' in spec:
				subs = spec.replace('"subscriberCount": "', '').replace('"', '').replace(' ', '').replace(',', '')
			elif 'viewCount' in spec:
				views = spec.replace('"viewCount": "', '').replace('"', '').replace(' ', '').replace(',', '')
			elif 'videoCount' in spec:
				videos = spec.replace('"videoCount": "', '').replace('"', '').replace(' ', '').replace(',', '')
	
		print('Subscribers -> ' + str(subs))
		print('      Views -> ' + str(views))
		print('    Uploads -> ' + str(videos))
		print('-------------------------------')
		time.sleep(5)
	except KeyboardInterrupt:
		print('Exiting...')
		sys.exit(0)
