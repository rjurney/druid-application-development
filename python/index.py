from flask import Flask, render_template
import json
import re
from pydruid.client import *
from utils import *

# Setup Flask
app = Flask(__name__)

# Druid Config
endpoint = 'druid/v2/?pretty'
demo_bard_url =  'http://localhost:8083'
dataSource = 'webstream'

query = pyDruid(demo_bard_url, endpoint)

def fetch_data():
    intervals = prepare_intervals(600)
    counts = query.timeseries(dataSource = dataSource, 
    	                      granularity = "second", 
    						  intervals = intervals, 
    						  aggregations = {"count" : doubleSum("rows")}
    					     )
    json_data = json.dumps(counts)
    return json_data

# Fetch from/to totals and list them
@app.route("/time_series")
def time_series():
    json_data = fetch_data()
    return render_template('index.html', json_data=json_data)

@app.route("/time_series_data")
def time_series_data():
    return fetch_data()

if __name__ == "__main__":
    app.run(debug=True)