# Back-end challenge

Olá!

Estamos felizes por você ter chegado até aqui! Agora é a hora de conhecermos um pouco mais da sua bagagem técnica. Esperamos que goste do Desafio!

## API de carrinho

Você deverá implementar uma API HTTP (JSON) de e-commerce (venda online) e que terá um endpoint de carrinho (checkout). Esse endpoint aceitará uma requisição com método POST, a estrutura do payload de requisição deve seguir o exemplo:

Em resumo a requisição deve conter uma lista de produtos e a quantidade de cada um a ser comprado.

```javascript
{
    "products": [
        {
            "id": 1,
            "quantity": 1 // Quantidade a ser comprada do produto
        }
    ]
}
```

## Base de dados

Você deve utilizar o conteúdo do arquivo JSON `products.json`, como fonte de dados para a API. Não sendo necessário modelar ou utilizar algum tipo de banco de dados para o teste.

## Regras

Após receber a requisição deverão ser aplicadas as seguintes regras:

### Regra número 1

Para cada produto você precisará calcular a porcentagem de desconto e isso deve ser feito consumindo um serviço gRPC fornecido por nós para auxiliar no seu teste. Utilize a [imagem Docker](https://hub.docker.com/r/hashorg/hash-mock-discount-service) para subir esse serviço de desconto e o [arquivo proto](https://github.com/hashlab/hiring/blob/master/challenges/pt-br/new-backend-challenge/discount.proto) para gerar o cliente na linguagem escolhida. Você pode encontrar como gerar um cliente gRPC nas documentações oficiais da ferramenta e em outros guias encontrados na internet.

### Regra número 2
Caso o serviço de desconto esteja indisponível o endpoint de carrinho deverá continuar funcionando porém não vai realizar o cálculo com desconto.

### Regra número 3

Deverá ser verificado se é black friday e caso seja, você deve adicionar um produto brinde no carrinho. Lembrando que os produtos brindes possuem a flag `is_gift = true` e não devem ser aceitos em requisições para adicioná-los ao carrinho (em uma loja virtual, esse produto não deveria ir para "vitrine").
A data da Black Friday fica a seu critério.

### Regra número 4

Deverá existir apenas uma entrada de produto brinde no carrinho. 

### Regra número 5

É mandatório o uso de Docker para rodar a aplicação, de preferência utilizar docker-compose, pois facilitará o processo de correção.

## Resposta da API

A resposta da API deverá trazer o valor total do carrinho com e sem desconto, valor total de descontos e a lista de produtos com seus descontos individuais. A resposta deverá respeitar a estrutura do seguinte payload de exemplo:

*Todos os valores monetários devem estar em centavos.*

```javascript
{
    "total_amount": 20000, // Valor total da compra sem desconto
    "total_amount_with_discount": 19500, // Valor total da compra com desconto
    "total_discount": 500, // Valor total de descontos
    "products": [
        {
            "id": 1,
            "quantity": 2,
            "unit_amount": 10000, // Preço do produto em centavos
            "total_amount": 20000, // Valor total na compra desse produto em centavos
            "discount": 500, // Valor total de desconto em centavos
            "is_gift": false // É brinde?
        },
        {
            "id": 3,
            "quantity": 1,
            "unit_amount": 0, // Preço do produto em centavos
            "total_amount": 0, // Valor total na compra desse produto em centavos
            "discount": 0, // Valor total de desconto em centavos
            "is_gift": true // É brinde?
        }
    ]
}
```

## O que vai ser avaliado?

- Documentação sobre como subir e executar o seu teste
- Bons testes unitários (não se preocupe em alcançar 100% de cobertura no projeto)
- Configuração flexível (uso de envvars etc) 
- Histórico de commits
- Qualidade do código: legibilidade, estrutura e facilidade de manutenção
- Funcionamento das regras
- Tratamento de erros e pontos de falhas

## Não se preocupe

- Você receberá a base de dados de produtos em um arquivo JSON, não sendo necessário utilizar algum banco de dados ou implementar um CRUD. Você pode utilizar o JSON na memória da sua API.
- Fique à vontade em escolher a linguagem e framework para o desenvolvimento da solução

## Dúvidas

Fique à vontade para nos acessar enquanto estiver desenvolvendo o teste. Qualquer dúvida sua pode ser esclarecida diretamente com a recruiter responsável pelo seu processo.

Boa atividade e encaminhe seu teste finalizado para a recruiter responsável pelo seu processo.
