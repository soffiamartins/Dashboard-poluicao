#gráfico de dispersão: usar a métrica poluente x internações;
#gráfico de barras horizontais: usar a métrica ranking de municípios.

import plotly.express as px

#gráfico de linha: usar a métrica internações por mês;
def grafico_internacoes_por_mes(internacoes_por_mes):
    """
    Cria gráfico de linha com o total de internações por mês.
    """

    fig = px.line(
        internacoes_por_mes,
        x="periodo",
        y="internacoes_total",
        markers=True,
        title="Nº internações por mês"
    )

    fig.update_layout(
        xaxis_title="Período",
        yaxis_title="Total de internações",
        title_x=0.0
    )

    return fig
