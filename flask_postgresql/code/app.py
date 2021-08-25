# Importa as bibliotecas necessarias
from types import MethodType
from flask import Flask, render_template, jsonify, request
import psycopg2

# Cria a instancia do App Flask 
app = Flask(__name__)

def bd_connection():# Update connection string information 
    # Documentacao: https://docs.microsoft.com/pt-br/azure/postgresql/flexible-server/connect-python
    host = "postgres_prod"
    dbname = "test"
    user = "test"
    password = "test"

    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
    conn = psycopg2.connect(conn_string) 
    print("Connection established")
    return conn

def inserirDado(nome, idade, ip_address):
    try:
        conn = bd_connection()
        cursor = conn.cursor()
        # Insert some data into the table
        cursor.execute("INSERT INTO inventory (nome, idade, ip_address) VALUES (%s, %s, %s);", (nome, idade, ip_address))
        print("Inserted 1 rows of data")
        # Clean up
        conn.commit()
        cursor.close()
        conn.close()

        return "Dado inserido!"
    except:
        return "Error ao inserir dados"

def lerDados():
    conn = bd_connection()
    cursor = conn.cursor()

    try:
        # Fetch all rows from table
        cursor.execute("SELECT id, nome, idade FROM inventory ORDER BY id DESC LIMIT 10;")
        rows = cursor.fetchall()
        # Print all rows
        dados = []
        for row in rows:
            dados.append(("Data row = (%s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]))))
        # Clean up
        conn.commit()
        cursor.close()
        conn.close()

        return dados
    except:
        return "Error ao exibir dados"

def criarTabela():
    try:
        conn = bd_connection()
        cursor = conn.cursor()

        # Create a table
        cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, nome VARCHAR(50), idade INTEGER, ip_address VARCHAR(50));")
        print("Finished creating table")

        # Clean up
        conn.commit()
        cursor.close()
        conn.close()
    
        return "Tabela criada!"
    except:
        return "Error ao criar tabela"

def limparBase():
    
    try:
        conn = bd_connection()
        cursor = conn.cursor()

        # Drop previous table of same name if one exists
        cursor.execute("DROP TABLE IF EXISTS inventory;")
        print("Finished dropping table (if existed)")

        # Clean up
        conn.commit()
        cursor.close()
        conn.close()

        return "Tabela excluida!"
    except:
        return "Error ao excluir tabela"

# Cria a rota do Flask ao acessar a raiz
@app.route('/')
# Funcao Home
def home():
    return render_template('index.html')

@app.route('/createTable', methods=["POST"])
# Funcao Home
def createTable():
    print(">> criar tabela")
    try:
        message = criarTabela()
        return jsonify({'output' : message})
    except:
        print(">> error ao criar tabela")
        message = "Error ao criar tabela"
        return jsonify({'output' : message})

@app.route('/insertData', methods=["POST"])
# Funcao Home
def insertData():
    print(">> inserir dados")
    nome = request.form['nome']
    idade = request.form['idade']
    ip_adrres = request.remote_addr
    try:
        message = inserirDado(nome, idade, ip_adrres)
        return jsonify({'output' : message})
    except:
        print(">> error ao inserir dados")
        message = "Error ao inserir dados"
        return jsonify({'output' : message})

@app.route('/showData', methods=["POST"])
# Funcao Home
def showData():
    print(">> criar tabela")
    try:
        message = lerDados()
        return jsonify({'output' : message})
    except:
        print(">> error ao exibir dados")
        message = "Error ao exibir dados"
        return jsonify({'output' : message})

@app.route('/deleteData', methods=["POST"])
# Funcao Home
def clearData():
    print(">> criar tabela")
    try:
        message = limparBase()
        return jsonify({'output' : message})
    except:
        print(">> error ao excluir tabela")
        message = "Error ao excluir tabela"
        return jsonify({'output' : message})



# Instancia o main do script
if __name__ == "__main__":
    # Executa a aplicacao no modo Debug e com acesso a todos
    app.run(host="0.0.0.0", debug=True)