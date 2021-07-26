# Bandcamp song title fixer
# Removes artist and album labels from song name. 
# Cameron McDrury 2021

'''
Changes in this version:

Modularised code. 
Added conditional renaming. 
Added FileNotFoundError exception and handling. 
Added repeatability. 
'''

import os

#We only need to ask this once. 
LIBRARY = str(input("Where is your music library? (D:\Music)") or "D:\Music") # Default music library is D:\Music.

CNT = 0

def make_caps(name):
    '''Capitalizes every word'''
    words = name.split()
    name = ""
    for word in words:
        name += word.capitalize()
        if word != words[len(words)-1]: #Don't add a space to the end of the name
            name += " "
    
    return name
    
def get_path():

    #get album path;
    if CNT == 1:
        artist = input("Artist: ") 
        album = input("Album: ")
    else: 
        artist = input("Next artist: ") 
        album = input("Next album: ")
        
    #Capitalise each word in artist and album name
    artist = make_caps(artist)
    album = make_caps(album)
    
    actual_path = LIBRARY + "\\" + artist + "\\" + album   # Actual Path
    
    return [actual_path, artist, album]
    
def rename():

    # Check that the path exists. if it doesn't, ask the user to try again. 
    count = 0;
    while True:
        data = get_path()
        actual_path = data[0]
        artist = data[1]
        album = data[2]
        try:
            songs = os.listdir(actual_path) #List all the songs in the album
            break
        except FileNotFoundError:
            count = count + 1
            print("Path does not exist. Please try again.")
            if count > 1: 
                print("If this error persists, close all music players and try again. ")
            
    
    #Turn file names into song names
    for song in songs:
        
        words = song.split('- ') # Split at every "- " (with a space) to ensure we don't leave a space at the start of the title. 
        new = words[len(words)-1] # The song title comes last in the format
        
        old_name = actual_path + "\\" + song
        new_name = actual_path + "\\" + new
        
        print(old_name)
        print(new_name)
        print("++++++++++++")
        
        if new_name != old_name:
            os.rename(old_name, new_name)
            
    print("Successfully renamed all songs in", album, "by", artist)
    print('''=========================================
    

    ''')

while True:
    CNT = CNT + 1 # Ignoring the possibility of overflow as ints in python are 32 bit. 
    rename()

