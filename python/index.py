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

# Fetch from/to totals and list them
@app.route("/timeseries")
def time_series():

    intervals = prepare_intervals(60)
    print intervals
    counts = query.timeseries(dataSource = dataSource, 
    	                      granularity = "second", 
    						  intervals = intervals, 
    						  aggregations = {"count" : doubleSum("rows")}
    					     )
    json_data = json.dumps(counts)
    print json_data
    return render_template('index.html', counts=counts, json_data=json_data)

if __name__ == "__main__":
    app.run(debug=True)