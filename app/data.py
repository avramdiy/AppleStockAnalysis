from flask import Flask, render_template_string
import pandas as pd

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

if __name__ == '__main__':
    app.run(debug=True)
