library(shiny)
library(RDruid)
library(ggplot2)
 
 
url <- druid.url(host="localhost", port="8083")
datasource <- "wikipedia"
timespan <- interval(ymd(20130101), ymd(20200101))
 
 
shinyServer(function(input, output, session) {
  tsdata <- reactive({
    # update data every 3 seconds
    invalidateLater(3000, session)
    
    druid.query.timeseries(url=url, dataSource=datasource,
                            intervals = timespan,
                            aggregations = sum(metric("count")),
                            granularity = granularity(input$granularity)
    )
  })
  
  output$plot <- renderPlot({
    print(ggplot(data=tsdata(), aes_string(x="timestamp", y="count")) + geom_line())
  })
 
  output$table <- renderTable({
    df <- tsdata()
    # convert timestamps to strings for display
    df$timestamp <- as.character(df$timestamp)
    df
  })
})