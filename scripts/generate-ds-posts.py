#!/usr/bin/env python3
"""Generate detailed Quarto posts for PaulChanCyber/Data-Science-Project-."""

from pathlib import Path
from urllib.parse import quote

from ds_projects_enriched import COMMON_PDS, ENRICHED

REPO = "https://github.com/PaulChanCyber/Data-Science-Project-"
TREE = f"{REPO}/tree/main"
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

# Metadata: slug, title, date, description, repo path
POSTS_META = [
    ("data-science-collection", "Data Science Projects Collection", "2024-03-01",
     "20+ PDS term projects—scraping, prediction, and forecasting across Cambodian markets (PaulChanCyber/GitHub).", None, None),
    ("book-analysis", "Book Analysis", "2024-03-10",
     "Book price prediction from 2,393 Bookshop listings—format, category, and feature engineering per PDS guideline.", "Book analysis", None),
    ("cambodia-land-price", "Cambodia Land Price Analysis and Prediction", "2024-03-15",
     "ITC Group 3 capstone: scrape land listings, EDA, and best-model selection for Cambodian land prices.", "Cambodia land price analysis and prediction", None),
    ("cambodia-tour-price", "Cambodia Tour Price Prediction", "2024-03-20",
     "Tour package price forecasting from historical Cambodian travel-market data.", "Cambodia tour price prediction", None),
    ("cambodian-motorcycle-consumer", "Cambodian Motorcycle Consumer Analysis", "2024-03-25",
     "Segmentation and brand/price analysis in Cambodia's motorcycle market.", "Cambodian motocycle comuser analysis", None),
    ("computer-component-price", "Computer Component Price Analysis", "2024-04-01",
     "Khmer24 PC parts (1,055 rows): Ridge, Lasso, tree, and forest models per project guideline.", "Computer component price analysis", None),
    ("condo-price-cambodia", "Condo Price Analysis in Cambodia", "2024-04-05",
     "ITC condo-for-sale study: price drivers, districts, and formal PDS project management.", "Condo price analysis in Cambodia", None),
    ("condo-rent-phnom-penh", "Condo Rent Price Prediction in Phnom Penh", "2024-04-10",
     "Monthly rent regression from Phnom Penh rental listings.", "Condo rent price predicition in Phnom Penh", None),
    ("fridge-price-prediction", "Fridge Price Prediction", "2024-04-15",
     "Appliance price regression from brand, capacity, and energy features.", "Fridge Price prediction", None),
    ("house-price-cambodia", "House Price Prediction in Cambodia", "2024-04-20",
     "Khmer24 house prices: cleaning, feature engineering, and ML valuation per step-by-step guideline.", "House price prediction in Cambodia", None),
    ("job-analysis", "Job Market Analysis", "2024-04-25",
     "Salary prediction and skill-demand analysis from Cambodian job postings (ITC PDS 2022–2023).", "Job Analysis", None),
    ("khmer-riel-forecasting", "Khmer Riel Currency Forecasting (ARIMA & LSTM)", "2024-05-01",
     "USD/KHR forecasting with ARIMA, ETS, LSTM, and Flask apps in Docker (CHAN Sophal capstone).", "Khmer Riel Currency forcesting using arima and lstm with web flask app throw docker", None),
    ("laptop-price-analysis", "Laptop Price Analysis", "2024-05-05",
     "Khmer24 laptop fair-price model—Team 05, ITC AMS (July 2023).", "Laptop price analysis", None),
    ("moto-price-streamlit", "Moto Price Prediction (Streamlit App)", "2024-05-10",
     "Used moto price regression with interactive Streamlit app (Ngim Panha, Lim Sunheng).", "Moto price prediction with streamlit app", None),
    ("movie-recommendation", "Movie Recommendation System", "2024-05-15",
     "Content-based movie recommender—PDS 2020–2021, Prof. Chan Sophal.", "Movie Recommendation", None),
    ("outlier-detection", "Outlier Detection and Treatment", "2024-05-20",
     "IQR, Z-score, and Isolation Forest methods for messy marketplace data.", "Outlier detection and treatment", None),
    ("phone-price-analysis", "Phone Price Analysis", "2024-05-25",
     "Smartphone pricing drivers and brand premiums in the Cambodian market.", "Phone Price analysis", None),
    ("used-car-price-prediction", "Used Car Price Prediction", "2024-06-01",
     "Three-month capstone: scrape → EDA → linear/Ridge/Lasso/polynomial regression.", "Used Car Price Prediction", None),
    ("gold-price-forecasting", "Gold Price Forecasting", "2024-06-05",
     "Time-series gold price forecasts with ARIMA-style models.", None, "Gold Price forecasting.ipynb"),
    ("home-loan-analysis", "Home Loan Analysis", "2024-06-10",
     "Loan approval EDA and logistic regression on applicant data.", None, "Home Loan Analysis.ipynb"),
    ("churn-prediction", "Customer Churn Prediction", "2024-06-15",
     "Churn classification for retention campaigns (PDS PDF report).", None, "Churn Prediction_Programming for Data Science.pdf"),
    ("logistic-analysis", "Logistic Regression Analysis", "2024-06-20",
     "Binary outcomes with odds ratios, ROC/AUC, and stakeholder interpretation.", None, "Logistic Analysis.pdf"),
]

