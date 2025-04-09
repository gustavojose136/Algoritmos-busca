import time

def naive_search(text, pattern):
    occurrences = 0
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            occurrences += 1
    return occurrences

def rabin_karp_search(text, pattern, prime=101):
    occurrences = 0
    n = len(text)
    m = len(pattern)
    if m > n:
        return 0
    
    d = 256

    # Calcula o valor de h = d^(m-1) % prime
    h = 1
    for i in range(m-1):
        h = (h * d) % prime

    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                occurrences += 1
        
        if i < n - m:
            t_hash = (d*(t_hash - ord(text[i])*h) + ord(text[i+m])) % prime
            if t_hash < 0:
                t_hash += prime

    return occurrences

def load_book(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

filename = 'frankenstein.txt'
pattern = "creature"

# Carrega o livro
book_text = load_book(filename)

book_text_lower = book_text.lower()
pattern_lower = pattern.lower()

start_naive = time.time()
occurrences_naive = naive_search(book_text_lower, pattern_lower)
time_naive = time.time() - start_naive

start_rk = time.time()
occurrences_rk = rabin_karp_search(book_text_lower, pattern_lower)
time_rk = time.time() - start_rk

print("Resultados da Busca:")
print("---------------------")
print(f"Trecho buscado: '{pattern}'")
print(f"Ocorrências (Busca Ingênua): {occurrences_naive} | Tempo: {time_naive:.6f} segundos")
print(f"Ocorrências (Rabin-Karp):   {occurrences_rk} | Tempo: {time_rk:.6f} segundos")
