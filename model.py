import sqlite3

class Database:
    def __init__(self, db_name='wayne_industries.db'):
        self.db_name = db_name

    def connect(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def create_user(self, username, password, role):
        """Cria um novo usuário no banco de dados."""
        conn = self.connect()
        try:
            conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
        except sqlite3.IntegrityError:
            return False  # O nome de usuário já existe
        finally:
            conn.close()
        return True

    def get_user(self, username, password):
        """Obtém um usuário baseado no nome de usuário e senha."""
        conn = self.connect()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        conn.close()
        return user

    def get_role_permissions(self, role):
        """Obtém as permissões de acesso de uma função."""
        conn = self.connect()
        role_data = conn.execute("SELECT * FROM roles WHERE role = ?", (role,)).fetchone()
        conn.close()
        if role_data:
            return role_data["access_areas"].split(",")  # Retorna a lista de áreas de acesso
        return []
    

    def delete_user(username):
       # Conecta ao banco de dados
       conn = sqlite3.connect('wayne_industries.db')
       cursor = conn.cursor()

       # Executa a query de deletação
       cursor.execute('''DELETE FROM users WHERE username = ?''', (username,))

       # Verifica se algum usuário foi deletado
       if cursor.rowcount > 0:
          conn.commit()  # Confirma a operação no banco de dados
          print(f"Usuário {username} deletado com sucesso!")
       else:
          print(f"Usuário {username} não encontrado.")
    
          conn.close()

          
   





