# Importa as bibliotecas necessarias
from kafka import KafkaConsumer
from datetime import date, datetime
from json import loads
import os, time

# Cria o consumer
def setKafkaConnection():
    global consumer
    try: 
        consumer = KafkaConsumer(
        # Informa o topico
            'fullfillment.public.inventory', 
            # Informa o servidor Kafka
            bootstrap_servers='kafka:9092',
            # Informa a qual grupo o consumer pertence
            group_id='python-consumer'
        )
        return 'success'
    except:
        return 'false'

# Funcao para enviar alerta, recebe o message do offset do Kafka para envio
def sendAlert(message):
    # Token do Bot Telegram responsavel por enviar a mensagem
    bottoken = "421548220:AAFAtwLxRUzKae9b50UONZhq0S9OIjhxSeg"
    # O ID do Chat para o qual o Bot devera enviar a mensagem
    chatid = "93702435"

    # Envia a mensagem utilizando CURL e os dados acima informados.
    os.system("curl -s -X POST \
        -H 'Content-Type: application/json' \
        -d '{\"chat_id\": %s, \"text\": \"%s\", \"disable_notification\": true}' \
        https://api.telegram.org/bot%s/sendMessage >> /dev/null" % (chatid,message,bottoken))

# Variavel de controle para inicializacao
count = 1
# Cria laco infinito para ficar processamento as mensagem do topico do Kafka
while True:
    try:
        # Checa se e a primeira conexao
        if count == 1:
            try:
                print("Testando primeira conexao com Kafka!!")
                # Chama funcao de conexao com Kafka
                status = setKafkaConnection()
                # Estrutura condicional para validar o restante do script
                if status == "success":
                    print("Conexao estabelecida com sucesso!\n\nCarregando mensagem do Kafka...\n")
                else:
                    print("Deu ruim!! Vamos continuar tentando conectar...\n\n")
            except:
                pass

        # Entra no objeto consumer para ler as mensagens
        for message in consumer:
            # Guarda o timestamp do evento do Kafka
            timestamp = datetime.fromtimestamp(message.timestamp/1000.0).strftime("%A, %B %d, %Y %H:%M:%S")
            # Guarda a mensagem do evento do Kafka
            message = message.value.decode("utf-8")
            # Imprime a saida horario + menssagem do evento
            print ("%s: %s" % (timestamp,message))
            # Envia alerta via Telegram
            #sendAlert(message.value.decode("utf-8"))

    # Mensagem ao apertar CTRL+C para finalizar o script
    except KeyboardInterrupt:
        print("\n[*]CTRL+C was pressed...")
        # Quebra o Loop 'while True'
        break
    except:
        # Mensagem caso o script nao conecte com o Kafka
        print("DIED! You need to investigate the reason!!")
        # Tempo de espera para nova execucao
        time.sleep(count)
        # Incrementa o tempo de execucao com +1 segundo
        count = count + 1
        # Apos o tempo de espera o script tenta conectar novamente no Kafka
        try:
            status = setKafkaConnection()           
            # Estrutura condicional para validar a conexao com o Kafka esta Ok
            if status == "success":
                print("[*]Estamos de volta Baby! ;)\n\nCarregando mensagem do Kafka...\n")          
        except:
            pass