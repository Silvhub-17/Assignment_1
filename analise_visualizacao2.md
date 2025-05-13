# Análise da Segunda Visualização: Gráfico de Setores 3D Problemático

**Fonte Original (conforme imagem no artigo):** Python Graph Gallery (implícito, dado o link sob a imagem no artigo do Medium)
**Artigo Intermediário (onde a imagem foi encontrada e criticada):** Medium, "Os erros mais comuns no design de dashboards | Parte 1" por Fernando Pinho
**Link do Artigo Intermediário:** https://medium.com/@fernando_pinho/os-erros-mais-comuns-no-design-de-dashboards-parte-1-6ad5e21ac2ef
**Link Sugerido sob a Imagem no Artigo:** https://www.python-graph-gallery.com/3d/ (leva a uma galeria de gráficos 3D, não à imagem específica, mas indica a origem provável do estilo)
**Imagem Original:** /home/ubuntu/visualizacoes_originais/grafico_setores_3d_incorreto.webp
**Contexto:** A imagem é apresentada no artigo do Medium como um exemplo de "Escolhendo visuais inadequados", especificamente um gráfico de setores (pizza) 3D que mostra a proporção de vendas por região (Norte 35%, Sul 30%, Este 20%, Oeste 15%). O autor do artigo critica o uso de 3D, mencionando a distorção que o ângulo escolhido gera.

## Falhas Identificadas

### Falha 1: Distorção Perspética de Ângulos e Áreas das Fatias

*   **Nome da Falha:** Deformação Proporcional por Perspetiva 3D.
*   **Explicação das Implicações e Más Interpretações:** O efeito tridimensional aplicado ao gráfico de setores distorce severamente a perceção visual dos ângulos centrais e das áreas relativas de cada fatia. Fatias posicionadas na parte frontal do gráfico (mais próximas do observador) tendem a parecer desproporcionalmente maiores do que as fatias posicionadas na parte traseira, mesmo que estas últimas representem percentagens iguais ou até superiores. No exemplo, a fatia "Sul" (30%) e "Norte" (35%), devido à sua posição e ao ângulo de inclinação, podem ter as suas áreas visuais percebidas de forma imprecisa em comparação com "Este" (20%) e "Oeste" (15%). Isto dificulta a tarefa fundamental de um gráfico de setores: comparar com precisão as partes de um todo.
*   **Melhorias Propostas:** A solução mais direta e eficaz é a conversão do gráfico para uma representação 2D. Um gráfico de setores 2D padrão elimina a distorção da perspetiva, permitindo que os ângulos e as áreas das fatias sejam diretamente proporcionais aos valores que representam. Os rótulos com as percentagens devem ser mantidos e posicionados claramente dentro ou adjacentes a cada fatia.

### Falha 2: Dificuldade na Comparação Precisa de Segmentos (Especialmente Não Adjacentes)

*   **Nome da Falha:** Comparabilidade Reduzida entre Segmentos.
*   **Explicação das Implicações e Más Interpretações:** Humanos têm dificuldade em comparar com precisão ângulos e áreas, mesmo em gráficos de setores 2D, especialmente quando as fatias não são adjacentes ou quando as diferenças percentuais são subtis. O efeito 3D exacerba este problema, pois a inclinação e a perspetiva alteram a forma aparente de cada fatia. Comparar, por exemplo, a fatia "Oeste" (15%) com a "Este" (20%) torna-se um exercício de adivinhação visual em vez de uma leitura direta, devido à deformação. A legenda posicionada abaixo também exige que o observador mapeie cores para fatias e depois tente comparar as fatias distorcidas, adicionando carga cognitiva.
*   **Melhorias Propostas:** Para além de converter para 2D, se a comparação precisa entre as magnitudes das categorias for o objetivo principal (em vez de apenas mostrar a composição do todo), um gráfico de barras 2D simples seria uma alternativa superior. As barras permitiriam uma comparação direta e fácil dos comprimentos, que são mais fáceis de julgar visualmente do que ângulos/áreas. Se um gráfico de setores 2D for mantido, ordenar as fatias por tamanho (do maior para o menor, no sentido horário) pode ajudar ligeiramente na comparabilidade, e os rótulos de dados diretamente nas fatias são essenciais.

### Falha 3: Uso Desnecessário de Cores Escuras e Legenda Separada Aumentando a Carga Cognitiva

*   **Nome da Falha:** Sobrecarga Visual por Estética e Legenda Ineficiente.
*   **Explicação das Implicações e Más Interpretações:** As cores escuras e com gradientes subtis (devido ao efeito 3D) podem não oferecer o melhor contraste, especialmente se o gráfico for reproduzido em diferentes meios. Mais importante, a legenda está separada do gráfico, forçando o observador a um constante vaivém visual entre as fatias coloridas e as etiquetas da legenda para identificar cada região. Este processo aumenta a carga cognitiva e o tempo necessário para interpretar o gráfico. Embora as percentagens estejam rotuladas diretamente nas fatias (o que é bom), a identificação da região a que cada percentagem pertence ainda depende da legenda ou da memorização das cores.
*   **Melhorias Propostas:** Num gráfico de setores 2D, utilizar cores sólidas, distintas e com bom contraste. Idealmente, os rótulos das categorias (Norte, Sul, Este, Oeste) deveriam ser colocados diretamente adjacentes ou dentro das suas respetivas fatias, juntamente com as percentagens. Isto eliminaria a necessidade de uma legenda separada, tornando o gráfico autoexplicativo e reduzindo a carga cognitiva. Se os rótulos diretos tornarem o gráfico muito congestionado (o que não parece ser o caso aqui com apenas quatro categorias), linhas de chamada (callout lines) podem ser usadas para conectar os rótulos às fatias de forma clara.

