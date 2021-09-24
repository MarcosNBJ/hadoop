PARES = 1000

friendscount:
		docker-compose up -d
		docker-compose exec namenode hdfs dfsadmin -safemode leave
		docker-compose exec namenode ./friendscount.sh $(PARES)

wordscount:
		docker-compose up -d
		docker-compose exec namenode hdfs dfsadmin -safemode leave
		docker-compose exec namenode ./wordscount.sh