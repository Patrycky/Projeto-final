import os

SECRET_KEY = os.getenv("SECRET_KEY", "chave_secreta_super_segura")
JWT_SECRET_KEY = SECRET_KEY
