#!/usr/bin/env python3
"""Generate Quarto posts for PaulChanCyber/Data-Science-Project- portfolio."""

from pathlib import Path

REPO = "https://github.com/PaulChanCyber/Data-Science-Project-"
TREE = f"{REPO}/tree/main"
# Single sidebar category for all collection projects
DS_CATEGORY = "Data Science and Analyst"

HUB_TABLE = '''
## All Projects in This Collection

| Project | Portfolio page | GitHub folder |
|---------|----------------|---------------|
| Book Analysis | [Details](../book-analysis/) | [Book analysis](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Book%20analysis) |
| Cambodia Land Price | [Details](../cambodia-land-price/) | [Land price](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Cambodia%20land%20price%20analysis%20and%20prediction) |
| Cambodia Tour Price | [Details](../cambodia-tour-price/) | [Tour price](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Cambodia%20tour%20price%20prediction) |
| Motorcycle Consumer Analysis | [Details](../cambodian-motorcycle-consumer/) | [Motorcycle analysis](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Cambodian%20motocycle%20comuser%20analysis) |
| Computer Component Prices | [Details](../computer-component-price/) | [PC components](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Computer%20component%20price%20analysis) |
| Condo Prices (Cambodia) | [Details](../condo-price-cambodia/) | [Condo sales](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Condo%20price%20analysis%20in%20Cambodia) |
| Condo Rent (Phnom Penh) | [Details](../condo-rent-phnom-penh/) | [Condo rent](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Condo%20rent%20price%20predicition%20in%20Phnom%20Penh) |
| Fridge Price Prediction | [Details](../fridge-price-prediction/) | [Fridge prediction](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Fridge%20Price%20prediction) |
| House Price (Cambodia) | [Details](../house-price-cambodia/) | [House prediction](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/House%20price%20prediction%20in%20Cambodia) |
| Job Market Analysis | [Details](../job-analysis/) | [Job Analysis](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Job%20Analysis) |
| Khmer Riel Forecasting | [Details](../khmer-riel-forecasting/) | [ARIMA & LSTM](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Khmer%20Riel%20Currency%20forcesting%20using%20arima%20and%20lstm%20with%20web%20flask%20app%20throw%20docker) |
| Laptop Price Analysis | [Details](../laptop-price-analysis/) | [Laptop analysis](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Laptop%20price%20analysis) |
| Moto Price (Streamlit) | [Details](../moto-price-streamlit/) | [Streamlit app](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Moto%20price%20prediction%20with%20streamlit%20app) |
| Movie Recommendation | [Details](../movie-recommendation/) | [Recommender](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Movie%20Recommendation) |
| Outlier Detection | [Details](../outlier-detection/) | [Outliers](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Outlier%20detection%20and%20treatment) |
| Phone Price Analysis | [Details](../phone-price-analysis/) | [Phone analysis](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Phone%20Price%20analysis) |
| Used Car Price Prediction | [Details](../used-car-price-prediction/) | [Used cars](https://github.com/PaulChanCyber/Data-Science-Project-/tree/main/Used%20Car%20Price%20Prediction) |
| Gold Price Forecasting | [Details](../gold-price-forecasting/) | [Notebook](https://github.com/PaulChanCyber/Data-Science-Project-/blob/main/Gold%20Price%20forecasting.ipynb) |
| Home Loan Analysis | [Details](../home-loan-analysis/) | [Notebook](https://github.com/PaulChanCyber/Data-Science-Project-/blob/main/Home%20Loan%20Analysis.ipynb) |
| Customer Churn Prediction | [Details](../churn-prediction/) | [PDF report](https://github.com/PaulChanCyber/Data-Science-Project-/blob/main/Churn%20Prediction_Programming%20for%20Data%20Science.pdf) |
| Logistic Regression Analysis | [Details](../logistic-analysis/) | [PDF report](https://github.com/PaulChanCyber/Data-Science-Project-/blob/main/Logistic%20Analysis.pdf) |
'''

