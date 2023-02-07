import time
import sys
from time import sleep
import PySimpleGUI as sg
##

print("""

░██████╗░░░░░██╗███████╗
██╔════╝░░░░░██║██╔════╝
╚█████╗░░░░░░██║█████╗░░
░╚═══██╗██╗░░██║██╔══╝░░
██████╔╝╚█████╔╝██║░░░░░
╚═════╝░░╚════╝░╚═╝░░░░░""")
print("---------------------------------------------------------------------------------")

print("""
O processo SJF consiste em o menor processo vem primeiro,
ou seja, caso tenhamos um processo com 1mb de tamanho e 
outro de 2Mb o processo de 1Mb seria processado primeiro
""")
print("")

print("Tamanho do Processo A (0-15)")
prcA = int(input(":"))
print("---------------------------------------------------------------------------------")
print("Tamanho do Processo B (0-15)")
prcB = int(input(":"))
print("---------------------------------------------------------------------------------")
print("Tamanho do Processo C (0-15)")
prcC = int(input(":"))
print("---------------------------------------------------------------------------------")

if prcA > 15 or prcB > 15 or prcC > 15:
    print("Limite de tempo excedido, tente novamente com valores menores que 15 segundos por processo")
    print("---------------------------------------------------------------------------------")
else:
    proc = [prcA, prcB, prcC]
    proc.sort()
    temp = proc[0]

    print("PROCESSANDO")
    for contagem in range(0, temp):
        sleep(1)
        sys.stdout.write("██")

    print("")
    print("---------------------------------------------------------------------------------")
    print(f"PROCESSO FINALIZADO {temp} segundos.")
    print("---------------------------------------------------------------------------------")

    temp = proc[1]
    print("PROCESSANDO")
    for contagem in range(0, temp+):
        sleep(1)

        sys.stdout.write("██")

    print("")

    print("---------------------------------------------------------------------------------")
    print(f"PROCESSO FINALIZADO em {temp} segundos.")
    print("---------------------------------------------------------------------------------")

    temp = proc[2]

    print("PROCESSANDO")
    for contagem in range(0, temp):
        sleep(1)

        sys.stdout.write("██")

    print("")
    print("---------------------------------------------------------------------------------")
    print(f"PROCESSO FINALIZADO em {temp} segundos.")
    print("---------------------------------------------------------------------------------")

print(f"""
PROCESSO A:{prcA} segundos
PROCESSO B:{prcB} segundos
PROCESSO C:{prcC} segundos

""")

