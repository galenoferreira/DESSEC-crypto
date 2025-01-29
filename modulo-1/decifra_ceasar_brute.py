# Importa o módulo os para verificar se o arquivo fornecido existe
import os

# Solicita ao usuário o nome do arquivo que contém o texto cifrado
filename = input("Informe o nome do arquivo que contém o texto cifrado (com extensão): ")

# Verifica se o arquivo existe
if not os.path.isfile(filename):
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
else:
    # Lê o conteúdo do arquivo
    with open(filename, "r") as file:
        ciphertext = file.read().strip()  # Remove espaços extras ou quebras de linha

    # Alfabeto padrão para o deslocamento
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Dicionário para armazenar os resultados de cada chave
    possible_decryptions = {}

    # Loop para testar todas as 26 chaves possíveis
    for key in range(1, 27):  # Testa chaves de 1 a 26
        decrypted_text = ""  # String para armazenar o texto decifrado atual

        # Decifra cada caractere do texto cifrado
        for char in ciphertext:
            if char.lower() in alphabet:  # Verifica se o caractere está no alfabeto
                # Calcula o índice do caractere após o deslocamento
                new_index = (alphabet.index(char.lower()) - key) % 26
                
                # Mantém a mesma capitalização do caractere original
                if char.isupper():
                    decrypted_text += alphabet[new_index].upper()
                else:
                    decrypted_text += alphabet[new_index]
            else:
                # Mantém os caracteres que não estão no alfabeto (espaços, pontuações, etc.)
                decrypted_text += char

        # Armazena o texto decifrado associado à chave usada
        possible_decryptions[key] = decrypted_text
        print(f"Chave {key}: {decrypted_text}")  # Exibe cada texto decifrado

    # Solicita ao usuário que escolha a chave correta
    correct_key = int(input("Com base nas tentativas acima, informe a chave correta: "))

    if correct_key in possible_decryptions:
        # Exibe o texto decifrado com a chave correta
        print("\nTexto decifrado com a chave correta:")
        print(possible_decryptions[correct_key])
        print(f"\nChave utilizada: {correct_key}")
    else:
        print("Chave inválida. Tente novamente.")

