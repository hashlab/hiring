# Software Developer (Financial Infrastructure)

Parabéns! Você acabou de começar a trabalhar numa empresa chamada "Petssenger" - basicamente, um Uber para levar seus doguíneos para o Pet Shop. Os usuários pedem um carro, embarcam seu animal e o motorista o leva em segurança até o pet shop!

Sua primeira tarefa é prototipar um novo serviço de precificação de corridas. Para isso, você terá que construir uma API REST seguindo algumas considerações.

- A formula de cálculo é para o preço é: 
`Preço Total = Tarifa Base + ((Preço Por Minuto x Tempo da Corrida) + (Preço Por Km x Distancia) x Multiplicador de Demanda) + Taxa de Serviço`

- Diferentes cidades tem diferentes valores para cálculo. Alguns exemplos:

|      City      | Tarifa Base | Preço Por Minuto | Preço por Km | Taxa de Serviço |  
|----------------|-----------|---------------|-----------|------------|
| São Paulo      |      3.50 |          1.00 |      0.50 |       0.75 |
| Salvador       |      1.50 |          0.75 |      0.20 |       1.20 |
| Curitiba       |      2.00 |          0.80 |      0.50 |        1.0 |
| Rio de Janeiro |      3.00 |          0.95 |      0.60 |       1.40 |

Por exemplo, uma corrida de 3 km em São Paulo que leve 10 minutos num momento de demanda normal (1x), você teria: 
`Preço Total = 3.50 + ((1.00 * 10) + (0.5 * 3) * 1.0) + 0.75 = 15.75`

## Requisitos
- Sua API deve lidar com múltiplas cidades e diferenciar entre usuários da plataforma
- Sua API deve oferecer uma rota para estimativa que receba  os seguintes parâmetros:
    - `User ID: String`
    - `Distancia Em Km: Float`
    - `Time Estimate In Mins: Float`
    - `City: String`

- O multiplicador de demanda de cada cidade aumenta em 0.1 com cada requisição, e diminui em 0.1 depois de 5 minutos da requisição.
- Você pode criar seu projeto usando a linguagem que desejar, não temos restrição de linguagem específica.
- O seu projeto deve ser Dockerizado e conter instruções para utilização.

## Avaliação
Envie o resultado do seu desafio para [dev@hash.com.br](mailto:dev@hash.com.br) (ele pode ser open source!). 

Iremos avaliar o seu teste conforme as especificações acima (se ele funciona de forma efetiva e eficiente), sua organização de código e o seu conhecimento de como testar sua aplicação (não é necessário ter 100% de cobertura de testes).
A próxima etapa será uma entrevista onde avaliaremos com você o seu teste, conversaremos sobre suas decisões de projeto e de como ele pode expandir. 

