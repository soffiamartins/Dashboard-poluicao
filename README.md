## Entrega 3 — MVP Final

### Protótipo

Foi desenvolvido um dashboard em Python com Streamlit para visualização e análise de dados sobre poluição do ar e internações hospitalares por doenças respiratórias no estado do Espírito Santo.

O protótipo permite ao usuário explorar os dados de forma interativa, aplicando filtros e visualizando indicadores, gráficos e análises comparativas entre os níveis de poluentes atmosféricos e o número de internações.

O dashboard possui:

* filtros por ano e município;
* seleção de poluente para análise;
* cards com total de internações, média de PM2,5, correlação entre poluente e internações e estação predominante;
* gráfico de internações por mês;
* gráfico de poluentes por mês;
* gráfico de dispersão entre poluente e internações;
* ranking de municípios com maior número de internações;
* análise de sazonalidade das internações respiratórias;
* funcionalidade de exportação dos gráficos em PNG e HTML.

### Análise de dados preliminar

Os dados foram tratados e organizados por ano, mês e município. Foram utilizadas bases de internações hospitalares por doenças respiratórias e médias mensais de poluentes atmosféricos dos anos de 2024 e 2025.

A análise preliminar permite observar a variação das internações ao longo do tempo, comparar esses dados com os níveis mensais dos poluentes e identificar possíveis padrões sazonais.

Também é possível analisar quais municípios concentram maior número de internações e observar a relação entre os poluentes selecionados e o total de internações por meio de gráficos de dispersão e cálculo de correlação.

### Modelos ou métodos aplicados

Nesta etapa, foi aplicada uma análise exploratória dos dados, com uso de agregações mensais, filtros interativos e gráficos comparativos.

Foram utilizados os seguintes métodos:

* soma mensal de internações;
* cálculo da média mensal dos poluentes;
* ranking de municípios por total de internações;
* cálculo de correlação entre poluentes e internações;
* gráfico de dispersão para observar possíveis relações entre poluição e internações;
* análise de sazonalidade por mês e por estação do ano.

A análise realizada não indica causalidade entre poluição do ar e internações hospitalares, mas permite identificar padrões e levantar hipóteses para estudos futuros.

### Funcionalidade de exportação

O dashboard possui funcionalidade de exportação dos gráficos, permitindo que o usuário baixe as visualizações em dois formatos:

* PNG: imagem estática para uso em relatórios, apresentações e documentação;
* HTML: versão interativa do gráfico, mantendo recursos de visualização do Plotly.

Essa funcionalidade foi adicionada para facilitar o compartilhamento dos resultados e a documentação das análises realizadas no MVP.

### Insights iniciais

A partir do MVP, foi possível observar que:

* as internações variam ao longo dos meses;
* alguns municípios concentram maior número de internações;
* os poluentes apresentam variações mensais;
* a análise de sazonalidade ajuda a identificar períodos com maior concentração de internações;
* a comparação entre poluentes e internações pode ajudar a levantar hipóteses sobre a relação entre qualidade do ar e saúde respiratória;
* os gráficos exportáveis facilitam o registro e a apresentação dos resultados obtidos no dashboard.

### Como executar o projeto

1. Clonar o repositório:

```bash
git clone <https://github.com/soffiamartins/Dashboard-poluicao.git>
```

2. Acessar a pasta do projeto:

```bash
cd Dashboard-poluicao
```

3. Instalar as dependências:

```bash
pip install streamlit pandas plotly kaleido statsmodels
```

4. Executar o dashboard:

```bash
streamlit run dashboard/app.py
```

### Integrantes

* Enrico Schultz
* Kathelyn Farias
* Pedro Henrique da Silva
* Pedro Henrique Pontes
* Soffia Martins
