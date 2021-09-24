#!/usr/bin/env python3

import sys

# lendo entradas da stdin
for line in sys.stdin:
    
    # removendo espacos do inicio e do fim
    line = line.strip()
    
    # a linha vem no formato "pessoa, amigo" 
    # queremos apenas a pessoa
    person = line.split(",")[0]

    # jogando nome da pessoa para stdin para contarmos as ocorrencias com os reducers
    # utilizamos tab como separador
    print('%s\t1' % (person))
