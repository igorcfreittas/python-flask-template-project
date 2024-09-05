# Python RESTful API Example


## Introdução

Esse é um projeto que pretendo usar como template para futuros projetos com flask
é baseado no padrão arquitetural MVC, foi adicionada uma camada de respotórios (fazendo um pouco do trabalho do que seria a camada de model), nesse caso, como estou utilizando MongoDB,
não fiz a implementação da camada de Model literalmente, **a principal ideia do projeto é orientado ao padrão "request-response".**

É um trabalho em andamento, podemos dizer que essa é uma versão 0.0.1, a ideia é que eu aplique conceitos que penso serem úteis
para o desenvolvimento de API's no geral.

Explicando rapidamente, utilizei Python + Flask, MongoDB, Docker/docker compose, Flake8 como o linter, também escrevi testes
unitários com o modulo padrão da linguagem (unittest), há uma pipeline criada com o linter e testes unitários caso tenha curiosidade (diretório .github).

## Fluxo da aplicação

 - Observação: Um exemplo foi adicionado -User-, rota, recurso, controller, respotiório.

Abaixo é mostrado como funciona o fluxo da aplicação, desde subir o server até a saída com a resposta para o cliente:

![Python Template](https://iili.io/dvxKInt.png)


# Setup

Primeiro, faça o download do projeto e depois realize o build utilizando docker compose.

### Na raiz do projeto (onde o docker-compose.yml esta localizado):
``
docker compose up -d --build
``

A aplicação deve estar escutando na rota e porta:

**http://127.0.0.1:5000**

### Teste (UserController example)

Realize um POST para a rota /user e verifique se o banco de dados esta funcionando:
 
 - Os campos em branco são campos "opcionais", verifique em *user_resource.py*

```
POST /user

{
	"username": "example",
	"password": "example",
	"email": "example@example.com",
	"cellphone": "",
	"age": 0,
	"birth_date": ""
}
```

Há outra rota de teste para recuperar o usuário:

```
http://127.0.0.1:5000/user/id (mongodb id)
```

### Comandos

 - Pra monitorar os logs da app (print, etc) em tempo real:

``
docker compose up api
``

 - Testes unitários:

``
docker compose run --rm api sh -c "python -m unittest"
``

 - Lint:

``
docker compose run --rm api sh -c "flake8"
``

*Se houver resultado no console, o código esta organizado corretamente*

# Extras

## Pipeline (Github actions)

As credenciais da pipeline foram criadas com base no docker hub (.github/workflows/actions-config.yml):
 
 - DOCKERHUB_USER: nome de usuário utilizado para entra no docker hub
 - DOCKERHUB_TOKEN: Token gerado no painel de usuário do docker hub

Caso queira aprender sobre pipelines, sugiro estudar github actions.

## MongoDB and Mongo Express

- Verifique as configurações do MongoDB no arquivo **docker-compose.yml**
- O Mongo Express pode ser acessado pela rota:

``
http://127.0.0.1:8081/
``

- A collection só vai ser criada quando um documento for inserido

- A estrutura da rota: ME_CONFIG_MONGODB_URL (as configurações são feitas com base no serviço do mongodb declarado anteriormente)
  - user: MONGO_INITDB_ROOT_USERNAME
  - password: MONGO_INITDB_ROOT_PASSWORD
  - port: Declaração das portas no serviço mongodb
  - service_host: Nome do serviço pro container do mongo, nesse caso mongodb, linha 23

```
    mongodb://root:root@mongodb:27017
    =
    mongodb://user:password@service_host:port
```


