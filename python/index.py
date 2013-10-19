from flask import Flask, render_template
import json
import re
from pydruid.client import *

# Setup Flask
app = Flask(__name__)

# Druid Config
endpoint = 'druid/v2/?pretty'
demo_bard_url =  'http://localhost:8083'
dataSource = 'webstream'

# Boot a Druid 
query = pyDruid(demo_bard_url, endpoint)

# Display our HTML Template
@app.route("/time_series")
def time_series():
    return render_template('index.html')

# Fetch our data from Druid
def fetch_data(start_iso_date, end_iso_date):
    intervals = [start_iso_date + "/" + end_iso_date]
    counts = query.timeseries(dataSource = dataSource, 
    	                      granularity = "second", 
    						  intervals = intervals, 
    						  aggregations = {"count" : doubleSum("rows")}
    					     )				     
    json_data = json.dumps(counts)
    return json_data

# Deliver data in JSON to our chart
@app.route("/time_series_data/<start_iso_date>/<end_iso_date>")
def time_series_data(start_iso_date, end_iso_date):
    return fetch_data(start_iso_date, end_iso_date)

if __name__ == "__main__":
    app.run(debug=True)