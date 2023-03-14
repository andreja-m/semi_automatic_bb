#!/usr/bin/env python

import os
import time
import sqlite3
import sys


conn = sqlite3.connect('semi.db')
c = conn.cursor()


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
            print(f'\n{bcolors.FAIL}[ ! ] Code Error{bcolors.ENDC}\n')
            time.sleep(0.5)
            start()


class AddProject:
    def __init__(self):
        print(f'\n{bcolors.OKBLUE}You are in frame for adding new project{bcolors.ENDC}\n')
        self.project = input("Enter project name: ")
        self.ip = input("Enter IP address: ")
        self.url = input("Enter URL: ")

        try:
            c.execute(f""" CREATE TABLE {self.project} \
                           (info TEXT(255) NOT NULL,
                           sqlmap TEXT(255));
                       """)
        except sqlite3.OperationalError:
            print(f'\n{bcolors.FAIL}[ ! ] Table/Project {self.project} already exist{bcolors.ENDC}')
            err = input('Do you want to drop this and start over? y/n ')
            
            if err == 'y':
                c.execute(f"DROP TABLE IF EXISTS {self.project}")
                c.execute(f""" CREATE TABLE {self.project} \
                               (info TEXT(255) NOT NULL,
                               sqlmap TEXT(255));
                           """)
                
            else:
                print('\n...program will return to Main Menu')
                time.sleep(0.5)
                MainMenu()

        c.execute(f""" INSERT INTO {self.project} \
                       (info) VALUES (?)""", \
                  (self.ip,))

        c.execute(f""" INSERT INTO {self.project} \
                       (info) VALUES (?)""", \
                  (self.url,))

        conn.commit()
        print(f'Project {self.project} is added to DB.')

    def another_one(self):
        another = input('\nDo you want do add another url? y/n: ')

        if another == 'n':
            pass

        if another == 'y':
            another_url = input('Enter another url: ')
            AddProject.another_one(self)

        else:
            print(f'\n{bcolors.FAIL}[ ! ] Invalid option{bcolors.ENDC}')
            return


class ProjectEdit:
    def __init__(self):
        pass

    def check_link():
        pass


class Scann:
    def __init__(self):
        pass


def start():
    #os.system('clear')
    starting = MainMenu()


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print(f'\n\n{bcolors.FAIL}[!!!] {bcolors.BOLD}Keyboard Interrupt')
