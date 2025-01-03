# Regras do Jogo: **Fut XP**

## 1. **Objetivo do Jogo**
- Simular uma partida de futebol interativa ou automatizada onde o jogador principal tenta vencer o adversário.
- O vencedor é determinado pelo número de gols marcados ao final de 90 minutos simulados.

---

## 2. **Estrutura da Partida**
### 2.1. **Início do Jogo**
- O jogador seleciona um personagem principal e define sua posição no time (Atacante, Meio-campo ou Zagueiro).
- Um time adversário é gerado automaticamente.

### 2.2. **Duração do Jogo**
- A partida ocorre em turnos alternados com intervalos simulados de 3 minutos por turno.
- Cada ação realizada equivale a um turno.
- O jogo termina ao atingir 90 minutos simulados.

---

## 3. **Turno do Jogador (Seu Time)**
- O jogador tem posse de bola e escolhe entre as ações disponíveis:
  1. **Driblar:** Tentar passar pelo adversário.
  2. **Correr:** Avançar no campo.
  3. **Tocar Bola:** Passar para outro jogador.
  4. **Lançar:** Enviar a bola a longa distância.
  5. **Segurar:** Manter a posse de bola.
- Cada ação é avaliada com base nos atributos do jogador, rolando um dado (D20) para calcular o resultado.

---

## 4. **Turno do Adversário**
- O adversário age automaticamente, selecionando aleatoriamente entre as ações:
  - Driblar, Chutar ou Lançar.
- As ações do adversário são avaliadas com base em seus atributos, rolando um dado (D20).

---

## 5. **Resolução de Ações**
- **Atributos Importantes**  
  Cada jogador possui atributos como Força, Velocidade, Impulso, Chute, Destreza, Defesa e Agilidade.  
  O sucesso de cada ação depende da combinação entre o atributo relevante e um dado (D20) rolado.  

- **Regras de Sucesso ou Falha**  
  - Uma ação é bem-sucedida se o resultado for maior que 15.
  - Ações podem ter modificadores de vantagem ou desvantagem:
    - **Vantagem:** +2 no resultado.
    - **Desvantagem:** -2 no resultado.

- **Consequências das Ações**
  - **Gol:** Se uma ação ofensiva for bem-sucedida no ataque, um gol é marcado.
  - **Perda de Posse:** Uma ação falha resulta em troca de posse de bola.
  - **Defesa Bem-sucedida:** Anula o ataque do adversário.

---

## 6. **Mecânicas de Jogo**
### 6.1. **Cruzamento e Cabeceio**
- Em certas situações, o jogador pode realizar um cruzamento e optar por cabecear para tentar marcar um gol.
- A jogada é determinada por atributos de Destreza e Impulso.

### 6.2. **Defesas do Goleiro**
- Durante um chute adversário, o goleiro realiza uma defesa baseada em seu atributo de Defesa, combinado com um dado (D20).

---

## 7. **Modo de Simulação**
- **Funcionamento**
  - Todas as decisões são automatizadas.
  - Erros são registrados em um log (`logs_simulacao.txt`).
  - A simulação continua mesmo em caso de erros.
  
- **Finalidade**
  - Testar o funcionamento do jogo.
  - Identificar e registrar erros para posterior análise.

---

## 8. **Logs e Relatórios**
- **Logs de Simulação**
  - Erros encontrados durante a execução do jogo ou simulação são registrados no arquivo `logs_simulacao.txt` com:
    - Timestamp.
    - Contexto do erro.
    - Solução proposta (se houver).

- **Relatório Final**
  - Geração de relatórios sobre:
    - Total de simulações realizadas.
    - Resultados de partidas (placares).
    - Erros encontrados e ações corretivas sugeridas.

---

## 9. **Finalização do Jogo**
- Ao atingir 90 minutos simulados, o jogo exibe:
  - **Placar Final:** Exemplo: "Seu Time 3 x 2 Adversário".
  - Mensagem de encerramento.

