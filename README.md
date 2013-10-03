druid-application-development
=============================

This project documents application development with Druid, a rockin' exploratory analytic datastore.

Setting up Druid
----------------

To setup Druid and its wikipedia example, follow the instructions [here](https://github.com/metamx/druid/wiki/Tutorial%3A-A-First-Look-at-Druid).

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

    tsdata <- druid.query.timeseries(url=url, dataSource=datasource,
                            intervals = timespan,
                            aggregations = sum(metric("count")),
                            granularity = granularity("PT1M")
    )
    
    print(ggplot(data=tsdata, aes_string(x="timestamp", y="count")) + geom_line())

For more R examples, check out the R directory in this project and see the examples [here](https://github.com/metamx/RDruid/wiki/Examples).

Python Applications with pyDruid
--------------------------------

pyDruid provides a python interface to the Druid analytic store. Typical usage often looks like this:

    #!/usr/bin/env python

    from pydruid.client import *

    # Druid Config
    endpoint = 'druid/v2/?pretty'
    demo_bard_url =  'http://localhost:8083'
    dataSource = 'wikipedia'
    intervals = ["2013-01-01/p1y"]

    query = pyDruid(demo_bard_url, endpoint)

    counts = query.timeseries(dataSource = dataSource, 
    	          granularity = "minute", 
    			  intervals = intervals, 
    			  aggregations = {"count" : doubleSum("edits")}
    		      )

    print counts
    [{'timestamp': '2013-09-30T23:31:00.000Z', 'result': {'count': 0.0}}, {'timestamp': '2013-09-30T23:32:00.000Z', 'result': {'count': 0.0}}, {'timestamp': '2013-09-30T23:33:00.000Z', 'result': {'count': 0.0}}, {'timestamp': '2013-09-30T23:34:00.000Z', 'result': {'count': 0.0}}]


Ruby Applications with ruby-druid
---------------------------------

The ruby-druid project is a Ruby connector for Druid, complete with a repl for querying Druid in a ruby shell. The project's source code is [here](https://github.com/madvertise/ruby-druid) and its gem page is [here](http://rubygems.org/gems/druid).

To install druid, clone the repository:

    git clone git@github.com:madvertise/ruby-druid.git

If you haven't already, install bundler:

    gem install bundler

Then install the pre-requisites:
    
    bundle install

Next you'll need to copy the file dot_driplrc_example to .dripl and edit this file to include this line:

    options :static_setup => { 'realtime/wikipedia' => 'http://localhost:8083/druid/v2/' }

To launch the repl, run:

    bundle exec bin/dripl

Now you can query Druid!

    long_sum(:added)[-7.days].granularity(:minute)
