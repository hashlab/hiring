# Hash Teste SRE

Olá candidato! Antes de começar, leia a nossa [página sobre cultura](https://tech-culture.hash.com.br/) para entender um pouco sobre o que nós priorizamos no desenvolvimento e faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço ;)

O teste consiste em dois desafios. O primeiro deles explora seu entendimento sobre arquitetura de microserviços e o segundo suas habilidades de automação.

## Arquitetura

#### O resultado deve conter um documento de texto (pdf, markdown, git, etc) contendo a arquitetura proposta e documentação relevante (se houver).
- **Opcional.** Caso queira demonstrar a arquitetura em código de forma reprodutível também seria bem legal. (ex. Terraform e/ou outros)

1) Imagine que o time de engenharia da Hash criou dois novos serviços: `/cart` e `/checkout` na mesma aplicação, e a complexidade implementada nessas rotas cresceu de forma demasiada e chegaram a conclusão de segmentá-las em um microserviço distinto da aplicação principal. Diagrame uma arquitetura que contemple esse cenário explicando a estratégia de _rollout_ entre o serviço antigo e novo: parte do tráfego deve servir os dois microserviços no primeiro momento para garantir uma migração segura e transparente.

2) Agora múltiplas tenâncias desse produto precisam ser entregues utilizando o Kubernetes e é importante que cada tenância do produto seja isolada uma da outra. Considere uma solução gerenciada do Kubernetes como o GKE ou EKS e então diagrame uma arquitetura contemplando esse cenário.

Esperamos que você entregue um arquivo de texto (pdf, markdown, git, etc) contendo as arquiteturas propostas e as documentações relevantes. Caso queira demonstrar a arquitetura em código, de forma reprodutível, também seria bem legal (ex. Terraform e/ou outros).

## Automação

Enviaremos por e-mail um arquivo zip contendo uma aplicação e o desafio é desenvolver uma [CLI](https://en.wikipedia.org/wiki/Command-line_interface) que realize testes de carga nesse serviço, seguindo os seguintes requisitos:

- Utilizar múltiplas [threads](https://en.wikipedia.org/wiki/Thread_(computing)) em um único teste
- Emitir um sumário de execução do teste contendo:
  - Quantas requisições falharam
  - Quantas requisições ocorreram com sucesso
  - O [percentil](https://pt.wikipedia.org/wiki/Percentil) ou média de latência do total de requisições realizadas
  - O [percentil](https://pt.wikipedia.org/wiki/Percentil) ou média de latência do total de requisições realizadas por backend (Opcional)
  - Conseguir identificar qual instância do serviço respondeu a requisição (Opcional)
