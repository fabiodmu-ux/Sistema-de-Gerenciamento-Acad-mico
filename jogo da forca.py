"""
jogo_forca.py
Implementação do jogo da forca em Python com modularização, controle de fluxo
e interface textual interativa.
"""

import random


def inicializar_jogo():
    """
    Inicializa o estado inicial do jogo da forca.

    Propósito:
        Preparar os dados primários antes da interação do usuário.

    Argumentos:
        Não recebe parâmetros.

    Retorno:
        palavra_secreta (str): palavra sorteada do banco.
        letras_tentadas (set): conjunto vazio para armazenar letras já escolhidas.
        palavra_oculta (list): lista de sublinhados representando a palavra.
        tentativas_restantes (int): número máximo de tentativas permitidas.
    """
    palavras = ["python", "modularizacao", "forca", "engenharia", "software"]
    palavra_secreta = random.choice(palavras)

    # Usamos um Set para armazenar letras tentadas porque:
    # - Evita duplicidade automaticamente.
    # - Permite busca rápida (O(1)) para verificar se a letra já foi usada.
    # - É mais eficiente do que listas para esse tipo de operação.
    letras_tentadas = set()

    palavra_oculta = ["_"] * len(palavra_secreta)
    tentativas_restantes = 6

    return palavra_secreta, letras_tentadas, palavra_oculta, tentativas_restantes


def processar_tentativa(letra, palavra_secreta, palavra_oculta, tentativas_restantes):
    """
    Processa uma tentativa do jogador.

    Propósito:
        Validar se a letra escolhida está na palavra secreta e atualizar o estado.

    Argumentos:
        letra (str): letra digitada pelo jogador.
        palavra_secreta (str): palavra sorteada.
        palavra_oculta (list): lista representando a palavra com acertos.
        tentativas_restantes (int): número atual de tentativas disponíveis.

    Retorno:
        palavra_oculta (list): lista atualizada com acertos.
        tentativas_restantes (int): número atualizado de tentativas.
    """
    if letra in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                palavra_oculta[i] = letra
        print(f"✅ Boa! A letra '{letra}' está na palavra.")
    else:
        tentativas_restantes -= 1
        print(f"❌ A letra '{letra}' não está na palavra. Restam {tentativas_restantes} tentativas.")

    return palavra_oculta, tentativas_restantes


def jogar():
    """
    Função principal que controla o fluxo do jogo da forca.
    """
    palavra_secreta, letras_tentadas, palavra_oculta, tentativas_restantes = inicializar_jogo()

    print("🎮 Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra secreta. Você tem 6 tentativas.\n")

    while tentativas_restantes > 0 and "_" in palavra_oculta:
        print("\nPalavra:", " ".join(palavra_oculta))
        print("Tentativas restantes:", tentativas_restantes)
        print("Letras já tentadas:", ", ".join(sorted(letras_tentadas)) if letras_tentadas else "Nenhuma")

        letra = input("Digite uma letra: ").strip().lower()

        if letra in letras_tentadas:
            print(f"⚠️ Você já tentou a letra '{letra}'. Escolha outra.")
            continue

        letras_tentadas.add(letra)
        palavra_oculta, tentativas_restantes = processar_tentativa(
            letra, palavra_secreta, palavra_oculta, tentativas_restantes
        )

    # Desfecho da partida
    if "_" not in palavra_oculta:
        print(f"\n🎉 Parabéns! Você venceu! A palavra era: {palavra_secreta}")
    else:
        print(f"\n💀 Fim de jogo! Você perdeu. A palavra era: {palavra_secreta}")


# Executa o jogo
if __name__ == "__main__":
    jogar()
