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

#gráfico de linhas múltiplas: usar a métrica poluentes por mês;
def grafico_poluentes_por_mes(poluentes_por_mes):
    """
    Cria gráfico de linhas múltiplas com os poluentes por mês.
    """

    colunas_poluentes = ["PM25", "PM10", "NO2", "SO2", "CO", "O3"]

    colunas_existentes = [
        coluna for coluna in colunas_poluentes
        if coluna in poluentes_por_mes.columns
    ]

    dados_grafico = poluentes_por_mes.melt(
        id_vars=["periodo", "ano", "mes"],
        value_vars=colunas_existentes,
        var_name="poluente",
        value_name="media"
    )

    fig = px.line(
        dados_grafico,
        x="periodo",
        y="media",
        color="poluente",
        markers=True,
    )

    fig.update_layout(
        xaxis_title="Período",
        yaxis_title="Média do poluente",
        legend_title="Poluente",
        title_x=0.0,
        title="",
    )

    return fig

#dispersão
def grafico_dispersao_poluente_internacoes(base_analise, poluente):
    """
    Cria gráfico de dispersão entre o poluente selecionado e as internações.
    """

    dados_grafico = base_analise.copy()

    if "ano" in dados_grafico.columns and "mes" in dados_grafico.columns:
        dados_grafico["periodo"] = (
            dados_grafico["ano"].astype(str)
            + "-"
            + dados_grafico["mes"].astype(str).str.zfill(2)
        )
    elif "periodo" in dados_grafico.columns:
        dados_grafico["periodo"] = dados_grafico["periodo"].astype(str)

    fig = px.scatter(
    base_analise,
    x=poluente,
    y="internacoes_total",
    trendline="ols",
    title="Cada ponto representa um mês",
    hover_data=["periodo", "ano", "mes"],
    render_mode="svg"
)

    fig.update_layout(
        xaxis_title=f"Média de {poluente}",
        yaxis_title="Total de internações",
        title_x=0.0
    )

    return fig

#ranking de municipios
def grafico_ranking_municipios(ranking_municipios, top_n=10):
    """
    Cria gráfico de barras horizontais com o ranking de municípios.
    """

    ranking_top = ranking_municipios.head(top_n).copy()

    ranking_top = ranking_top.sort_values(
        "internacoes_total",
        ascending=True
    )

    fig = px.bar(
        ranking_top,
        x="internacoes_total",
        y="municipio",
        orientation="h",
        text="internacoes_total",
        title=f"Top {top_n} municípios por internações"
    )

    fig.update_layout(
        xaxis_title="Total de internações",
        yaxis_title="",
        title_x=0.0
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig

def grafico_sazonalidade_internacoes(sazonalidade_internacoes):
    """
    Cria gráfico de barras mostrando a média de internações por mês do ano.
    """

    fig = px.bar(
        sazonalidade_internacoes,
        x="mes_nome",
        y="media_internacoes",
        text="media_internacoes",
        hover_data=["total_internacoes", "anos_observados"],
        title="Sazonalidade das internações respiratórias"
    )

    fig.update_layout(
        xaxis_title="Mês do ano",
        yaxis_title="Média de internações",
        title_x=0.0
    )

    fig.update_traces(
        texttemplate="%{text:.0f}",
        textposition="outside"
    )

    return fig

def grafico_sazonalidade_por_estacao(sazonalidade_estacao):
    """
    Cria gráfico de barras mostrando a média de internações por estação do ano.
    """

    fig = px.bar(
        sazonalidade_estacao,
        x="estacao",
        y="media_internacoes",
        text="media_internacoes",
        hover_data=["total_internacoes", "anos_observados"],
        title="Sazonalidade das internações por estação do ano"
    )

    fig.update_layout(
        xaxis_title="Estação do ano",
        yaxis_title="Média de internações",
        title_x=0.0
    )

    fig.update_traces(
        texttemplate="%{text:.0f}",
        textposition="outside"
    )

    return fig