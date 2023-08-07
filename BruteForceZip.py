"""
BRUTE FORCE DE ARQUIVOS ZIP CRIADO POR: KRYOONZZ
"""

import zipfile
from tqdm import tqdm

wordlist = "lista.txt"
zipfile = "arquivo.zip"

n_words = sum(1 for _ in open(wordlist, "rb"))

print("Quantidade de senhas testadas:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            with zipfile.ZipFile(zipfile, "r") as zip_ref:
                zip_ref.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("\n[+] SENHA ENCONTRADA:", word.decode().strip())
            exit(0)

print("[!] Nenhuma senha encontrada.")