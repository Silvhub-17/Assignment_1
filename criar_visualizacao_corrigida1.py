import matplotlib.pyplot as plt
import numpy as np

categorias = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D']
valores_serie1 = [450, 300, 500, 350]  # Ex: Cor azul claro no original
valores_serie2 = [380, 220, 420, 280]  # Ex: Cor amarela no original
valores_serie3 = [250, 150, 300, 200]  # Ex: Cor roxa no original

n_categorias = len(categorias)

# Configurações do gráfico
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.25
index = np.arange(n_categorias)

# Plotar as barras agrupadas
barras1 = ax.bar(index - bar_width, valores_serie1, bar_width, label='Série 1 (ex: Controlo)', color='#ADD8E6') # Azul claro
barras2 = ax.bar(index, valores_serie2, bar_width, label='Série 2 (ex: Tratamento X)', color='#FFFFE0') # Amarelo claro
barras3 = ax.bar(index + bar_width, valores_serie3, bar_width, label='Série 3 (ex: Tratamento Y)', color='#E6E6FA') # Lavanda (Roxo claro)

# Adicionar rótulos, título e legenda
ax.set_xlabel('Categorias de Pacientes (Exemplo)')
ax.set_ylabel('Taxa de Mortalidade (por 1.000 pacientes - Exemplo)')
ax.set_title('Comparação da Taxa de Mortalidade por Grupo e Tratamento (Exemplo Corrigido)')
ax.set_xticks(index)
ax.set_xticklabels(categorias)
ax.legend(title='Legenda das Séries')

# Adicionar linhas de grelha horizontais para facilitar a leitura
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout() # Ajusta o layout para evitar sobreposições

# Guardar o gráfico
output_path = 'C:/Users/rodri/Documents/Escola/4_ANO/2º SEMESTRE/Seminário(Lau)/A1/visualizacoes_corrigidas/grafico_barras_2d_corrigido.png'
plt.savefig(output_path)

print(f"Gráfico corrigido guardado em: {output_path}")

