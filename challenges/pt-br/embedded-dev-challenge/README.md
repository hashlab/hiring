# Hash - Exercício Desenvolvedor C Linux

Antes de começar, leia os nossos [key values](https://www.keyvalues.com/hash) para entender um pouco sobre o que nós priorizamos no desenvolvimento e faça o seu melhor, pois iremos avaliar o teste como se fosse seu melhor esforço ;)

O teste consiste no desenvolvimento de uma biblioteca C para trabalhar com objetos BER-TLV. A biblioteca deve ser capaz de interpretar objetos BER-TLV existentes em memória, e deve permitir que sua estrutura seja facilmente impressa na tela por um programa de usuário.

Exemplo:

Um programa possui em memória o seguinte objeto TLV:

```c
uint8_t tlvObject[] = {0xE1, 0x0B, 0xC1, 0x03, 0x01, 0x02,
                       0x03, 0xC2, 0x00, 0xC3, 0x02, 0xAA,
                       0xBB};
```

A biblioteca deve possibilitar a este programa escrever o seguinte texto na tela:

```
TAG – 0xE1 (private class, constructed)
LEN – 11 bytes

  TAG – 0xC1 (private class, primitive)
  LEN – 3 bytes
  VAL – 0x01 0x02 0x03

  TAG – 0xC2 (private class, primitive)
  LEN – 0 bytes

  TAG – 0xC3 (private class, primitive)
  LEN – 2 bytes
  VAL – 0xAA 0xBB
```

Para este exercício devem ser implementados:

1. Biblioteca que acabamos de especificar, em linguagem C;
2. Programa que utiliza a biblioteca implementada e imprima o conteúdo de um TLV na tela, tal qual o exemplo acima.

Para auxiliar no desenvolvimento, você encontra, neste repositório, trecho da especificação técnica que específica o formato de codificação de objetos BER-TLV.

## Restrições

1. Uso da linguagem C
2. Biblioteca deve ser um SO (shared object) Linux
3. Processo de build via CMake ou Makefile


## Avaliação

1. Capacidade de compreensão de um texto técnico avançado em inglês.
2. Capacidade de compreensão e implementação de uma estrutura abstrata complexa. (BER-TLV)
3. Qualidade da documentação escrita. Deve ser objetiva, e de fácil compreensão; de forma que permita a qualquer desenvolvedor ser capaz de utilizar a biblioteca implementada para lidar com objetos BER-TLV.
4. Lógica implementada. O resultado precisa funcionar e trabalhar com objetos BER-TLV.
5. Conversaremos sobre estrutura de código, lógica e decisões tomadas
6. Considere a possibilidade de evolução e trabalho em time na manutenção da biblioteca
