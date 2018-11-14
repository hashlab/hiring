# Hash Teste Back-end

Antes de começar, leia os nossos [key values](https://github.com/hashlab/hiring/blob/master/README.md) para entender um pouco sobre o que nós priorizamos no desenvolvimento e faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço ;)

O teste consiste em escrever 2 microserviços que possibilitam retornar uma lista de produtos com desconto personalizado para cada usuário.

Envie o resultado do seu desafio para dev@hash.com.br (ele pode ser open source!). Em até uma semana marcaremos uma conversa com você após analisarmos seu desafio.

## Restrições

 1. Os serviços desse teste devem ser escritos usando linguagens distintas
 2. Os serviços desse teste devem se comunicar via [gRPC](https://grpc.io/)
 3. Utilize [docker](https://www.docker.com/) para provisionar os serviços
 4. Para facilitar, os serviços podem usar um banco de dados compartilhado

## Avaliação

1. Conversaremos sobre a estrutura do código, escolha do banco, e outras decisões que foram tomadas
2. Discutiremos como esse sistema evoluiria ao longo do tempo
3. Considere que as regras de descontos irão mudar com o tempo
4. Considere que mais pessoas irão trabalhar junto com você nesse projeto

## Serviço 1: Desconto invidual de produto

* Este serviço recebe um id de produto e um id de usuário e retorna um desconto.

Produto exemplo:
```
{
    id: string
    price_in_cents: int
    title: string
    description: string
    discount: {
        pct: float
        value_in_cents: int
    }
}
```

Usuário exemplo:
```
{
    id: string: string
    first_name: string
    last_name: string
    date_of_birth: Date
}
```

* A função de desconto será baseada na data de nascimento do usuário

* Caso a data de nascimento seja 29 de fevereiro, o serviço deve retornar um erro qualquer.

## Serviço 2: Listagem de produtos
* Expõe uma rota HTTP tal que `GET /product` retorne um json com uma
lista de produtos.

* Essa rota deve receber opcionalmente via header `X-USER-ID` um id de usuário.

* Para obter o desconto personalizado este serviço deve utilizar o serviço 1.

* Caso o serviço 1 retorne um erro, a lista de produtos ainda precisa ser retornada, porém com esse produto que deu erro sem desconto.

* Se o serviço de desconto (1) cair, o serviço de lista (2) tem que continuar funcionando e retornando a lista normalmente, só não vai aplicar os descontos.
