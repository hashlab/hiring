# Hash Teste Front-end

Antes de começar, leia a nossa [página sobre cultura](https://tech-culture.hash.com.br/) para entender um pouco sobre o que nós priorizamos no desenvolvimento e **faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço** ;)

Envie o resultado do seu desafio para dev@hash.com.br (ele pode ser open source!).
Se possível, faça deploy da sua aplicação em algum serviço como [Netlify](https://www.netlify.com/), [Heroku](https://heroku.com/) ou qualquer outro de sua preferência.

## Objetivo

O objetivo do desafio é validar seus conhecimentos nos seguintes tópicos:

- **JavaScript**: aproveite o desafio para mostrar tudo o que sabe sobre as novas features da linguagem.
- **React**: siga boas práticas e mantenha o código idiomático. Busque utilizar features recentes e se mantenha atento a problemas comuns como re-renders desnecessários.
- **TypeScript**: Opcional. Caso opte por usá-lo, mostre todo o seu domínio.
- **Componentização**
- **CSS**: seja optando por vanilla, pré-processadores ou CSS-in-JS.
- **Testes unitários**
- **Testes end-to-end**

Analisaremos seu teste com base nos critérios acima, então dê um show para que fiquemos impressionados.

## Restrições

1.  **Não é permitido** utilizar frameworks e/ou bibliotecas de UI que não seja o React (como Vue.js ou Angular).
2.  **São permitidas** ferramentas modernas de desenvolvimento como TypeScript, Babel, eslint, webpack, assim como o uso de polyfills (e outras ferramentas para melhorar o suporte a browsers, como Modernizr) e/ou bibliotecas para testes.
3.  **São permitidos** pré-processadores de CSS e/ou ferramentas CSS-in-JS.
4.  Não é uma regra, mas evite usar lodash, underscore, ramda e similares.

## Como Avaliaremos seu Teste Técnico

Sua performance será avaliada com base nos seguintes pontos:

1. A aplicação funciona conforme o esperado.
2. Os problemas foram resolvidos com eficiência.
3. A aplicação é fornecida com comandos de instalação e execução para ambientes de desenvolvimento e de testes.
4. Você demonstra conhecimento de como testar as partes críticas da aplicação. Não exigimos 100% de cobertura.
5. A aplicação tem uma estrutura lógica e bem organizada.
6. O teste acompanha documentação com o raciocínio sobre as decisões tomadas.
7. O código está documentado e/ou é de fácil leitura.
8. Segue algum guia de estilo de código padronizado.
9. Possui um histórico do git (mesmo que breve) com mensagens claras e concisas.

## O Teste

Hoje nossos clientes precisam saber quanto custa antecipar uma transação, e para isso, precisamos desenvolver uma calculadora de antecipação para que os mesmos consigam saber quais valores receberão caso optem por antecipar o recebimento.

Você deverá desenvolver o teste seguindo os requisitos abaixo.

## Requisitos

- Use componentização.
- Os períodos de recebimento devem ser configuráveis já que a API pode receber uma lista de periódos para realizar os cálculos.
- Faça testes unitários e/ou de ponta-a-ponta (end-to-end)

Os possíveis cenários devem ser cobertos e terem soluções implementadas. Não foi desenvolvido layout para isso, pois queremos observar como você lidará com eles:

- Demora de respostas da API
- Timeout da API
- Conexão lenta
- Usuário estar offline

## Front
O layout proposto para essa calculadora pode ser visto no link abaixo.

[Link para o layout](https://www.figma.com/file/ipV80xJ29T7rdz0Aoo7xWv/Antecipation?node-id=0%3A1) - **Lembrando que a sua aplicação deve seguir o layout pixel by pixel**

## API

Você consumirá uma API já existente no endereço abaixo. Em seguida há uma especificação simplificada dela.

`https://hash-front-test.herokuapp.com/`

### Post

| Parâmetro    | Obrigatório? | Tipo          | Descrição                                                                              |
|--------------|----------|---------------|----------------------------------------------------------------------------------------|
| `amount`       | Sim      | `number`        | Valor total da transação em centavos                                                   |
| `installments` | Sim      | `number`        | Número de parcelas                                                                     |
| `mdr`          | Sim      | `number`        | É a taxa cobrada pelas adquirentes sobre cada transação de cartão de crédito ou débito |
| `days`         | Não      | `Array<number>` | Uma lista com os dias a serem calculadas as antecipações                               |

### Exemplo

```bash
$ curl --request POST \
  --url https://hash-front-test.herokuapp.com/ \
  --header 'content-type: application/json' \
  --data '{
	"amount": 15000,
	"installments": 3,
	"mdr": 4
}'

{"1":13267,"15":13536,"30":13824,"90":14400}
```

### Exemplo informando períodos

```bash
$ curl --request POST \
  --url https://hash-front-test.herokuapp.com/ \
  --header 'content-type: application/json' \
  --data '{
	"amount": 15000,
	"installments": 3,
	"mdr": 4,
	"days": [30, 60, 90]
}'

{"30":13824,"60":14208,"90":14400}
```

### Simulando Timeout, Internal Server Error e Delay de resposta

Para **Timeout** basta executar a request post passando `timeout` através da query string, exemplo:
`https://hash-front-test.herokuapp.com/?timeout`

Para **Internal Server Error** basta executar a request post passando `internalError` através da query string, exemplo:
`https://hash-front-test.herokuapp.com/?internalError`

Para **Delay de resposta**, que pode ser usado como simulador de conexão lenta, basta executar a request post passando `delay`, e informando o tempo do delay em milissegundos, exemplo:
`https://hash-front-test.herokuapp.com/?delay=tempoEmMilissegundos`
