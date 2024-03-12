from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from pynput.keyboard import Key, Controller
import time
import re
import webbrowser

keyboard = Controller()

input("Para funcionar, logue no nfstock primeiro e depois pressione ENTER aqui nesta tela.")

#diretorio da pasta onde estao os xml's
path_of_xmls = input("\n\n\nDigite o diretorio dos cte que deseja verificar: \n")

#pega todos os nomes dos arquivos e joga pra uma lista
all_xmls = [file for file in listdir(path_of_xmls) if isfile(join(path_of_xmls, file))]

i=0
while (i<len(all_xmls)): 
    with open(path_of_xmls+"\\"+all_xmls[i], 'r') as file:
        data = file.read()

    all_data = BeautifulSoup(data, "xml")

    #procura no arquivo apenas a tag que tem o cte
    cte_number = str(all_data.find_all('nCT'))

    #pega apenas o que esta dentro da tag
    cte_number = re.findall('\d+', cte_number)
    cte_number = cte_number[0]
    
    print(cte_number)
    
    #aqui vai o link do nfstock + a variavel cte_number
    webbrowser.open("https://nfstock.alterdata.com.br/Cte/ContratadosFiltro?OrdernarPor=0&MostrarOpcaoFiltroImportacao=True&Modelo=&Serie=&Numero="+cte_number+"&Chave=&StatusManifestacao=-1&Tipo=Tomador&DataDe=&DataAte=")
    time.sleep(5)
    
    #fecha a aba do nfstock sozinho
    with keyboard.pressed(Key.ctrl):
        keyboard.press('w')
        keyboard.release('w')     
    
    if(i == len(all_xmls)-1): 
        break
    else:
        print("proximo cte:")
    i+=1

print("\nTotal de ctes:", i+1)
input("Verificacao concluida. Aperte enter para sair.")
