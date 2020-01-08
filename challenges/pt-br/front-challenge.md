# Hash Teste Front-end

Antes de começar, leia os nossos [key values](https://www.keyvalues.com/hash) para entender um pouco sobre o que nós priorizamos no desenvolvimento e **faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço** ;)

## Objetivo

O objetivo do desafio é validar seus conhecimentos nos seguintes tópicos:
- **JavaScript**: aproveite o desafio para mostrar tudo o que sabe sobre as novas features da linguagem.
- **TypeScript**: Opcional. Caso opte por usá-lo, mostre todo o seu domínio. 
- **Componentização** 
- **Processadores de CSS**: seja IN-JS ou demais
-  **Testes unitários** 
- **Testes end-to-end**

Analisaremos seu teste com base nos critérios acima, então dê um show para que fiquemos impressionados.

## Restrições

1.  **Não é permitido** utilizar frameworks e/ou bibliotecas de UI, como React, Vue.js, Angular e JSX (queremos ver sua habilidade com JS e DOM).
2.  **São permitidas** ferramentas modernas de desenvolvimento como TypeScript, Babel, eslint, webpack, assim como o uso de polyfills (e outras ferramentas para melhorar o suporte a browsers, como Modernizr) e/ou bibliotecas para testes.
3.  **São permitidos** pré-processadores de CSS e/ou ferramentas CSS-in-JS.
4.  Não é uma regra, mas evite usar lodash, underscore, ramda e similares.

## Como Avaliaremos seu Teste Técnico

Sua performance será avaliada com base nos seguintes pontos:

1. Os problemas foram resolvidos com eficiência e eficácia, a aplicação funciona conforme o esperado.
2. A aplicação é fornecida com comandos de instalação e execução para ambientes de desenvolvimento e de testes.
3. Você demonstra conhecimento de como testar as partes críticas do aplicativo. **Não exigimos** 100% de cobertura.
4. A aplicação tem uma estrutura lógica e bem organizada.
5. O teste acompanha documentação com o raciocínio sobre as decisões tomadas.
6. O código está documentado e/ou é de fácil leitura.
7. Segue algum guia de estilo de código padronizado
8. Possui um histórico do git (mesmo que breve) com mensagens claras e concisas.

## O Teste

Hoje nossos clientes precisam saber quanto custa antecipar uma transação, e para isso, precisamos desenvolver uma calculadora de antecipação para que os mesmos consigam saber quais valores receberão caso optem por antecipar o recebimento.

Você deverá desenvolver o teste seguindo os requisitos abaixo.

## Requisitos

- Use componentização.
- Os períodos de recebimento devem ser configuráveis já que a API pode receber uma lista de periódos para realizar os cálculos.
- Faça testes unitários e/ou de ponta-a-ponta (end-to-end)
- Os possíveis cenários devem ser cobertos e terem suas soluções implementadas. Não foi desenvolvido layout para isso, pois queremos observar como você vai lidar com esses cenários:
  - Demora de respostas da API
  - Timeout da API
  - Conexão lenta
  - Usuário estar offline

## Front
O layout proposto para essa calculadora pode ser visto no link abaixo.

[Link para o layout](https://www.figma.com/file/ipV80xJ29T7rdz0Aoo7xWv/Antecipation?node-id=0%3A1) - **Lembrando que a sua aplicação deve seguir o layout pixel by pixel**

## API

Você irá consumir uma api já existente. Segue as especifiações da API:

`http://hash-front-test.herokuapp.com/`

### Post

| Parâmetro    | Required | Tipo          | Descrição                                                                              |
|--------------|----------|---------------|----------------------------------------------------------------------------------------|
| amount       | Sim      | number        | Valor total da transação em centavos                                                   |
| installments | Sim      | number        | Número de parcelas                                                                     |
| mdr          | Sim      | number        | É a taxa cobrada pelas adquirentes sobre cada transação de cartão de crédito ou débito |
| days         | Não      | Array<number> | Uma lista com os dias a serem calculadas as antecipações                               |


### Exemplo

```bash
$ curl --request POST \
  --url http://hash-front-test.herokuapp.com/ \
  --header 'content-type: application/json' \
  --data '{
	"amount": 15000,
	"installments": 3,
	"mdr": 4
}'

{"1":13267,"15":13536,"30":13824,"90":14400}%
```

### Exemplo informando períodos

```bash
$ curl --request POST \
  --url http://hash-front-test.herokuapp.com/ \
  --header 'content-type: application/json' \
  --data '{
	"amount": 15000,
	"installments": 3,
	"mdr": 4,
	"days": [30, 60, 90]
}'

{"30":13824,"60":14208,"90":14400}%
```

### Simulando Timeout, Internal Server Error e Delay de resposta

Para **Timeout** basta executar a request post passando `timeout` como query string, exemplo:
`http://hash-front-test.herokuapp.com/?timeout`

Para **Internal Server Error** basta executar a request post passando `timeout` como query string, exemplo:
`http://hash-front-test.herokuapp.com/?internalError`

Para **Delay de resposta**, que pode ser usado como simulador de conexão lenta, basta executar a request post passando `delay` informando o tempo do delay em milissegundos, exemplo:
`http://hash-front-test.herokuapp.com/?delay=tempoEmMilissegundos`
