import random
import string


API_HOST = '127.0.0.1'
API_PORT = 5000
API_BASE_URL = '/api'

# configurando dados hardcore - mocado
# código escrito direto na aplicação
LOGIN_TESTE = 'admin@admin.com'
SENHA_TESTE = 'Admin1234@'

# Geração de token segurança lib JWT
# Lembrete - toda vez que a aplicação for iniciada nos perdemos o token
# que foi gerada na inicialização anterior
gen = string.ascii_letters + string.digits + string.ascii_uppercase
SECRET_KEY = ''.join(random.choice(gen) for i in range(32))


DEBUG = True