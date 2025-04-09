# Wayne Industries - Sistema de Controle de Acesso

## Descrição do Projeto
Este projeto consiste em um sistema de controle de acesso desenvolvido para a Wayne Industries. Utilizando Flask e SQLite, o sistema autentica usuários, gerencia permissões de acesso a áreas restritas e disponibiliza recursos administrativos como visualização de inventário e painel de dashboard.

## Tecnologias Utilizadas
- Python 3
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- JWT (JSON Web Tokens)

## Estrutura do Projeto

```
wayne_access_system/
├── app.py
├── config.py
├── model.py
├── setup_db.py
├── wayne_industries.db
├── static/
│   ├── images/
│   │   ├── batmovel.jpg
│   │   ├── batmoto.jpg
│   │   ├── batrang.jpg
│   │   └── ...
│   └── styles.css
├── templates/
│   └── index.html
```

## Funcionalidades

### Login e Autenticação
Usuários devem fornecer nome de usuário e senha para autenticação. Um token JWT é gerado e utilizado para autorizar acessos subsequentes.

### Controle de Acesso
Acesso às áreas é baseado no papel do usuário:
- **Batman**: acesso total a todas as áreas.
- **Gerente**: acesso às áreas operacionais.
- **Engenheiro**: acesso às áreas técnicas.
- **Técnico**: acesso limitado à construção.

### Painel Administrativo
O usuário "wayne" pode:
- Adicionar novos usuários
- Consultar o inventário de equipamentos
- Visualizar o dashboard de dados industriais

### Inventário do Batman
Exibe lista com nome, descrição e imagem de equipamentos como:
- Batmóvel
- Batmoto
- Batarang
- Capa

### Dashboard
Mostra informações industriais como:
- Total de produtos
- Vendas do mês
- Funcionários ativos
- Novos produtos

## Instalação e Execução
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/wayne_access_system.git
```

2. Instale as dependências:
```bash
pip install flask flask-jwt-extended
```

3. Configure o banco de dados:
```bash
python setup_db.py
```

4. Execute o aplicativo:
```bash
python app.py
```

Acesse via navegador em `http://127.0.0.1:5000/`

## Requisitos para Login Inicial
- Usuário: `wayne`
- Senha: `Batman`

## Considerações Finais
O sistema oferece uma base sólida para controle de acesso com segurança JWT, permissões dinâmicas por papel e possibilidade de expansão com novos módulos, como autenticação biométrica ou RFID.

---

**Autor:** Desenvolvedor Full Stack - Wayne Tech Solutions

**Licença:** MIT
