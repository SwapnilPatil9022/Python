import random, os
music_dir = 'E:\\Recording PPA & LB\\LB_recording'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

# Prints The Song Name
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[0]))