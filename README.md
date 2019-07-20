# PythonInGIS_EagleOwl

## Context
This report summarizes the methods and outcomes of a study project which was car- ried out in the course "Python in Geographic information system (GIS)" in the summer semester 2019. The aim of the project was to come up and answer a research question with the help of a data set which was provided by the Movebank database. Movebank is a huge database which contains animal tracks of many species all over the globe.

## Data Set

The data set from the movebank database contains data from the year 2011 to 2017. Twenty one owls where tracked during that time. The resolution of the tracks differ from each individual. Some owls where for example tracked every two minutes and others every thirty. The duration and time that the owls where tracked also differ for every individual. The data set that was used during this study consists of a Comma- Separated Values (CSV) file which contains metadata about the individual owls and a shapefile which stores the tracks of the animals. The metadata contains information such as the identification number, the date of deployment and the sex of the owls.


The shapefile we used to calculate the flight distances contains 518711 entries. Each entry is a tracking point of an owl and stores the timestamp, latitude, longitude and the animal identification amongst other things.

## Research Questions and Hypothesis

During this study project we wanted to answer the following research questions:
• What is the average Eagle Owl Flight Distance per month?
• How does the flight distance change over the year?
• Does the flight distance change in the same direction for every owl?
