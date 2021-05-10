# Sample Flask APlication

Essa é uma simples aplicação em Flask com um contador de requisições utilizando o Redis. As requisições devem conter um token de autorização e seu valor é definido através da variável de ambiente `AUTH_TOKEN`.

## Testando a aplicação

```shell
$ docker-compose up -d
$ curl -H "Authorization: Token 123456" http://localhost:8000
```
