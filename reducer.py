#!/usr/bin/env python3

from operator import itemgetter
import sys

# variaveis para manter o registro das palavras e sua contagem atual
current_word = None
current_count = 0
word = None

# leitura de cada palavra através do stdin, por onde o hadoop vai mandar
for line in sys.stdin:
    
    # removendo espacos do inicio e do fim
    line = line.strip()

    # separando palavra e sua contagem atual
    word, new_count = line.split('\t', 1)

    
    # convertendo numero recebido para int
    try:
        new_count = int(new_count)
    except ValueError:
        continue

    # incrementando contagem da palavra ao encontra-la novamente
    if current_word == word:
        current_count += new_count
    else:
        if current_word:
            
            # palavra nova
            print ('%s\t%s' % (current_word, current_count))
        current_count = new_count
        current_word = word

# jogando a ultima palavra lida pelo reducer de volta pra stdin pra continuar o processo
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))