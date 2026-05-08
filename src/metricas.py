#gerar ranking de municípios
#calcular total de internações - internacoes_filtradas(municipio), base_filtrada(total de internacoes)
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
#gerar
