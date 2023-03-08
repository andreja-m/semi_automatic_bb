#!/usr/bin/env python

import os
import time
import sys


banner = """
                                                                                
               (%&&&&&%#%#%%%%%%%%%%&*******%%%%%%%&%#&&&%%&%&%%%%%%%           
               &&&&&&&&&%@&&@&&&&&&@@*/////&&&&&&&&&&&&%&&&&%%&&&&&&&&&           
              (%%&&&&%&&&&&@%%%&@&&&&&&&&&&&&%&&%&&%&%&&&&&%&&%&%@@&&&&           
               #%%&&&#%%%&&&&&&&%%%&%%&%@@%&%&&&&@@@@@@&@@&&&&&&&&&&&           
                    &#%%&&&&&&&&&&&&%,       %&                                 
                   %%(%%%%%%%&&&&& @((        (                                 
                  &&##%%&&&&&&%%%&   (@ -===-,%                                 
                %&%##%%&&&%%&&                                                  
               (&###%&&&&&&&&%                                                  
              &&%#(%&&&&&&&&%                    SEMI                               
              %%#%%%&&&&&&%&                     AUTOMATIC                               
             &%#&%&%&&%&%&&                      BUG                               
            %&%#%&&%&&&#%&*                      BOUNTY                               
            &%%#&&%&&&%&&&                                                      
            &%%&&&&&&&&&&&                                                      
                                                                                
"""
class bcolors:
    HEADER =    '\033[95m'
    OKBLUE =    '\033[94m'
    OKCYAN =    '\033[96m'
    OKGREEN =   '\033[92m'
    WARNING =   '\033[93m'
    FAIL =      '\033[91m'
    ENDC =      '\033[0m'
    BOLD =      '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC =    '\033[3m'
    BLINK =     '\033[5m'

class MainMenu:
    def __init__(self):
        #print(banner)
        print('[ 1 ] - Add Project')
        print('[ 2 ] - Edit Project')
        print('[ 3 ] - Start Scann')
        print(f'{bcolors.WARNING}[ x ] {bcolors.ENDC}- Exit')
        inp = input('\n[ ? ] Select Option >>> ')

        if inp == '1':
            AddProject()
            AddProject.another_one(self)

        if inp == '2':
            pass

        if inp == '3':
            pass

        if inp == 'x' or inp == 'X':
            print(f'\n{bcolors.OKCYAN}[...] Bye')
            sys.exit()

        else:
            print(f'\n{bcolors.FAIL}[ ! ] Code Error{bcolors.ENDC}')
            time.sleep(0.5)
            start()


class AddProject:
    def __init__(self):
        print(f'\n{bcolors.OKBLUE}You are in frame for adding new project{bcolors.ENDC}\n')
        self.project = input("Enter project name: ")
        self.ip = input("Enter IP address: ")
        self.url = input("Enter URL: ")

    def another_one(self):
        another = input('\nDo you want do add another url? y/n: ')

        if another == 'n':
            pass

        if another == 'y':
            another_url = input('Enter another url: ')
            AddProject.another_one(self)

        else:
            print(f'{bcolors.FAIL}[ ! ] Invalid option{bcolors.ENDC}')
            return


def start():
    #os.system('clear')
    starting = MainMenu()

if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print(f'\n{bcolors.FAIL}[!!!] {bcolors.BOLD}Keyboard Interrupt')
