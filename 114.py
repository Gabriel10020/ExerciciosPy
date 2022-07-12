import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mDeu Erro.\033[m')
else:
    print('\033[32mTudo Certo.\033[m')
