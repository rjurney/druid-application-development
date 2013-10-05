from flask import Flask, render_template
import json
import re
from pydruid.client import *

# Setup Flask
app = Flask(__name__)

# Druid Config
endpoint = 'druid/v2/?pretty'
demo_bard_url =  'http://localhost:8083'
dataSource = 'wikipedia'
dimension = "page"
intervals = ["2013-01-01/p1y"]

query = pyDruid(demo_bard_url, endpoint)

# Fetch from/to totals and list them
@app.route("/timeseries")
def time_series():
    counts = query.timeseries(dataSource = dataSource, 
    	                      granularity = "minute", 
    						  intervals = intervals, 
    						  aggregations = {"count" : doubleSum("edits")}
    					     )
    json_data = json.dumps(counts)
    return render_template('index.html', counts=counts, json_data=json_data)

if __name__ == "__main__":
    app.run(debug=True)