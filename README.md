# 🎮 Jogo da Velha em Python (Terminal)

Um jogo da velha completo rodando no terminal, com **modo memória**, **3 níveis de dificuldade** e **CPU com lógica básica de IA**.

Projeto feito em **Python puro** 🐍 — ideal para estudar lógica de programação, estruturas de dados e IA simples.

---

## 📌 Funcionalidades

- Interface em ASCII no terminal  
- Jogador vs Computador  
- 3 níveis de dificuldade  
- Modo memória (esconde jogadas antigas)  
- CPU que tenta vencer e bloquear o jogador  
- Possibilidade de jogar várias partidas seguidas  

---

## 🧠 Níveis de dificuldade da CPU

| Nível | Descrição |
|---|---|
| **1 – Fácil** | CPU joga totalmente aleatório |
| **2 – Médio** | CPU tenta vencer ou bloquear |
| **3 – Difícil** | Mesmo comportamento do médio (IA básica mais competitiva) |

---

## 🕹️ Como jogar

As jogadas são feitas usando **Letra + Número**:

```

```
A   B   C
```

+---+---+---+
1 |   |   |   |
+---+---+---+
2 |   |   |   |
+---+---+---+
3 |   |   |   |
+---+---+---+

```

### Exemplos de jogadas válidas:
```

A1
B2
C3

````

- O jogador usa **X**
- O computador usa **O**

---

## 👁️ Modo Memória

Quando ativado, o tabuleiro **esconde jogadas antigas** durante a partida.

Isso deixa o jogo mais difícil e treina sua memória 😈

---

## ▶️ Como executar o projeto

### 1️⃣ Instale o Python (3.8 ou superior)

Verifique a instalação:
```bash
python --version
````

### 2️⃣ Clone o repositório

```bash
git clone https://github.com/EdcleyVitor/JogoDaVelha.git
```

### 3️⃣ Entre na pasta do projeto

```bash
cd JogoDaVelha
```

### 4️⃣ Execute o jogo

```bash
python jogo.py
```

---

## 📂 Estrutura do código

| Função       | Responsabilidade                |
| ------------ | ------------------------------- |
| `desenhar()` | Desenha o tabuleiro no terminal |
| `checar()`   | Verifica se houve vitória       |
| `cpumove()`  | Lógica de decisão da CPU        |
| `partida()`  | Executa uma partida completa    |
| `main`       | Loop para jogar várias partidas |

---

## 🤖 Lógica da IA

Nos níveis Médio e Difícil, a CPU segue a ordem:

1. Procura jogada para **vencer**
2. Se não existir, tenta **bloquear o jogador**
3. Caso não haja risco → joga aleatoriamente

---

## 💡 Melhorias futuras

Ideias para evoluir o projeto:

* Interface gráfica (Tkinter ou Pygame)
* IA Minimax (CPU invencível)
* Multiplayer local
* Sistema de pontuação
* Versão web

---

## 👨‍💻 Autor

**Edcley Vítor**

Se gostou do projeto, deixe uma ⭐ no repositório!
