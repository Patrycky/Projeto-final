from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from model import Database

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Use uma chave segura
jwt = JWTManager(app)
db = Database()  # Instância do banco de dados

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota de login para gerar token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = db.get_user(username, password)
    if user:
        token = create_access_token(identity={"username": user["username"], "role": user["role"]})
        return jsonify({"token": token, "message": "Login bem-sucedido!"})
    else:
        return jsonify({"message": "Credenciais inválidas"}), 401

# Define as permissões de acesso às áreas
area_access = {
    "Batman": ["Batcaverna", "Sala de Operações", "Construção", "Laboratório", "Pesquisa", "Dashboard"],
    "Gerente": ["Sala de Operações", "Construção", "Laboratório", "Pesquisa", "Dashboard"],
    "Engenheiro": ["Construção", "Laboratório", "Pesquisa"],
    "Técnico": ["Construção"]
}

# Rota para acessar áreas restritas
@app.route('/access', methods=['POST'])
@jwt_required()
def access_area():
    current_user = get_jwt_identity()
    area = request.json.get("area")

    if area in area_access.get(current_user["role"], []):
        return render_template('area.html', area=area)
    else:
        return jsonify({"message": f"Acesso negado à área {area}."}), 403

# Rota para adicionar usuários (somente admin "wayne")
@app.route('/add_user', methods=['POST'])
@jwt_required()
def add_user():
    current_user = get_jwt_identity()
    if current_user["username"] != "wayne":
        return jsonify({"message": "Acesso negado."}), 403

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")

    if db.create_user(username, password, role):
        return jsonify({"message": f"Usuário {username} adicionado com sucesso!"}), 201
    else:
        return jsonify({"message": "Erro ao adicionar o usuário. O nome de usuário pode já existir."}), 400

# Rota para buscar inventário de itens do Batman
@app.route('/batman_inventory', methods=['GET'])
@jwt_required()
def batman_inventory():
    current_user = get_jwt_identity()
    if current_user["username"] != "wayne":
        return jsonify({"message": "Acesso negado ao inventário do Batman."}), 403

    inventory = [
    {"name": "Batarang", "description": "Arma de arremesso em forma de morcego.", "image": "static/images/batrang.jpg"},
    {"name": "Batmóvel", "description": "Veículo de combate ao crime.", "image": "static/images/batmovel.jpg"},
    {"name": "Capa", "description": "Capa que proporciona stealth.", "image": "static/images/capa.jpg"},
    {"name": "Batmoto", "description": "Veículo super rápido e furtivo.", "image": "static/images/batmoto.jpg"},
]
    return jsonify({"items": inventory})


# Rota do Dashboard
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    industry_data = {
        "total_produtos": 1500,
        "vendas_do_mes": 30000,
        "funcionarios": 50,
        "novos_produtos": 5
    }

    if current_user["role"] in ["Batman", "Gerente"]:
        return jsonify(industry_data)
    else:
        return jsonify({"message": "Acesso negado ao dashboard."}), 403


if __name__ == "__main__":
    app.run(debug=True)
































