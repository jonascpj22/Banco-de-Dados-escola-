#pip install mysql-connector-python
#pip install pandas

import mysql.connector
import pandas as pd
from mysql.connector import Error

nomeColuna1 = "ID"
nomeColuna2 = "Descrição"
nomeColuna3 = "Fabricante"
nomeColuna4 = "Valor"

dataframe = pd.DataFrame()


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Altere para o seu host
            user='root',        # Altere para seu usuário
            password='',      # Altere para sua senha
            database='dbescola'  # Altere para seu banco de dados
        )
        if connection.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso.")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def insert_data(connection, tabela, colunas, valores):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO {tabela} ("
        for coluna in colunas:
            query = query + coluna + ", "

        query = query + ") values ("
        for coluna in colunas:
            query = query + "%s, "
        
        query = query + ")"
        query = query.replace(", )", ")")
        cursor.execute(query, valores)
        connection.commit()
        print("Dados inseridos com sucesso.")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        cursor.close()

def update_data(connection, tabela, colunas, valores, colunaid, id):
    try:
        cursor = connection.cursor()
        query = f"UPDATE {tabela} SET "
        for coluna in colunas:
            query = query + coluna + " = %s, "

        query = query + f"where {colunaid} = %s"
        query = query.replace(", where", " where")
        valores.append(id)
        cursor.execute(query, valores)
        connection.commit()
        print("Dados atualizados com sucesso.")
    except Error as e:
        print(f"Erro ao atualizar dados: {e}")
    finally:
        cursor.close()

def delete_data(connection, tabela, coluna, id):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {tabela} WHERE {coluna} = %s"
        cursor.execute(query, (id,))
        connection.commit()
        print("Dados deletados com sucesso.")
    except Error as e:
        print(f"Erro ao deletar dados: {e}")
    finally:
        cursor.close()

def read_data(connection, tabela, colunas):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {tabela}"
        cursor.execute(query)
        rows = cursor.fetchall()
        listaColunas = [] * len(colunas)
        for i in range(len(colunas)):
            listaColunas.append([])
        dataframe = {}
        
        for row in rows:
            for i, coluna in enumerate(colunas):
                listaColunas[i].append(row[i])

            
        for i in range(len(colunas)):
            dataframe[colunas[i]] = listaColunas[i]
                    
        dataframe = pd.DataFrame(dataframe)
        dataframe.index = [''] * len(dataframe)
        print(dataframe)
    except Error as e:
        print(f"Erro ao ler dados: {e}")
    finally:
        cursor.close()

    
def query_arb(connection, query, colunas):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        listaColunas = [] * len(colunas)
        for i in range(len(colunas)):
            listaColunas.append([])
        dataframe = {}
        
        for row in rows:
            for i in range(len(colunas)):
                listaColunas[i].append(row[i])

            
        for i in range(len(colunas)):
            dataframe[colunas[i]] = listaColunas[i]
                    
        dataframe = pd.DataFrame(dataframe)
        dataframe.index = [''] * len(dataframe)
        print(dataframe)
    except Error as e:
        print(f"Erro ao ler dados: {e}")
    finally:
        cursor.close()

