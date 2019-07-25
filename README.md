# Megasend
Batch file uploader for the LPix image hosting service. 


# How to Install

You'll need:

* Python installed on your computer. (Python 2 or 3 should both work.)

* The ['requests'] python module to be installed. Check the link for instructions.

* To change the 'username' and 'password' variables in the script to your LPix username and password.\
_Be sure not to share a copy of the script that has your personal user/pass with others!_  
  

# Using Megasend

The basic idea is just run the script and feed it names of files to upload, such as: 

`./megasend.py my_cool_image.png`

`./megasend.py Huey.png Dewey.png Louie.png`

`./megasend.py MyLetsPlay-Chapter1-*.png`

It'll upload those files, or tell you what went wrong.

## Options: Image URL Logging, Custom Galleries

Megasend has three command-line options. They are *--log*, *--tlog*, and *--gallery*.

### Logging

*--log* and *--tlog* will write the image URLs of the uploaded images to a log file you specify, with \[img\]\[/img\] tags (when using --log) or \[timg\]\[/timg\] tags (when using --tlog) around them. This can be handy for batch-replacing the URLs into a post later.

If you specify the same file for both --log and --tlog, each file's \[img\] and \[timg\] links are kept together in the resulting log.

`./megasend.py --log image_urls.txt FileBatch*.png`

`./megasend.py --tlog thumb_urls.txt HowToMakeOneMillionImagesInThirtyDays*.png`

`./megasend.py --log image_urls.txt --tlog thumb_urls.txt Pic_Of_My_Thumb.png`

### Custom Gallery Selection

You can use *--gallery* to choose what gallery your files are uploaded to, if given the name of the gallery (in quotes).

If the gallery of the name you specified doesn't exist, I have no idea what will happen. Please double-check your gallery names before uploading.

`./megasend.py --gallery "Dubstep Visualizations" Bass_Drop.png`


## Advanced Configuration: Boosted Upload Limit

If you have a boosted upload limit, you can also change the script's 'my\_mb\_limit' variable to let Megasend know - normally it's set to 2, for a 2MB upload limit, but you can change it to the size of your personal limit. Megasend will normally skip oversize files to save your bandwidth.  
  

# Future Improvements 

Here are some ideas for improvements, which I haven't yet got around to making.

(If you decide to implement one of these, please test your changes on Python 2 _and_ 3 to make sure they both work!)

* *Username/password storage outside script:* Currently, sharing your personal copy of this script is a bad idea. Outside-of-script user/pass storage would fix that.

* *Folder support:* Currently, feeding Megasend a folder name will make it politely reject it, which is an improvement from last version - but recursively uploading its contents might be better.


['requests']: https://2.python-requests.org/en/master/user/install/#install