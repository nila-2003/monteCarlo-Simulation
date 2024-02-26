import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import plotly.express as px

# preprocess the data
df = pd.read_csv("Test Project-Work.csv")
df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
df['Finish Date'] = pd.to_datetime(df['Finish Date'], errors='coerce')
df['Completion Time'] = pd.to_datetime(df['Completion Time'], errors='coerce', unit='ns')

def monte_carlo_simulation(df, num_simulations, num_items):
    completion_times = []
    for _ in range(num_simulations):
        sampled_df = df.sample(num_items, replace=True)
        sampled_df['Completion Time'] = np.random.uniform(
            sampled_df['Start Date'].view('int64'), 
            sampled_df['Finish Date'].view('int64'),
        )
        completion_times.append(sampled_df['Completion Time'].max())

    completion_times_datetime = pd.to_datetime(completion_times, unit='ns')
    return completion_times_datetime

app = Flask(__name__)

@app.route('/')
def index():
    teams = sorted(df['Assigned Team'].unique())
    return render_template('index.html', teams=teams)

@app.route('/monte_carlo/')
def monte_carlo():
    team = request.args.get('team')
    num_items = int(request.args.get('num_items', 10))

    if team not in df['Assigned Team'].unique():
        return "Invalid Team Selection"
    
    df_team = df[df['Assigned Team'] == team]

    completion_times = monte_carlo_simulation(df_team, 10000, num_items)

    confidence_levels = np.percentile(completion_times, [50, 70, 85])

    fig = px.histogram(completion_times, nbins=50, labels={'value': 'Completion Time'},
                       title=f'Monte Carlo Simulation - {team} - {num_items} Items',
                       template='plotly_white')
    fig.update_layout(
        shapes=[dict(type='line', yref='paper', y0=0, y1=1, x0=x, x1=x,
                     line=dict(color='red', width=2)) for x in confidence_levels],
    )
    return fig.to_html()

if __name__ == '__main__':
    app.run(debug=True)
