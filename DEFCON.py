""""
Autor: Fabio Monreal
Python -V: 3.6.4
E-mail: fabio.monreal@outlook.com

Esse script tem seu intuito de teste ou diversao, o mesmo deve ser compilado em EXE e usando eng reversa deve-se
quebrar as senhas em formato de string para realizar o lancamento nuclear de misseis russos :D

#KGB n me prende pfv :(
"""

import socket
import os, platform
import getpass
import time
import sys
from geopy.geocoders import Nominatim

st1 = """"
 _____ _____ _________  ___   _____ ___________ _     
|_   _/  __ \| ___ \  \/  |  /  __ \_   _| ___ \ |    
  | | | /  \/| |_/ / .  . |  | /  \/ | | | |_/ / |    
  | | | |    | ___ \ |\/| |  | |     | | |    /| |    
 _| |_| \__/\| |_/ / |  | |  | \__/\ | | | |\ \| |____
 \___/ \____/\____/\_|  |_/   \____/ \_/ \_| \_\_____/
"""

print(st1)

import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print ('Status da sessao\n ')
print ('IP : {4} \nEstado : {1} \nPais : {2} \nCidade : {3} \nProvedor : {0}'.format(org,region,country,city,IP))
ipint = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ipint.connect(("8.8.8.8", 80))
print("IP interno: " + ipint.getsockname()[0])
ipint.close()

print("Maquina: " + socket.gethostname())
print("Tipo de sistema: " + os.name, "\nPlataforma: " + platform.system() + " " + platform.release())
print("Usuario: " + getpass.getuser())


def lacamento(missil):
       print("Preparando lancamento: " + missil)
       for remaining in range(10, 0, -1):
              time.sleep(2)
              sys.stdout.write("\r")
              sys.stdout.write("{:2d} Segundos para patente nuclear" .format(remaining))
              sys.stdout.flush()
              time.sleep(1)
       sys.stdout.write("\rCompleto!\n")
       aviso = """"
       ______      __                     ___ 
       |  _  \    / _|                   /   |
       | | | |___| |_ ___ ___  _ __     / /| |
       | | | / _ \  _/ __/ _ \| '_ \   / /_| |
       | |/ /  __/ || (_| (_) | | | |  \___  |
       |___/ \___|_| \___\___/|_| |_|      |_/
       """
       print(aviso)
       alvo(missil);

def alvo(missil):
       while True:
              local = input("Endereco do alvo: ")
              geolocator = Nominatim()
              location = geolocator.geocode(local)
              print("ENDERECO: " + location.address + "\n")
              print("CORDENADAS: " + str(location.latitude), str(location.longitude))
              decisao = input("O alvo esta correto? Y|N")
              if decisao == "Y":
                     aviso1 = """"
                     ______      __                   _____ 
                     |  _  \    / _|                 |____ |
                     | | | |___| |_ ___ ___  _ __        / /
                     | | | / _ \  _/ __/ _ \| '_ \       \ \ 
                     | |/ /  __/ || (_| (_) | | | |  .___/ /
                     |___/ \___|_| \___\___/|_| |_|  \____/ 
                     """
                     print(aviso1)
                     time.sleep(2)
                     print ("Preparando lancamento! \n"
                            "ICBM: " + missil + "\n"
                            "Alvo: "+ location.latitude, location.longitude)
                     for remaining in range(20, 0, -1):
                            print("Lancamento iminente")
                            time.sleep(2)
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} Segundos para o lancamento".format(remaining))
                            sys.stdout.flush()
                            time.sleep(1)
                            aviso2 = """
                                   ______      __                   _____ 
                                   |  _  \    / _|                 / __  \ 
                                   | | | |___| |_ ___ ___  _ __    `' / /'
                                   | | | / _ \  _/ __/ _ \| '_ \     / /  
                                   | |/ /  __/ || (_| (_) | | | |  ./ /___
                                   |___/ \___|_| \___\___/|_| |_|  \_____/
                                """
                            sys.stdout.write(aviso2)

                     for remaining in range(15, 0, -1):
                            print("ICBM Lancado")
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} Segundos ate o alvo".format(remaining))
                            sys.stdout.flush()
                            time.sleep(1)
                            aviso3 = """
                                   ______      __                   __  
                                   |  _  \    / _|                 /  | 
                                   | | | |___| |_ ___ ___  _ __    `| | 
                                   | | | / _ \  _/ __/ _ \| '_ \    | | 
                                   | |/ /  __/ || (_| (_) | | | |  _| |_
                                   |___/ \___|_| \___\___/|_| |_|  \___/
                             """
                            sys.stdout.write(aviso3)
                     print("ICBM Efetivo no alvo:" + location.address)
                     time.sleep(10)
                     gg = """"
                      _____ _____   ___  ___ _      _   __    ______ 
                     |  __ \  __ \  |  \/  || |    | | / /   _|  _  \ 
                     | |  \/ |  \/  | .  . || |    | |/ /   (_) | | |
                     | | __| | __   | |\/| || |    |    \     | | | |
                     | |_\ \ |_\ \  | |  | || |____| |\  \   _| |/ / 
                      \____/\____/  \_|  |_/\_____/\_| \_/  (_)___/                                                
                     """
                     print(gg)
                     time.sleep(10)
                     sys.exit(0)

              elif decisao == "N":
                     alvo();
              else:
                     print("Opcao invalida")
                     alvo();


