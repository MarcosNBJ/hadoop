#!/bin/bash

hdfs dfs -rm -r -f words words_result

echo "Arquivo de entrada copiado para filesystem do hadoop"

hadoop fs -mkdir -p words
hdfs dfs -put words.txt words

echo "Iniciando maprduce"

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files words_mapper.py,reducer.py \
-input words \
-output words_result \
-mapper "python3 words_mapper.py" \
-reducer "python3 reducer.py"

echo "Adquirindo resultado"

hadoop fs -getmerge words_result words_result.txt

echo -e "Resultados: \n"

cat words_result.txt