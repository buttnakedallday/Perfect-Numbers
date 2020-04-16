from colorama import Fore
from colorama import Style
from tqdm import tqdm

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
            maxrng1=int(input('Check for perfect numbers in range 0 to: '))
        except ValueError:
            print(Fore.RED + "Must be a whole number.")
            print(Style.RESET_ALL)
        else:
            txt = str(maxrng1)
            print('Checking for perfect numbers in range 0 to ' + txt )
            return maxrng1

# look for perfect numbers
while True:
    maxrng = maxrngf()
    perfectnumb=[]
    searchrng=list(range(1,maxrng))
    for i1 in tqdm((range(0,len(searchrng)))):
        posnumb=int(i1)
        posdiv=[]
        sumposdiv=[]
        for i in range(1,int(((posnumb)/2)+1)):
            if((posnumb)%i==0):
                posdiv.append(i)
                sumposdiv=sum(posdiv)
        if(sumposdiv==posnumb):
            perfectnumb.append(posnumb)
    print('\n')
    print('Perfect numbers found are:')
    print(Fore.RED + str(perfectnumb))
    print(Style.RESET_ALL)
    print('\n')
    del maxrng
    
# ask if the user would like to try a differnet range
    while True:
        yn = input('Would you like to check a different range? (y/n) : ')
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