# Bandcamp song title fixer
# Removes annoying artist and album labels from song name. 


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
artist = input("Artist name: ") 
album = input("Album name: ")

#Capitalise each word in artist and album name
artist = make_caps(artist)
album = make_caps(album)

path = "D:\Documents\Passion Projects\Bandcamp Title Fixer\Test Album" # For testing only

#path = "D:\Music\\" + artist + "\\" + album

#List all the songs in the album

songs = os.listdir(path)


