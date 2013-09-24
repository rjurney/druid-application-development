druid-application-development
=============================

This project documents application development with Druid, a rockin' exploratory analytic datastore.

Setting up Druid
----------------

Download the latest Druid tarball at 

R Applications with RDruid
--------------------------

The [RDruid](https://github.com/metamx/RDruid) project is a Druid connector for R. To install RDruid, run:

    install.packages("devtools")
    library(devtools)
    install_github("RDruid", "metamx")
    
Go ahead and install ggplot2, so we can create charts:

    install.packages("ggplot2")
    
Run an example query and display it as a chart, like so:

    tsdata <- druid.query.timeseries(url=url, dataSource=datasource,
                            intervals = timespan,
                            aggregations = sum(metric("count")),
                            granularity = granularity("PT1M")
    )
    
    print(ggplot(data=tsdata, aes_string(x="timestamp", y="count")) + geom_line())

For more R examples, check out the R directory in this project and see the examples [here](https://github.com/metamx/RDruid/wiki/Examples).

Ruby Applications with Druid
----------------------------

