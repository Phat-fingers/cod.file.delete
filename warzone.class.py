import os
import shutil
from time import sleep

class Warzone:
    # Edit this directorys use \\ to seperate dirs
    ################################################
    # ppsod file is located in documents/Call of Duty Modern Warfare/players
    ppsod_file = 'C:\\Users\\Admin\\Documents\\Call of Duty Modern Warfare\\players'

    # Game dir
    game_dir = 'G:\\Games\\Call of Duty Modern Warfare\\main'

    # ProgramData/Nvidia Cooperation/NV_Cache
    nv_cache = 'C:\\ProgramData\\NVIDIA Corporation\\NV_Cache'

    # Blizzard Entertainment folder
    blizzard_dir = 'C:\\ProgramData\\Blizzard Entertainment'

    # Battle.net launcher dir
    battle_net_l = 'C:\\Program Files (x86)\\Battle.net\\Battle.net.exe'


    def menu(self):
        print('Press 1 to only delete the ppsod.dat file.')
        print('Press 2 to delete all the files.')
        print('Press 3 to quit.')

    def info(self):
        print('Scan & Repair the game.\n'
              'Start the game and WAIT in the main menu until the shaders are fully installed.\n'
              'Once the shaders are finished click the button to restart the game.\n'
              'Now once you are in the main menu again WAIT, for ~5-10 minutes.\n'
              'Now go into a Submenu (Multiplayer, Warzone, Coop, whatever) and again WAIT for 5-10 minutes\n'
              "Now either your game crashed again and you are one of the unlucky ones or it didn't and you can play")
        print()

    def close_battle_net(self):
        print('Trying to closing Battle.net launcher')
        sleep(0.5)
        os.system('taskkill /F /IM Battle.net.exe')
        sleep(0.5)
        print('Battle.net is closed')

    def delete_dat_file(self):
        print('Removing ppsod.dat file...')
        sleep(0.5)
        os.chdir(self.ppsod_file)
        if os.path.isfile('ppsod.dat'):
            os.remove('ppsod.dat')
            print('File was removed')
        else:
            print('No file was found')

    def del_main_content(self):
        print('Removing files in main folder...')
        os.chdir(self.game_dir)
        if not os.listdir(self.game_dir):
            print('No files was found')
        else:
            for file in os.listdir(self.game_dir):
                os.remove(file)
            print('All files removed...')

    def del_blizzard_folder(self):
        print('Removing Blizzard Entertainment folder...')
        try:
            shutil.rmtree(self.blizzard_dir)
            print('Folder was removed')
        except:
            print('Folder not found...')

    def del_nv_cache(self):
        print('Removing Nvidia cache files...')
        os.chdir(self.nv_cache)
        if not os.listdir(self.nv_cache):
            print('No files was found')
        else:
            for file in os.listdir(self.nv_cache):
                os.remove(file)
            print('All files removed')


    def start_battle_net(self):
        print('Starting Battle.net launcher...')
        os.startfile(self.battle_net_l)





def main():
    w = Warzone()
    w.menu()

    while True:
        answer = input()
        if answer == '1':
            w.close_battle_net()
            sleep(0.5)
            w.delete_dat_file()
            sleep(0.5)
            w.start_battle_net()
            print('Now scan and repair the game before you start playing.')
        elif answer == '2':
            w.close_battle_net()
            sleep(1)
            w.delete_dat_file()
            sleep(1)
            w.del_main_content()
            sleep(1)
            w.del_blizzard_folder()
            sleep(1)
            w.del_nv_cache()
            sleep(1)
            w.start_battle_net()
            sleep(0.5)
            w.info()
        else:
            break

if __name__ == '__main__':
    main()

