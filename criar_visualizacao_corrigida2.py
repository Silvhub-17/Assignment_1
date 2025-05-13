import matplotlib.pyplot as plt
import numpy as np

# Dados da visualização original
regioes = ["Norte", "Sul", "Este", "Oeste"]
percentagens = [35, 30, 20, 15]

# Cores distintas e claras (evitando as muito escuras do original 3D)
cores = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"] # Exemplo de paleta ColorBrewer

# Criar o gráfico de setores 2D
fig, ax = plt.subplots(figsize=(8, 8))

# Criar as fatias do gráfico de setores
# autopct='%1.1f%%' adiciona a percentagem diretamente na fatia
# startangle=90 inicia a primeira fatia na vertical (opcional, para estética)
# pctdistance controla a distância do centro onde as percentagens são escritas
wedges, texts, autotexts = ax.pie(percentagens,
                                 autopct=lambda p: f'{p:.0f}%',
                                 startangle=90,
                                 colors=cores,
                                 pctdistance=0.85) # Ajustar para que a percentagem fique bem dentro da fatia

# Melhorar a aparência dos textos de autopct (percentagens)
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(12)
    autotext.set_fontweight("bold")

# Construir rótulos combinados: Região \n Percentagem
rotulos_diretos = [f"{regiao}\n{p}%" for regiao, p in zip(regioes, percentagens)]

# Reajustando para colocar o nome da região e a percentagem na legenda, e só a percentagem na fatia.

ax.legend(wedges, [f"{regiao} ({p}%)" for regiao, p in zip(regioes, percentagens)],
          title="Vendas por Região",
          loc="center left",
          bbox_to_anchor=(0.95, 0, 0.5, 1), # Ajustar posição da legenda
          fontsize=10)

# Garantir que o gráfico é um círculo
ax.axis("equal")

# Adicionar título
ax.set_title("Distribuição Percentual de Vendas por Região (Corrigido)", fontsize=14, pad=20)

plt.tight_layout()

# Guardar o gráfico
output_path_pie = "C:/Users/rodri/Documents/Escola/4_ANO/2º SEMESTRE/Seminário(Lau)/A1/visualizacoes_corrigidas/grafico_setores_2d_corrigido.png"
plt.savefig(output_path_pie)

print(f"Gráfico de setores corrigido guardado em: {output_path_pie}")

