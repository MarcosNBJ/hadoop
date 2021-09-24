#!/usr/bin/env python3

import sys

# lendo entradas da stdin
for line in sys.stdin:
    
    # removendo espacos do inicio e do fim
    line = line.strip()
    
    # vetor com todas as palavras lidas
    words = line.split()
    for word in words:
        
        # jogando cada palavra pro stdin com uma contagem inicial de 1 para os reducers
        # utilizamos tab como separador
        print ('%s\t1' % (word))