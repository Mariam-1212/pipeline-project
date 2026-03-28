# pipeline-project

## Team Members
- [Mariam Mazen 231000980 ]
- [Alaa Tamer 231001409]

## Project Overview
This project implements a complete Big Data pipeline using Python and Docker to analyze **2024-2025 La Liga Player Statistics**. 
The pipeline covers:
- **Ingestion**: Loading raw data.
- **Preprocessing**: Cleaning, feature transformation, dimensionality reduction, and discretization.
- **Analytics**: Extracting performance insights.
- **Visualization**: Generating statistical plots.
- **Clustering**: Grouping players using K-Means.

## Execution Flow
1. **Build the Docker Image:**
   ```bash
   docker build -t la-liga-pipeline .