def icbmlaunch():
       launchwelcome = """
        _____ _____ _________  ___   _                            _       _______   _______ 
       |_   _/  __ \| ___ \  \/  |  | |                          | |     /  ___\ \ / /  ___|
         | | | /  \/| |_/ / .  . |  | |     __ _ _   _ _ __   ___| |__   \ `--. \ V /\ `--. 
         | | | |    | ___ \ |\/| |  | |    / _` | | | | '_ \ / __| '_ \   `--. \ \ /  `--. \ 
        _| |_| \__/\| |_/ / |  | |  | |___| (_| | |_| | | | | (__| | | | /\__/ / | | /\__/ /
        \___/ \____/\____/\_|  |_/  \_____/\__,_|\__,_|_| |_|\___|_| |_| \____/  \_/ \____/ 
       """
       print(launchwelcome)
       time.sleep(3)
       types = """
       (1) RS-28 Sarmat / SS-X-30 Satan 2 - Ativo
       (2) R-36M2 Voevoda / SS-18 Satan - Ativo
       (3) UR-100N 15A30 / SS-19 Stiletto - Ativo
       (4) RT-2PM Topol / 15Zh58 / SS-25 Sickle - Offline
       (5) RT-2PM2 Topol-M / SS-27 / RS12M1 / RS12M2 - Offline
       (6) RS-24 Yars: MIRV-equipped - Ativo
       (7) R-29R SS-N-18 Stingray - Ativo
       (8) R-29RK SS-N-18 Stingray Mod 2 - Ativo
       (9) R-29RL MIRV-equipped/SS-N-18 Stingray Mod 3 - Ativo
       (10) R-29RM MIRV-equipped/SS-N-23 Skiff - Offline
       (11) R-29RMU Sineva MIRV-equipped/SS-N-23 Sineva mode 2 - Ativo
       (12) R-29RMU2 MIRV-equipped/SS-N-23 Liner - Ativo
       (13) RSM-56 Bulava MIRV-equipped/SS-NX-30 - Offline
       """
       print(types)
       icbmlaunchmenu();

