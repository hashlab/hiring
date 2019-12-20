# Hash Teste Front-end

Antes de começar, leia os nossos [key values](https://www.keyvalues.com/hash) para entender um pouco sobre o que nós priorizamos no desenvolvimento e **faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço** ;)

## Objetivo

O objetivo do desafio é validar seus conhecimentos em JavaScript, então aproveite o desafio para mostrar tudo o que você sabe sobre as novas features da linguagem, TypeScript(caso opte, mostre todo o seu domínio), componentização, processadores de CSS seja IN-JS ou demais, testes unitário e end-to-end. 

Vamos analisar o seu teste com base no que foi dito acima, então, dê um show pra gente ficar impressionado.

## Restrições

1.  Não é permitido utilizar frameworks e/ou bibliotecas de UI, como React, Vue.js, Angular e JSX (queremos ver a sua habilidade com JS e DOM).
2.  São permitidas ferramentas modernas de desenvolvimento como TypeScript, Babel, eslint, webpack, assim como o uso de polyfills (e outras ferramentas para melhorar o suporte a browsers, como o Modernizr) e/ou bibliotecas para testes.
3.  São permitidos pré-processadores de CSS e/ou ferramentas CSS-in-JS.
4.  Não é uma regra, mas evite usar lodash, underscore, ramda e similares.

## Como Avaliaremos seu Teste Técnico

Sua performance será avaliada com base nos seguintes pontos:

1. Os problemas foram resolvidos com eficiência e eficácia, a aplicação funciona conforme o esperado.
2. A aplicação é fornecida com scripts de instalação e execução para ambientes de desenvolvimento e de testes.
3. Você demonstra conhecimento de como testar as partes críticas do aplicativo. **Não exigimos** 100% de cobertura.
4. A aplicação tem uma estrutura lógica e bem organizada.
5. O teste acompanha documentação com o raciocínio sobre as decisões tomadas.
6. O código está documentado e/ou é de fácil leitura.
7. Segue algum guia de estilo padronizado
8. Um histórico do git (mesmo que breve) com mensagens claras e concisas.

## O Teste

Hoje nossos clientes precisam saber o quanto custa antecipar uma transação, e para isso, precisamos desenvolver uma calculadora de antecipação para que os mesmos consigam saber quais valores eles vão receber caso optem por antecipar o recebimento.


### Front
O layout proposto para essa calculadora pode ser visto no link abaixo.

[Link para o layout](https://www.figma.com/file/ipV80xJ29T7rdz0Aoo7xWv/Antecipation?node-id=0%3A1) - **Lembrando que deve ser pixel by pixel**

### API

Você irá consumir uma api já existente. Segue as especifiações da API:

`http://hash-front-test.herokuapp.com/`

### Post

| Parâmetro    | Required | Tipo          | Descrição                                                                              |
|--------------|----------|---------------|----------------------------------------------------------------------------------------|
| amount       | Sim      | number        | Valor total da transação em centavos                                                   |
| installments | Sim      | number        | Número de parcelas                                                                     |
| mdr          | Sim      | number        | É a taxa cobrada pelas adquirentes sobre cada transação de cartão de crédito ou débito |
| days         | Não      | Array<number> | Uma lista com os dias a serem calculadas as antecipações                               |

### Simulando Timeout, Internal Server Error e Delay de resposta

Para **Timeout** basta executar a request post passando `timeout` como query string parametros, exemplo:
`http://hash-front-test.herokuapp.com/?timeout`

Para **Internal Server Error** basta executar a request post passando `timeout` como query string parametros, exemplo:
`http://hash-front-test.herokuapp.com/?internalError`

Para **Delay de resposta** que pode ser usado como simulador de conexão lenta, basta executar a request post passando `timeout` como query string parametros, exemplo:
`http://hash-front-test.herokuapp.com/?delay=tempoEmMilissegundos`

Você deverá desenvolver o teste seguindo os requisitos abaixo.

## Requisitos

- Componentize todos os elementos
- Os períodos de recebimento devem ser configuráveis já que a API recebe um lista de periódos para realizar os cálculos.
- Faça testes unitários e/ou de ponta-a-ponta (end-to-end)
- Possíveis cenários devem ser cobertos e terem suas soluções implementadas. Não foi desenvolvido layout para isso, pois queremos observar como você vai lidar com esses cenários:
  - Demora de respostas da API
  - Timeout da API
  - Conexão lenta
  - Usuário estar offline
