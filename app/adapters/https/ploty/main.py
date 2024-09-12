import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go

# Datos de ejemplo
reusability_data = [{'key': 'true', 'doc_count': 200}, {'key': 'false', 'doc_count': 5}]
engine_count_avg = 9.24
payload_weight_avg = 6838.47
launch_success_data = [{'key': 'true', 'doc_count': 181}, {'key': 'false', 'doc_count': 5}]
success_rate_by_rocket = [
    {'key': 'Falcon 9', 'success_rate': 0.9025},
    {'key': 'Falcon 1', 'success_rate': 0.4},
    {'key': 'Falcon Heavy', 'success_rate': 0.6}
]
launches_per_year = [
    {'year': '2006', 'doc_count': 1}, {'year': '2007', 'doc_count': 1}, {'year': '2008', 'doc_count': 2},
    {'year': '2009', 'doc_count': 1}, {'year': '2010', 'doc_count': 2}, {'year': '2011', 'doc_count': 0},
    {'year': '2012', 'doc_count': 2}, {'year': '2013', 'doc_count': 3}, {'year': '2014', 'doc_count': 6},
    {'year': '2015', 'doc_count': 7}, {'year': '2016', 'doc_count': 9}, {'year': '2017', 'doc_count': 18},
    {'year': '2018', 'doc_count': 21}, {'year': '2019', 'doc_count': 13}, {'year': '2020', 'doc_count': 26},
    {'year': '2021', 'doc_count': 31}, {'year': '2022', 'doc_count': 62}
]
cost_comparison_by_rocket = [
    {'key': 'Falcon 9', 'average_cost': 50000000},
    {'key': 'Falcon 1', 'average_cost': 6700000},
    {'key': 'Falcon Heavy', 'average_cost': 90000000}
]

# Crear la app de Dash
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Dashboard de Lanzamientos Espaciales"),
    
    html.H2("Reusabilidad"),
    dcc.Graph(
        figure=px.pie(names=[d['key'] for d in reusability_data], values=[d['doc_count'] for d in reusability_data])
    ),
    
    html.H2("Promedio de motores por lanzamiento"),
    html.P(f"Promedio de motores: {engine_count_avg}"),
    
    html.H2("Peso promedio de la carga útil"),
    html.P(f"Peso promedio de la carga útil: {payload_weight_avg} kg"),
    
    html.H2("Tasa de éxito de los lanzamientos"),
    dcc.Graph(
        figure=px.bar(x=[d['key'] for d in launch_success_data], y=[d['doc_count'] for d in launch_success_data])
    ),
    
    html.H2("Tasa de éxito por tipo de cohete"),
    dcc.Graph(
        figure=px.bar(x=[r['key'] for r in success_rate_by_rocket], y=[r['success_rate'] for r in success_rate_by_rocket])
    ),
    
    html.H2("Lanzamientos por año"),
    dcc.Graph(
        figure=px.line(x=[l['year'] for l in launches_per_year], y=[l['doc_count'] for l in launches_per_year])
    ),
    
    html.H2("Costo promedio por tipo de cohete"),
    dcc.Graph(
        figure=px.bar(x=[r['key'] for r in cost_comparison_by_rocket], y=[r['average_cost'] for r in cost_comparison_by_rocket])
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)