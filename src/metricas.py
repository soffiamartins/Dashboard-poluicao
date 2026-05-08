#gerar ranking de municípios
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
