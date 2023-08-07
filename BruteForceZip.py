"""
BRUTE FORCE DE ARQUIVOS ZIP CRIADO POR: KRYOONZZ
"""

import zipfile  # Importa o módulo zipfile para trabalhar com arquivos zip
from tqdm import tqdm  # Importa a função tqdm para exibir uma barra de progresso

wordlist = "lista.txt"  # Define o nome do arquivo de palavras
zipfile = "arquivo.zip"  # Define o nome do arquivo zip

n_words = sum(1 for _ in open(wordlist, "rb"))  # Conta o número de palavras no arquivo wordlist
print("Quantidade de senhas testadas:", n_words)  # Imprime a quantidade de palavras a serem testadas

with open(wordlist, "rb") as wordlist:  # Abre o arquivo wordlist para leitura binária
    for word in tqdm(wordlist, total=n_words, unit="word"):  # Itera sobre cada palavra no arquivo wordlist
        try:
            with zipfile.ZipFile(zipfile, "r") as zip_ref:  # Abre o arquivo zip para leitura
                zip_ref.extractall(pwd=word.strip())  # Tenta extrair o conteúdo do arquivo zip usando a palavra como senha
        except:
            continue  # Se ocorrer um erro, continua para a próxima palavra
        else:
            print("\n[+] SENHA ENCONTRADA:", word.decode().strip())  # Se a extração for bem-sucedida, imprime a senha encontrada
            exit(0)  # Encerra o programa
print("[!] Nenhuma senha encontrada.")  # Se nenhuma senha for encontrada, imprime essa mensagem