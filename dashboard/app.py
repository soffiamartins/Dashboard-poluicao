import sys
from pathlib import Path

import streamlit as st
import plotly.express as px

ROOT_DIR = Path(file).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

#IMPORTS
from src.carregar_dados import carregar_dados
from src.filtros import aplicar_filtros