POSTS = [
    {
        "slug": "data-science-collection",
        "dir": None,
        "title": "Data Science Projects Collection",
        "date": "2024-03-01",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "A curated collection of 20+ student term projects on scraping, prediction, and forecasting across Cambodian markets—hosted on PaulChanCyber/GitHub.",
        "overview": "This hub links the full **Data Science Projects Collection** on GitHub—a portfolio of term projects focused on data analysis, prediction, and forecasting using real scraped data from Cambodian and regional markets.",
        "problem": "Learners needed end-to-end experience moving from raw web/market data to cleaned datasets, exploratory analysis, predictive models, and—in several cases—deployable apps.",
        "approach": "Each subdirectory is a standalone project with Jupyter notebooks covering EDA, feature engineering, model training (regression, classification, time series), and visualization. Several projects extend to **Flask**, **Streamlit**, or **Docker** for interactive delivery.",
        "tech": "Python · pandas · NumPy · scikit-learn · Matplotlib · Seaborn · Jupyter · Flask · Streamlit · Docker · ARIMA · LSTM",
        "outcomes": "Covers real estate, consumer goods, labor markets, currency forecasting, recommender systems, and ML fundamentals—demonstrating breadth in **data analytics** and **applied machine learning** instruction.",
        "is_hub": True,
    },
    {
        "slug": "book-analysis",
        "dir": "Book analysis",
        "title": "Book Analysis",
        "date": "2024-03-10",
        "categories": ["Data Analytics"],
        "description": "Exploratory analysis of book sales and publishing trends from scraped market data.",
        "problem": "Understanding how title, genre, pricing, and demand signals relate in the book retail market.",
        "approach": "Data collection and cleaning, summary statistics, trend visualization, and comparative analysis across categories.",
        "tech": "Python · pandas · Matplotlib · Seaborn · Jupyter",
        "outcomes": "Actionable insights into sales patterns and category performance for retail and publishing analytics.",
    },
    {
        "slug": "cambodia-land-price",
        "dir": "Cambodia land price analysis and prediction",
        "title": "Cambodia Land Price Analysis and Prediction",
        "date": "2024-03-15",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Regression models predicting land values across Cambodian provinces using location and parcel features.",
        "problem": "Land buyers and analysts lack data-driven price benchmarks across heterogeneous districts and plot attributes.",
        "approach": "Scrape and normalize listing data, engineer location/size/amenity features, train supervised regression models, and evaluate error on hold-out sets.",
        "tech": "Python · pandas · scikit-learn · Jupyter · visualization libraries",
        "outcomes": "Predictive price estimates and EDA dashboards supporting real-estate market comparison.",
    },
    {
        "slug": "cambodia-tour-price",
        "dir": "Cambodia tour price prediction",
        "title": "Cambodia Tour Price Prediction",
        "date": "2024-03-20",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Predicts tour package pricing from historical travel-market data in Cambodia.",
        "problem": "Tour operators and travelers need fair price expectations amid seasonal demand and package variability.",
        "approach": "Historical price ingestion, feature encoding (duration, destination, season), and regression-based forecasting.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Estimated price ranges for tour products with interpretable drivers (seasonality, route, inclusions).",
    },
    {
        "slug": "cambodian-motorcycle-consumer",
        "dir": "Cambodian motocycle comuser analysis",
        "title": "Cambodian Motorcycle Consumer Analysis",
        "date": "2024-03-25",
        "categories": ["Data Analytics"],
        "description": "Consumer behavior analysis in Cambodia's motorcycle market—brands, price bands, and purchase patterns.",
        "problem": "Manufacturers and dealers need visibility into how consumers trade off price, brand, and specifications.",
        "approach": "Market data scraping, segmentation analysis, and visualization of brand share and price elasticity proxies.",
        "tech": "Python · pandas · Seaborn · Jupyter",
        "outcomes": "Segment profiles and trend charts supporting marketing and inventory decisions.",
    },
    {
        "slug": "computer-component-price",
        "dir": "Computer component price analysis",
        "title": "Computer Component Price Analysis",
        "date": "2024-04-01",
        "categories": ["Data Analytics"],
        "description": "Tracks and analyzes pricing trends for PC components (CPU, GPU, RAM, storage).",
        "problem": "Component prices fluctuate rapidly; buyers need trend awareness across SKUs and vendors.",
        "approach": "Time-series and cross-sectional analysis of scraped retailer data with outlier review and category breakdowns.",
        "tech": "Python · pandas · Matplotlib · Jupyter",
        "outcomes": "Price trend reports and category comparisons for build-planning and procurement.",
    },
    {
        "slug": "condo-price-cambodia",
        "dir": "Condo price analysis in Cambodia",
        "title": "Condo Price Analysis in Cambodia",
        "date": "2024-04-05",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Market analysis and modeling of condominium sale prices in Cambodian urban markets.",
        "problem": "Condo investors require comparable unit pricing adjusted for floor, size, district, and amenities.",
        "approach": "Listing aggregation, feature engineering for unit attributes, EDA, and predictive modeling.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "District-level price insights and model-based valuation estimates.",
    },
    {
        "slug": "condo-rent-phnom-penh",
        "dir": "Condo rent price predicition in Phnom Penh",
        "title": "Condo Rent Price Prediction in Phnom Penh",
        "date": "2024-04-10",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Predicts monthly condo rental rates in Phnom Penh from property and neighborhood features.",
        "problem": "Renters and landlords need accurate rent benchmarks in a fast-moving Phnom Penh rental market.",
        "approach": "Scrape rental listings, encode location and unit features, train regression models, validate with MAE/RMSE.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Rent estimates with sensitivity to district, size, and furnishing factors.",
    },
    {
        "slug": "fridge-price-prediction",
        "dir": "Fridge Price prediction",
        "title": "Fridge Price Prediction",
        "date": "2024-04-15",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Predicts refrigerator retail prices from brand, capacity, energy rating, and feature attributes.",
        "problem": "Appliance shoppers compare many SKUs; a model helps normalize price vs. specifications.",
        "approach": "Retail data scraping, categorical encoding, regression training, and residual analysis.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Fair-price estimates highlighting over/under-priced listings.",
    },
    {
        "slug": "house-price-cambodia",
        "dir": "House price prediction in Cambodia",
        "title": "House Price Prediction in Cambodia",
        "date": "2024-04-20",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "End-to-end house price prediction using Cambodian residential listing data.",
        "problem": "Residential buyers need defensible valuations across diverse neighborhoods and home types.",
        "approach": "Multi-feature regression with EDA on location, size, age, and listing metadata; cross-validation for generalization.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Predicted sale prices with feature importance for interpretability.",
    },
    {
        "slug": "job-analysis",
        "dir": "Job Analysis",
        "title": "Job Market Analysis",
        "date": "2024-04-25",
        "categories": ["Data Analytics"],
        "description": "Analyzes Cambodian job postings for salary trends, skill demand, and role distribution.",
        "problem": "Job seekers and educators need visibility into in-demand skills and compensation patterns.",
        "approach": "Job board scraping, text and categorical analysis, salary band aggregation, and trend visualization.",
        "tech": "Python · pandas · Matplotlib · Jupyter",
        "outcomes": "Skill-frequency rankings and salary summaries by sector and experience level.",
    },
    {
        "slug": "khmer-riel-forecasting",
        "dir": "Khmer Riel Currency forcesting using arima and lstm with web flask app throw docker",
        "title": "Khmer Riel Currency Forecasting (ARIMA & LSTM)",
        "date": "2024-05-01",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Forecasts USD/KHR exchange rates with ARIMA and LSTM, served via a Flask web app in Docker.",
        "problem": "Businesses and analysts need short-horizon FX forecasts with both statistical and deep-learning baselines.",
        "approach": "Time-series preprocessing, ARIMA and LSTM model comparison, Flask API/UI for forecasts, Dockerized deployment.",
        "tech": "Python · pandas · statsmodels · TensorFlow/Keras · Flask · Docker · Jupyter",
        "outcomes": "Comparable ARIMA vs. LSTM forecasts and a containerized app for interactive prediction.",
    },
    {
        "slug": "laptop-price-analysis",
        "dir": "Laptop price analysis",
        "title": "Laptop Price Analysis",
        "date": "2024-05-05",
        "categories": ["Data Analytics"],
        "description": "Analyzes laptop listing prices vs. CPU, RAM, storage, and brand across retailers.",
        "problem": "Consumers face opaque pricing across configurations and brands.",
        "approach": "Specification-based feature matrix, correlation analysis, clustering/segmentation, and price trend charts.",
        "tech": "Python · pandas · Seaborn · Jupyter",
        "outcomes": "Specification–price benchmarks and brand premium estimates.",
    },
    {
        "slug": "moto-price-streamlit",
        "dir": "Moto price prediction with streamlit app",
        "title": "Moto Price Prediction (Streamlit App)",
        "date": "2024-05-10",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Motorbike price prediction with an interactive Streamlit front end for live estimates.",
        "problem": "Used moto buyers need instant fair-price estimates from bike attributes.",
        "approach": "Train regression on historical listings; deploy Streamlit UI for user inputs and predicted price output.",
        "tech": "Python · scikit-learn · Streamlit · pandas · Jupyter",
        "outcomes": "Interactive app delivering on-demand price predictions for common moto configurations.",
    },
    {
        "slug": "movie-recommendation",
        "dir": "Movie Recommendation",
        "title": "Movie Recommendation System",
        "date": "2024-05-15",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Collaborative/content-based movie recommender built from ratings and metadata.",
        "problem": "Users need personalized suggestions beyond popularity lists.",
        "approach": "User–item matrix construction, similarity metrics (cosine/pearson), and top-N recommendation generation.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Personalized movie lists with explainable similarity to past preferences.",
    },
    {
        "slug": "outlier-detection",
        "dir": "Outlier detection and treatment",
        "title": "Outlier Detection and Treatment",
        "date": "2024-05-20",
        "categories": ["Data Analytics"],
        "description": "Identifies and treats outliers using statistical and ML-based detection methods.",
        "problem": "Dirty real-world datasets skew models and visualizations without robust outlier handling.",
        "approach": "IQR/Z-score rules, isolation forest, comparison of imputation vs. removal strategies.",
        "tech": "Python · pandas · scikit-learn · Matplotlib · Jupyter",
        "outcomes": "Cleaner datasets with documented outlier policy and before/after model impact.",
    },
    {
        "slug": "phone-price-analysis",
        "dir": "Phone Price analysis",
        "title": "Phone Price Analysis",
        "date": "2024-05-25",
        "categories": ["Data Analytics"],
        "description": "Smartphone price analysis across brands, specs, and release generations.",
        "problem": "Rapid SKU turnover makes fair pricing difficult for buyers and resellers.",
        "approach": "Scrape phone listings, normalize specs, analyze depreciation curves and brand premiums.",
        "tech": "Python · pandas · Seaborn · Jupyter",
        "outcomes": "Spec-adjusted price benchmarks and brand/model depreciation insights.",
    },
    {
        "slug": "used-car-price-prediction",
        "dir": "Used Car Price Prediction",
        "title": "Used Car Price Prediction",
        "date": "2024-06-01",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Predicts used vehicle prices from mileage, year, brand, and condition features.",
        "problem": "Used-car markets need transparent valuations from observable vehicle attributes.",
        "approach": "Listing scrape, feature engineering, ensemble/regression models, error analysis by segment.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Price predictions with segment-level accuracy reporting.",
    },
    {
        "slug": "gold-price-forecasting",
        "dir": None,
        "file": "Gold Price forecasting.ipynb",
        "title": "Gold Price Forecasting",
        "date": "2024-06-05",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Time-series forecasting of gold prices using historical market data.",
        "problem": "Investors and analysts track gold as a macro indicator; short-horizon forecasts aid planning.",
        "approach": "Historical price series EDA, stationarity checks, ARIMA/prophet-style modeling, forecast visualization.",
        "tech": "Python · pandas · statsmodels · Matplotlib · Jupyter",
        "outcomes": "Forecast plots with confidence intervals and model diagnostics.",
    },
    {
        "slug": "home-loan-analysis",
        "dir": None,
        "file": "Home Loan Analysis.ipynb",
        "title": "Home Loan Analysis",
        "date": "2024-06-10",
        "categories": ["Data Analytics"],
        "description": "Exploratory analysis of home loan applicants—approval factors, income, and credit patterns.",
        "problem": "Lenders and applicants benefit from understanding drivers of approval and default risk proxies.",
        "approach": "Loan dataset EDA, categorical breakdowns, correlation analysis, and logistic/regression prototypes.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Risk-factor summaries and baseline classification metrics.",
    },
    {
        "slug": "churn-prediction",
        "dir": None,
        "file": "Churn Prediction_Programming for Data Science.pdf",
        "title": "Customer Churn Prediction",
        "date": "2024-06-15",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Classification project predicting customer churn for retention campaigns.",
        "problem": "Subscription businesses lose revenue when churn is detected too late.",
        "approach": "Feature engineering on usage/billing data, logistic regression and tree models, precision/recall evaluation.",
        "tech": "Python · pandas · scikit-learn · Jupyter",
        "outcomes": "Churn risk scores prioritizing outreach to high-risk accounts.",
    },
    {
        "slug": "logistic-analysis",
        "dir": None,
        "file": "Logistic Analysis.pdf",
        "title": "Logistic Regression Analysis",
        "date": "2024-06-20",
        "categories": ["Data Analytics", "AI/ML"],
        "description": "Applied logistic regression for binary outcome modeling with interpretable coefficients.",
        "problem": "Many business questions are yes/no outcomes requiring probabilistic classifiers with explainability.",
        "approach": "Data prep, odds-ratio interpretation, ROC/AUC evaluation, and confusion-matrix review.",
        "tech": "Python · pandas · scikit-learn · statsmodels · Jupyter",
        "outcomes": "Calibrated probability estimates and coefficient-driven business narratives.",
    },
]

