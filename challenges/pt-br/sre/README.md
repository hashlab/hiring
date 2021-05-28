# Hash SRE Challenge

Obrigado por dedicar um tempo extra para completar este desafio. A solução entregue ajudará a avaliar sua capacidade de criar uma solução funcional com base em um caso de uso. Sabemos que seu tempo é valioso, portanto, gaste o tempo que achar apropriado.

Estamos à disposição em caso de dúvidas. Um excelente exercício pra você.

# O que procuramos

- Que seu código seja facilmente reprodutível.
- Que você gere documentação.
- Que seja utilizado um fluxo de CI/CD.

# Antes de Começar

- A entrega deverá ser versionada com o Git, porém não deverá ficar exposta em repositório público. Analisaremos cada *commit* para saber como a solução foi desenvolvida, então seja o mais objetivo possível. Após a conclusão, compacte o resultado de sua entrega com o Gzip e envie-o para email da *recruiter* que está conduzindo seu processo e para sre@hash.com.br com o assunto "Desafio de SRE".
  
- A documentação de sua entrega é parte do desafio, então capriche!
  
- Não tem problema se você não conseguir finalizar tudo! Não deixe de enviar seu desafio por isso!

# O Desafio

1) Utilizando o Terraform, crie um cluster do Kubernetes em algum *cloud provider*. Você poderá utilizar uma solução gerenciada como, por exemplo, o EKS ou GKE.

2) Utilize a ferramenta de sua preferência e crie um pipeline de CI/CD para a criação da infraestrutura.
   
3) No diretório do desafio há uma aplicação. Crie os manifestos do Kubernetes e faça o deploy da aplicação no cluster. Você é livre para fazer melhorias no código, caso seja necessário.

4) De forma descritiva, proponha uma forma de monitorar o cluster e a aplicação definindo alertas importantes. Como sugestão, crie um diagrama para elucidar sua explicação.  
   
5) (Opcional) Implemente sua proposta de monitoramento.