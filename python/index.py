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

def fetch_data(start_iso_date, end_iso_date):
    intervals = [start_iso_date + "/" + end_iso_date]
    counts = query.timeseries(dataSource = dataSource, 
    	                      granularity = "second", 
    						  intervals = intervals, 
    						  aggregations = {"count" : doubleSum("rows")}
    					     )				     
    json_data = json.dumps(counts)
    print json_data
    return json_data

# Fetch from/to totals and list them
@app.route("/time_series")
def time_series():
    return render_template('index.html')

@app.route("/time_series_data/<start_iso_date>/<end_iso_date>")
def time_series_data(start_iso_date, end_iso_date):
    return fetch_data(start_iso_date, end_iso_date)

if __name__ == "__main__":
    app.run(debug=True)