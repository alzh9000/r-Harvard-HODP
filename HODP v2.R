source("styleguide.R")
library(tidyverse)
library(ggplot2)
library(grid)
logo <- image_read("logo.png")
df <- read_csv("HODP Data 4.csv")
df$School <- factor(df$School, levels = df$School)
viz <- ggplot(data = df, aes(x = School, y=Value, fill=Subjectivity)) + 
  geom_bar(position="dodge", stat="identity") + 
  scale_fill_manual(values = c("#78C4D4", "#FF6B61")) + 
  labs(title="Ivy League Subjectivity", x="Ivy Leagues", y="Subjectivity") +
  theme_hodp() +theme(plot.margin = unit(c(1,1,1,1), "cm"))

viz
grid::grid.raster(logo, x = 0.01, y = 0.01, just = c('left', 'bottom'), width = unit(2, 'cm'))
ggplotly(viz)
#scale_fill_manual(values=c("#760000", "#BE1E26", "#D84742", "#FF6B61", "#FF9586")) +
#scale_fill_manual(values=c("#760000", "#BE1E26", "#D84742", "#D84742", "#EE3838", "#EE3838", "#FF6B61", "#FF9586")) 
#theme(legend.position="none")

