# 2018.2-Roles_Events

![license mit](https://img.shields.io/badge/license-MIT-blue.svg) 
[![Build Status](https://travis-ci.org/RolesFGA/2018.2-Roles_Events.svg?branch=master)](https://travis-ci.org/RolesFGA/2018.2-Roles_Events)
[![Coverage Status](https://coveralls.io/repos/github/RolesFGA/2018.2-Roles_Events/badge.svg?branch=master)](https://coveralls.io/github/RolesFGA/2018.2-Roles_Events?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/9b69b6a00a1ee30a293d/maintainability)](https://codeclimate.com/github/RolesFGA/2018.2-Roles_Events/maintainability)

## Microsserviço de gerencimanento de eventos

O microsserviço de eventos é utilizado no aplicativo IntegraFGA para gerenciar os eventos.


## Instalação 

### Requisitos 
Para instalação do projeto você deve ter instalado:
* Docker
* Docker Compose

### Como instalar

1 - Clone o repositório

2 - Entre na pasta do projeto

3 - Rode o comando:
```
sudo docker-compose up
```

4 - Acesse localhost:8003


Para acessar o container da aplicação use o seguinte comando:
```
sudo docker exec -it rolesevents_web_1 bash
```

Para ver todos os containers rodando na sua máguina use o seguinte comando:

```
sudo docker ps
```

## Outros microsserviços 
* [Roles Comments](https://github.com/RolesFGA/2018.2-Roles_Comments)


