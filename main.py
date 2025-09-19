import os
import time

def menu():
    print("="*65)
    print("MENU DE SUPORTE TECNICO T.I")
    print("Criado por Carlos Eduardo Lemos")
    print("="*65)
    print("""
1.  Verificar e Reparar Disco (CHKDSK)
2.  Reparar Arquivos de Sistema (SFC)
3.  Limpar Arquivos Temporários e Cache DNS
4.  Diagnóstico de Memória
5.  Verificar Conectividade de Rede (Ping)
6.  Rastreamento de Rota (Tracert)
7.  Abrir Gerenciador de Tarefas
8.  Backup de Drivers (Lista)
9.  Abrir Windows Update
10. Informações do Sistema
11. Limpar Cache DNS
12. Reiniciar Serviços de Rede
13. Desfragmentar Disco
14. Gerenciar Usuários Locais
15. Verificar Integridade (DISM)
16. Ver Logs de Eventos
17. Testar Velocidade Básica (ping google.com)
18. Criar Ponto de Restauração
19. Executar Comando Personalizado
20. Atualizar Programas com Winget
21. Executar Manutenção Completa (Auto)
22. Abrir Ferramentas do Sistema
23. Sair
""")
    print("="*65)

def pausar():
    input("Pressione Enter para continuar...")

def verificar_disco():
    print("Executando chkdsk...")
    os.system("chkdsk C:")
    pausar()

def reparar_sistema():
    print("Executando sfc /scannow...")
    os.system("sfc /scannow")
    pausar()

def limpar_temp_dns():
    print("Limpando arquivos temporários e cache DNS...")
    os.system("del /q/f/s %TEMP%\\*")
    os.system("ipconfig /flushdns")
    pausar()

def diagnostico_memoria():
    print("Executando diagnóstico de memória...")
    os.system("mdsched.exe")
    pausar()

def conectividade_ping():
    print("Testando conectividade de rede (ping 8.8.8.8)...")
    os.system("ping 8.8.8.8")
    pausar()

def executar_opcao(opcao):
    try:
        if opcao == "1":
            verificar_disco()
        elif opcao == "2":
            reparar_sistema()
        elif opcao == "3":
            limpar_temp_dns()
        elif opcao == "4":
            diagnostico_memoria()
        elif opcao == "5":
            conectividade_ping()
        elif opcao == "6":
            print("Rastreamento de rota (tracert google.com)...")
            os.system("tracert google.com")
            pausar()
        elif opcao == "7":
            print("Abrindo Gerenciador de Tarefas...")
            os.system("taskmgr")
            pausar()
        elif opcao == "8":
            print("Listando drivers instalados...")
            os.system("driverquery")
            pausar()
        elif opcao == "9":
            print("Abrindo Windows Update...")
            os.system("start ms-settings:windowsupdate")
            pausar()
        elif opcao == "10":
            print("Informações do sistema:")
            os.system("systeminfo")
            pausar()
        elif opcao == "11":
            print("Limpando cache DNS...")
            os.system("ipconfig /flushdns")
            pausar()
        elif opcao == "12":
            print("Reiniciando serviços de rede...")
            os.system("netsh winsock reset")
            os.system("netsh int ip reset")
            pausar()
        elif opcao == "13":
            print("Desfragmentando disco...")
            os.system("defrag C:")
            pausar()
        elif opcao == "14":
            print("Abrindo gerenciamento de usuários locais...")
            os.system("lusrmgr.msc")
            pausar()
        elif opcao == "15":
            print("Verificando integridade do sistema (DISM)...")
            os.system("DISM /Online /Cleanup-Image /ScanHealth")
            pausar()
        elif opcao == "16":
            print("Abrindo Visualizador de Eventos...")
            os.system("eventvwr")
            pausar()
        elif opcao == "17":
            print("Testando velocidade básica (ping google.com)...")
            os.system("ping google.com")
            pausar()
        elif opcao == "18":
            print("Criando ponto de restauração...")
            os.system("powershell -command \"Checkpoint-Computer -Description 'Ponto de Restauração MenuSuporteTecnico'\"")
            pausar()
        elif opcao == "19":
            comando = input("Digite o comando personalizado: ")
            os.system(comando)
            pausar()
        elif opcao == "20":
            print("Atualizando programas com Winget...")
            os.system("winget upgrade --all")
            pausar()
        elif opcao == "21":
            print("Executando manutenção completa...")
            os.system("chkdsk C:")
            os.system("sfc /scannow")
            os.system("defrag C:")
            os.system("del /q/f/s %TEMP%\\*")
            os.system("ipconfig /flushdns")
            os.system("netsh winsock reset")
            os.system("netsh int ip reset")
            pausar()
        elif opcao == "22":
            print("Abrindo ferramentas do sistema...")
            os.system("control")
            pausar()
        elif opcao == "23":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida!")
            pausar()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        pausar()

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Digite sua opção [1-23]: ")
        if escolha.isdigit() and 1 <= int(escolha) <= 23:
            executar_opcao(escolha)
        else:
            print("Por favor, digite um número válido entre 1 e 23.")
            time.sleep(1)