def main():
    """Função principal do script."""
    connection = connect_to_database()
    if connection:
        while True:
            print("\nEscolha uma opção:")
            print("1. Tabela alunos")
            print("2. Tabela disciplinas")
            print("3. Tabela notas")
            print("4. Sair\n")
            choice = int(input("Digite o número da opção: "))

            match choice:
                case 1:
                    while True:
                        print("\nEscolha uma opção:")
                        print("1. Inserir aluno")
                        print("2. Atualizar aluno")
                        print("3. Deletar aluno")
                        print("4. Mostrar alunos")
                        print("5. Sair\n")

                        choice = int(input("Digite o número da opção: "))
                        match choice:
                            case 1:
                                nome = input("Digite o nome do aluno: ")
                                datanascimento = input("Digite a data de nascimento (YYYY/MM/DD): ")
                                email = input("Digite o email do aluno: ")
                                insert_data(connection, "alunos", ["nome", "datanascimento", "email"], [nome, datanascimento, email])
                            case 2:
                                id = int(input("Digite o ID do aluno para atualizar: "))
                                nome = input("Digite o novo nome: ")
                                datanascimento = input("Digite a nova data de nascimento (YYYY/MM/DD): ")
                                email = input("Digite o novo email do aluno: ")
                                valores = [nome, datanascimento, email]
                                update_data(connection, "alunos", ["nome", "datanascimento", "email"], valores, "alunoid", id)
                            case 3:
                                id = int(input("Digite o ID do aluno para deletar: "))
                                delete_data(connection, "alunos", "alunoid", id)
                            case 4:
                                print("Dados da tabela 'produtos':")
                                read_data(connection, "Alunos", ["alunoid", "nome", "datanascimento", "email"])
                            case 5:
                                break
                            case _:
                                print("Opção inválida. Tente novamente.")

                case 2:
                    while True:
                        print("\nEscolha uma opção:")
                        print("1. Inserir disciplinas")
                        print("2. Atualizar disciplinas")
                        print("3. Deletar disciplinas")
                        print("4. Mostrar disciplinas")
                        print("5. Sair\n")

                        choice = int(input("Digite o número da opção: "))
                        match choice:
                            case 1:
                                nome = input("Digite o nome da disciplina: ")
                                cargahoraria = input("Digite a carga horaria: ")
                                insert_data(connection, "disciplinas", ["nome", "cargahoraria"], [nome, cargahoraria])
                            case 2:
                                id = int(input("Digite o ID da disciplina para atualizar: "))
                                nome = input("Digite o novo nome: ")
                                cargahoraria = input("Digite a carga horaria: ")
                                valores = [nome, cargahoraria]
                                update_data(connection, "disciplinas", ["nome", "cargahoraria"], valores, "disciplinaid", id)
                            case 3:
                                id = int(input("Digite o ID da disciplina para deletar: "))
                                delete_data(connection, "disciplinas", "disciplinaid", id)
                            case 4:
                                print("Dados da tabela 'produtos':")
                                read_data(connection, "disciplinas", ["disciplinaid", "nome", "cargahoraria"])
                            case 5:
                                break
                            case _:
                                print("Opção inválida. Tente novamente.")


                case 3:
                    while True:
                        print("\nEscolha uma opção:")
                        print("1. Inserir notas")
                        print("2. Atualizar notas")
                        print("3. Deletar notas")
                        print("4. Mostrar notas")
                        print("5. Sair\n")

                        choice = int(input("Digite o número da opção: "))
                        match choice:
                            case 1:
                                alunoid = input("Digite o id do aluno: ")
                                disciplinaid = input("Digite o id da disciplina: ")
                                nota = input("Digite a nota: ")
                                insert_data(connection, "notas", ["alunoid", "disciplinaid", "nota"], [alunoid, disciplinaid, nota])
                            case 2:
                                id = int(input("Digite o ID da nota para atualizar: "))
                                alunoid = input("Digite o novo id do aluno: ")
                                disciplinaid = input("Digite o novo id da disciplina: ")
                                nota = input("Digite a nova nota: ")
                                valores = [alunoid, disciplinaid, nota]
                                update_data(connection, "notas", ["alunoid", "disciplinaid", "nota"], valores, "notaid", id)
                            case 3:
                                id = int(input("Digite o ID da nota para deletar: "))
                                delete_data(connection, "notas", "notaid", id)
                            case 4:
                                print("Dados da tabela 'notas':")
                                query = "select notas.notaid as ID, notas.alunoid, alunos.nome as aluno, notas.disciplinaid, disciplinas.nome as disciplina, notas.nota from notas inner join alunos on notas.alunoid = alunos.alunoid inner join disciplinas on notas.disciplinaid = disciplinas.disciplinaid"
                                query_arb(connection, query, ["id", "idaluno", "aluno", "iddisciplina", "disciplina", "nota"])
                            case 5:
                                break
                            case _:
                                print("Opção inválida. Tente novamente.")


                case 4:
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

            

        connection.close()

if __name__ == "__main__":
    main()
