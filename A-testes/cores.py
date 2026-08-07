cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    
    # Estilos de Texto
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    
    # Cores Padrão (Texto)
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',
    
    # Cores Claras/Brilhantes (Texto)
    'cinza_escuro': '\033[90m',
    'vermelho_claro': '\033[91m',
    'verde_claro': '\033[92m',
    'amarelo_claro': '\033[93m',
    'azul_claro': '\033[94m',
    'magenta_claro': '\033[95m',
    'ciano_claro': '\033[96m',
    'branco_brilhante': '\033[97m',
    
    # Cores de Fundo (Background)
    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_magenta': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m',
    'fundo_cinza': '\033[100m'
}
print (f"{cores['vermelho']}VERMELHO{cores['limpa']}")
print (f"{cores['verde']}VERDE{cores['limpa']}")
print (f"{cores['azul']}AZUL{cores['limpa']}")
print (f"{cores['magenta_claro']}ROSA{cores['limpa']}")
# 1. Texto Verde Claro
print(f"Status do sistema: {cores['verde_claro']}ONLINE{cores['limpa']}")

# 2. Texto Vermelho em Negrito
print(f"{cores['negrito']}{cores['vermelho']}ERRO CRÍTICO!{cores['limpa']}")

# 3. Texto Preto com Fundo Amarelo (Aviso)
print(f"{cores['fundo_amarelo']}{cores['preto']} ATENÇÃO: Verifique os dados {cores['limpa']}")

# 4. Texto Ciano Sublinhado
print(f"Acesse o {cores['sublinhado']}{cores['ciano']}link do projeto{cores['limpa']} para mais detalhes.")

# 5. Sucesso ou Conclusão (Texto Verde com Ícone)
print(f"[{cores['verde']}✔{cores['limpa']}] Download concluído com sucesso!")

# 6. Informação Geral ou Dica (Texto Ciano Claro)
print(f"{cores['ciano_claro']}DICA:{cores['limpa']} Pressione ENTER para continuar.")

# 7. Título em Destaque (Texto Branco Brilhante com Fundo Azul)
print(f"{cores['fundo_azul']}{cores['branco_brilhante']}  SISTEMA DE CADASTRO  {cores['limpa']}")

# 8. Pergunta ou Prompt de Entrada (Texto Amarelo)
nome = input(f"Digite o seu {cores['amarelo']}nome de usuário{cores['limpa']}: ")

# 9. Notificação de Alerta Suave (Texto Amarelo Claro)
print(f"{cores['amarelo_claro']}Aviso: O espaço em disco está acabando (85% usado).{cores['limpa']}")

# 10. Destaque de Valores no Meio de uma Frase (Várias Cores)
print(f"O usuário {cores['magenta']}Admin{cores['limpa']} alterou o status para {cores['verde_claro']}ATIVO{cores['limpa']}.")

# 11. Mensagem de Carregamento (Texto Cinza Escuro para parecer secundário)
print(f"{cores['cinza_escuro']}Carregando banco de dados... Por favor, aguarde.{cores['limpa']}")

# 12. Estilo Negativo ou Cancelado (Texto Branco com Fundo Vermelho)
print(f"{cores['fundo_vermelho']}{cores['branco']} OPERAÇÃO ABORTADA pelo usuário. {cores['limpa']}")
