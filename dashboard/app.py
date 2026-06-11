import sys
from pathlib import Path

import streamlit as st
import plotly.express as px

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

#IMPORTS
from src.carregar_dados import carregar_dados
from src.filtros import aplicar_filtros
from src.metricas import (
    calcular_total_internacoes,
    calcular_media_poluente,
    montar_base_analise,
    calcular_correlacao,
    gerar_ranking_municipios,
    gerar_internacoes_por_mes,
    gerar_poluentes_por_mes,
    gerar_sazonalidade_internacoes,
    calcular_estacao_predominante
)
from src.graficos import (
    grafico_internacoes_por_mes,
    grafico_poluentes_por_mes,
    grafico_dispersao_poluente_internacoes,
    grafico_ranking_municipios,
)

st.set_page_config(
    page_title=" Poluição do ar e Internações - ES",
    layout="wide"
)

base, internacoes, poluentes = carregar_dados()
anos_disponiveis = sorted(base["ano"].unique())
municipios_disponiveis = (
internacoes["municipio"].dropna().astype(str).str.strip().sort_values().unique())

#DICIONARIO
mapa_poluentes = {
    "PM25": "PM25",
    "PM10": "PM10",
    "NO2": "NO2",
    "SO2": "SO2",
    "CO": "CO",
    "O3": "O3"
}

#SIDEBAR
anos_selecionados = st.sidebar.multiselect(
    "ANO",
    anos_disponiveis,
    default=anos_disponiveis
)

municipios_selecionados = st.sidebar.multiselect(
    "MUNICÍPIO",
    municipios_disponiveis,
    placeholder="Todos os municípios"
)

poluente_label = st.sidebar.selectbox(
    "POLUENTE P/ ANÁLISE",
    list(mapa_poluentes.keys())
)

poluente_selecionado = mapa_poluentes[poluente_label]
base_filtrada, internacoes_filtrada, poluicoes_filtrada = aplicar_filtros(
    base, internacoes, poluentes, anos_selecionados, municipios_selecionados)

base_filtrada, internacoes_filtrada, poluentes_filtrada = aplicar_filtros(
    base=base,
    internacoes=internacoes,
    poluentes=poluentes,
    anos_selecionados=anos_selecionados,
    municipios_selecionados=municipios_selecionados
)

total_internacoes = calcular_total_internacoes(internacoes_filtrada)

media_pm25 = calcular_media_poluente(
    poluentes_filtrada=poluentes_filtrada,
    poluente="PM25"
)

base_analise = montar_base_analise(
    internacoes_filtrada=internacoes_filtrada,
    poluentes_filtrada=poluentes_filtrada
)

correlacao = calcular_correlacao(
    base_analise=base_analise,
    poluente=poluente_selecionado
)

#gerando as bases
ranking_municipios = gerar_ranking_municipios(internacoes_filtrada)

internacoes_por_mes = gerar_internacoes_por_mes(internacoes_filtrada)

poluentes_por_mes = gerar_poluentes_por_mes(poluentes_filtrada)

sazonalidade_internacoes = gerar_sazonalidade_internacoes(internacoes_filtrada)

#sazonalidade_estacao = gerar_sazonalidade_por_estacao(internacoes_filtrada)

estacao_predominante = calcular_estacao_predominante(internacoes_filtrada)

st.title("Poluição do Ar e Internações Hospitalares - ES")

st.markdown(
    "Dashboard acadêmico de análise das internações respiratórias e dos níveis de poluentes atmosféricos "
    "no estado do Espírito Santo."
)

st.info(
    "Observação: Os poluentes representam médias mensais gerais das estações disponíveis.",
    icon=":material/info:"
)
st.divider()

st.subheader("Resumo dos indicadores")

col1, col2, col3, col4 = st.columns(4, border=True)

with col1:
    st.metric(
        label= ":material/local_hospital: Total de internações",
        value = f"{total_internacoes:,}".replace(",", "."),
    )

with col2:
    st.metric(
        label=":material/air: Média de PM2,5",
        value=media_pm25,
    )

with col3:
    valor_correlacao = correlacao if correlacao is not None else "Sem dados"

    st.metric(
        label=f":material/monitoring: Correlação {poluente_selecionado} x internações",
        value=valor_correlacao,
    )

with col4:
    st.metric(
        label="Estação predominante",
        value=estacao_predominante
    )

st.divider()

#Exibição de gráfico - Internações por mês
st.subheader("Análises gráficas")

grafico_col1, grafico_col2 = st.columns(2)

with grafico_col1:
    with st.container(border=True):
        st.markdown("#### :material/show_chart: Internações por mês")

        fig_internacoes = grafico_internacoes_por_mes(internacoes_por_mes)

        st.plotly_chart(
            fig_internacoes,
            use_container_width=True
        )

with grafico_col2:
    with st.container(border=True):
        st.markdown("#### :material/air: Poluentes por mês ug/m²")

        fig_poluentes = grafico_poluentes_por_mes(poluentes_por_mes)

        st.plotly_chart(
            fig_poluentes,
            use_container_width=True
        )


grafico_col3, grafico_col4 = st.columns(2)

with grafico_col3:
    with st.container(border=True):
        st.markdown(f"#### :material/scatter_plot: Dispersão: {poluente_selecionado} x internações")

        fig_dispersao = grafico_dispersao_poluente_internacoes(
            base_analise=base_analise,
            poluente=poluente_selecionado
        )

        st.plotly_chart(
            fig_dispersao,
            use_container_width=True
        )

with grafico_col4:
    with st.container(border=True):
        st.markdown("#### :material/bar_chart: Ranking de municípios")

        fig_ranking = grafico_ranking_municipios(
            ranking_municipios=ranking_municipios,
            top_n=10
        )

        st.plotly_chart(
            fig_ranking,
            use_container_width=True
        )

st.divider()
