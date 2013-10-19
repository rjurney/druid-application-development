druid-application-development
=============================

This project documents application development with Druid, a rockin' exploratory analytic datastore.

Setting up Druid
----------------

To setup Druid and its webstream example, follow the instructions [here](https://github.com/metamx/druid/wiki/Tutorial:-Webstream).

R Applications with RDruid
--------------------------

The [RDruid](https://github.com/metamx/RDruid) project is a Druid connector for R. To install RDruid, run:

    install.packages("devtools")
    library(devtools)
    install_github("RDruid", "metamx")
    library(RDruid)
    
Go ahead and install ggplot2, so we can create charts:

    install.packages("ggplot2")
    library(ggplot2)
    
Run an example query and display it as a chart, like so:

    url <- druid.url(host="localhost", port="8083")
    datasource <- "webstream"
    timespan <- interval(ymd(20130101), ymd(20200101))

    tsdata <- druid.query.timeseries(url=url, 
                            dataSource=datasource,
                            intervals = timespan,
                            aggregations = sum(metric("rows")),
                            granularity = granularity("PT1S")
    )
    
    print(ggplot(data=tsdata, aes_string(x="timestamp", y="rows")) + geom_line())

For more R examples, check out the R directory in this project and see the examples [here](https://github.com/metamx/RDruid/wiki/Examples).

Python Applications with pyDruid
--------------------------------

pyDruid provides a python interface to the Druid analytic store. Typical usage often looks like this:

    #!/usr/bin/env python

    from pydruid.client import *

    # Druid Config
    endpoint = 'druid/v2/?pretty'
    demo_bard_url =  'http://localhost:8083'
    dataSource = 'webstream'
    intervals = ["2013-01-01/p1y"]

    query = pyDruid(demo_bard_url, endpoint)

    counts = query.timeseries(dataSource = dataSource, 
    	          granularity = "minute", 
    			  intervals = intervals, 
    			  aggregations = {"count" : doubleSum("rows")}
    		      )

    print counts
    [{'timestamp': '2013-09-30T23:31:00.000Z', 'result': {'count': 0.0}}, {'timestamp': '2013-09-30T23:32:00.000Z', 'result': {'count': 0.0}}, {'timestamp': '2013-09-30T23:33:00.000Z', 'result': {'count': 0.0}}, {'timestamp': '2013-09-30T23:34:00.000Z', 'result': {'count': 0.0}}]


Ruby Applications with ruby-druid
---------------------------------

The ruby-druid project is a Ruby connector for Druid, complete with a repl for querying Druid in a ruby shell. The project's source code is [here](https://github.com/madvertise/ruby-druid).

To install druid, clone the repository:

    git clone git@github.com:madvertise/ruby-druid.git

If you haven't already, install bundler:

    gem install bundler

Then install the pre-requisites:
    
    bundle install

Next you'll need to copy the file dot_driplrc_example to .dripl and edit this file to include this line:

    options :static_setup => { 'realtime/webstream' => 'http://localhost:8083/druid/v2/' }

To launch the repl, run:

    bundle exec bin/dripl

Now you can query Druid!

    long_sum(:added)[-7.days].granularity(:minute)

To query druid in raw ruby:

    bundle exec irb
    
    client = Druid::Client.new('', {:static_setup => { 'realtime/webstream' => 'http://localhost:8083/druid/v2/' }})
    query = Druid::Query.new('realtime/webstream').double_sum(:rows).granularity(:minute)
    result = client.send(query)
    puts result
    ["2013-10-03T23:29:00.000Z":{"rows"=>3124.0}, "2013-10-03T23:30:00.000Z":{"rows"=>73508.0}, "2013-10-03T23:31:00.000Z":{"rows"=>26791.0}, "2013-10-03T23:32:00.000Z":{"rows"=>29966.0}, "2013-10-03T23:33:00.000Z":{"rows"=>21450.0}]
