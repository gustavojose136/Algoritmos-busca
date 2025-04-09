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
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return occurrences

def load_book(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

filename = 'frankenstein.txt'

patterns = [                
    "frankenstein",                              
    "no man on earth could so completely",     
    "Will you smile"  
    "Everyone loved Elizabeth",
    "Every minute",
    "I am happy",
    "“to have gained a disciple; and if your application equals your ability, I have no doubt of your success. Chemistry is that branch of natural philosophy in which the greatest improvements have been and may be made; it is on that account that I have made it my peculiar study; but at the same time, I have not neglected the other branches of science. A man would make but a very sorry chemist if he attended to that department of human knowledge alone. If your wish is to become really a man of science and not merely a petty experimentalist, I should advise you to apply to every branch of natural philosophy, including mathematics.”"
]

book_text = load_book(filename)

book_text_lower = book_text.lower()

print("Resultados da Busca:")
print("---------------------")

for pattern in patterns:
    pattern_lower = pattern.lower()

    start_naive = time.time()
    occurrences_naive = naive_search(book_text_lower, pattern_lower)
    time_naive = time.time() - start_naive

    start_rk = time.time()
    occurrences_rk = rabin_karp_search(book_text_lower, pattern_lower)
    time_rk = time.time() - start_rk

    print(f"\nTrecho buscado: '{pattern}'")
    print(f"Ocorrências (Busca Ingênua): {occurrences_naive} | Tempo: {time_naive:.6f} segundos")
    print(f"Ocorrências (Rabin-Karp):   {occurrences_rk} | Tempo: {time_rk:.6f} segundos")
