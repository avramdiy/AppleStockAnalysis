from flask import Flask, render_template_string
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np

app = Flask(__name__)

DATA_PATH = r'C:\Users\Ev\Desktop\TRG Week 18\AAPL.csv'

@app.route('/')
def index():
    # Read CSV into DataFrame
    df = pd.read_csv(DATA_PATH)

    # Drop the original "Close" column
    if 'Close' in df.columns:
        df.drop(columns=['Close'], inplace=True)

    # Rename "Adj Close" to "Close"
    if 'Adj Close' in df.columns:
        df.rename(columns={'Adj Close': 'Close'}, inplace=True)

    # Convert DataFrame to HTML
    table_html = df.to_html(classes='table table-bordered table-hover', index=False)

    # HTML page
    html_page = '''
    <!doctype html>
    <html lang="en">
    <head>
        <title>AAPL CSV Viewer</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="p-4">
        <h1 class="mb-4">AAPL.csv Data</h1>
        <div class="table-responsive">
            {{ table|safe }}
        </div>
    </body>
    </html>
    '''

    return render_template_string(html_page, table=table_html)

@app.route('/1980chart')
def firstchart():
    df = pd.read_csv(DATA_PATH)

    # Prepare date column
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Date'].dt.year >= 1980) & (df['Date'].dt.year <= 1989)]

    # Create Year-Month key
    df['YearMonth'] = df['Date'].dt.to_period('M').dt.to_timestamp()

    # Group and compute monthly averages
    monthly = df.groupby('YearMonth').agg({
        'High': 'mean',
        'Low': 'mean',
        'Volume': 'mean'
    }).reset_index()

    # Log scale for volume
    monthly['LogVolume'] = monthly['Volume'].apply(lambda x: 0 if x <= 0 else np.log10(x))


    # Plotly traces
    trace_high = go.Scatter(x=monthly['YearMonth'], y=monthly['High'],
                            mode='lines', name='Avg High', line=dict(color='red'))

    trace_low = go.Scatter(x=monthly['YearMonth'], y=monthly['Low'],
                           mode='lines', name='Avg Low', line=dict(color='blue'))

    trace_volume = go.Bar(x=monthly['YearMonth'], y=monthly['LogVolume'],
                          name='Log₁₀ Avg Volume', yaxis='y2', marker=dict(color='lightgray'))

    # Layout
    layout = go.Layout(
        title='Monthly Avg High, Low, and Volume (1980-1989)',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Price (USD)'),
        yaxis2=dict(title='Log₁₀ Volume', overlaying='y', side='right'),
        legend=dict(x=0, y=1.1, orientation='h'),
        margin=dict(t=60)
    )

    fig = go.Figure(data=[trace_volume, trace_high, trace_low], layout=layout)

    chart_html = pyo.plot(fig, output_type='div')

    # Render chart page
    chart_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <title>AAPL Chart 1980s</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body class="p-4">
        <h1>Chart: AAPL Monthly Averages (1980-1989)</h1>
        <a href="/" class="btn btn-secondary mb-4">← Back to Table</a>
        {{ chart|safe }}
    </body>
    </html>
    '''

    return render_template_string(chart_template, chart=chart_html)

@app.route('/1990chart')
def secondchart():
    df = pd.read_csv(DATA_PATH)

    # Prepare date column
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Date'].dt.year >= 1990) & (df['Date'].dt.year <= 1999)]

    # Create Year-Month key
    df['YearMonth'] = df['Date'].dt.to_period('M').dt.to_timestamp()

    # Group and compute monthly averages
    monthly = df.groupby('YearMonth').agg({
        'High': 'mean',
        'Low': 'mean',
        'Volume': 'mean'
    }).reset_index()

    # Log scale for volume
    monthly['LogVolume'] = monthly['Volume'].apply(lambda x: 0 if x <= 0 else np.log10(x))


    # Plotly traces
    trace_high = go.Scatter(x=monthly['YearMonth'], y=monthly['High'],
                            mode='lines', name='Avg High', line=dict(color='red'))

    trace_low = go.Scatter(x=monthly['YearMonth'], y=monthly['Low'],
                           mode='lines', name='Avg Low', line=dict(color='blue'))

    trace_volume = go.Bar(x=monthly['YearMonth'], y=monthly['LogVolume'],
                          name='Log₁₀ Avg Volume', yaxis='y2', marker=dict(color='lightgray'))

    # Layout
    layout = go.Layout(
        title='Monthly Avg High, Low, and Volume (1990-1999)',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Price (USD)'),
        yaxis2=dict(title='Log₁₀ Volume', overlaying='y', side='right'),
        legend=dict(x=0, y=1.1, orientation='h'),
        margin=dict(t=60)
    )

    fig = go.Figure(data=[trace_volume, trace_high, trace_low], layout=layout)

    chart_html = pyo.plot(fig, output_type='div')

    # Render chart page
    chart_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <title>AAPL Chart 1990s</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body class="p-4">
        <h1>Chart: AAPL Monthly Averages (1990-1999)</h1>
        <a href="/" class="btn btn-secondary mb-4">← Back to Table</a>
        {{ chart|safe }}
    </body>
    </html>
    '''

    return render_template_string(chart_template, chart=chart_html)

@app.route('/2000chart')
def thirdchart():
    df = pd.read_csv(DATA_PATH)

    # Prepare date column
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Date'].dt.year >= 2000) & (df['Date'].dt.year <= 2022)]

    # Create Year-Month key
    df['YearMonth'] = df['Date'].dt.to_period('M').dt.to_timestamp()

    # Group and compute monthly averages
    monthly = df.groupby('YearMonth').agg({
        'High': 'mean',
        'Low': 'mean',
        'Volume': 'mean'
    }).reset_index()

    # Log scale for volume
    monthly['LogVolume'] = monthly['Volume'].apply(lambda x: 0 if x <= 0 else np.log10(x))


    # Plotly traces
    trace_high = go.Scatter(x=monthly['YearMonth'], y=monthly['High'],
                            mode='lines', name='Avg High', line=dict(color='red'))

    trace_low = go.Scatter(x=monthly['YearMonth'], y=monthly['Low'],
                           mode='lines', name='Avg Low', line=dict(color='blue'))

    trace_volume = go.Bar(x=monthly['YearMonth'], y=monthly['LogVolume'],
                          name='Log₁₀ Avg Volume', yaxis='y2', marker=dict(color='lightgray'))

    # Layout
    layout = go.Layout(
        title='Monthly Avg High, Low, and Volume (2000-2022)',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Price (USD)'),
        yaxis2=dict(title='Log₁₀ Volume', overlaying='y', side='right'),
        legend=dict(x=0, y=1.1, orientation='h'),
        margin=dict(t=60)
    )

    fig = go.Figure(data=[trace_volume, trace_high, trace_low], layout=layout)

    chart_html = pyo.plot(fig, output_type='div')

    # Render chart page
    chart_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <title>AAPL Chart 2000s</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body class="p-4">
        <h1>Chart: AAPL Monthly Averages (2000-2022)</h1>
        <a href="/" class="btn btn-secondary mb-4">← Back to Table</a>
        {{ chart|safe }}
    </body>
    </html>
    '''

    return render_template_string(chart_template, chart=chart_html)

if __name__ == '__main__':
    app.run(debug=True)