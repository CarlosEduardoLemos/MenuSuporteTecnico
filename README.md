# MenuSuporteTecnico

## Descrição

Este projeto é um menu interativo em Python para suporte técnico de T.I, criado por Carlos Eduardo Lemos. Ele automatiza tarefas comuns do primeiro atendimento, facilitando diagnósticos e manutenções em sistemas Windows. O objetivo é agilizar o suporte ao usuário, reunindo diversas ferramentas e comandos em um único local.

## Funcionalidades

O menu oferece as seguintes opções:

1. **Verificar e Reparar Disco (CHKDSK):** Verifica e repara erros no disco rígido.
2. **Reparar Arquivos de Sistema (SFC):** Verifica e repara arquivos corrompidos do Windows.
3. **Limpar Arquivos Temporários e Cache DNS:** Remove arquivos temporários e limpa o cache DNS.
4. **Diagnóstico de Memória:** Inicia o diagnóstico de memória do Windows.
5. **Verificar Conectividade de Rede (Ping):** Testa a conexão de rede com o comando ping.
6. **Rastreamento de Rota (Tracert):** Analisa o caminho até um destino na internet.
7. **Abrir Gerenciador de Tarefas:** Abre o gerenciador de tarefas do Windows.
8. **Backup de Drivers (Lista):** Lista todos os drivers instalados.
9. **Abrir Windows Update:** Abre as configurações do Windows Update.
10. **Informações do Sistema:** Exibe informações detalhadas do sistema.
11. **Limpar Cache DNS:** Limpa apenas o cache DNS.
12. **Reiniciar Serviços de Rede:** Restaura configurações de rede.
13. **Desfragmentar Disco:** Otimiza o disco rígido (permite escolher a letra do disco).
14. **Gerenciar Usuários Locais:** Abre o gerenciamento de usuários locais.
15. **Verificar Integridade (DISM):** Verifica a integridade do sistema com DISM (confirmação antes de executar).
16. **Ver Logs de Eventos:** Abre o visualizador de eventos do Windows.
17. **Testar Velocidade Básica:** Testa a velocidade de conexão com ping no Google.
18. **Criar Ponto de Restauração:** Cria um ponto de restauração do sistema (confirmação antes de executar).
19. **Executar Comando Personalizado:** Permite executar qualquer comando do usuário.
20. **Atualizar Programas com Winget:** Atualiza todos os programas via Winget.
21. **Executar Manutenção Completa:** Executa uma sequência de comandos de manutenção (confirmação antes de executar).
22. **Abrir Ferramentas do Sistema:** Abre o painel de controle.
23. **Sair:** Encerra o programa.
24. **Ajuda:** Exibe explicações detalhadas sobre cada comando.

## Registro de Ações

Todas as operações realizadas pelo menu são registradas automaticamente no arquivo `suporte_log.txt`, permitindo histórico e auditoria das atividades de suporte.

## Ajuda e Segurança

- O menu possui uma opção de **Ajuda** que explica cada comando.
- Antes de executar ações críticas (como CHKDSK, DISM, criar ponto de restauração ou manutenção completa), o sistema solicita confirmação do usuário.
- Para comandos que envolvem discos, o usuário pode escolher a letra do disco desejado.

## Requisitos

- Python 3.x instalado no Windows.

## Como usar

1. Certifique-se de ter o Python instalado no Windows.
2. Recomenda-se executar o terminal como administrador para garantir o funcionamento de todos os comandos.
3. Execute o arquivo `main.py`:
   ```
   python main.py
   ```
4. Escolha a opção desejada digitando o número correspondente e pressionando Enter.

## Exemplo de Uso

Ao iniciar o programa, você verá um menu como este:

```
1. Verificar e Reparar Disco (CHKDSK)
2. Reparar Arquivos de Sistema (SFC)
...
24. Ajuda
```

Digite o número da opção desejada e pressione Enter.

## Melhorias Futuras

- Interface gráfica para facilitar o uso.
- Suporte a múltiplos idiomas.
- Execução assíncrona de comandos demorados.

## Licença

Este projeto está sob a licença MIT.

