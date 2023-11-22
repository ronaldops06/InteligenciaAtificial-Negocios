# Inteligencia Atificial - Negocios

## Objetivo
Desenvolver soluções Utilizando Inteligência Artificial, para maximizar o resultado nos negócios de diferentes organizações.

## Conceitos
### Equação de Bellman
- Estado (s): Onde o agente se encontra no tempo atual;
- Ação(a): Ação que o agente irá executar;
- Recompensa (R): Retorno obtido pelo agente após executar tal ação;
- Gamma(γ): Fator de desconto.
```
V(s) = max(R(s,a) + γ * V(s'))
        a
```
#### Markov Process
Um processo estocástico possúi a propriedade Markov se a distribuição de probabilidade condicional de estados futuros do processo (concional em estados passados e presentes) depende apenas do estado presente, não da sequência de eventos que o precedeu. Ou seja, descisões passadas não tem relevância.

#### Markov Decision Process (MDP)
O MDP fornece uma estrutura matemática para modelar a tomada de decisões em situações onde os resultados são parcialmente aleatórios e parcialmente sobre o controle de um tomador de decisão.

O MDP pode ser adicionado na equação de Bellman, conforma a seguir:
- Probabilidade (P): Probabilidade de o agente executar determinada ação.
```
V(s) = max(R(s,a) + γ * Sum(P(s,a,s') * V(s')))
        a
```

### Living Panalty
Consiste na penalidade aplicada ao agente por se manter no ambiente sem resolver o problema. Quanto mais o agente se manter no ambiente sem resolver o problema, mas pontos ele perde, isso força com que ele busque resolver o problema.

É necessário tomar cuidado para não incluir uma penalidade muito alta em situações onde há outras situações que descontam pontuação, em um jogo com um precipício, que o jogador perde ao cair, pois se a *living penalty* for maior do que a penalidade por cair no precipício a tendência é que ele caia, pois para ele será mais vantajoso.

### Q-Learning
- Qualidade (Q): Qualidade de cada ação.

```
Q(s,a) = R(s,a) + γ * Sum(P(s,a,s') * max(Q(s',a'))
                                       a'
```

### Diferença Temporal
- Taxa de Aprendizado(α)
- Tempo (t)

```
Qt(s,a) = Qt-1(s,a) + α(R(s,a) + γ(max(Q(s',a')) - Qt-1(s,a))
```

### ε-greedy (ε-gulosa)
Se refere a inclusão de uma probabilidade do agente escolher uma ação aleatória, que não necessáriamente seja a melhor, mas que permitirá a ele explorar novos caminhos.
Isso evita que o agente encontre um caminho e nunca mais procure por novos caminhos.
Será representado por *épsilon* no código.

## Projetos

### Otimizar processos de negócios

Com base no estudo de caso de fluxos em um armazém de comércio eletrônico, foi desenvolvido uma IA para otimização de coleta de produtos na expedição, usando o algoritmo Q-Learning, da área da Aprendizagem por Reforço.

### Minimizar custos

Para este caso, foi construído uma IA com o objetivo de minimizar os custos no consumo de energia de um data center em mais de 50%. Neste estudo de caso foi utilizado o algoritmo Deep Q-Learning, unindo as área de Aprendizagem por Reforço e Deep Learning.

### Maximizar receitas

Neste estudo de caso foi construído uma IA com o objetivo de maximizar a receita de um negócio de varejo on-line, fazendo com que ele tenha mais de 100% de retorno se comparada com uma estratégia que não usa inteligência artificial. Neste projeto, foi utilizado o algoritmo Thompson Sampling também da área da Aprendizagem por Reforço.
