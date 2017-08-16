import urllib2
import time
import sys

followers = 0
old = -1

while 1:
	try:
		urlString = 'https://www.instagram.com/' + str(sys.argv[1]) + '/?__a=1'
		stringStat = ''
		try:
			result = urllib2.urlopen(urlString).read()
		except:
			getData = False	
	
		for stat in result:
			stringStat = stringStat + str(stat)
	
	
		for spec in stringStat.split(', '):
			if '"full_name": "' in spec:
				name = spec.replace('"full_name": "', '').replace('"', '').replace(',', '')
			elif '"followed_by": {"count": ' in spec:
				followers = spec.replace('"followed_by": {"count": ', '').replace('"', '').replace(' ', '').replace('}', '')	

		if int(followers) != int(old):
			print('     User -> ' + str(name))
			print('Followers -> ' + str(followers))
			print('-------------------------------')
			old = followers
		time.sleep(1)
	except KeyboardInterrupt:
		print('Exiting...')
		sys.exit(0)
