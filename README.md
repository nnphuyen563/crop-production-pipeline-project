# Crop Production Pipeline Project 🌏

The Food and Agriculture Organization of the United Nations (FAO) provides comprehensive crop statistics covering 173 products across various regions globally. <br>
For more detailed information, you can visit <a href = "https://www.fao.org/faostat/en/#data">the FAO website</a> crop statistics.

## Table of contents

- [Crop Production Pipeline Project 🌏](#crop-production-pipeline-project-)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Dataset](#dataset)
  - [Infrastructure](#infrastructure)
  - [Dashboard](#dashboard)
  - [Reproducibility](#reproducibility)
  - [Special Thanks](#special-thanks)

## Introduction

This project aims to provide comprehensive insights into global crop production statistics sourced from the Food and Agriculture Organization of the United Nations (FAO). By ingesting data from <a href = "https://data.world/agriculture/crop-production">Data World</a> and generating <a href = "https://lookerstudio.google.com/reporting/f62e4703-b18e-491c-97f5-c34551975fa4">Crop Production Dashboard</a>, the project will strive to enhance understanding and facilitate informed decision-making. <br>

This could help answer questions:
<ol>
    <li>What are the top 5 crop items produced in each continent in terms of quantity over the years?</li>
    <li>How does the proportion of crop production vary across category?</li>
    <li>What is the geographical distribution of specific crop categories across different areas?</li>
</ol>

## Dataset
The dataset in which all transformations and analysis will be developed is <a href = "https://data.world/agriculture/crop-production">Crop Production</a> published on Data World. Given that this dataset is in CSV format and largely clean. <br>

Crop Production dataset contains multiple tables:
- FAO Metadata
- Reference
  - Elements
  - Flags
  - Items
  - Units
- Production Crops (5 tables for each continent)

## Infrastructure
The following tools and technologies are used:
- Cloud - <a href = "https://cloud.google.com/?hl=en">Google Cloud Platform</a>
- Infrastructure as Code - <a href = "https://www.terraform.io/">Terraform</a>
- Containerization - <a href = "https://www.docker.com/">Docker</a>
- Orchestration - <a href = "https://www.mage.ai/">Mage</a>
- Transformation - <a href = "https://cloud.getdbt.com/">dbt</a>
- Data Lake - <a href = "https://cloud.google.com/storage?hl=en">Google Cloud Storage</a>
- Data Warehouse - <a href = "https://cloud.google.com/bigquery?hl=en">BigQuery</a>
- Data Visualization - <a href = "https://lookerstudio.google.com/">Looker Studio</a>
<img src="/images/infrastructure.jpg">
## Dashboard
List of features provided by your project.

## Reproducibility
Guidelines for contributing to your project.

## Special Thanks
Information about the license under which your project is distributed.
