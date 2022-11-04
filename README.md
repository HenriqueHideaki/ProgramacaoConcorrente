## [Programação Concorrente e Assíncrona em Python](https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/)

# Conceitos

O que ocorre ao executar um código Python?



![pythoncompiler](image.png)

> Source Code(Código Fonte) é compilado, o interpretador Python transforma em Bytecode e a máquina virtual Python vai executar, na máquina virtual Python o processo será criado e a Thread será executada

Em Ciência da Computação, Concorrência é a execução de múltiplas instruções sequenciais ao mesmo tempo, sendo os dois tipos principais: 

1. Programação Paralela

2. Programação Assíncrona

   

Devemos nos atentar então para alguns pontos fundamentais como:

   1. Ordem de Execução 

   2. Recursos Compartilhados

Quanto mais recursos são compartilhados entre execuções concorrentes, mais coordenação entre as execuções será necessaria para garantir que o resultado final esteja correto, dificultando o processo, ou seja, a execução deve compartilhar o mínimo de recursos possíveis entre as instruções 