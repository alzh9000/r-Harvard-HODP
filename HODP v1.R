source("styleguide.R")
library(tidyverse)
library(ggplot2)
library(grid)
logo <- image_read("logo.png")
df <- read_csv("HODP Data 2.csv")
df$School <- factor(df$School, levels = df$School)
viz <- ggplot(data = df, aes(x = School, y=Subjectivity, fill=School)) + 
  geom_bar(stat="identity") + 
  labs(title="Average Harvard Subjectivities by Ivy League", x="Ivy Leagues", y="Harvard Mentions' Average Subjectivities") +
  scale_fill_manual(values=c("#760000", "#BE1E26", "#D84742", "#D84742", "#EE3838", "#EE3838", "#FF6B61", "#FF9586")) +
  theme_hodp() +theme(plot.margin = unit(c(1,1,1,1), "cm")) + theme(legend.position="none")

viz
grid::grid.raster(logo, x = 0.01, y = 0.01, just = c('left', 'bottom'), width = unit(2, 'cm'))
ggplotly(viz)
#scale_fill_manual(values=c("#760000", "#BE1E26", "#D84742", "#FF6B61", "#FF9586")) +
df

