from DB import Database
import pandas as pd
from flask import Flask, Markup, render_template

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

app = Flask(__name__)

@app.route('/')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=150, labels=line_labels, values=line_values)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)