import os
import time
from datetime import datetime

LOG_FILE = "suporte_log.txt"

def log_acao(acao):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {acao}\n")

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
24. Ajuda
""")
    print("="*65)

def ajuda():
    print("\n=== AJUDA ===")
    print("Escolha o número da opção desejada e pressione Enter.")
    print("Algumas opções exigem permissões de administrador.")
    print("Principais comandos:")
    print("1. CHKDSK: Verifica e repara erros no disco rígido.")
    print("2. SFC: Verifica e repara arquivos corrompidos do Windows.")
    print("3. Limpeza: Remove arquivos temporários e limpa cache DNS.")
    print("4. Diagnóstico de Memória: Testa a memória RAM.")
    print("15. DISM: Verifica integridade do sistema.")
    print("18. Ponto de Restauração: Cria um ponto de restauração do Windows.")
    print("21. Manutenção Completa: Executa uma sequência de comandos de manutenção.")
    print("19. Comando Personalizado: Permite executar qualquer comando do Windows.")
    print("Para mais detalhes, consulte a documentação ou peça suporte ao T.I.\n")
    pausar()

def pausar():
    input("Pressione Enter para continuar...")

def confirmar_acao(mensagem):
    resposta = input(f"{mensagem} (s/n): ").strip().lower()
    return resposta == "s"

def escolher_disco():
    disco = input("Informe a letra do disco (ex: C): ").strip().upper()
    if len(disco) == 1 and disco.isalpha():
        return disco
    else:
        print("Letra de disco inválida. Usando C por padrão.")
        return "C"

def verificar_disco():
    disco = escolher_disco()
    if not confirmar_acao(f"Tem certeza que deseja executar CHKDSK em {disco}:? Isso pode demorar e exigir reinicialização."):
        print("Ação cancelada.")
        return
    print(f"Executando chkdsk em {disco}: ...")
    log_acao(f"CHKDSK executado em {disco}:")
    os.system(f"chkdsk {disco}:")
    pausar()

def reparar_sistema():
    if not confirmar_acao("Executar SFC pode demorar. Deseja continuar?"):
        print("Ação cancelada.")
        return
    print("Executando sfc /scannow...")
    log_acao("SFC /scannow executado")
    os.system("sfc /scannow")
    pausar()

def limpar_temp_dns():
    print("Limpando arquivos temporários e cache DNS...")
    log_acao("Limpeza de arquivos temporários e cache DNS")
    os.system("del /q/f/s %TEMP%\\*")
    os.system("ipconfig /flushdns")
    pausar()

def diagnostico_memoria():
    print("Executando diagnóstico de memória...")
    log_acao("Diagnóstico de memória iniciado")
    os.system("mdsched.exe")
    pausar()

def conectividade_ping():
    print("Testando conectividade de rede (ping 8.8.8.8)...")
    log_acao("Ping 8.8.8.8 executado")
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
            log_acao("Tracert google.com executado")
            os.system("tracert google.com")
            pausar()
        elif opcao == "7":
            print("Abrindo Gerenciador de Tarefas...")
            log_acao("Gerenciador de Tarefas aberto")
            os.system("taskmgr")
            pausar()
        elif opcao == "8":
            print("Listando drivers instalados...")
            log_acao("Lista de drivers exibida")
            os.system("driverquery")
            pausar()
        elif opcao == "9":
            print("Abrindo Windows Update...")
            log_acao("Windows Update aberto")
            os.system("start ms-settings:windowsupdate")
            pausar()
        elif opcao == "10":
            print("Informações do sistema:")
            log_acao("Informações do sistema exibidas")
            os.system("systeminfo")
            pausar()
        elif opcao == "11":
            print("Limpando cache DNS...")
            log_acao("Cache DNS limpo")
            os.system("ipconfig /flushdns")
            pausar()
        elif opcao == "12":
            print("Reiniciando serviços de rede...")
            log_acao("Serviços de rede reiniciados")
            os.system("netsh winsock reset")
            os.system("netsh int ip reset")
            pausar()
        elif opcao == "13":
            disco = escolher_disco()
            print(f"Desfragmentando disco {disco}: ...")
            log_acao(f"Desfragmentação executada em {disco}:")
            os.system(f"defrag {disco}:")
            pausar()
        elif opcao == "14":
            print("Abrindo gerenciamento de usuários locais...")
            log_acao("Gerenciamento de usuários locais aberto")
            os.system("lusrmgr.msc")
            pausar()
        elif opcao == "15":
            if not confirmar_acao("Executar DISM pode afetar o sistema. Deseja continuar?"):
                print("Ação cancelada.")
                return
            print("Verificando integridade do sistema (DISM)...")
            log_acao("DISM /ScanHealth executado")
            os.system("DISM /Online /Cleanup-Image /ScanHealth")
            pausar()
        elif opcao == "16":
            print("Abrindo Visualizador de Eventos...")
            log_acao("Visualizador de Eventos aberto")
            os.system("eventvwr")
            pausar()
        elif opcao == "17":
            print("Testando velocidade básica (ping google.com)...")
            log_acao("Ping google.com executado")
            os.system("ping google.com")
            pausar()
        elif opcao == "18":
            if not confirmar_acao("Criar ponto de restauração?"):
                print("Ação cancelada.")
                return
            print("Criando ponto de restauração...")
            log_acao("Ponto de restauração criado")
            os.system("powershell -command \"Checkpoint-Computer -Description 'Ponto de Restauração MenuSuporteTecnico'\"")
            pausar()
        elif opcao == "19":
            comando = input("Digite o comando personalizado: ")
            log_acao(f"Comando personalizado executado: {comando}")
            os.system(comando)
            pausar()
        elif opcao == "20":
            print("Atualizando programas com Winget...")
            log_acao("Atualização de programas com Winget")
            os.system("winget upgrade --all")
            pausar()
        elif opcao == "21":
            if not confirmar_acao("Executar manutenção completa?"):
                print("Ação cancelada.")
                return
            print("Executando manutenção completa...")
            log_acao("Manutenção completa executada")
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
            log_acao("Painel de controle aberto")
            os.system("control")
            pausar()
        elif opcao == "23":
            print("Saindo...")
            log_acao("Programa encerrado")
            exit()
        elif opcao == "24":
            ajuda()
        else:
            print("Opção inválida!")
            pausar()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        log_acao(f"Erro: {e}")
        pausar()

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Digite sua opção [1-24]: ")
        if escolha.isdigit() and 1 <= int(escolha) <= 24:
            executar_opcao(escolha)
        else:
            print("Por favor, digite um número válido entre 1 e 24.")
            time.sleep(1)