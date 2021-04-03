from DB import Database
import pandas as pd
from flask import Flask, Markup, render_template
import plotly
import plotly.graph_objects as go
import plotly.express as px
import json

# Database = Database()
# connection = Database.connect()
# cursor = connection.cursor()

app = Flask(__name__)

# sql = """
# SELECT * FROM aapl 
# ORDER BY date asc
# """
# df = pd.read_sql(sql, con=connection)
df = pd.read_csv('./data/AAPL.csv')
labels = list(df['Date'])
values = list(df['Close'])
data = df[['Date', 'Open', 'High', 'Low', 'Close']]
x = list(df['Date'])
y = df[['Open', 'High', 'Low', 'Close']].values.tolist()

app = Flask(__name__)

@app.route('/')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=150, labels=line_labels, values=line_values)

@app.route("/plotly")
def plot_plotly_global():
    fig = px.line(data, x='Date', y=['Close', 'High', 'Low', 'Open'], title='Global daily new cases')
    #fig.update_xaxes(rangeslider_visible=True)
    #fig.update_layout(autosize = true, width=1500, height=500)
    plottry = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    context = {'plot_global_time_series': plottry}
    aapldata = df.to_dict('list')
    return render_template('plotly.html', aapldata=aapldata, context=context, xjson=json.dumps(x), yjson=json.dumps(y), x=x, y=y)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)