from tkinter import *

root = Tk(screenName=None,baseName=None,className="av screen",useTk=True)

# Return a new Toplevel widget on screen SCREENNAME. A new Tcl interpreter will be created. BASENAME will be used for the identification of the profile file (see readprofile). It is constructed from sys.argv[0] without extensions if None is given. CLASSNAME is the name of the widget class.

root.title("avnish screen") # To change the window’s title
print(root.title())

root.mainloop()