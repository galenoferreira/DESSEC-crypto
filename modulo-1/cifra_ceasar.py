import os

def cifra_cesar(texto, chave):
    # Função que aplica a cifra de César em um texto com base em uma chave fornecida.
    resultado = ""
    for caractere in texto:
        # Verifica se o caractere é uma letra do alfabeto.
        if caractere.isalpha():
            # Define a base ASCII dependendo se o caractere é maiúsculo ou minúsculo.
            base = ord('A') if caractere.isupper() else ord('a')
            # Calcula o novo caractere após aplicar a cifra de César.
            deslocado = (ord(caractere) - base + chave) % 26 + base
            # Adiciona o caractere cifrado ao resultado.
            resultado += chr(deslocado)
        else:
            # Mantém o caractere inalterado caso não seja uma letra.
            resultado += caractere
    return resultado

def main():
    try:
        # Solicita ao usuário o caminho do arquivo a ser cifrado.
        arquivo = input("Digite o caminho do arquivo a ser cifrado: ").strip()
        if not os.path.isfile(arquivo):
            # Verifica se o arquivo existe no caminho especificado.
            print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
            return

        try:
            # Solicita ao usuário o valor da chave de transposição e converte para inteiro.
            chave = int(input("Digite o valor de transposição (número inteiro): "))
        except ValueError:
            # Informa o usuário caso o valor fornecido não seja numérico.
            print("Por favor, insira um valor numérico válido.")
            return

        # Abre o arquivo em modo de leitura com codificação UTF-8.
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Aplica a cifra de César no conteúdo do arquivo.
        texto_cifrado = cifra_cesar(conteudo, chave)

        # Cria o nome para o novo arquivo cifrado, adicionando o sufixo '_cifrado'.
        novo_arquivo = arquivo.rsplit('.', 1)[0] + '_cifrado.txt'
        # Salva o texto cifrado no novo arquivo.
        with open(novo_arquivo, 'w', encoding='utf-8') as f:
            f.write(texto_cifrado)

        # Informa ao usuário que o texto foi cifrado com sucesso.
        print(f"Texto cifrado com sucesso! Arquivo salvo como: {novo_arquivo}")

    except Exception as e:
        # Captura e exibe quaisquer erros que possam ocorrer durante a execução.
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Ponto de entrada do programa.
    main()

