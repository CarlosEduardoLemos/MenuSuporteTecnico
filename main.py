import os

def menu():
    print("Menu de Suporte Técnico")
    print("1 - Verificar e reparar disco (chkdsk)")
    print("2 - Reparar arquivos do sistema (sfc /scannow)")
    print("3 - Otimizar disco (defrag)")
    print("4 - Excluir arquivos temporários")
    print("5 - Testar velocidade de conexão (ping)")
    print("6 - Informações do dispositivo")
    print("7 - Resetar configurações de rede")
    print("8 - Reiniciar placa de rede")
    print("9 - Sair")

def executar_opcao(opcao):
    if opcao == "1":
        print("Executando chkdsk...")
        os.system("chkdsk C:")
    elif opcao == "2":
        print("Executando sfc /scannow...")
        os.system("sfc /scannow")
    elif opcao == "3":
        print("Otimizando disco...")
        os.system("defrag C:")
    elif opcao == "4":
        print("Excluindo arquivos temporários...")
        os.system("del /q/f/s %TEMP%\\*")
    elif opcao == "5":
        print("Testando velocidade de conexão (ping google.com)...")
        os.system("ping google.com")
    elif opcao == "6":
        print("Informações do dispositivo:")
        os.system("systeminfo")
    elif opcao == "7":
        print("Resetando configurações de rede...")
        os.system("netsh winsock reset")
        os.system("netsh int ip reset")
    elif opcao == "8":
        print("Reiniciando placa de rede...")
        os.system("ipconfig /release")
        os.system("ipconfig /renew")
    elif opcao == "9":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        executar_opcao(escolha)