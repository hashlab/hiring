# Hash Teste Front-end

Antes de começar, leia os nossos [key values](https://www.keyvalues.com/hash) para entender um pouco sobre o que nós priorizamos no desenvolvimento e **faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço** ;)

O teste consiste desenvolver um simulador de antecipação de recebíveis composto por:

> - App com formulário para o usuário interagir.
> - Biblioteca para executar o cálculo de recebíveis
>   - Parcelamento máximo de 12x

Envie o resultado do seu desafio para dev@hash.com.br (ele pode ser open source!). Em até uma semana marcaremos uma conversa com você após analisarmos seu desafio.

## Restrições

1.  Não é permitido utilizar frameworks e/ou bibliotecas de UI, como React, Vue.js, Angular e JSX (queremos ver a sua habilidade com JS e DOM).
2.  São permitidas ferramentas modernas de desenvolvimento como TypeScript, Babel, eslint, webpack, assim como o uso de polyfills (e outras ferramentas para melhorar o suporte a browsers, como o Modernizr) e/ou bibliotecas para testes.
3.  São permitidos pré-processadores de CSS ou ferramentas CSS-in-JS.
4.  Não é uma regra, mas evite usar lodash, underscore, ramda e similares.

## Como Avaliaremos seu Teste Técnico

Sua performance será avaliada com base nos seguintes pontos:

1. **Organização do projeto** pensando em **escala de novas funcionalidades**, tanto sistema de arquivos como organização do código em si (nome de arquivos, nome de variáveis, etc)
2. Se o **layout está idêntico (pixel by pixel)** como proposto no documento do Figma (link logo abaixo)
3. Que a calculadora de antecipação **apresente os cálculos corretos**.
4. **Testes automatizados da biblioteca** de cálculo. Aproveite para **testar o parcelamento máximo (12x)**.

## Recomendações

1. Maior cobertura de testes
2. Conte uma história do projeto em commits (preferêncialmente em inglês)
3. Escreva um bom [README.md (exemplo)](https://github.com/elsewhencode/project-guidelines/blob/master/README.sample.md), se possível com a documentação de como consumir a biblioteca de cálculos.
  3.1. Caso adicione um passo a passo de como executar o seu teste, garanta que ele esteja funcionando.
4. Garanta a qualidade do código usando eslint, pre-commit, e outras boas práticas

## Formulário de Simulação da Antecipação

[Link para o layout](https://www.figma.com/file/ipV80xJ29T7rdz0Aoo7xWv/Antecipation?node-id=0%3A1) - **Lembrando que deve ser pixel by pixel**

- Todos os campos são obrigatórios
- A data de recebimento do **valor total da compra** deve ser fixada nos seguintes periodos: (como apresentado no layout)
  - Amanhã, quanto eu receberia se antecipasse tudo
  - 15 dias, quanto eu receberia se antecipasse tudo
  - 30 dias, quanto eu receberia se antecipasse tudo
  - 60 dias, quanto eu receberia se antecipasse tudo
- O cálculo deve ser executado assim que os campos estiverem válidos

## Biblioteca de Cálculo de Antecipação

A taxa de recebimento antecipado é calculada a juros simples e aplicada sobre o valor líquido da transação, ou seja, primeiro é deduzida a taxa de **MDR²** e então é aplicada a taxa de recebimento antecipado. A taxa de recebimento antecipado é mensal, mas seu cálculo é feito com taxa diária (taxa mensal/30), uma vez que algumas transações são antecipadas por períodos menores que 30 dias.

A taxa de recebimento antecipado é sempre proporcional ao tempo em que a parcela está sendo antecipada. Supondo uma venda em 3x sem juros - normalmente, a primeira parcela seria recebida pelo lojista em 30 dias, a segunda parcela em 60 dias e a terceira em 90 dias.

Desse modo, para o lojista receber a primeira parcela no dia seguinte da venda, precisamos antecipar, aproximadamente, 1 mês. Logo, a taxa de recebimento antecipado vai incidir uma vez. Já a segunda parcela precisaria ser antecipada em 2 meses, logo, a taxa de recebimento antecipado incide 2x. A terceira parcela seria antecipada em 3 meses, sendo a taxa de recebimento antecipado multiplicada por 3 nessa parcela.

#### Exemplo com números:

**Transação**

| Valor      | Parcelas | MDR |
| ---------- | -------- | --- |
| R\$ 150,00 | 3x       | 4%  |

**Antecipação Total**

| Parcela | Recebível | Com Atencipação       |
| ------- | --------- | --------------------- |
| 1       | R\$ 48,00 | R\$ 46,08             |
| 2       | R\$ 48,00 | R\$ 44,16             |
| 3       | R\$ 48,00 | R\$ 42,24             |
|         |           | Total: **R\$ 132,48** |

**² Taxa de MDR é uma porcentagem do valor da sua venda que é cobrada diretamente dos seus recebíveis.**

#### Exemplo animado baseado nessa tabela anterior

![](anticipation.gif)
