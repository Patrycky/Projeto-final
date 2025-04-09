import sqlite3

def setup_database():
    conn = sqlite3.connect('wayne_industries.db')
    cursor = conn.cursor()

    # Cria a tabela de usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                    )''')

    # Cria a tabela de funções
    cursor.execute('''CREATE TABLE IF NOT EXISTS roles (
                        role TEXT PRIMARY KEY,
                        access_areas TEXT
                    )''')

    # Insere dados de exemplo para usuários
    cursor.execute('''INSERT OR IGNORE INTO users (username, password, role)
                      VALUES ('wayne', 'Batman', 'Batman')''')

    # Insere dados de exemplo para as funções e suas áreas de acesso
    cursor.execute('''INSERT OR IGNORE INTO roles (role, access_areas)
                      VALUES ('Batman', 'Batcaverna,Sala de Operações,Construção,Laboratório,Pesquisa'),
                             ('Gerente', 'Sala de Operações,Construção,Laboratório,Pesquisa'),
                             ('Engenheiro', 'Construção,Laboratório,Pesquisa'),
                             ('Técnico', 'Construção')''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()





