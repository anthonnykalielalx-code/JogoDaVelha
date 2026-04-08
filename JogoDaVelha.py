import random
import sys


def desenhar(tab, mem, final=False):
    if mem and not final:
        return

    print("\n    A   B   C")
    moldura = "  +---+---+---+"
    for i, linha in enumerate(tab):
        print(moldura)
        print(f"{i + 1} | {' | '.join(linha)} |")
    print(moldura)


def checar(t, p):
    for i in range(3):
        if all(t[i][j] == p for j in range(3)) or all(t[j][i] == p for j in range(3)):
            return True
    return t[0][0] == t[1][1] == t[2][2] == p or t[0][2] == t[1][1] == t[2][0] == p


def cpumove(t, d):
    vagas = [(r, c) for r in range(3) for c in range(3) if t[r][c] == " "]
    if not vagas:
        return None

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
    mapa = {"A": 0, "B": 1, "C": 2}
    reverso_mapa = {0: "A", 1: "B", 2: "C"}

    print("\n--- JOGO DA VELHA ---")
    mem = input("Modo memoria? (s/n): ").lower() == "s"
    try:
        dif = int(input("Dificuldade (1-Facil, 2-Medio, 3-Dificil): "))
    except:
        dif = 1

    turno, contador = True, 0
    while contador < 9:
        desenhar(tab, mem)

        if turno:
            try:
                cmd = input("\nSua vez (Ex: A1): ").upper()
                r, c = int(cmd[1]) - 1, mapa[cmd[0]]
                if tab[r][c] == " ":
                    tab[r][c] = "X"
                    if mem:
                        print(f"\nJOGADA REGISTRADA: Você em {cmd}")

                    if checar(tab, "X"):
                        desenhar(tab, False, True)
                        print("\nVITÓRIA DO JOGADOR!")
                        return
                    turno, contador = False, contador + 1
                else:
                    print("\nPosição ocupada!")
            except (KeyError, IndexError, ValueError):
                print("\nEntrada inválida!")
        else:
            jogada = cpumove(tab, dif)
            if jogada:
                r, c = jogada
                tab[r][c] = "O"
                print(f"\nIA JOGOU EM: {reverso_mapa[c]}{r + 1}")

                if checar(tab, "O"):
                    desenhar(tab, False, True)
                    print("\nVITÓRIA DA CPU!")
                    return
                turno, contador = True, contador + 1

    desenhar(tab, False, True)
    print("\nEMPATE!")


if __name__ == "__main__":
    try:
        while True:
            partida()
            if input("\nJogar novamente? (s/n): ").lower() != "s":
                break
    except KeyboardInterrupt:
        sys.exit()
