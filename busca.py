import time

def naive_search(text, pattern):
    """Busca Ingênua – Percorre o texto verificando o padrão em cada posição."""
    occurrences = 0
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            occurrences += 1
    return occurrences

def rabin_karp_search(text, pattern, prime=101):
    """Rabin-Karp – Calcula hash para o padrão e para cada trecho do texto de tamanho igual ao padrão."""
    occurrences = 0
    n = len(text)
    m = len(pattern)
    if m > n:
        return 0
    
    # Constante para o sistema de numeração (número de caracteres possíveis)
    d = 256

    # Calcula o valor de h = d^(m-1) % prime
    h = 1
    for i in range(m-1):
        h = (h * d) % prime

    # Calcula o hash para o padrão e para o primeiro "window" do texto
    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    # Percorre o texto comparando os hash e, se necessário, os trechos
    for i in range(n - m + 1):
        if p_hash == t_hash:
            # Em caso de colisão de hash, verifica os caracteres
            if text[i:i+m] == pattern:
                occurrences += 1
        
        # Calcula o hash para o próximo trecho, removendo o primeiro caractere e incluindo o próximo
        if i < n - m:
            t_hash = (d*(t_hash - ord(text[i])*h) + ord(text[i+m])) % prime
            # Se t_hash for negativo, converte para positivo
            if t_hash < 0:
                t_hash += prime

    return occurrences

# Função para ler o arquivo .txt
def load_book(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Nome do arquivo e trecho a ser buscado
filename = 'frankenstein.txt'
pattern = "creature"

# Carrega o livro
book_text = load_book(filename)

# Limpeza simples: convertemos tudo para minúsculas para uma busca case-insensitive
book_text_lower = book_text.lower()
pattern_lower = pattern.lower()

# Executa e mede a Busca Ingênua
start_naive = time.time()
occurrences_naive = naive_search(book_text_lower, pattern_lower)
time_naive = time.time() - start_naive

# Executa e mede o Rabin-Karp
start_rk = time.time()
occurrences_rk = rabin_karp_search(book_text_lower, pattern_lower)
time_rk = time.time() - start_rk

# Exibe os resultados
print("Resultados da Busca:")
print("---------------------")
print(f"Trecho buscado: '{pattern}'")
print(f"Ocorrências (Busca Ingênua): {occurrences_naive} | Tempo: {time_naive:.6f} segundos")
print(f"Ocorrências (Rabin-Karp):   {occurrences_rk} | Tempo: {time_rk:.6f} segundos")