TEMPLATE = '''---
title: "{title}"
description: "{description}"
date: {date}
categories: [{categories}]
author: Sophal Chan
repo-url: "{repo_url}"
---

## Overview

{overview}

## Problem & Data

{problem}

## Approach

{approach}

## Technologies

{tech}

## Outcomes

{outcomes}

## Source Code

[View project on GitHub ({link_label})]({repo_url})
'''


def main():
    root = Path(__file__).resolve().parents[1] / "posts"
    for p in POSTS:
        slug = p["slug"]
        out_dir = root / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        if p.get("is_hub"):
            repo_url = REPO
            link_label = "PaulChanCyber/Data-Science-Project-"
            overview = p["overview"]
        elif p.get("dir"):
            from urllib.parse import quote
            repo_url = f"{TREE}/{quote(p['dir'])}"
            link_label = p["dir"]
            overview = p.get("overview") or (
                f"Part of the [**Data Science Projects Collection**]({REPO}) "
                f"({link_label})—{p['description']}"
            )
        else:
            from urllib.parse import quote
            repo_url = f"{REPO}/blob/main/{quote(p['file'])}"
            link_label = p["file"]
            overview = p.get("overview") or (
                f"Standalone notebook/report in the [**Data Science Projects Collection**]({REPO})—"
                f"{p['description']}"
            )

        p["categories"] = [DS_CATEGORY]
        cats = ", ".join(f'"{c}"' for c in p["categories"])
        body = TEMPLATE.format(
            title=p["title"].replace('"', '\\"'),
            description=p["description"].replace('"', '\\"'),
            date=p["date"],
            categories=cats,
            repo_url=repo_url,
            overview=overview,
            problem=p["problem"],
            approach=p["approach"],
            tech=p["tech"],
            outcomes=p["outcomes"],
            link_label=link_label,
        )
        if p.get("is_hub"):
            body = body.replace(
                "## Source Code\n\n[View project on GitHub",
                HUB_TABLE
                + "\n## Source Code\n\n[View full repository on GitHub",
                1,
            )
        (out_dir / "index.qmd").write_text(body, encoding="utf-8")
        print(f"Wrote {out_dir / 'index.qmd'}")


if __name__ == "__main__":
    main()
