import pandas as pd

def calcular_total_internacoes(internacoes_filtrada):
    """
    Calcula o total de internações considerando os filtros aplicados pelo usuário.
    """

    if internacoes_filtrada.empty:
        return 0

    return int(internacoes_filtrada["internacoes"].sum())


#calcular média de PM2,5
def calcular_media_poluente(poluentes_filtrada, poluente):
    """
    Calcula a média de um poluente selecionado.
    Exemplo de poluente: PM25, PM10, NO2, CO, O3.
    """

    if poluentes_filtrada.empty:
        return None

    if poluente not in poluentes_filtrada.columns:
        return None

    media = poluentes_filtrada[poluente].mean()

    if pd.isna(media):
        return None

    return round(media, 2)
    

#base mensal para análise
def montar_base_analise(internacoes_filtrada, poluentes_filtrada):
    """
    Base mensal que une internações e poluentes.

    A internação pode estar filtrada por município.
    Os poluentes são mensais e gerais, sem município.
    """

    internacoes_mensal = (
        internacoes_filtrada
        .groupby(["periodo", "ano", "mes"], as_index=False)["internacoes"]
        .sum()
        .rename(columns={"internacoes": "internacoes_total"})
    )

    base_analise = internacoes_mensal.merge(
        poluentes_filtrada,
        on=["periodo", "ano", "mes"],
        how="inner"
    )
    return base_analise


#calcular correlação
def calcular_correlacao(base_analise, poluente):
    """
    Calcula a correlação entre o poluente selecionado e as internações.
    """

    if base_analise.empty:
        return None

    if poluente not in base_analise.columns:
        return None

    if "internacoes_total" not in base_analise.columns:
        return None

    # Correlação precisa de pelo menos 2 registros
    if len(base_analise) < 2:
        return None

    # Se uma das colunas não varia, a correlação não é calculável
    if base_analise[poluente].nunique() <= 1:
        return None

    if base_analise["internacoes_total"].nunique() <= 1:
        return None

    correlacao = base_analise[poluente].corr(
        base_analise["internacoes_total"]
    )

    if pd.isna(correlacao):
        return None

    return round(correlacao, 2)


def gerar_ranking_municipios(internacoes_filtrada):
    """
    Gera ranking de municípios por total de internações.
    """

    if internacoes_filtrada.empty:
        return pd.DataFrame(columns=["municipio", "internacoes_total"])

    ranking = (
        internacoes_filtrada
        .groupby("municipio", as_index=False)["internacoes"]
        .sum()
        .rename(columns={"internacoes": "internacoes_total"})
        .sort_values("internacoes_total", ascending=False)
    )

    return ranking


#gerar internacoes por mês
def gerar_internacoes_por_mes(internacoes_filtrada):
    """
    Gera a série mensal de internações.
    Essa base será usada no gráfico de internações por mês.
    """

    if internacoes_filtrada.empty:
        return pd.DataFrame(columns=["periodo", "ano", "mes", "internacoes_total"])

    internacoes_por_mes = (
        internacoes_filtrada
        .groupby(["periodo", "ano", "mes"], as_index=False)["internacoes"]
        .sum()
        .rename(columns={"internacoes": "internacoes_total"})
        .sort_values("periodo")
    )

    return internacoes_por_mes


#gerar poluentes por mês
def gerar_poluentes_por_mes(poluentes_filtrada):
    """
    Gera a série mensal de poluentes.
    Essa base será usada no gráfico de poluentes por mês.
    """

    if poluentes_filtrada.empty:
        return pd.DataFrame()

    colunas_poluentes = ["PM25", "PM10", "NO2", "SO2", "CO", "O3"]

    colunas_existentes = [
        coluna for coluna in colunas_poluentes
        if coluna in poluentes_filtrada.columns
    ]
    poluentes_por_mes = (
        poluentes_filtrada
        .groupby(["periodo", "ano", "mes"], as_index=False)[colunas_existentes]
        .mean()
        .sort_values("periodo")
    )

    return poluentes_por_mes

