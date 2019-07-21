#!/usr/bin/env python
from __future__ import print_function
from sys import argv
from os.path import getsize
import requests #error? try 'pip install requests'


#HEY YOU: Change these to your personal LPix username and password.
username = 'AzureDiamond'
password = 'hunter2'

gallery = 'Default' #you can change this to upload into another gallery, too.	

my_mb_limit = 2 #Most LPix users have a 2 MB upload limit. If you have a boosted upload limit, increase this number to your personal limit, in MB.


if len(argv) < 2:
	print("Usage: {} file1 [file2] [file3...]".format(argv[0]))

for file in argv[1:]:
	try:
		with open(file, 'rb') as thisfile:
			print("Uploading file {}.".format(file))
			size = getsize(file)
			if size > 1024 * 1024 * my_mb_limit:
				print("This file is too big to upload (over {} MB).".format(my_mb_limit))
				continue #skip file
		
			r = requests.post("https://lpix.org/api", data={'username':username, 'password':password, 'gallery':gallery, 'output':'json'}, files={'file': thisfile})
		
			result = r.json()
			if result['err'] is not None:
				error = result['err']
				permanent_error = False
				
				if error == 'err1':
					error_explanation = 'something went wrong during the upload itself.'
				elif error == 'err2':
					error_explanation = 'authentication error. Check your username and password!'
					permanent_error = True
				elif error == 'err3':
					error_explanation = 'this file doesn\'t appear to be an image or MP3 file.'
				elif error == 'err4':
					error_explanation = 'your file is too big.'
				elif error == 'err5':
					error_explanation = 'at time of writing, this error code is reserved by Baldurk for future use. Maybe post about this on the forums?'
				elif error == 'err6':
					error_explanation = 'the server is down for maintenance. Try again later.'
					permanent_error = True
				else:
					error_explanation = 'unknown error, using the error code "{}".'.format(error)
					permanent_error = True
				print("Received error when uploading {}: {}")
				if permanent_error: 
					print("Stopping now.")
					break # we're done uploading images
				continue #otherwise, if there's an error, jump to the next file
			print("Image URL: [img]{}[/img]\nThumbnail code: [timg]{}[/timg]\n".format(result['imageurl'],result['thumburl']))
	except IOError:
		print("Couldn't open file {} for uploading.".format(file))