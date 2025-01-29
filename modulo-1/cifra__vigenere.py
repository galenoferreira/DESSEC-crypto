#!/usr/bin/env python3
import sys

def vigenere_transform(text, key, mode='encrypt'):
    """
    Aplica a cifra de Vigenère em 'text' usando a 'key'.
    - mode='encrypt' para criptografar
    - mode='decrypt' para descriptografar
    """
    result = []
    # Remover espaços da chave e converter para maiúsculo
    key = key.replace(" ", "").upper()
    # Convertemos todo o texto para maiúsculo
    text = text.upper()

    # Tamanho da chave
    key_length = len(key)
    if key_length == 0:
        # Evita divisão por zero e comportamentos incorretos
        return text

    # Índice para a chave
    key_index = 0

    for char in text:
        if 'A' <= char <= 'Z':  
            # Converte letra de A-Z em 0-25
            char_val = ord(char) - ord('A')
            key_val = ord(key[key_index % key_length]) - ord('A')

            if mode == 'encrypt':
                new_val = (char_val + key_val) % 26
            else:  # mode == 'decrypt'
                # soma 26 para evitar valores negativos
                new_val = (char_val - key_val + 26) % 26

            # Converte de volta para caractere
            new_char = chr(new_val + ord('A'))
            result.append(new_char)

            # Avança o índice da chave
            key_index += 1
        else:
            # Mantém caracteres fora de A-Z sem mudança
            result.append(char)

    # Retorna o resultado como string
    return "".join(result)


def main():
    """
    Uso:
        python vigenere.py encrypt CHAVE input.txt output.txt
        python vigenere.py decrypt CHAVE input.txt output.txt
    """
    if len(sys.argv) < 5:
        print("Uso: python vigenere.py <encrypt|decrypt> <CHAVE> <ARQUIVO_ENTRADA> <ARQUIVO_SAIDA>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    key = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]

    if mode not in ('encrypt', 'decrypt'):
        print("Erro: modo deve ser 'encrypt' ou 'decrypt'.")
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as fin, \
             open(output_file, 'w', encoding='utf-8') as fout:
            for line in fin:
                # Aplica Vigenère para cada linha do arquivo
                transformed_line = vigenere_transform(line, key, mode=mode)
                fout.write(transformed_line)
        print(f"Processo '{mode}' concluído. Arquivo de saída: {output_file}")
    except FileNotFoundError:
        print(f"Erro: não foi possível encontrar o arquivo '{input_file}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    main()

