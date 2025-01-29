import string
from collections import Counter

def frequencia_portugues():
    # Frequências aproximadas das letras em português do Brasil, do mais comum ao menos comum
    return "aeosrnidmutclpvghfbqxzjykw"

def calcular_chave(texto):
    # Calcula a chave com base na análise de frequência
    # Conta a frequência das letras no texto ignorando caracteres não alfabéticos
    frequencia_texto = Counter(c for c in texto.lower() if c in string.ascii_lowercase)
    # Obtém a letra mais comum no texto
    letra_mais_comum = frequencia_texto.most_common(1)[0][0]
    # Assume-se que a letra mais comum no texto cifrado corresponde ao 'a' no português
    chave = (ord(letra_mais_comum) - ord('a')) % 26
    return chave

def decifrar_cesar(texto, chave):
    # Decifra o texto cifrado utilizando a chave estimada
    texto_decifrado = []
    for c in texto:
        if c.isalpha():  # Verifica se o caractere é uma letra
            base = ord('a') if c.islower() else ord('A')  # Define a base dependendo se é minúscula ou maiúscula
            # Decifra a letra utilizando a fórmula da cifra de César
            texto_decifrado.append(chr((ord(c) - base - chave) % 26 + base))
        else:
            # Mantém caracteres não alfabéticos inalterados
            texto_decifrado.append(c)
    return ''.join(texto_decifrado)

def main():
    # Função principal que controla o fluxo do programa
    nome_arquivo = input("Digite o nome do arquivo a ser decifrado: ")
    try:
        # Tenta abrir o arquivo especificado pelo usuário
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            texto_cifrado = f.read()

        # Calcula a chave estimada com base no texto cifrado
        chave = calcular_chave(texto_cifrado)
        print(f"Chave estimada: {chave}")

        # Decifra o texto utilizando a chave estimada
        texto_decifrado = decifrar_cesar(texto_cifrado, chave)

        # Exibe o texto decifrado ao usuário
        print("Texto decifrado:\n")
        print(texto_decifrado)

        # Pergunta se o usuário deseja salvar o texto decifrado em um arquivo
        salvar = input("Deseja salvar o texto decifrado em um arquivo? (s/n): ").strip().lower()
        if salvar == 's':
            # Solicita o nome do arquivo para salvar o texto decifrado
            nome_arquivo_saida = input("Digite o nome do arquivo para salvar o texto decifrado: ")
            with open(nome_arquivo_saida, 'w', encoding='utf-8') as f_out:
                f_out.write(texto_decifrado)
            print(f"Texto decifrado salvo em {nome_arquivo_saida}")
    except FileNotFoundError:
        # Trata o caso em que o arquivo especificado não é encontrado
        print("Arquivo não encontrado. Certifique-se de fornecer o caminho correto.")

if __name__ == "__main__":
    # Ponto de entrada do programa
    main()

