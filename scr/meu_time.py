import random
from jogador import Jogador

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = self.criar_time()

    def criar_time(self):
        posicoes = ["Atacante", "Meio-campo", "Zagueiro", "Goleiro"]
        jogadores = []
        try:
            for posicao in posicoes:
                limite = 2 if posicao != "Goleiro" else 1
                for j in range(limite):  # Apenas um goleiro por time
                    nome_jogador = f"{posicao} {j + 1} ({self.nome})"
                    jogador = Jogador(nome_jogador, posicao)
                    jogadores.append(jogador)
            return jogadores
        except Exception as e:
            self.registrar_erro_time(f"Erro ao criar time: {e}")
            return []

    def exibir_time(self):
        try:
            print(f"\nTime: {self.nome}")
            for jogador in self.jogadores:
                print(f"- {jogador.nome} ({jogador.posicao})")
                jogador.exibir_atributos()
        except Exception as e:
            self.registrar_erro_time(f"Erro ao exibir time: {e}")

    def registrar_erro_time(self, mensagem):
        """
        Adiciona uma funcionalidade para registrar erros específicos do time.
        """
        with open("logs_simulacao.txt", "a") as log_file:
            log_file.write(f"[ERRO DE TIME]: {mensagem}\n")