def icbmlaunchmenu():
       while True:
              raw_input = input("ICBM Launch>")
              if raw_input == '1':
                     missil = "RS-28 Sarmat / SS-X-30 Satan 2"
                     print("Codigo de lacamento: Sarmat")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '2':
                     missil = "R-36M2 Voevoda / SS-18 Satan"
                     print("Codigo de lacamento: Voevoda")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '3':
                     missil = "UR-100N 15A30 / SS-19 Stiletto"
                     print("Codigo de lacamento: Stiletto")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '4':
                     missil = "RT-2PM Topol / 15Zh58 / SS-25 Sickle"
                     print("Rede de acionamento offline")
                     icbmlaunchmenu();
              elif raw_input == '5':
                     missil = "RT-2PM2 Topol-M / SS-27 / RS12M1 / RS12M2"
                     print("Rede de acionamento offline")
                     icbmlaunchmenu();
              elif raw_input == '6':
                     missil = "RS-24 Yars: MIRV-equipped"
                     print("Codigo de lacamento: Yars")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '7':
                     missil = "R-29R SS-N-18 Stingray"
                     print("Codigo de lacamento: StingrayR")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '8':
                     missil = "R-29RK SS-N-18 Stingray Mod 2"
                     print("Codigo de lacamento: StingrayRK")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '9':
                     missil = "R-29RL MIRV-equipped/SS-N-18 Stingray Mod 3"
                     print("Codigo de lacamento: StingrayRL")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '10':
                     missil = "R-29RM MIRV-equipped/SS-N-23 Skiff"
                     print("Rede de acionamento offline")
                     icbmlaunchmenu();
              elif raw_input == '11':
                     missil = "R-29RMU Sineva MIRV-equipped/SS-N-23 Sineva mode 2"
                     print("Codigo de lacamento: Sineva")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '12':
                     missil = "R-29RMU2 MIRV-equipped/SS-N-23 Liner"
                     print("Codigo de lacamento: Liner")
                     time.sleep(2)
                     lacamento(missil);
              elif raw_input == '13':
                     missil = "RSM-56 Bulava MIRV-equipped/SS-NX-30"
                     print("Rede de acionamento offline")
                     icbmlaunchmenu();
              else:
                     print("Erro selecione um missil para lancar")
                     icbmlaunchmenu();


def icmblaunchauth():
       passwd = str(input("\n\nCodigo de autorizacao: "))
       if passwd == "DUCK5007HPPMA":
              print("Abrindo sistema de lancamento nuclear!")
              icbmlaunch();
       else:
              print("ACESSO NEGADO")
              icmblaunchauth();

def menu():
       while True:
              raw_input = input("CLI>")
              if raw_input == 'help':
                     print("icbm list" " - mostra lista de icbm's ativos")
                     print("icbm launch - acessa habilita sistema de lancamento de icmb (WARNING!)")
                     print("state - status global de sistema nuclear")
                     print("detection - usa radares de radio para identificar lancamentos")
              elif raw_input == 'icbm list':
                     icbmlist = """
                     RS-28 Sarmat / SS-X-30 Satan 2 - Ativo
                     R-36M2 Voevoda / SS-18 Satan - Ativo
                     UR-100N 15A30 / SS-19 Stiletto - Ativo
                     RT-2PM Topol / 15Zh58 / SS-25 Sickle - Maintence
                     RT-2PM2 Topol-M / SS-27 / RS12M1 / RS12M2 - Maintence
                     RS-24 Yars: MIRV-equipped - Ativo
                     R-29R SS-N-18 Stingray - Ativo
                     R-29RK SS-N-18 Stingray Mod 2 - Ativo
                     R-29RL MIRV-equipped/SS-N-18 Stingray Mod 3 - Ativo
                     R-29RM MIRV-equipped/SS-N-23 Skiff - Maintence
                     R-29RMU Sineva MIRV-equipped/SS-N-23 Sineva mode 2 - Ativo
                     R-29RMU2 MIRV-equipped/SS-N-23 Liner - Ativo
                     RSM-56 Bulava MIRV-equipped/SS-NX-30 - Disabled
                     """
                     print(icbmlist)
              elif raw_input == 'state':
                     defcon5 = """
                     ______      __                   _____ 
                     |  _  \    / _|                 |  ___|
                     | | | |___| |_ ___ ___  _ __    |___ \ 
                     | | | / _ \  _/ __/ _ \| '_ \       \ \ 
                     | |/ /  __/ || (_| (_) | | | |  /\__/ /
                     |___/ \___|_| \___\___/|_| |_|  \____/ 
                     """
                     print(defcon5)
              elif raw_input == 'detection':
                     print("No ICMB launch detected in Global, used: Radio, satellite, sub-echoes")
              elif raw_input == 'icbm launch':
                     print("Preparando sistemas de defesa...")
                     time.sleep(9)
                     print("Iniciando patente nuclear...")
                     time.sleep(3)
                     print("Abrindo sistema de autorizacao...")
                     time.sleep(5)
                     icmblaunchauth();
              else:
                     print("Erro digite help para ajuda")

senha = str(input("\n\nSenha de controle Global: "))
if senha == "ADX102FDCAK201":
    print ("Central de controle de sistema nuclear!")
    menu();
else:
    print ("ACESSO NEGADO")
