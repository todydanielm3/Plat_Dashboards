from dash import Dash
from dash import html, dcc
import pandas as pd
import plotly.express as px


# Criação do aplicativo Dash para o Dashboard 1
app = Dash(__name__)
app.title = 'Demonstrativo de Despesas Primeiro Quadrimestre 2023'

# Carregando os dados
df = pd.read_csv('D1.csv',sep=';',header=0)


#removendo pontos e virgulas
df['jan.-23'] = df['jan.-23'].str.replace('.','')
df['fev.-23'] = df['fev.-23'].str.replace('.','')
df['mar.-23'] = df['mar.-23'].str.replace('.','')
df['abr.-23'] = df['abr.-23'].str.replace('.','')
df['jan.-23'] = df['jan.-23'].str.replace(',','.')
df['fev.-23'] = df['fev.-23'].str.replace(',','.')
df['mar.-23'] = df['mar.-23'].str.replace(',','.')
df['abr.-23'] = df['abr.-23'].str.replace(',','.')
df['Total'] = df['Total'].str.replace('.','')
df['Total'] = df['Total'].str.replace(',','.')

#convertendo para float
df['jan.-23'] = df['jan.-23'].astype(float)
df['fev.-23'] = df['fev.-23'].astype(float)
df['mar.-23'] = df['mar.-23'].astype(float)
df['abr.-23'] = df['abr.-23'].astype(float)
df['Total'] = df['Total'].astype(float)


# Linhas de interesses
linhas_interesse = ['CUSTO COM PESSOAL','DESPESAS GERAIS','CONCESSIONÁRIAS','MATERIAL DE CONSUMO','SERVIÇOS DE TERCEIROS','INVESTIMENTOS','TOTAL DE DESPESAS']

df_interesse = df[df['DESCRIÇÃO'].isin(linhas_interesse)]


valores_jan = df_interesse['jan.-23'].tolist()
valores_fev = df_interesse['fev.-23'].tolist()
valores_mar = df_interesse['mar.-23'].tolist()
valores_abr = df_interesse['abr.-23'].tolist()
valores_total = df_interesse['Total'].tolist()

#Criando grafico de barras com os meses
figura1 = px.bar(df_interesse, x=['jan.-23','fev.-23','mar.-23','abr.-23'], y='DESCRIÇÃO', title='Despesas por categoria')
figura1.update_layout(
    xaxis_title="Meses",
    yaxis_title="Categorias",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

dashboard_style = {
    'title': 'Demonstrativo de Despesas Primeiro Quadrimestre 2023',
    'background-color': '#FFFFFF',
    'padding': '10px 10px',
    'margin': '10px 10px',
    'border-radius': '15px',
    'color': 'black'


}
app.layout = html.Div(
    style=dashboard_style,
    children=[
        html.H1('Demonstrativo de Despesas Primeiro Quadrimestre 2023',
                style={'color': 'black'}  # Texto branco
                ),

        # Adicione os componentes e gráficos desejados aqui
        # Exemplo de gráfico de barras
        dcc.Graph(
            id='bar-chart',
            figure=figura1
        ),

        # Exemplo de gráfico de rosca
        dcc.Graph(
            id='donut-chart',
            figure=px.pie(df_interesse, values='Total', names='DESCRIÇÃO', title='Despesas por categoria', hole=0.3)
        ),


        # Exemplo de gráfico de funil
        dcc.Graph(
            id='funnel-chart',
            figure=px.funnel(df_interesse, x='Total', y='DESCRIÇÃO', title='Despesas por categoria')
        )
    ]

)



if __name__ == '__main__':
    app.run_server(debug=True)

