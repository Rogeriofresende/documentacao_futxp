import random
import os
import datetime

class Partida:
    def __init__(self, jogador, adversario, modo_simulacao=False):
        self.jogador = jogador
        self.adversario = adversario
        self.placar = {"Seu Time": 0, "Adversário": 0}
        self.minutos = 0
        self.prorrogacao = random.randint(1, 5)
        self.posse_bola = random.choice(["Seu Time", "Adversário"])
        self.campo = "Meio-campo próprio" if self.posse_bola == "Seu Time" else "Meio-campo adversário"
        self.cruzamento_bem_sucedido = False  # Flag para rastrear cruzamentos bem-sucedidos
        self.modo_simulacao = modo_simulacao

    def registrar_log(self, mensagem):
        with open("logs_simulacao.txt", "a") as log_file:
            log_file.write(mensagem + "\n")

    def registrar_erro(self, simulacao_num, tipo_erro, mensagem, estado_jogo, contexto, codigo_correcao=None, observacoes=None):
        """
        Registra erros no log com suporte para códigos de correção e observações.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"[DATA/HORA]: {timestamp}\n"
            f"[SIMULAÇÃO]: {simulacao_num}\n"
            f"[TIPO DE ERRO]: {tipo_erro}\n"
            f"[MENSAGEM]: {mensagem}\n"
            f"[ESTADO DO JOGO]: \n"
            f"    - Posse de Bola: {estado_jogo.get('posse_bola', 'N/A')}\n"
            f"    - Minutos: {estado_jogo.get('minutos', 'N/A')}\n"
            f"    - Ação: {estado_jogo.get('acao', 'N/A')}\n"
        )
        if codigo_correcao:
            log_entry += f"[CÓDIGO DE CORREÇÃO]:\n{codigo_correcao}\n"
        if observacoes:
            log_entry += f"[OBSERVAÇÕES]:\n{observacoes}\n"
        log_entry += "---------------------------------------\n"
        with open("logs_simulacao.txt", "a") as log_file:
            log_file.write(log_entry)

    def determinar_dado(self, pontos):
        if pontos <= 3:
            return "D4"
        elif pontos <= 7:
            return "D6"
        elif pontos <= 11:
            return "D8"
        elif pontos <= 15:
            return "D10"
        elif pontos <= 19:
            return "D12"
        else:
            return "D20"

    def apresentar_ficha_jogador(self):
        atributos_para_acoes = {
            "driblar": "Agilidade",
            "correr": "Velocidade",
            "chutar": "Chute",
            "cabecear": "Impulso",
            "tocar bola": "Destreza",
            "cruzar": "Chute",
            "lançar": "Destreza",
            "segurar": "Força",
            "isolar": "Força",
        }

        print("\n==== Ficha do Jogador ====")
        print(f"Nome: {self.jogador.nome}")
        print(f"Posição: {self.jogador.posicao}")
        print("\nAções e Atributos:")
        print(f"{'Ação':<15}{'Atributo':<15}{'Pontos':<10}{'Dado':<10}")
        print("=" * 50)
        for acao, atributo in atributos_para_acoes.items():
            pontos = self.jogador.atributos[atributo]
            dado = self.determinar_dado(pontos)
            print(f"{acao:<15}{atributo:<15}{pontos:<10}{dado:<10}")
        print("=" * 50)
        if not self.modo_simulacao:
            input("\nPressione qualquer tecla para começar a partida...\n")

    def rolar_dado(self, jogador_dado, defensor_dado, vantagem=None):
        roll_jogador1 = random.randint(1, jogador_dado)
        roll_jogador2 = random.randint(1, jogador_dado) if vantagem == "vantagem" else roll_jogador1
        roll_defensor1 = random.randint(1, defensor_dado)
        roll_defensor2 = random.randint(1, defensor_dado) if vantagem == "desvantagem" else roll_defensor1

        resultado_jogador = max(roll_jogador1, roll_jogador2) if vantagem == "vantagem" else min(roll_jogador1, roll_jogador2) if vantagem == "desvantagem" else roll_jogador1
        resultado_defensor = max(roll_defensor1, roll_defensor2) if vantagem == "desvantagem" else min(roll_defensor1, roll_defensor2) if vantagem == "vantagem" else roll_defensor1

        print("=== Rolagem dos Dados ===")
        if vantagem == "vantagem":
            print(f"Jogador rolou: {roll_jogador1}, {roll_jogador2} (D{jogador_dado}) -> Resultado final: {resultado_jogador}")
            print(f"Defensor rolou: {roll_defensor1} (D{defensor_dado}) -> Resultado final: {resultado_defensor}")
        elif vantagem == "desvantagem":
            print(f"Jogador rolou: {roll_jogador1} (D{jogador_dado}) -> Resultado final: {resultado_jogador}")
            print(f"Defensor rolou: {roll_defensor1}, {roll_defensor2} (D{defensor_dado}) -> Resultado final: {resultado_defensor}")
        else:
            print(f"Jogador rolou: {roll_jogador1} (D{jogador_dado}) -> Resultado final: {resultado_jogador}")
            print(f"Defensor rolou: {roll_defensor1} (D{defensor_dado}) -> Resultado final: {resultado_defensor}")

        if resultado_jogador > resultado_defensor:
            return True
        elif resultado_jogador == resultado_defensor:
            print("Defesa vence em caso de empate")
            return False
        else:
            return False

    def iniciar(self, simulacao_num=0):
        try:
            print("\n================ Início da Partida ================")
            self.registrar_log("================ Início da Partida ================")
            print(f"O jogo começa! {self.posse_bola} tem a posse de bola no {self.campo}.")
            self.registrar_log(f"O jogo começa! {self.posse_bola} tem a posse de bola no {self.campo}.")

            while self.minutos < 90 + self.prorrogacao:
                if self.posse_bola == "Seu Time":
                    print(f"\n===== Turno do Seu Time =====")
                    self.registrar_log(f"===== Turno do Seu Time =====")
                    acoes = {
                        "Meio-campo próprio": ["driblar", "correr", "tocar bola", "lançar", "segurar"],
                        "Meio-campo adversário": ["driblar", "correr", "tocar bola", "lançar", "chutar"],
                        "Ataque": ["driblar", "correr", "tocar bola", "chutar", "cruzar"]
                    }[self.campo]

                    if self.cruzamento_bem_sucedido:
                        acoes = ["cabecear"]

                    if not self.modo_simulacao:
                        acoes_numeradas = [f"{i+1}-{acao}" for i, acao in enumerate(acoes)]
                        print("Escolha uma ação:")
                        for acao in acoes_numeradas:
                            print(f"{acao}")

                        escolha = input("Digite o número da ação escolhida: ").strip()
                        if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(acoes):
                            print("Ação inválida. Tente novamente.")
                            self.registrar_log("Ação inválida escolhida pelo jogador.")
                            continue

                        acao = acoes[int(escolha) - 1]
                    else:
                        acao = random.choice(acoes)

                    sucesso = self.simular_acao(
                        self.jogador.nome,
                        acao,
                        random.randint(5, 15),
                        vantagem=None if acao not in ["chutar", "cabecear"] else "desvantagem",
                        goleiro=self.adversario.jogadores[-1] if acao in ["chutar", "cabecear"] else None
                    )

                    self.minutos += 3
                    if sucesso:
                        mensagem = f"Minuto {self.minutos}: Sucesso! {self.jogador.nome} realizou a ação {acao} com sucesso. (Local: {self.campo})"
                        print(mensagem)
                        self.registrar_log(mensagem)

                        if acao == "chutar":
                            self.placar["Seu Time"] += 1
                            mensagem = f"Minuto {self.minutos}: GOL de {self.jogador.nome}! Placar: Seu Time {self.placar['Seu Time']} x {self.placar['Adversário']} Adversário"
                            print(mensagem)
                            self.registrar_log(mensagem)
                            self.posse_bola = "Adversário"
                            self.campo = "Meio-campo próprio"
                        elif acao == "correr":
                            self.campo = "Meio-campo adversário" if self.campo == "Meio-campo próprio" else "Ataque"
                        elif acao in ["tocar bola", "lançar"] and self.campo == "Meio-campo adversário":
                            self.campo = "Ataque"
                        elif acao == "cruzar":
                            self.cruzamento_bem_sucedido = True
                        elif acao == "cabecear":
                            self.placar["Seu Time"] += 1
                            mensagem = f"Minuto {self.minutos}: GOL de cabeça por {self.jogador.nome}! Placar: Seu Time {self.placar['Seu Time']} x {self.placar['Adversário']} Adversário"
                            print(mensagem)
                            self.registrar_log(mensagem)
                            self.posse_bola = "Adversário"
                            self.campo = "Meio-campo próprio"
                            self.cruzamento_bem_sucedido = False
                    else:
                        mensagem = f"Minuto {self.minutos}: Jogada falhou! O adversário recuperou a posse. (Local: {self.campo})"
                        print(mensagem)
                        self.registrar_log(mensagem)
                        self.posse_bola = "Adversário"
                else:
                    print(f"\n===== Turno do Adversário =====")
                    self.registrar_log(f"===== Turno do Adversário =====")
                    print(f"O adversário está jogando...")
                    acoes = ["driblar", "correr", "chutar"]
                    acao_adversario = random.choice(acoes)
                    jogador_adversario = random.choice(self.adversario.jogadores)  # Escolher jogador do adversário
                    sucesso_adversario = self.simular_acao(
                        "Adversário",
                        acao_adversario,
                        jogador_adversario.atributos["Defesa"],
                        vantagem=None,
                        goleiro=self.jogador if acao_adversario in ["chutar", "cabecear"] else None
                    )
                    self.minutos += 3
                    if sucesso_adversario:
                        mensagem = f"Minuto {self.minutos}: Sucesso! Adversário realizou a ação {acao_adversario}. (Local: {self.campo})"
                        print(mensagem)
                        self.registrar_log(mensagem)

                        if acao_adversario == "chutar":
                            self.placar["Adversário"] += 1
                            mensagem = f"Minuto {self.minutos}: GOL do Adversário! Placar: Seu Time {self.placar['Seu Time']} x {self.placar['Adversário']} Adversário"
                            print(mensagem)
                            self.registrar_log(mensagem)
                            self.posse_bola = "Seu Time"
                            self.campo = "Meio-campo próprio"
                        elif acao_adversario == "correr":
                            self.campo = "Ataque"
                    else:
                        mensagem = f"Minuto {self.minutos}: Seu Time recuperou a bola! (Local: {self.campo})"
                        print(mensagem)
                        self.registrar_log(mensagem)
                        self.posse_bola = "Seu Time"

            mensagem = f"Placar final: Seu Time {self.placar['Seu Time']} x {self.placar['Adversário']} Adversário"
            print(mensagem)
            self.registrar_log(mensagem)
            print("\n================ Fim da Partida ================")
            self.registrar_log("================ Fim da Partida ================")
        except Exception as e:
            estado_jogo = {
                "posse_bola": self.posse_bola,
                "minutos": self.minutos,
                "acao": "Desconhecida"
            }
            contexto = "partida.py, iniciar"
            self.registrar_erro(
                simulacao_num=simulacao_num,
                tipo_erro=type(e).__name__,
                mensagem=str(e),
                estado_jogo=estado_jogo,
                contexto=contexto
            )
            print(f"Erro registrado na Simulação {simulacao_num}: {e}")
