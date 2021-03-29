# Mini-projeto
1 - Para este projeto, iremos utilizar o dataset de COVID-19
   dos casos nos Estados Unidos no período de 21 de janeiro até 09 de abril de 2020 processado.
  
2 - Tarefa: implementar a função “fit_k_means(pontos, parada, max_iter)”, com K fixo e igual a 3. Retorne os centroids finais.

- pontos: conjunto de pontos 2D (casos x mortes) que serão clusterizados
- parada: valor da variação dos clusters que indicará o fim do treinamento, i.e., se distancia(centroide_antigo, centroide_novo) <= parada então termine o treiname
- max_iter: quantidade máxima de vezes que o algoritmo deve ser repetido caso "parada” não seja alcançada
- Desafio: adicionar parâmetro com a quantidade de centroides K variável

3 - O seu relatório será o notebook exportado para um arquivo HTML e deve conter:

 - Um scatter plot mostrando os centroides (com marcador x) e seus respectivos pontos (cada cluster deve estar em uma cor distinta)
 - Para cada cluster, também devem ser exibidas as distâncias médias entre os pontos e seu respectivo centroide final
 - Discorra sobre cada cluster: o que eles indicam?
 - Desafio: implementar uma visualização iterativa do processo de treinamento igual ao gif do início da aula
 - Desafio: plotar o gráfico que permite visualizar o elbow point, variando o valor de K e indicar qual o melhor valor
 - Desafio: compare os resultados obtidos pelo seu algoritmo com os da função do K-Means do sklearn
