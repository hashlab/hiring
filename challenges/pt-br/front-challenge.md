# Hash Teste Front-end

Antes de começar, leia os nossos [key values](https://www.keyvalues.com/hash) para entender um pouco sobre o que nós priorizamos no desenvolvimento e faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço ;)

O teste consiste desenvolver um simulador de antecipação de recebíveis composto por um formulário para o usuário interagir e uma biblioteca para executar o cálculo.

Envie o resultado do seu desafio para dev@hash.com.br (ele pode ser open source!). Em até uma semana marcaremos uma conversa com você após analisarmos seu desafio.

## Restrições

 1. Não é permitido utilizar frameworks, como React, Vue.js, Angular.
 2. São permitidas ferramentas modernas de desenvolvimento como TypeScript, Babel, eslint, webpack, assim como o uso de polyfills (e outras ferramentas para melhorar o suporte a browsers, como o Modernizr) e/ou bibliotecas para testes.
 3. São permitidos pré-processadores de CSS ou ferramentas CSS-in-JS.

## Avaliação

1. Conversaremos sobre a estrutura do código, a forma como o projeto foi organizado, e outras decisões que foram tomadas.
2. Discutiremos como esse sistema evoluiria ao longo do tempo.
3. Considere que mais pessoas irão trabalhar junto com você nesse projeto

## Formulário de Simulação da Antecipação

[Link para o layout](https://zpl.io/ameEPBe)

- Todos os campos são obrigatórios
- A data de recebimento devem ser fixas nos seguintes periodos: (como apresentado no layout)
    - Amanhã
    - 15 dias
    - 30 dias
    - 60 dias
- O cálculo deve ser executado assim que os campos estiverem válidos
- Mantenha o layout pixel by pixel como proposto no link

## Biblioteca de Cálculo de Antecipação

A taxa de recebimento antecipado é calculada a juros simples e aplicada sobre o valor líquido da transação, ou seja, primeiro é deduzida a taxa de **MDR²** e então é aplicada a taxa de recebimento antecipado. A taxa de recebimento antecipado é mensal, mas seu cálculo é feito com taxa diária (taxa mensal/30), uma vez que algumas transações são antecipadas por períodos menores que 30 dias.

A taxa de recebimento antecipado é sempre proporcional ao tempo em que a parcela está sendo antecipada. Supondo uma venda em 3x sem juros - normalmente, a primeira parcela seria recebida pelo lojista em 30 dias, a segunda parcela em 60 dias e a terceira em 90 dias.

Desse modo, para o lojista receber a primeira parcela no dia seguinte da venda, precisamos antecipar, aproximadamente, 1 mês. Logo, a taxa de recebimento antecipado vai incidir uma vez. Já a segunda parcela precisaria ser antecipada em 2 meses, logo, a taxa de recebimento antecipado incide 2x. A terceira parcela seria antecipada em 3 meses, sendo a taxa de recebimento antecipado multiplicada por 3 nessa parcela.

#### Exemplo com números:

**Transação**

| Valor      | Parcelas | MDR |
| ---------- | -------- | --- |
| R$ 150,00  | 3x       | 4%  |


**Antecipação Total**

| Parcela | Recebível | Com Atencipação  |
| ------  | --------- | ---------------- |
| 1       | R$ 48,00  | R$ 46,08         |
| 2       | R$ 48,00  | R$ 44,16         |
| 3       | R$ 48,00  | R$ 42,24         |
|         |           | Total: **R$ 132,48** |

**² Taxa de MDR é uma porcentagem do valor da sua venda que é cobrada diretamente dos seus recebíveis.**
