import random
import sys

def desenhar(tab, mem, vez):
    print("\n    A   B   C")
    moldura = "  +---+---+---+"
    for i, linha in enumerate(tab):
        print(moldura)
        pos = [(c if not mem or vez else " ") for c in linha]
        print(f"{i+1} | {' | '.join(pos)} |")
    print(moldura)

def checar(t, p):
    for i in range(3):
        if all(t[i][j] == p for j in range(3)) or all(t[j][i] == p for j in range(3)):
            return True
    return t[0][0] == t[1][1] == t[2][2] == p or t[0][2] == t[1][1] == t[2][0] == p

def cpumove(t, d):
    vagas = [(r, c) for r in range(3) for c in range(3) if t[r][c] == " "]
    if d > 1:
        for p in ["O", "X"]:
            for r, c in vagas:
                t[r][c] = p
                if checar(t, p):
                    t[r][c] = "O"
                    return (r, c)
                t[r][c] = " "
    return random.choice(vagas)

def partida():
    tab = [[" " for _ in range(3)] for _ in range(3)]
    mapa = {'A': 0, 'B': 1, 'C': 2}

    print("--- JOGO DA VELHA ---")
    mem = input("Modo memoria? (s/n): ").lower() == 's'
    try:
        dif = int(input("Dificuldade (1-Facil, 2-Medio, 3-Dificil): "))
    except:
        dif = 1

    turno, contador = True, 0
    while contador < 9:
        desenhar(tab, mem, turno)
        if turno:
            try:
                cmd = input("\nSua jogada (Ex: A1): ").upper()
                r, c = int(cmd[1])-1, mapa[cmd[0]]
                if tab[r][c] == " ":
                    tab[r][c] = "X"
                    if checar(tab, "X"):
                        desenhar(tab, False, True)
                        print("Vitoria do jogador.")
                        return
                    turno, contador = False, contador + 1
                else:
                    print("Posicao ocupada.")
            except (KeyError, IndexError, ValueError):
                print("Entrada invalida.")
        else:
            r, c = cpumove(tab, dif)
            tab[r][c] = "O"
            print(f"\nComputador jogou em: {list(mapa.keys())[c]}{r+1}")
            if checar(tab, "O"):
                desenhar(tab, False, True)
                print("Vitoria da CPU.")
                return
            turno, contador = True, contador + 1

    desenhar(tab, False, True)
    print("Empate.")

if __name__ == "__main__":
    try:
        while True:
            partida()
            if input("\nJogar novamente? (s/n): ").lower() != 's':
                print("\nEncerrando.")
                break
    except KeyboardInterrupt:
        print("\n\nForçando Parada")
        sys.exit()
