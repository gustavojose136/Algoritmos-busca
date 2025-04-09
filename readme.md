# Análise dos Algoritmos de Busca em Texto

Este projeto implementa duas abordagens para buscar padrões dentro de um texto:
• Busca Ingênua
• Busca com o algoritmo Rabin-Karp

A seguir, as respostas às questões propostas:

1. Ambos os algoritmos retornaram os mesmos resultados?  
   Sim.  
   Ambos os métodos são capazes de identificar corretamente as ocorrências do padrão buscado, retornando a mesma contagem de ocorrências. No algoritmo de Rabin-Karp, mesmo utilizando o cálculo de hash para otimização, é realizada uma verificação direta (quando os hashes coincidem) para confirmar que o trecho realmente corresponde ao padrão.

2. Qual algoritmo foi mais rápido?  
   O desempenho pode variar conforme o padrão e o tamanho do texto.  
   - Em textos de tamanho moderado e com padrões pequenos, a busca ingênua pode ser mais rápida, pois o slicing de strings em Python é altamente otimizado.  
   - Para textos muito extensos ou padrões maiores, a abordagem com Rabin-Karp tende a apresentar vantagens, já que o seu uso de hash pode reduzir as comparações diretas e acelerar a busca em alguns cenários.  
   Portanto, não há uma resposta única; o “mais rápido” depende do contexto do problema.

3. O tamanho do texto ou do trecho buscado influencia no tempo de execução?  
   Sim, ambos influenciam significativamente.  
   - Um texto maior implica mais iterações na busca, aumentando o tempo de execução.
   - Padrões maiores aumentam a complexidade das comparações no algoritmo ingênuo e o custo do cálculo do hash no Rabin-Karp.
   Assim, quanto maiores o texto e/ou o padrão, maior será o tempo necessário para finalizar a busca.

4. Em que situações um algoritmo pode ser preferido ao outro?  
   - Busca Ingênua:
     • É simples de implementar e compreender.
     • Pode ser mais eficiente para textos curtos e padrões pequenos, onde a sobrecarga de calcular e atualizar hashes não compensa.
     
   - Algoritmo Rabin-Karp:
     • É vantajoso em textos extensos ou em buscas onde o padrão é relativamente longo, pois o uso de hash permite descartar rapidamente muitas janelas sem necessidade de comparar cada caractere.
     • Quando se deseja realizar buscas múltiplas ou paralelas, o algoritmo Rabin-Karp pode oferecer ganhos de desempenho ao reduzir comparações diretas.

Em resumo, ambos os algoritmos são corretos e retornam os mesmos resultados, mas a escolha de qual utilizar dependerá das características específicas dos dados (tamanho do texto e do padrão) e dos requisitos de desempenho da aplicação.