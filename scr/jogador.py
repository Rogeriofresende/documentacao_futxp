import random

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        self.atributos = {
            "Força": random.randint(5, 15),
            "Velocidade": random.randint(5, 15),
            "Impulso": random.randint(5, 15),
            "Chute": random.randint(5, 15),
            "Destreza": random.randint(5, 15),
            "Defesa": random.randint(5, 15),
            "Agilidade": random.randint(5, 15),
        }

    def exibir_atributos(self):
        print("Atributos:")
        for atributo, valor in self.atributos.items():
            print(f" {atributo}: {valor}")

    def registrar_log_correcoes(self, mensagem):
        """
        Adiciona uma funcionalidade para registrar correções relacionadas ao jogador.
        """
        with open("logs_simulacao.txt", "a") as log_file:
            log_file.write(f"[CORREÇÃO DE JOGADOR]: {mensagem}\n")
