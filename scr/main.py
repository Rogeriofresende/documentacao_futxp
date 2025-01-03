from jogador import Jogador
from meu_time import Time
from partida import Partida

# Configuração para rodar múltiplas simulações
numero_de_simulacoes = 1000  # Defina o número de simulações desejado
modo_simulacao = True  # Define se é simulação automática ou modo interativo

# Variáveis para relatórios
simulacoes_completadas = 0
erros_encontrados = 0

if modo_simulacao:
    print(f"Iniciando {numero_de_simulacoes} simulações...\n")

# Loop para rodar múltiplas simulações
for simulacao in range(1, numero_de_simulacoes + 1):
    print(f"=== Simulação {simulacao} ===") if modo_simulacao else None

    # Criar os times e jogadores
    meu_time = Time("Seu Time")
    adversario_time = Time("Adversário")

    # Escolher um jogador principal do time
    jogador_principal = meu_time.jogadores[0]  # Seleciona o primeiro jogador do time

    # Criar a partida com o modo simulação
    partida = Partida(jogador_principal, adversario_time, modo_simulacao=modo_simulacao)

    # Apresentar a ficha do jogador (somente no modo interativo)
    if not modo_simulacao:
        partida.apresentar_ficha_jogador()

    try:
        # Iniciar a partida
        partida.iniciar()
        simulacoes_completadas += 1  # Incrementa simulações concluídas
    except Exception as e:
        # Registrar qualquer erro encontrado durante a simulação
        with open("logs_simulacao.txt", "a") as log_file:
            log_file.write(f"Erro na Simulação {simulacao}: {str(e)}\n")
        print(f"Erro na Simulação {simulacao}: {e}")
        erros_encontrados += 1  # Incrementa contador de erros

# Gerar relatório final
total_simulacoes = numero_de_simulacoes
simulacoes_sucesso = simulacoes_completadas
percentual_sucesso = (simulacoes_sucesso / total_simulacoes) * 100 if total_simulacoes > 0 else 0

print("\n=== Relatório Final ===")
print(f"Total de Simulações: {total_simulacoes}")
print(f"Simulações Bem-sucedidas: {simulacoes_sucesso}")
print(f"Erros Encontrados: {erros_encontrados}")
print(f"Percentual de Sucesso: {percentual_sucesso:.2f}%")

# Salvar relatório no arquivo
with open("relatorio_simulacoes.txt", "w") as relatorio_file:
    relatorio_file.write("=== Relatório Final ===\n")
    relatorio_file.write(f"Total de Simulações: {total_simulacoes}\n")
    relatorio_file.write(f"Simulações Bem-sucedidas: {simulacoes_sucesso}\n")
    relatorio_file.write(f"Erros Encontrados: {erros_encontrados}\n")
    relatorio_file.write(f"Percentual de Sucesso: {percentual_sucesso:.2f}%\n")

print("\nRelatório salvo em 'relatorio_simulacoes.txt'!")
