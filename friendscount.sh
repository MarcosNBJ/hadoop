#!/bin/bash

hdfs dfs -rm -r -f friends friends_result

echo "Gerando nova lista de pares de amigos com $1 amigos"

python3 friends_generator.py $1

echo "Arquivo de entrada copiado para filesystem do hadoop"

hadoop fs -mkdir -p friends
hdfs dfs -put friends.txt friends

echo "Iniciando maprduce"

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files friends_mapper.py,reducer.py \
-input friends \
-output friends_result \
-mapper "python3 friends_mapper.py" \
-reducer "python3 reducer.py"

echo "Adquirindo resultado"

hadoop fs -getmerge friends_result friends_result.txt

echo -e "Resultados: \n"

cat friends_result.txt