# Megasend
Batch file uploader for the LPix image hosting service. 


# How to Install

You'll need:

* Python installed on your computer. (Python 2 or 3 should both work.)

* The ['requests'] python module to be installed. Check the link for instructions.

* To change the 'username' and 'password' variables in the script to your LPix username and password.\
_Be sure not to share a copy of the script that has your personal user/pass with others!_

  \

# Using Megasend

The basic idea is just run the script and feed it names of files to upload, such as: 

`./megasend.py my_cool_image.png`

`./megasend.py Huey.png Dewey.png Louie.png`

`./megasend.py MyLetsPlay-Chapter1-*.png`

It'll upload those files, or tell you what went wrong.

\
You can change what gallery your files are uploaded to by changing the value of the 'gallery' variable in the script. The name should match the name of one of your existing LPix galleries.

If you have a boosted upload limit, you can also change the script's 'my\_mb\_limit' variable to let Megasend know - normally it's set to 2, for a 2MB upload limit, but you can change it to the size of your personal limit.

  \

# Future Improvements 

Here are some ideas for improvements, which I haven't yet got around to making.

(If you decide to implement one of these, please test your changes on Python 2 _and_ 3 to make sure they both work!)

* *Command-line arguments (gallery):* Specifying a destination gallery name through a command-line argument. As it is now, it's kind of hard to change and easy to forget that you have changed it.

* *Username/password storage outside script:* Currently, sharing your personal copy of this script is a bad idea. Outside-of-script user/pass storage would fix that.

* *Folder support:* Currently, feeding Megasend a folder name will make it try to open it like a file, and fail.


['requests']: https://2.python-requests.org/en/master/user/install/#install