TEMPLATE = '''---
title: "{title}"
description: "{description}"
date: {date}
categories: ["{category}"]
author: Sophal Chan
repo-url: "{repo_url}"
---

## Overview

{overview}

## Background & Motivation

{background}

{motivation}

## Project Guidelines & Objectives

{guidelines}

## Data Collection & Preparation

{data}

## Methodology & Analysis

{methodology}

## Model Evaluation

{evaluation}

## Results & Key Learnings

{outcomes}

## Source Code

[View project on GitHub ({link_label})]({repo_url})
'''


def repo_url_for(slug, dir_name, file_name):
    if slug == "data-science-collection":
        return REPO, "PaulChanCyber/Data-Science-Project-"
    if dir_name:
        return f"{TREE}/{quote(dir_name)}", dir_name
    return f"{REPO}/blob/main/{quote(file_name)}", file_name


def main():
    root = Path(__file__).resolve().parents[1] / "posts"
    for slug, title, date, description, dir_name, file_name in POSTS_META:
        e = ENRICHED[slug]
        url, link_label = repo_url_for(slug, dir_name, file_name)

        if slug == "data-science-collection":
            overview = (
                "This page is the **master index** for the Data Science Projects Collection on "
                f"[PaulChanCyber/GitHub]({REPO})—student **Programming for Data Science (PDS)** "
                "work at the Institute of Technology of Cambodia."
            )
        else:
            overview = (
                f"**{title}** — part of the "
                f"[Data Science Projects Collection]({REPO}). "
                f"{description}"
            )

        body = TEMPLATE.format(
            title=title.replace('"', '\\"'),
            description=description.replace('"', '\\"'),
            date=date,
            category=DS_CATEGORY,
            repo_url=url,
            overview=overview,
            background=e["background"].strip(),
            motivation=e["motivation"].strip(),
            guidelines=e["guidelines"].strip(),
            data=e["data"].strip(),
            methodology=e["methodology"].strip(),
            evaluation=e["evaluation"].strip(),
            outcomes=e["outcomes"].strip(),
            link_label=link_label,
        )

        if slug == "data-science-collection":
            pds_note = COMMON_PDS.strip() + "\n\n"
            body = body.replace(
                "## Background & Motivation\n\n" + e["background"].strip(),
                "## Background & Motivation\n\n" + pds_note + e["background"].strip(),
                1,
            )
            body = body.replace(
                "## Source Code\n\n[View project on GitHub",
                HUB_TABLE + "\n## Source Code\n\n[View full repository on GitHub",
                1,
            )

        out = root / slug / "index.qmd"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
