# Bandcamp song title fixer
# Removes annoying artist and album labels from song name. 
# Cameron McDrury 2020

import os

def make_caps(name):
    '''Capitalizes every word'''
    words = name.split()
    name = ""
    for word in words:
        name += word.capitalize()
        if word != words[len(words)-1]: #Don't add a space to the end of the name
            name += " "
    
    return name
    

#get album path;
path = input("Where is your music library? (C:\Music) ")
artist = input("Artist name: ") 
album = input("Album name: ")

#Capitalise each word in artist and album name
artist = make_caps(artist)
album = make_caps(album)

#path = "\Test Album" # For testing only EDIT THIS TO WORK ON YOUR MACHINE

path = path + "\\" + artist + "\\" + album   # Actual Path

#List all the songs in the album
songs = os.listdir(path)

#Turn file names into song names
for song in songs:
    old = song;
    words = old.split('- ')

    new = words[len(words)-1]
    
    old_name = path + "\\" + old
    new_name = path + "\\" + new
    
    print(old_name)
    print(new_name)
    print("++++++++++++")
    
    os.rename(old_name, new_name)
    
print("Completed!")
input("Press enter to exit")
