import os
from time import sleep


# Edit this directorys use \\ to seperate dirs
################################################
# ppsod file is located in documents/Call of Duty Modern Warfare/players
ppsodFile = 'C:\\Users\\Ander\\Documents\\Call of Duty Modern Warfare\\players'
# Game dir
game_dir = ''
################################################
nv_cache = 'C:\\ProgramData\\Nvidia Cooperation\\NV_Cache'
blizzard_dir = 'C:\\ProgramData\\'
# Battle.net launcher dir
battle_net_l = 'C:\\Program Files (x86)\\Battle.net\\Battle.net.exe'

def close_battle_net():
    print('Trying to closing Battle.net launcher')
    sleep(0.5)
    os.system('taskkill /F /IM Battle.net.exe')
    sleep(0.5)
    print('Battle.net is closed')


def delete_dat_file():
    print('Removing ppsod.dat file....')
    sleep(0.5)
    os.chdir(ppsodFile)
    if os.path.isfile('ppsod.dat'):
        os.remove('ppsod.dat')
        print('File was removed')
    else:
        print('No file was found')

def delete_main_content():
    pass

def del_blizzard_folder():
    pass

def delete_nv_cache():
    print('Removing Nvidia cache files...')
    os.chdir(nv_cache)
    sleep(0.5)
    if not os.listdir(nv_cache):
        print('There is no files to remove..\n'
              'Moving on..')
    else:
        print('Files being removed')
        for file in os.listdir(nv_cache):
            os.remove(file)
        print('All files removed.')


def battle_net():
    print('Starting battle.net launcher')
    os.startfile(battle_net_l)

def main():
    sleep(1)
    close_battle_net()
    sleep(1)
    delete_dat_file()
    sleep(1)
    delete_nv_cache()
    sleep(1)
    battle_net()

main()