def gerar_sazonalidade_internacoes(internacoes_filtrada):
    """
    Gera uma análise de sazonalidade das internações respiratórias.

    A lógica é:
    1. Soma as internações por ano e mês.
    2. Calcula a média de internações para cada mês do ano.
    Exemplo: média de janeiro considerando jan/2024 e jan/2025.
    """

    if internacoes_filtrada.empty:
        return pd.DataFrame(
            columns=["mes", "mes_nome", "media_internacoes", "total_internacoes", "anos_observados"]
        )

    nomes_meses = {
        1: "Jan",
        2: "Fev",
        3: "Mar",
        4: "Abr",
        5: "Mai",
        6: "Jun",
        7: "Jul",
        8: "Ago",
        9: "Set",
        10: "Out",
        11: "Nov",
        12: "Dez"
    }

    internacoes_ano_mes = (
        internacoes_filtrada
        .groupby(["ano", "mes"], as_index=False)["internacoes"]
        .sum()
    )

    sazonalidade = (
        internacoes_ano_mes
        .groupby("mes", as_index=False)
        .agg(
            media_internacoes=("internacoes", "mean"),
            total_internacoes=("internacoes", "sum"),
            anos_observados=("ano", "nunique")
        )
        .sort_values("mes")
    )

    sazonalidade["mes_nome"] = sazonalidade["mes"].map(nomes_meses)
    sazonalidade["media_internacoes"] = sazonalidade["media_internacoes"].round(2)

    return sazonalidade

def gerar_sazonalidade_por_estacao(internacoes_filtrada):
    """
    Gera análise de sazonalidade por estações do ano.

    Como os dados são mensais, as estações foram agrupadas assim:
    - Verão: Dezembro, Janeiro e Fevereiro
    - Outono: Março, Abril e Maio
    - Inverno: Junho, Julho e Agosto
    - Primavera: Setembro, Outubro e Novembro
    """

    if internacoes_filtrada.empty:
        return pd.DataFrame(
            columns=["estacao", "media_internacoes", "total_internacoes", "anos_observados"]
        )

    def identificar_estacao(mes):
        if mes in [12, 1, 2]:
            return "Verão"
        elif mes in [3, 4, 5]:
            return "Outono"
        elif mes in [6, 7, 8]:
            return "Inverno"
        elif mes in [9, 10, 11]:
            return "Primavera"

    ordem_estacoes = {
        "Verão": 1,
        "Outono": 2,
        "Inverno": 3,
        "Primavera": 4
    }

    dados = internacoes_filtrada.copy()

    dados["estacao"] = dados["mes"].apply(identificar_estacao)

    internacoes_ano_estacao = (
        dados
        .groupby(["ano", "estacao"], as_index=False)["internacoes"]
        .sum()
    )

    sazonalidade_estacao = (
        internacoes_ano_estacao
        .groupby("estacao", as_index=False)
        .agg(
            media_internacoes=("internacoes", "mean"),
            total_internacoes=("internacoes", "sum"),
            anos_observados=("ano", "nunique")
        )
    )

    sazonalidade_estacao["ordem"] = sazonalidade_estacao["estacao"].map(ordem_estacoes)

    sazonalidade_estacao = (
        sazonalidade_estacao
        .sort_values("ordem")
        .drop(columns=["ordem"])
    )

    sazonalidade_estacao["media_internacoes"] = sazonalidade_estacao["media_internacoes"].round(2)

    return sazonalidade_estacao

def calcular_estacao_predominante(internacoes_filtrada):
    """
    Identifica a estação do ano com maior número de internações
    considerando os filtros aplicados no dashboard.
    """

    if internacoes_filtrada.empty:
        return "Sem dados"

    def identificar_estacao(mes):
        if mes in [12, 1, 2]:
            return "Verão"
        elif mes in [3, 4, 5]:
            return "Outono"
        elif mes in [6, 7, 8]:
            return "Inverno"
        elif mes in [9, 10, 11]:
            return "Primavera"

    dados = internacoes_filtrada.copy()

    dados["estacao"] = dados["mes"].apply(identificar_estacao)

    internacoes_por_estacao = (
        dados
        .groupby("estacao", as_index=False)["internacoes"]
        .sum()
        .sort_values("internacoes", ascending=False)
    )

    estacao_predominante = internacoes_por_estacao.iloc[0]["estacao"]

    return estacao_predominante