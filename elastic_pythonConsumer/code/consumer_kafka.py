# Importa as bibliotecas necessarias
from kafka import KafkaConsumer
from datetime import date, datetime
from json import loads
import os, time, json, requests

def writeLog(log):
    with open('somefile.txt', 'a') as the_file:
        the_file.write(log+'\n')

def sendElastic(kafkaData):
    writeLog("Entrou na funcao de envia de logs para Elastic")
    url = "http://164.68.116.3:9200/pessoa_kafka/_doc/"+str(kafkaData['id'])

    payload = json.dumps(kafkaData)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code
    
# Cria o consumer
def setKafkaConnection():
    writeLog("Entrou na funcao de conexao com Kafka!!")
    global consumer
    try: 
        consumer = KafkaConsumer(
        # Informa o topico
            'fullfillment.public.inventory', 
            # Informa o servidor Kafka
            bootstrap_servers='host.docker.internal:9094',
            # Informa a qual grupo o consumer pertence
            group_id='python-consumer'
        )
        # writeLog(str(consumer))
        writeLog("Sucesso!!")
        return 'success'
    except:
        writeLog("Erro!!")
        return 'false'

# Variavel de controle para inicializacao
count = 1
# Cria laco infinito para ficar processamento as mensagem do topico do Kafka
while True:
    try:
        # Checa se e a primeira conexao
        if count == 1:
            try:
                writeLog("Testando primeira conexao com Kafka!!")
                # Chama funcao de conexao com Kafka
                status = setKafkaConnection()
                writeLog(status)
                # Estrutura condicional para validar o restante do script
                if status == "success":
                    writeLog("Conexao estabelecida com sucesso!\n\nCarregando mensagem do Kafka...\n")
                else:
                    writeLog("Deu ruim!! Vamos continuar tentando conectar...\n\n")
            except:
                pass

        writeLog("Ultimo passo antes do loop!!")

        # Entra no objeto consumer para ler as mensagens
        for message in consumer:
            writeLog("Entrou no loop de leitura de mensagens!!")
            # Guarda o timestamp do evento do Kafka
            timestamp = datetime.fromtimestamp(message.timestamp/1000.0).strftime("%A, %B %d, %Y %H:%M:%S")
            # Guarda a mensagem do evento do Kafka
            json_message = message.value.decode("utf-8")
            #print(type(json_message))
            messagem = json.loads(json_message)
            clean_message = messagem['payload']['after']
            # Imprime a saida horario + menssagem do evento
            writeLog ("%s: %s" % (timestamp,json.dumps(clean_message)))
            status = sendElastic(clean_message)
            if(status == 200 or status == 201):
                writeLog("[*] Dado inserido no Elasticsearch com sucesso!")
            else:
                writeLog("[!] Falha ao inserir dado no Elasticsearch!! X.X")
            # Envia alerta via Telegram
            #sendAlert(message.value.decode("utf-8"))

    # Mensagem ao apertar CTRL+C para finalizar o script
    except KeyboardInterrupt:
        writeLog("\n[*]CTRL+C was pressed...")
        # Quebra o Loop 'while True'
        break
    except:
        # Mensagem caso o script nao conecte com o Kafka
        writeLog("DIED! You need to investigate the reason!!")
        # Tempo de espera para nova execucao
        time.sleep(count)
        # Incrementa o tempo de execucao com +1 segundo
        count = count + 1
        # Apos o tempo de espera o script tenta conectar novamente no Kafka
        try:
            status = setKafkaConnection()           
            # Estrutura condicional para validar a conexao com o Kafka esta Ok
            if status == "success":
                writeLog("[*]Estamos de volta Baby! ;)\n\nCarregando mensagem do Kafka...\n")          
        except:
            pass