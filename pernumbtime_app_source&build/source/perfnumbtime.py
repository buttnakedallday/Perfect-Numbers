from colorama import Fore
from colorama import Style
import pandas as pd
import numpy as np
import time
global filepath
file_path = 'C:/Users/rjw3/OneDrive/Desktop/Side_projects' + \
                    '/Perfect_numbers/time_to_check_numbers.xlsx'


#check for correct input of (y/n)
def check(k):
    switch = {
            'y': 1,
            'n': 2,
        }
    return switch.get(k, 3)

#check for correct input of max range
def maxrngf():
    while True:
        try:
            maxrng1=int(input('max range: '))
        except ValueError:
            print(Fore.RED + "Must be a whole number.")
            print(Style.RESET_ALL)
        else:
            return maxrng1

#push times to excel
def push(list_):
    list_ = np.array(list_)
    list_ = pd.DataFrame(list_)
    global file_path
    list_.to_excel(file_path)

#ask user if the default file path is ok

while True:
    yn = input('Is the default filepath \n"' + str(file_path) + '"\nwhere the excel data should be sent? (y/n) : ')
    yn = check(yn)
    if yn == 1:
        break
    if yn == 2:
        file_path = input('Excel filepath for time data to be sent: ')
        break
    if yn == 3:
        print(Fore.RED + 'Error: Wrong input type')
        print(Style.RESET_ALL)





# look for perfect numbers
while True:
    maxrng = maxrngf()
    perfectnumb=[]
    searchrng=list(range(1,maxrng))
    times = [None] * (len(searchrng)+1)
    start = time.time()
    for i1 in ((range(0,len(searchrng)))):
        posnumb=int(i1)
        posdiv=[]
        sumposdiv=[]
        for i in range(1,int(((posnumb)/2)+1)):
            if((posnumb)%i==0):
                posdiv.append(i)
                sumposdiv=sum(posdiv)
        if(sumposdiv==posnumb):
            perfectnumb.append(posnumb)
        times[i1] = time.time() - start
    print('\n')
    print(str(perfectnumb))
    print('\n')
    del maxrng
    
# ask if the user would like to push data to "file_path"
    while True:
        yn = input('Push to excel (y/n) : ')
        yn = check(yn)
        if yn == 1:
            push(times)
            break
        if yn == 2:
            break
        if yn == 3:
            print(Fore.RED + 'Error: Wrong input type')
            print(Style.RESET_ALL)

# ask if the user would like to try a differnet range    
    while True:
        yn = input('Another? (y/n) : ')
        yn = check(yn)
        if yn == 1:
            continuethis = True
            break
        if yn == 2:
            continuethis = False
            break
        if yn == 3:
            print(Fore.RED + 'Error: Wrong input type')
            print(Style.RESET_ALL)
    if continuethis == False:
        break
    
    
