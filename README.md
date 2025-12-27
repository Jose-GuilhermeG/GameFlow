# GameFlow 🎮

GameFlow é um sistema desenvolvido em **Django** para gerenciar e realizar o chaveamento automático de jogos.
O objetivo é facilitar a organização e automação de partidas, torneios ou eventos relacionados a jogos digitais.

---

## 🚀 Principais tecnologias utilizadas

| Tecnologia            | Função                                   |
| --------------------- | ---------------------------------------- |
| Python                | linguagem de programação utilizada       |
| Django                | framework web                            |
| Django socketIo       | biblioteca de conexão em tempo real      |
| Pytest                | Biblioteca de testes automatizados       |
| Selenium              | framework usado para testes de interface |
| Mysql                 | Banco de dados                           |
| HTML, CSS, JavaScript | Interface web                            |
| TailwindCss           | ferramenta de estilização                |
| Nginx                 | servidor de arquivos estaticos           |
| Docker                | Deploy e ambiente isolado                |
| Redis                 | cache                                    |

---

## 📦 Instalação

1. Clone o repositório:

```bash
   git clone https://github.com/Jose-GuilhermeG/GameFlow/
   cd gameflow
```

2. Crie e ative um ambiente virtual:

```bash
python -m virtualenv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale os requiriments

```bash
pip install -r ./requirements/local.txt
npm i
```

4. Adicione suas variaveis de ambiente:

```bash
cp ./.env-exemple ./.env
## e substituia os valores
```

5. edite o arquivo .env com suas credenciais:

| Variável           | Serve para                              |
| ------------------ | --------------------------------------- |
| SECRET_KEY         | Chave usada para criptografia           |
| DEBUG              | modo de depuração                       |
| DATABASE_NAME      | nome da tabela no DB                    |
| DATABASE_HOST      | host do DB                              |
| DATABASE_PASSWORD  | senha para acessar o DB                 |
| DATABASE_USER      | usuario do DB                           |
| DATABASE_PORT      | porta do DB                             |
| REDIS_URL          | url para o redis                        |
| REDIS_PASSWORD     | senha para o redis                      |
| REDIS_USE_PASSWORD | diz se é necessario usar senha no redis |

6. Execute as migrações:

```bash
python manage.py migrate
```

7. Aplicar estilo:

```bash
npm run dev
```

8. Inicie o servidor:

```bash
python manage.py runserver
```

## Utilizando a autenticação Oauth

1. criar super user com :

```bash
python manage.py createsuperuser
```

2. entre no admin
3. social applications > add social application
4. preencha a tabela:
   - provider : provider que vc deseja
   - provider id : nome do provider
   - name : nome do serviço (qualquer nome)
   - client id : id do cliente oAuth
   - secret key : chave secreta do cliente
   - sites : exemple.com
5. salve os dados
6. va na tabela sites
7. modifique o site exemple
8. coloque Domain name como 127.0.0.1:8000

### ⚙️ Uso

Após iniciar o servidor, acesse no navegador:
http://127.0.0.1:8000/

### 📂 Estrutura básica

```
gameflow/ → Configurações principais do Django

apps/ → Aplicativos internos do sistema

templates/ → Arquivos HTML

static/ → CSS, JS e imagens
```

🤝 Contribuição
Sinta-se à vontade para abrir issues e enviar pull requests seguindo o
[as regras de contribuição](./CONTRIBUTING.md)

📜 Licença
Este projeto está sob a licença MIT.
