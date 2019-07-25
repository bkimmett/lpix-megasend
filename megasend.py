#!/usr/bin/env python
from __future__ import print_function
from sys import argv, exit
from os.path import basename, getsize, isfile, isdir
import argparse
import requests #error? try 'pip install requests'

#HEY YOU: Change these to your personal LPix username and password.
username = 'AzureDiamond'
password = 'hunter2'
my_mb_limit = 2 #Most LPix users have a 2 MB upload limit. If you have a boosted upload limit, increase this number to your personal limit, in MB.

def print_usage():
	print("usage: {} [--help] [--log <log_file>] [--tlog <log_file>] [--gallery <gallery_name>] file1 [file2] [file3...]".format(basename(argv[0])))
	
def print_help():
	print_usage()
	print("\n--log and --tlog take the name of a log file to store all resulting image URLs. The --log file saves [img] codes, and the --tlog file saves [timg] codes.\n--gallery takes the name of the gallery to upload to. If you don't specify, 'Default' is used.\n")
	

if len(argv) < 2: #no arguments at ALL? display help message
	print_help()
	exit()

#parse arguments
parser = argparse.ArgumentParser(usage="%(prog)s [--help] [--log <log_file>] [--tlog <log_file>] [--gallery <gallery_name>] file1 [file2] [file3...]", add_help=False)
parser.add_argument('--help', action='store_true')
parser.add_argument('--log', default=None, type=argparse.FileType('a'))
parser.add_argument('--tlog', default=None, type=argparse.FileType('a'))
parser.add_argument('--gallery', default="Default") #this sets the gallery. It may fall over if you renamed your default gallery and you don't tell it the new name.
parser.add_argument('files', nargs='*') #all other arguments treated as file names  #nargs=argparse.REMAINDER)

args = parser.parse_args()

#if you did --help, print the help message
if args.help:
	print_help()
	exit()

#set up logging
def log(what):
	if args.log is not None:
		args.log.write(what)
	if args.tlog is not None:
		args.tlog.write(what)
		
if len(args.files) == 0: #specified no files? complain
	print_usage()
	print("Error: You need to specify at least one file to upload.")
	exit()	

#iterate over files, (try to) upload each
for file in args.files:
	try:
		#check that we haven't been fed a directory by accident
		if isdir(file):
			print("Ignoring directory {} - Megasend doesn't upload recursively.".format(file))
			continue #move on
			
		if not isfile(file):
			print("File {} not found.".format(file))
			log("Couldn't find file {}.\n".format(file))
			continue #move on	
			
		with open(file, 'rb') as thisfile:
			print("Uploading file {}.".format(file))
			
			#size check
			size = getsize(file)
			if size > 1024 * 1024 * my_mb_limit:
				print("This file is too big to upload (over {} MB).".format(my_mb_limit))
				log("Skipped overlarge file {}.\n".format(file))
				continue #skip file
		
			r = requests.post("https://lpix.org/api", data={'username':username, 'password':password, 'gallery':args.gallery, 'output':'json'}, files={'file': thisfile}) #actually upload file
			result = r.json()
			
			if result['err'] is not None: #check for fails, tell people
				error = result['err']
				permanent_error = False
				
				if error == 'err1':
					error_explanation = 'something went wrong during the upload itself.'
				elif error == 'err2':
					error_explanation = 'authentication error. Check your username and password!'
					permanent_error = True
				elif error == 'err3':
					error_explanation = "this file doesn't appear to be an image or MP3 file."
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
				log("Couldn't upload file {}.\n".format(file))
				if permanent_error: 
					print("Stopping now.")
					break # abort! we're done uploading images
				continue #otherwise, if there's an error, jump to the next file	
				
			#report success	
			print("Image URL: [img]{}[/img]\nThumbnail code: [timg]{}[/timg]\n".format(result['imageurl'],result['thumburl']))
			#log it (custom text)
			if args.log is not None:
				args.log.write('[img]{}[/img]\n'.format(result['imageurl']))
			if args.tlog is not None:
				args.tlog.write('[timg]{}[/timg]\n'.format(result['thumburl']))
			
	except IOError: #file not found? any sort of file access error
		print("Couldn't open file {} for uploading.".format(file))
		log("Couldn't open file {}.\n".format(file))