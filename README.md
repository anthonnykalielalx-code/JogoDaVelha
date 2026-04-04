# 🎮 Jogo da Velha em Python (Terminal)

Um jogo da velha completo rodando no terminal, com **modo memória**, **3
níveis de dificuldade** e **CPU com lógica básica de IA**.

------------------------------------------------------------------------

## 📌 Funcionalidades

-   Interface em ASCII no terminal\
-   Jogador vs Computador\
-   3 níveis de dificuldade\
-   Modo memória (esconde jogadas antigas)\
-   CPU que tenta vencer ou bloquear\
-   Loop para jogar várias partidas

------------------------------------------------------------------------

## 🧠 Dificuldade da CPU

  Nível         Comportamento
  ------------- ----------------------------------
  1 - Fácil     Jogadas aleatórias
  2 - Médio     Tenta vencer ou bloquear
  3 - Difícil   Mesmo do médio (mais desafiador)

------------------------------------------------------------------------

## 🕹 Como jogar

Use **Letra + Número** para jogar:

    A   B   C

+---+---+---+ 1 \| \| \| \| +---+---+---+ 2 \| \| \| \| +---+---+---+ 3
\| \| \| \| +---+---+---+

Exemplos de jogadas: A1\
B2\
C3

Você joga com **X**\
O computador joga com **O**

------------------------------------------------------------------------

## 👁 Modo Memória

Quando ativado, o tabuleiro esconde jogadas antigas durante a partida.\
Isso aumenta a dificuldade e treina a memória do jogador 😈

------------------------------------------------------------------------

## ▶ Como executar

### 1) Instale o Python (3.8+)

Verifique: python --version

### 2) Clone o repositório

git clone https://github.com/EdcleyVitor/jogo-da-velha-python.git

### 3) Execute o jogo

python jogo.py

------------------------------------------------------------------------

## 📂 Estrutura do Código

  Função       Descrição
  ------------ -------------------------
  desenhar()   Mostra o tabuleiro
  checar()     Verifica vitória
  cpumove()    IA da CPU
  partida()    Executa uma partida
  main         Loop de várias partidas

------------------------------------------------------------------------

## 🤖 Lógica da IA

No modo médio/difícil a CPU: 1. Procura jogada para vencer\
2. Se não houver, tenta bloquear o jogador\
3. Caso contrário, joga aleatório

------------------------------------------------------------------------

## 💡 Possíveis melhorias

-   Interface gráfica (Tkinter/Pygame)
-   IA Minimax (invencível)
-   Multiplayer online
-   Placar de vitórias
-   Versão web

------------------------------------------------------------------------

## 👨‍💻 Autor

Edcley Vítor

Se gostou do projeto, deixe uma ⭐ no repositório!
