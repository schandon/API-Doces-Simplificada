# Api Doces 

Este é o desenvolvimento de uma API Rest, que tem como objetivo a continuação de um projeto produzido durante a pós-graduação de desenvolvimento web, focado para o frontend de pedido de doces. Aaplicação em questão irá fazer o registo de informações de clientes, produtos e pedidos, com suas respectivas requisições HTTP's 

---
## Executando a API com Docker

É necessário estar com docker desktop instalado na maquina, [Link Download Docker Desktop](https://www.docker.com/products/docker-desktop/),

### Importante
  - Configurar as informações necessários no arquivo de .env, em caso de não preenchimento a aplicação docker não irá funcionar

Após a instalação e configuração execute o comando a seguir. 
```
    docker-compose up -d
```
Assim a aplicação estara rodando, configuração feitas no arquivo de docker-compose.yml
---
## Como executar
Para não precisar instalar as bivliotecas na sua maquina, iremos utilizar a virtualização, como isso iremos seguir um conjunto de passos.
  * Passo 1:
    * Executar o código para criar a pasta do ambiente
 ```
      python -m venv env
```
  * Passo 2:
    * Entrar na modo virtualizado, executando o código
```
      env\Scripts\activate
```
##### OBS.
  * Passo 2.1:
    * Em caso de erro na criação do ambiente virtualizado, utilizaremos o comando a seguir, caso não de erro ao utilizar o Passo 02, ignore o Passo. 
```
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
``` 
  * Passo 3:
    * Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo. 
```
    pip install -r requirements.txt 
```
  * Passo 4:
    * Para executar a API  basta executar:
```
    flask run --host 0.0.0.0 --port 5000 --reload
```