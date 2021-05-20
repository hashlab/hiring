# Back-end challenge

Olá!

Estamos felizes por você ter chegado até aqui! Agora é a hora de conhecermos um pouco mais da sua bagagem técnica. Esperamos que goste do Desafio!

## API de carrinho

Você deverá implementar uma API HTTP (JSON) de e-commerce (venda online) e que terá um endpoint de carrinho (checkout). Esse endpoint aceitará uma requisição com método POST, header X-USER-ID contendo o id de um usuário e a estrutura do payload de requisição deve seguir o exemplo:

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

Em resumo a requisição deve conter uma lista de produtos e a quantidade de cada um a ser comprado.

## Regras

Após receber a requisição deverão ser aplicadas as seguintes regras:

### Regra número 1

Para cada produto você precisará calcular a porcentagem de desconto e isso deve ser feito consumindo um serviço gRPC fornecido por nós para auxiliar no seu teste. Utilize a imagem Docker para subir esse serviço de desconto e o arquivo proto para gerar o cliente na linguagem escolhida. Você pode encontrar como gerar um cliente gRPC nas documentações oficiais da ferramenta e em outros guias encontrados na internet.

### Regra número 2

Caso o serviço de desconto esteja indisponível o endpoint deverá continuar funcionando porém não vai realizar o cálculo com desconto.

### Regra número 3

Durante o cálculo do valor total deverá ser considerada a quantidade do produto.

### Regra número 4

Deverá ser verificado se é o aniversário do usuário recebido via header e caso seja você deve adicionar um produto brinde ao carrinho.

### Regra número 5

Deverá ser verificado se é black friday (para simplificar você pode escolher uma data fixa) e caso seja você deve adicionar um produto brinde ao carrinho se nenhum outro já tiver sido adicionado (apenas um produto brinde por carrinho).

## Resposta da API

A resposta da API deverá trazer o valor total do carrinho com e sem desconto, valor total de descontos e a lista de produtos com seus descontos individuais. A resposta deverá respeitar a estrutura do seguinte payload de exemplo:

```javascript
{
    "total_amount": 200, // Valor total da compra sem desconto
    "total_amount_with_discount": 170, // Valor total da compra com desconto
    "total_quantity": 30, // Quantidade total de produtos (considerando quantidade)
    "products": [
        {
            "id": 1,
            "quantity": 2,
            "amount": 100, // Preço do produto
            "total_amount": 200, // Valor total na compra desse produto
            "discount": 30,
            "Is_gift": false // É brinde?
        }
    ]
}
```

## O que vai ser avaliado?

- Documentação
- Testes automatizados
- O quanto sua aplicação está pronta para produção (logs, configuração flexível e etc): é mandatório o uso de Docker para rodar a aplicação
- Histórico de commits
- Qualidade do código: legibilidade, estrutura e facilidade de manutenção
- Funcionamento das regras
- Tratamento de erros e pontos de falhas

## Não se preocupe

- Você pode popular seu banco de dados manualmente portanto não é necessário um CRUD de produtos
- Não é necessário criar um serviço extra de autenticação ou mesmo de usuário, para simplificar esse teste você pode usar um banco de dados único e fazer todos acessos a partir da API
- Não é necessário ter 100% de cobertura de testes, foque em testar os casos de uso mais relevantes
- Iremos testar sua API apenas com payloads de formato válido então não é necessário fazer esse tipo de validação (vale notar que é aqui nos referimos apenas ao formato do payload, porém é necessário validar, por exemplo. se os produtos da lista existem)
- Fique à vontade em escolher a linguagem e framework para o desenvolvimento da solução

Fique à vontade para nos acessar enquanto estiver desenvolvendo o teste. Qualquer dúvida sua pode ser esclarecida diretamente com a recruiter responsável pelo seu processo.

Boa atividade!
