import sys
from pathlib import Path

import streamlit as st
import plotly.express as px

ROOT_DIR = Path(file).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

#IMPORTS
from src.carregar_dados import carregar_dados
from src.filtros import aplicar_filtros
from src.metricas import calcular_total_internacoes, calcular_media_poluente, gerar_ranking_municipios , gerar_internacoes_por_mes

base, internacoes, poluentes = carregar_dados()