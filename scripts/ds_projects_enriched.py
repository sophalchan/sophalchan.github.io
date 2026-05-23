# Enriched portfolio content from PaulChanCyber/Data-Science-Project- guidelines
# (Programming for Data Science — ITC / CHAN Sophal)

COMMON_PDS = """
Projects follow the **Programming for Data Science (PDS)** term-project framework at the **Institute of Technology of Cambodia (ITC)**, Department of Applied Mathematics and Statistics, under instructor **CHAN Sophal**. Typical deliverables include a written guideline alignment, exploratory analysis, modeling notebooks, evaluation metrics, and presentation slides.
"""

ENRICHED = {
    "data-science-collection": {
        "motivation": "Cambodia's digital marketplaces (Khmer24, Bookshop, job boards, FX sources) generate rich, under-analyzed data. Student teams need repeatable capstone experience: scrape → clean → model → present—using problems that mirror real analyst workflows.",
        "background": "This repository aggregates **20+ term projects** from PDS cohorts (2020–2023). Each folder is a student team's end-to-end study—often with **Project Guideline** PDFs, Jupyter notebooks, reports, and (for advanced teams) **Flask**, **Streamlit**, or **Docker** deployments.",
        "guidelines": """
**Collection-level expectations (PDS capstone):**

- Define a clear **problem statement** and measurable **objectives**
- Collect data via **web scraping** or curated CSV with documented schema
- Perform **EDA**, cleaning, outlier review, and **feature engineering**
- Train and compare **ML / statistical models** with train/validation/test discipline
- Document **evaluation metrics** (RMSE, MAE, accuracy, F1, etc.) and business interpretation
- Submit **report + slides + reproducible notebook(s)**

**Domains covered:** real estate (land, house, condo), consumer goods (phones, laptops, motos, fridges), labor markets, tourism, FX forecasting, recommenders, and ML fundamentals (outliers, logistic regression, churn).
""",
        "data": "Each sub-project maintains its own scraped or provided dataset (typically CSV in-repo). Sources commonly include **Khmer24**, retailer listings, Bookshop, job portals, and historical FX series.",
        "methodology": "Method varies by project: regression for prices, classification for churn/approval, time series (ARIMA, ETS, LSTM) for forecasting, collaborative filtering for recommendations. See individual project pages for model-specific pipelines.",
        "evaluation": "Teams report hold-out error, cross-validation where applicable, and visual diagnostics (residual plots, confusion matrices, forecast charts). Deployment projects add usability demos via web apps.",
        "outcomes": "Graduates demonstrate job-ready skills in **pandas**, **scikit-learn**, visualization, and optional app deployment—applied to Cambodian market contexts recruiters and regional employers recognize.",
    },
    "book-analysis": {
        "motivation": "Publishers and online sellers price books using format, length, language, and category signals that are not always transparent to authors or buyers. A data-driven pricing lens supports fair listing and competitive strategy.",
        "background": "**Group 2** — *Prediction of Books Price* (PDS). The study asks which structural features drive list price in Cambodian e-commerce book listings.",
        "guidelines": """
**From project guideline (*Prediction of Books Price*):**

- **Goal:** Study how book prices are defined by feature; help publishers/authors price competitively while maximizing sales and profitability
- **Objective:** Build a **high-accuracy book price prediction model** (features in → price out)
- **Pipeline:** Data collection → preprocessing → EDA → feature engineering → model selection → evaluation
- **Models specified:** Multiple linear regression, Random Forest, gradient boosting, SVR, neural network regression, Ridge, Lasso
""",
        "data": "**BookShopDataset** — scraped from Bookshop website; **2,393 books** with title, pages, format, language, publication date, publisher, author, dimensions, categories, and price (CSV, preprocessed).",
        "methodology": "Preprocessing: missing-value checks; parse length/width/height from dimensions; clean categories (spacing, brackets, sub-sections); outlier removal. Feature engineering: days since publish; bin surface area → cover size (S/M/L); height → thickness (Thin/Medium/Thick); ordinal encoding; target encoding on categories. EDA on format popularity over time (hardcover, paperback, etc.).",
        "evaluation": "Compare regression algorithms on held-out data; select model with strongest accuracy for price prediction use case.",
        "outcomes": "Interpretable drivers of book pricing and a reusable regression workflow for retail analytics capstones.",
    },
    "cambodia-land-price": {
        "motivation": "Land is a primary store of wealth in Cambodia; buyers and planners need defensible comparables across provinces where listing quality and units vary widely.",
        "background": "**Group 3 — Land Price Analysis** (ITC AMS, PDS 2022–2023, Lecturer CHAN Sophal). Five-member team capstone on Cambodian land listings.",
        "guidelines": """
**From *Final Project Guideline Land Price Analysis*:**

1. **Define problem & goal** — state the analytical problem; goal: find the **best model for land price analysis**
2. **Data collection** — web scraping from sites with land listing information
3. **EDA** — cleaning, preprocessing, visualization
4. **Modeling & analysis** — train/compare predictive models
5. **Conclusion** — summarize findings and model choice
""",
        "data": "Scraped land listings from Cambodian property websites; features include location, area, and listing attributes (see project notebooks).",
        "methodology": "Standard PDS pipeline: clean scraped text/numeric fields, visualize price distributions by region, engineer location and parcel features, fit regression models, compare errors.",
        "evaluation": "Model comparison on test split; emphasis on **best predictive model** per guideline goal.",
        "outcomes": "Regional land price insights and a documented modeling benchmark for ITC PDS assessment.",
    },
    "cambodia-tour-price": {
        "motivation": "Tourism pricing fluctuates with season, route, and inclusions—operators and travelers benefit from historical benchmarks rather than ad hoc quotes.",
        "background": "**Group 1 — Tour Price Prediction** (PDS). Aligns with collection README: predict tour package prices from Cambodian travel-market data.",
        "guidelines": """
**Typical PDS tour-pricing guideline structure:**

- Scrape or collect tour listings (duration, destination, season, price)
- Clean and encode categorical route/season features
- EDA on price vs. seasonality and package type
- Regression models with cross-validation
- Report expected price bands for sample itineraries
""",
        "data": "Historical tour listing/pricing data scraped for Cambodian tour products (see project folder notebooks).",
        "methodology": "Feature encoding for duration, destination, season; regression training; residual analysis on high-season vs. low-season segments.",
        "evaluation": "Hold-out RMSE/MAE; interpretability of season and route coefficients.",
        "outcomes": "Data-supported tour price ranges for planning and coursework demonstration.",
    },
    "cambodian-motorcycle-consumer": {
        "motivation": "Motorcycles dominate urban mobility in Cambodia; brands and dealers need evidence on how consumers trade off price, engine size, and brand loyalty.",
        "background": "Consumer behavior study in the **Cambodian motorcycle market** (PDS collection). Focus on segmentation rather than single-price prediction.",
        "guidelines": """
- Collect listing or survey-style market data on brands, specs, and prices
- Segment consumers/SKUs by price band and brand share
- Visualize market structure (bar/box plots, heatmaps)
- Summarize implications for inventory and marketing
""",
        "data": "Scraped motorcycle listing data from Cambodian classified/marketplace sources.",
        "methodology": "EDA, segmentation, brand share analysis, price distribution by specification tier.",
        "evaluation": "Descriptive and comparative metrics; segment stability across price quantiles.",
        "outcomes": "Market structure report supporting dealer positioning and PDS consumer-analytics learning outcomes.",
    },
    "computer-component-price": {
        "motivation": "PC builders face volatile component pricing (GPU, CPU, RAM). Systematic tracking clarifies fair pay-for-spec across Khmer24 listings.",
        "background": "**Group 2 — PC Component price analysis** (PDS guideline on repo).",
        "guidelines": """
**From *Project Guideline: PC Component price analysis*:**

- **Objective:** PC component **price prediction model** with strong accuracy
- **Data:** Khmer24 dataset — **11 features, 1,055 rows**
- **Steps:** Preprocessing (missing values, duplicates, outliers) → EDA (correlation, feature engineering/selection, transforms) → Models: **Multiple Linear Regression, Ridge, Lasso, Decision Tree, Random Forest** → Train/validation/test with **cross-validation**
""",
        "data": "Khmer24 scraped listings — 1,055 observations, 11 features per guideline.",
        "methodology": "Correlation plots vs. price; feature engineering and selection; compare linear, regularized, tree, and ensemble regressors.",
        "evaluation": "Cross-validated performance on validation and test splits.",
        "outcomes": "Component price benchmarks and model comparison report for DIY PC market analytics.",
    },
    "condo-price-cambodia": {
        "motivation": "Condo investment in Phnom Penh and provincial cities requires comparables adjusted for district, floor, and amenities—often buried in unstructured listings.",
        "background": "**Condo for Sale in Cambodia** — ITC AMS PDS 2022–2023 (Lecturer **CHAN Sophal**). Five-member group with formal project management sections in guideline.",
        "guidelines": """
**From *Project guideline: Condo for Sale in Cambodia*:**

- **Goal:** Analyze condo sale market—which units are most expensive and where; identify **price drivers**
- **Sections:** Objectives, scope, timeline, resources, risks/mitigation, approvals
- **Analytical flow:** EDA → modeling → conclusions aligned with condo-for-sale domain
""",
        "data": "Scraped condo sale listings across Cambodian markets (see team notebooks/reports).",
        "methodology": "Clean listing fields; visualize price by district and unit attributes; regression or tree models for sale price; geographic breakdown of premium segments.",
        "evaluation": "Model error on hold-out listings; map/visual summary of expensive districts.",
        "outcomes": "Investor-oriented view of condo price drivers and top-tier districts.",
    },
    "condo-rent-phnom-penh": {
        "motivation": "Phnom Penh's rental market moves quickly; expatriates and locals need rent benchmarks by district, size, and furnishing.",
        "background": "PDS project on **condo rent price prediction in Phnom Penh** (collection folder). Complements sale-price condo analysis with rental-specific features.",
        "guidelines": """
- Scrape rental listings (monthly rent, district, m², bedrooms, furnishing)
- Clean currency and numeric fields
- EDA: rent/m² by district
- Regression with MAE/RMSE on test set
- Optional: compare furnished vs. unfurnished premiums
""",
        "data": "Phnom Penh rental listings from marketplace scrapes (CSV in project).",
        "methodology": "Feature encoding for location and unit attributes; regression; district-level error analysis.",
        "evaluation": "MAE/RMSE on held-out rentals; interpret top features (district, size).",
        "outcomes": "Rent estimation playbook for Phnom Penh condo rentals.",
    },
    "fridge-price-prediction": {
        "motivation": "Appliance SKUs differ by capacity, energy class, and brand—shoppers need spec-adjusted fair price signals.",
        "background": "PDS **Fridge Price prediction** module in the collection—retail regression on scraped appliance listings.",
        "guidelines": """
- Collect refrigerator listings (brand, capacity, energy rating, features, price)
- Handle missing/outlier prices
- Encode categoricals; scale numerics
- Train regression; analyze residuals for over/under-priced units
""",
        "data": "Scraped fridge/appliance listings from Cambodian e-commerce or classified sites.",
        "methodology": "pandas cleaning; one-hot/ordinal encoding; scikit-learn regression; residual plots.",
        "evaluation": "Test-set RMSE; listing-level fair-price flags.",
        "outcomes": "Spec-adjusted fridge price guidance for consumers and resellers.",
    },
    "house-price-cambodia": {
        "motivation": "Residential buyers in Phnom Penh lack transparent valuation when listings mix USD/KHR formats, vague room counts, and inconsistent location tags.",
        "background": "**House Price Prediction in Phnom Penh** — detailed PDS guideline on repo with step-by-step data cleaning rules.",
        "guidelines": """
**From *Project guideLine* (House Price Prediction):**

- **Goal:** Predict house price from location, size, bedrooms, bathrooms, condition
- **Data source:** **Khmer24**
- **Steps:** (1) Data collection (2) Cleaning — strip `$`/`, validate prices, impute bedroom/bathroom `3+` as average 3 (3) **Feature engineering** — combine rooms; drop rare categories; scale; feature selection (4) **Model selection** — compare ML regressors (5) Evaluate on separate test set
""",
        "data": "Khmer24 house listings with price, location, size, bedrooms, bathrooms, condition.",
        "methodology": "Regex price cleaning; rare-category collapsing; normalization; feature selection algorithms; multiple regression candidates.",
        "evaluation": "Separate test dataset per guideline; compare model accuracy.",
        "outcomes": "Reproducible Phnom Penh house valuation pipeline documented for PDS grading.",
    },
    "job-analysis": {
        "motivation": "Students and job seekers in Cambodia need evidence on which skills and roles command higher salaries in local postings.",
        "background": "**Job Analysis Report: Salary Prediction** — ITC PDS 2022–2023. Team: SENG Lay, VANNAK Vireakyuth, YA Manon, VANN Visal, TAING Kimmeng, VINLAY Anusar. Instructor **CHAN Sophal**.",
        "guidelines": """
**From *Guideline* (Job Analysis):**

- **Introduction** to salary prediction study
- **Problem statement:** objectives, constraints, **expected deliverables**, **success criteria**
- **Data collection & preprocessing:** scrape job boards; text preprocessing; feature extraction/encoding; train/test split; imbalance handling if needed
- **EDA:** descriptive stats, visualizations
- **Modeling** for salary prediction (see full report in repo)
""",
        "data": "Scraped Cambodian job postings with role, skills, experience, and salary fields where available.",
        "methodology": "NLP-style text preprocessing on titles/descriptions; categorical encoding; regression or classification toward salary bands.",
        "evaluation": "Success criteria from guideline—prediction error or tier accuracy vs. deliverables.",
        "outcomes": "Skill-demand and salary insight report for career planning and curriculum alignment.",
    },
    "khmer-riel-forecasting": {
        "motivation": "USD/KHR exchange rate affects imports, payroll, and tuition priced in dollars—short-horizon forecasts support planning for SMEs and analysts.",
        "background": "**Khmer Riel Forecasting** — ITC PDS capstone (Instructor **CHAN Sophal**). Team: OUN Vikreth, MAO Kimlang, PEAN Chhinger, NANG Sreynich. Multi-phase: scraping → ARIMA/ETS/LSTM → **Flask + Docker** deployment.",
        "guidelines": """
**From *Project Guideline - PDS Final*:**

1. **Define objective** — team scoping meetings → **Khmer Riel Price Forecasting**
2. **Project 1 — Web scraping** — leader Oun Vikreth; team researches scrape methods and collects FX series
3. **Project 2 — Models** — Pean Chhinger: data processing; Nang Sreynich: **ARIMA**; Mao Kimlang: **ETS**; Oun Vikreth: **LSTM** + integration review
4. **Final — Deployment** — Flask apps per model; **Dockerfile**; API endpoints for forecasts
""",
        "data": "Scraped historical USD/KHR (Khmer Riel) exchange rate time series.",
        "methodology": "Time-series cleaning; ARIMA and ETS baselines; LSTM deep model; compare forecasts; containerized Flask services for each model family.",
        "evaluation": "Compare statistical vs. deep forecasts on test horizon; demo via web UI/API.",
        "outcomes": "End-to-end FX forecasting capstone with production-style deployment—strong systems + analytics story.",
    },
    "laptop-price-analysis": {
        "motivation": "Laptop SKUs multiply each year; Cambodian buyers on Khmer24 need to know fair price for a given CPU/RAM/storage configuration.",
        "background": "**Team 05 — Laptop Price Analysis** (ITC AMS, July 2023). Members: Ek Vong Panharith, Chou Vandy, Chorn Seyhak, Chea Rotha.",
        "guidelines": """
**From *Team05_project_guideline*:**

- **Objective:** Analyze laptop data, then develop an ML model predicting **laptop prices in the Cambodian market**
- **Data:** Scraped from **Khmer24**
- **Flow:** Train model on features→price relationship; use trained model for new listing predictions
""",
        "data": "Khmer24 laptop listings with CPU, RAM, storage, brand, condition, and price.",
        "methodology": "EDA on spec–price correlations; feature matrix; regression or ensemble models; optional price recommendation for sample configs.",
        "evaluation": "Hold-out error on listings; brand premium analysis.",
        "outcomes": "Cambodia-specific laptop fair-price model and team report (July 2023).",
    },
    "moto-price-streamlit": {
        "motivation": "Used motorbikes are Cambodia's most common vehicle purchase; buyers need instant fair-price estimates from year, brand, and mileage.",
        "background": "**Moto price prediction** — PDS 2022–2023. Members Ngim Panha, Lim Sunheng (ITC AMS). Instructor **CHAN Sophal**.",
        "guidelines": """
**From *Moto price prediction Guideline*:**

- Problem statement: **objectives, constraints, deliverables, success criteria**
- **Data collection & preprocessing:** scrape, clean, text preprocessing, feature extraction/encoding, train/test split
- **EDA:** descriptive statistics, visualizations
- **Modeling** + **Streamlit app** for interactive predictions (project folder name)
""",
        "data": "Scraped used moto listings; preprocessed CSV saved for modeling.",
        "methodology": "Full PDS preprocessing pipeline; regression model; **Streamlit** UI for live price quotes from user inputs.",
        "evaluation": "Success criteria from guideline; app demo for instructors/stakeholders.",
        "outcomes": "Interactive moto pricing tool—exemplar of analytics + lightweight productization.",
    },
    "movie-recommendation": {
        "motivation": "Streaming and rental platforms overwhelm users with choice; content-based recommendations improve discovery when collaborative data is sparse.",
        "background": "**Movie Recommendation System** — PDS 2020–2021, ITC Data Science (3rd year). Lecturer **Prof. Chan Sophal**. Six-member group.",
        "guidelines": """
**From *Project Guideline: Movie Recommendation System*:**

- **Approach:** **Content-based filtering**
- **Inputs:** Movie name, ratings, overview, cast/star, gross, votes, similar-user tastes
- **Steps:** (1) Scrape data (2) Preprocess (3) Build similarity (4) Recommend top-N titles (5) Evaluate relevance (6) Document system
""",
        "data": "Scraped movie metadata and rating features (see `Movie_Recommendation_System` subfolder).",
        "methodology": "Content feature vectors; cosine/pearson similarity; top-N recommendations per user profile.",
        "evaluation": "Qualitative and metric-based checks on recommendation relevance.",
        "outcomes": "Working recommender prototype and group report for PDS 2020–2021.",
    },
    "outlier-detection": {
        "motivation": "Scraped marketplace data contains typos, duplicate listings, and extreme prices that destroy regression unless treated systematically.",
        "background": "Foundational PDS lab-style project on **outlier detection and treatment**—applies across all price-prediction capstones in the collection.",
        "guidelines": """
- Identify outliers via **IQR**, **Z-score**, and **Isolation Forest**
- Compare **removal vs. imputation** strategies
- Re-fit a simple model before/after treatment
- Document policy choice for downstream teams
""",
        "data": "Sample messy numeric/categorical dataset (market-style) in project notebooks.",
        "methodology": "Rule-based and ML detectors; impact analysis on mean/variance and model coefficients.",
        "evaluation": "Before/after model metric comparison.",
        "outcomes": "Reusable outlier playbook referenced by other scraping projects in the repo.",
    },
    "phone-price-analysis": {
        "motivation": "Smartphone prices reflect brand premium, generation, and specs—buyers and resellers in Cambodia need structured comparisons across Apple, Samsung, and other leaders.",
        "background": "**Phone Price Analysis Report** — PDS with formal introduction on mobile market dynamics and competitive pricing.",
        "guidelines": """
**From *Project Guideline* (Phone Price Analysis):**

- **Introduction:** importance of understanding mobile pricing for consumers, sellers, manufacturers
- Analyze factors driving prices—focus on **leading brands** in Cambodian market
- EDA + modeling pipeline per PDS standards (see report in repo)
""",
        "data": "Scraped smartphone listings with brand, model, storage, condition, and price.",
        "methodology": "Brand-level EDA; depreciation by generation; regression or comparative pricing tables.",
        "evaluation": "Spec-adjusted price benchmarks; brand premium quantification.",
        "outcomes": "Phone market intelligence report aligned with guideline introduction.",
    },
    "used-car-price-prediction": {
        "motivation": "Used imported cars dominate Cambodian classifieds; transparent valuation from mileage, year, and brand reduces asymmetric information between buyer and seller.",
        "background": "**Used Car Price Prediction** — three-month PDS timeline in guideline PDF.",
        "guidelines": """
**From *Project guidelines* (timeline):**

- **Month 1:** Web scraping → store CSV; web research; data overview; variable selection
- **Month 2:** EDA — continuous/categorical feature distributions, target distribution
- **Month 3:** Preprocessing (outliers, encoding) → **Linear, Ridge, Lasso, Polynomial** regression + feature engineering + correlation matrix
""",
        "data": "Scraped used-car listings; CSV after month-1 scrape phase.",
        "methodology": "Structured 3-month capstone: EDA → clean → polynomial and regularized regression suite.",
        "evaluation": "Correlation analysis; compare linear and regularized models on test split.",
        "outcomes": "Documented semester arc from scrape to valuation model—strong teaching portfolio artifact.",
    },
    "gold-price-forecasting": {
        "motivation": "Gold acts as a macro hedge in emerging markets; short-term forecasts support coursework in time-series methods.",
        "background": "Standalone notebook **Gold Price forecasting.ipynb** in collection root—PDS time-series module.",
        "guidelines": """
- Load historical gold price series
- Test stationarity; difference if needed
- Fit ARIMA/ETS (or comparable) models
- Plot forecasts with confidence intervals
- Interpret limitations (macro shocks, non-stationarity)
""",
        "data": "Historical gold price time series (public market data in notebook).",
        "methodology": "Classical time-series EDA; ARIMA-style modeling; forecast visualization.",
        "evaluation": "In-sample vs. out-of-sample forecast error; residual diagnostics.",
        "outcomes": "Forecast notebook suitable for PDS time-series grading rubric.",
    },
    "home-loan-analysis": {
        "motivation": "Loan approval depends on income, credit history, and employment—applicants and analysts benefit from EDA on approval drivers.",
        "background": "**Home Loan Analysis.ipynb** — classic PDS tabular classification/regression dataset study.",
        "guidelines": """
- Import loan applicant dataset
- EDA: approval rate by income, credit grade, employment
- Correlation and chi-square style checks on categoricals
- Prototype logistic regression for approval prediction
- Summarize risk factors for lending narrative
""",
        "data": "Standard home-loan applicant tabular dataset (see notebook).",
        "methodology": "pandas EDA; visualization; baseline logistic model.",
        "evaluation": "Accuracy, precision/recall, or AUC on hold-out applicants.",
        "outcomes": "Risk-factor summary and baseline classifier for lending analytics intro.",
    },
    "churn-prediction": {
        "motivation": "Telecom and subscription businesses lose revenue when churn is detected late; early risk scoring targets retention spend.",
        "background": "**Churn Prediction — Programming for Data Science** (PDF report in repo root).",
        "guidelines": """
- Define churn label from usage/billing history
- Feature engineering on tenure, charges, contract type
- Train classifiers (logistic regression, trees)
- Optimize precision/recall for retention campaigns
- Present business recommendations in PDF report
""",
        "data": "Customer usage and billing features with churn label (per course dataset).",
        "methodology": "Classification pipeline; class imbalance handling; ROC and confusion matrix review.",
        "evaluation": "Precision/recall on high-risk segment; ROI narrative for retention.",
        "outcomes": "Formal PDS PDF report on churn modeling and intervention strategy.",
    },
    "logistic-analysis": {
        "motivation": "Many business outcomes are binary (approve/deny, buy/not buy); logistic regression remains the interpretable baseline analysts must master.",
        "background": "**Logistic Analysis.pdf** — PDS focus on odds ratios and probabilistic classification.",
        "guidelines": """
- Prepare binary target and numeric/categorical predictors
- Fit logistic regression (statsmodels or sklearn)
- Report **odds ratios** and coefficient signs
- ROC/AUC and confusion matrix
- Write interpretation for non-technical stakeholders
""",
        "data": "Course-provided or project CSV with binary outcome (see PDF).",
        "methodology": "Data prep → logistic fit → diagnostic plots → business narrative.",
        "evaluation": "AUC, calibration, confusion matrix at chosen threshold.",
        "outcomes": "Interpretable classification report emphasizing coefficient storytelling.",
    },
}
