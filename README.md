# python-data-engineering-assessment

This project is to develop a data solution for a marketing firm. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Start](#start)
* [Summary](#summary)

## General Info

The client is an Automobile research company which is going to launch a new research. They have asked us to analyse fuel economy between different car manufacturers. 

## Technologies
Project is created with:
* Python 3.7

## Setup

Clone this repo to your desktop and run npm install to install all the dependencies.

## Start
To run this project, run the main file. This gets the data needed for the analysis.

```
$ python Main.py
```

To see where the charts and information for the 2015 vs 2023 Section of Insights.pptx, run the Analysis file

```
Analysis(15).ipynb

Analysis(23).ipynb
```

To see where the charts and information for the Overtime Section of Insights.pptx, run the Overtime file

```
Overtime.ipynb
```

## Summary
- Scrapy.py: Includes a Download class. It access zip file urls and saves them in the folder raw_data.

- ETL.py: Includes a ETL class. The class has a different ETL methods.

- Main.py: Runs the Download class and methods in the ETL class. Then, it stores all csv files as one single csv file - Dataset.csv.

- Analysis(15).ipynb: Displays the charts for each question.

- Analysis(23).ipynb: Displays the charts for eah question.

- Overtime.ipynb: Analyse overtime.

- Insights.pptx: Presentation of data insights.

