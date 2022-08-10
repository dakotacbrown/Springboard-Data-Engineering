# Fraud Detector

## How to run
1. First run the docker command to start up kafka:
`docker-compose -f docker-compose.kafka.yml up`
2. Next, start the producers and consumers:
`docker-compose up`
3. Finally, look at the fraudulent and non-fraudulent transactions:

Non-fraudulent:
`docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit`

Fraudulent:
`docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud`