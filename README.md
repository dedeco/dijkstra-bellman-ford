# Algoritmo de Dijkstra

O Algoritmo de Dijkstra soluciona o problema do caminho mais curto num grafo dirigido ou não dirigido com arestas de peso não negativo.

Rode o script abaixo para calcular os caminhos minimos:

* Para o grafo abaixo adaptado do livro Algoritmos (Cormen) 3rd, página 480:

    ```
    python teste_cormen_djt.py
    ```
    ![Grafo adptado Comern](https://raw.githubusercontent.com/dedeco/dijkstra-bellman-ford/master/grafos-imagens/teste_cormen_djt.png)

* Rode o script abaixo para calcular os caminhos mínimos para exemplo das aulas do prof. Fernando Lobo da universidade Algarve in Portugal:

    ```
    python teste_lobo_djt.py
    ```
    ![Grafo lobo](https://raw.githubusercontent.com/dedeco/dijkstra-bellman-ford/master/grafos-imagens/teste_lobo_djt.png)

* Rode o script para calcular os caminhos mínimos para o exemplo abaixo criado por mim
    ```
    python teste_proprio_djt.py
    ```
    ![Grafo próprio](https://github.com/dedeco/dijkstra-bellman-ford/blob/master/grafos-imagens/teste_proprio_djt.png?raw=true)


# Algoritmo de Bellman-ford

O algoritmo de Bellman-Ford resolve o problema de caminhos mínimos de fonte única no caso geral no qual os pesos das arestas podem ser negativos. O algoritmo retorna um valor booleano que indica se existe ou não um ciclo de peso negativo.

Rode o script abaixo para calcular os caminhos minimos com pesos negativos:

* Para o grafo abaixo adaptado do livro Algoritmos (Cormen) 3rd, página 474:

    ```
    python teste_cormen_bford.py
    ```
    ![Grafo adptado Comern](https://raw.githubusercontent.com/dedeco/dijkstra-bellman-ford/master/grafos-imagens/teste_cormen_bford.png)


Eu desenvolvi o mesmo algoritmo em C#. Veja aqui> https://github.com/dedeco/dijkstra-bellman-ford-csharp
