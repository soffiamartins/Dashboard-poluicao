import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, datetime
import plotly.graph_objects as go


def converter_para_json_seguro(obj):
    """
    Converte valores que podem dar erro na exportação PNG,
    como Timestamp do Pandas, arrays do Numpy e valores NaN.
    """

    if isinstance(obj, pd.Timestamp):
        return obj.strftime("%Y-%m-%d")

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    if isinstance(obj, np.ndarray):
        return [converter_para_json_seguro(item) for item in obj.tolist()]

    if isinstance(obj, list):
        return [converter_para_json_seguro(item) for item in obj]

    if isinstance(obj, tuple):
        return tuple(converter_para_json_seguro(item) for item in obj)

    if isinstance(obj, dict):
        return {
            chave: converter_para_json_seguro(valor)
            for chave, valor in obj.items()
        }

    if isinstance(obj, np.integer):
        return int(obj)

    if isinstance(obj, np.floating):
        if np.isnan(obj):
            return None
        return float(obj)

    if pd.isna(obj) and not isinstance(obj, str):
        return None

    return obj


def limpar_figura_para_exportacao(fig):
    """
    Cria uma cópia da figura sem tipos problemáticos para exportação PNG.
    """

    fig_dict = fig.to_dict()
    fig_dict_limpo = converter_para_json_seguro(fig_dict)

    return go.Figure(fig_dict_limpo)


def gerar_html_grafico(fig):
    return fig.to_html(
        include_plotlyjs="cdn",
        full_html=True
    ).encode("utf-8")


def gerar_png_grafico(fig):
    fig_limpa = limpar_figura_para_exportacao(fig)

    fig_limpa.update_layout(
    width=1400,
    height=800,
    margin=dict(l=90, r=60, t=90, b=90)
)

    return fig_limpa.to_image(
    format="png",
    width=1400,
    height=800,
    scale=2
)


def botoes_exportar_grafico(fig, nome_arquivo, chave):
    st.markdown("##### Selecione o tipo de arquivo: ")

    col_png, col_html = st.columns(2)

    with col_png:
        try:
            png = gerar_png_grafico(fig)

            st.download_button(
                label="PNG",
                data=png,
                file_name=f"{nome_arquivo}.png",
                mime="image/png",
                key=f"png_{chave}",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Erro ao gerar PNG: {e}")

    with col_html:
        html = gerar_html_grafico(fig)

        st.download_button(
            label="HTML",
            data=html,
            file_name=f"{nome_arquivo}.html",
            mime="text/html",
            key=f"html_{chave}",
            use_container_width=True
        )