# Hash Teste SRE

Antes de começar, leia a nossa [página sobre cultura](https://tech-culture.hash.com.br/) para entender um pouco sobre o que nós priorizamos no desenvolvimento e faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço ;)

O teste de SRE é dividido em **arquitetura** e **desenvolvimento** e complementa o [desafio de back end](https://github.com/hashlab/hiring/blob/master/challenges/pt-br/back-challenge.md).

> Se você estiver fazendo parte do processo seletivo iremos enviar um arquivo zip com o desafio de backend

## Arquitetura

- Os dois cenários a seguir são baseados no [desafio de backend](https://github.com/hashlab/hiring/blob/master/challenges/pt-br/back-challenge.md), leia-os antes de prosseguir.

1) Imagine que o time de engenharia do produto criou mais 2 rotas: `/cart` e `/checkout` na mesma aplicação, e a complexidade implementada nessas rotas cresceu de forma demasiada e chegaram a conclusão de segmentá-las em um microserviço distinto da aplicação principal. Crie uma arquitetura que contemple esse cenário explicando a estratégia de _rollout_ entre o serviço antigo e novo: parte do tráfego deve servir os dois microserviços no primeiro momento para garantir uma migração segura e transparente.

2) Agora múltiplas tenâncias desse produto precisam ser entregues utilizando o Kubernetes*, é importante que cada tenância do produto seja isolada uma da outra. Crie uma arquitetura contemplando esse cenário.

> \* Assumir que é uma solução gerenciada. Ex: GKE

#### O resultado deve conter um documento de texto (pdf, markdown, git, etc) contendo a arquitetura proposta e documentação relevante (se houver).
- **Opcional.** Caso queira demonstrar a arquitetura em código de forma reprodutível também seria bem legal. (ex. Terraform e/ou outros)

## Desenvolvimento

A aplicação 2 do desafio de backend é um serviço GRPC, desenvolva uma [CLI](https://en.wikipedia.org/wiki/Command-line_interface) que realize testes de carga nesse serviço, seguindo os seguintes requisitos:

- Utilizar múltiplas [threads](https://en.wikipedia.org/wiki/Thread_(computing)) em um único teste
- Emitir um sumário de execução do teste contendo:
  - Quantas requisições falharam
  - Quantas requisições ocorreram com sucesso
  - O [percentil](https://pt.wikipedia.org/wiki/Percentil) ou média de latência do total de requisições realizadas
  - O [percentil](https://pt.wikipedia.org/wiki/Percentil) ou média de latência do total de requisições realizadas por backend (Opcional)
  - Conseguir identificar qual instância do serviço respondeu a requisição (Opcional)


## Avaliação

Discutiremos como esse sistema evoluiria ao longo do tempo, e quais trade-offs você fez hoje e/ou teria que fazer em futuros hipotéticos.
