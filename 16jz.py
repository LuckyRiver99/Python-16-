import os
import binascii
from pyfiglet import Figlet
from optparse import OptionParser

def str2hex(use):
    h = use.encode().hex()
    labelsWord = []
    m = 1
    for iword in h:
        if m <= len(h):
            if m % 2 == 1:
                labelsWord += '&#x' +iword
            if m % 2 == 0:
                labelsWord += iword + ';'
            # print('labelsWord = ', labelsWord)
            m += 1
    list = ''
    for i in labelsWord:
        list = list + str(i)
        list += ''
    print(list)

if __name__ == "__main__":
    os.system('chcp 936 >nul')
    f = Figlet(font='slant')
    print('\033[31m====================================================\033[0m')
    print('\033[34m{}\033[0m'.format(f.renderText('16jz')))
    print('   \033[33mAuthor:LuckyRiver  ver:1.0  time:2022-10-31\033[0m')
    print('\033[31m====================================================\033[0m' + '\n')
    usage = "\n" + "python3 %prog -u ym" + "\n" + "python3 %prog -f url.txt" + "\n"
    parser = OptionParser(usage=usage)
    parser.add_option('-u', '--use', dest='use', help="target use")
    parser.add_option('-f', '--file', dest='file', help="use file")
    (options, args) = parser.parse_args()
    if options.file:
        f = open(options.file, 'r', encoding='utf-8')
        uses = f.readlines()
        for use in uses:
            use = use.strip('\n')
            str2hex(str(use))
    if options.use:
        str2hex(str(options.use))
