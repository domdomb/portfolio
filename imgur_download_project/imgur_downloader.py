import urllib.request
import os

notepad_path = os.path.join(r"C:\Users\Dominic\Documents\projects\Projects\imgur_download_project\reddit_links.txt")
file = open(notepad_path, "r")
#this variable is a list
notepad_line = (file.readlines())
value = 0
changing_name = "image_"

def get_picture(url,file_name):
    #This line specifies save location and name of file
    filename = os.path.join(r"C:\Users\Dominic\Documents\Backgrounds\New_folder",file_name)

    #This line grabs the picuture from the URL and names it the specified name
    try:
        urllib.request.urlretrieve(url,filename)
    except:
        print ('broken link')

#retrieves the path of the notepad file
for i in range(0,len(notepad_line)):
    new_url = notepad_line[i]
    the_file_name = changing_name + str(i) + ".jpg"
    get_picture(new_url,the_file_name)
