## Entrega 2 — MVP

### Protótipo
Foi desenvolvido um dashboard em Python com Streamlit para visualização de dados sobre poluição do ar e internações hospitalares por doenças respiratórias no Espírito Santo.

O protótipo possui:
- filtros por ano e município;
- cards com total de internações e média de poluentes;
- gráfico de internações por mês;
- gráfico de poluentes por mês;
- gráfico de dispersão entre poluente e internações;
- ranking de municípios com maior número de internações.

### Análise de dados preliminar
Os dados foram tratados e organizados por ano, mês e município. Foram utilizadas bases de internações hospitalares e médias mensais de poluentes atmosféricos dos anos de 2024 e 2025.

A análise preliminar permite observar a variação das internações ao longo do tempo e comparar esses dados com os níveis mensais dos poluentes.

### Modelos ou métodos aplicados
Nesta etapa inicial, foi aplicada uma análise exploratória dos dados, com uso de agregações mensais, filtros e gráficos comparativos.

Também foi utilizado gráfico de dispersão para observar possíveis relações entre os níveis de poluentes e o número de internações. Essa análise não indica causalidade, mas ajuda a identificar padrões que podem ser aprofundados posteriormente.

### Insights iniciais
A partir do MVP, foi possível observar que:
- as internações variam ao longo dos meses;
- alguns municípios concentram maior número de internações;
- os poluentes também apresentam variações mensais;
- a comparação entre poluentes e internações pode ajudar a levantar hipóteses sobre a relação entre qualidade do ar e saúde respiratória.

### COMO EXECUTAR O PROJETO
1. Clonar o repositório
2. Acessar a pasta do projeto
3. Instalar as dependências: pip install streamlit pandas plotly matplotlib
4. Executar o dashboard
streamlit run dashboard/app.py

### INTEGRANTES:
-Enrico Schultz
-Kathelyn Farias
-Pedro Henrique da Silva
-Pedro Henrique Pontes
-Soffia Martins

