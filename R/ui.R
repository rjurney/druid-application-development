library(shiny)
 
shinyUI(pageWithSidebar(
  
  # Application title
  headerPanel("Druid | Wikipedia"),
  
  sidebarPanel(
    selectInput(
      "granularity", "Time resolution", 
      choices = c("1 minute" = "PT1M",
                  "5 minutes" = "PT5M",
                  "15 minutes" = "PT15M"),
      selected = "PT1M"          
    )
  ),
  
  mainPanel(
    plotOutput("plot"),
    tableOutput("table")
  )
))
