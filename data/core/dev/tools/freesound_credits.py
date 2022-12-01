import os

credits = ''
data = os.popen('ls assets/sfx').read().split('\n')

for field in data:
    userdata = field.split('__')
    try:
        credits += f'Author: {userdata[1]}, SFX: {userdata[2]}'+'\n'
    except:
        pass

with open ('freesound_credits.txt', 'w') as f:
    f.write('FreeSound SFX Authors:\n'+credits.strip('\n'))