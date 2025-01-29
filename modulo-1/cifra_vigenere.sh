#!/usr/bin/env bash

# Uso:
#   ./vigenere.sh encrypt CHAVE "TEXTO A SER CIFRADO"
#   ./vigenere.sh decrypt CHAVE "TEXTO A SER DECIFRADO"
#
# Exemplo:
#   ./vigenere.sh encrypt LIMAO "OLA MUNDO"
#   ./vigenere.sh decrypt LIMAO "ZZT AFZQE"

# Verifica número mínimo de parâmetros
if [[ $# -lt 3 ]]; then
    echo "Erro: parâmetros insuficientes."
    echo "Uso: $0 (encrypt|decrypt) CHAVE \"TEXTO\""
    exit 1
fi

# Primeiro argumento: modo (encrypt ou decrypt)
mode=$1

# Verifica se o modo é válido
if [[ "$mode" != "encrypt" && "$mode" != "decrypt" ]]; then
    echo "Erro: modo inválido. Use 'encrypt' ou 'decrypt'."
    exit 1
fi

# Segundo argumento: chave de Vigenere
key=$2

# Terceiro argumento: texto que será processado
text=$3

# Converte a chave e o texto para maiúsculo, removendo espaços na chave
key=$(echo "$key" | tr '[:lower:]' '[:upper:]' | tr -d ' ')
text=$(echo "$text" | tr '[:lower:]' '[:upper:]')

# Tamanho da chave
key_length=${#key}

# Índice para avançar sobre a chave
key_index=0

# Resultado final
result=""

# Percorre caractere a caractere o texto
for (( i=0; i<${#text}; i++ )); do
    char=${text:$i:1}

    # Verifica se é um caractere de A-Z
    if [[ $char =~ [A-Z] ]]; then
        # Converte o caractere em valor de 0 a 25 (A=0, B=1, ..., Z=25)
        char_val=$(( $(printf "%d" "'$char") - 65 ))

        # Caractere correspondente da chave
        key_char=${key:$((key_index % key_length)):1}
        key_val=$(( $(printf "%d" "'$key_char") - 65 ))

        # Se o modo for "encrypt", soma. Se for "decrypt", subtrai
        if [[ $mode == "encrypt" ]]; then
            new_val=$(( (char_val + key_val) % 26 ))
        else
            # Para evitar valores negativos, soma 26 antes de fazer o módulo
            new_val=$(( (char_val - key_val + 26) % 26 ))
        fi

        # Converte de volta para caractere ASCII (A=65)
        new_char=$(printf "\\$(printf "%03o" $((new_val + 65)))")
        result+=$new_char

        # Avança o índice da chave
        ((key_index++))
    else
        # Mantém o caractere (espaços, pontuação etc.)
        result+=$char
    fi
done

# Exibe o resultado no terminal
echo "$result"
