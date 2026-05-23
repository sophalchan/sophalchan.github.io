# Expands concise project notes into full portfolio narratives.

from ds_projects_enriched import ENRICHED, COMMON_PDS

PDS_FOOTER = (
    "The work was completed in the **Programming for Data Science (PDS)** course at the "
    "**Institute of Technology of Cambodia (ITC)**, Department of Applied Mathematics and "
    "Statistics, under instructor **CHAN Sophal**. Deliverables typically include a "
    "**Project Guideline** alignment document, Jupyter notebooks, visualizations, a written "
    "report, and presentation slides—mirroring how data analysts are expected to document "
    "real engagements for technical and non-technical audiences."
)

DOMAIN = {
    "book-analysis": {
        "setting": "online book retail and publishing analytics",
        "stakeholders": "publishers, booksellers, and consumers comparing formats and genres",
        "why": "Book prices reflect pages, binding, language, category demand, and publication age—yet listings rarely explain which features drive a given price point.",
    },
    "cambodia-land-price": {
        "setting": "Cambodian land and property markets across provinces",
        "stakeholders": "buyers, sellers, and small investors comparing plot prices",
        "why": "Land remains a core asset class; without models, buyers rely on anecdotal comparables that ignore size, road access, and district effects.",
    },
    "cambodia-tour-price": {
        "setting": "Cambodia's domestic and inbound tourism sector",
        "stakeholders": "tour operators, travel agents, and budget-conscious travelers",
        "why": "Package prices swing with season, route popularity, and inclusions—historical data can anchor fair quotes.",
    },
    "cambodian-motorcycle-consumer": {
        "setting": "Cambodia's motorcycle retail and classified-listing ecosystem",
        "stakeholders": "dealers, manufacturers, and first-time buyers",
        "why": "Motos are essential transport; understanding brand share and price bands improves inventory and marketing decisions.",
    },
    "computer-component-price": {
        "setting": "PC DIY and component resale on Khmer24",
        "stakeholders": "students, gamers, and IT shops building custom machines",
        "why": "CPU/GPU/RAM prices are volatile; buyers need spec-adjusted benchmarks before purchasing.",
    },
    "condo-price-cambodia": {
        "setting": "urban condo sales in Phnom Penh and other Cambodian cities",
        "stakeholders": "investors, agents, and owner-occupiers",
        "why": "Condo units vary by floor, view, and district; structured analysis reveals where premiums concentrate.",
    },
    "condo-rent-phnom-penh": {
        "setting": "Phnom Penh residential rental market",
        "stakeholders": "expatriates, young professionals, and landlords",
        "why": "Monthly rents shift quickly by district and furnishing; models reduce negotiation friction.",
    },
    "fridge-price-prediction": {
        "setting": "home appliance retail in Cambodia",
        "stakeholders": "households upgrading appliances and small retailers",
        "why": "Refrigerator prices depend on capacity, brand, and energy class—features that are easy to misread in ads.",
    },
    "house-price-cambodia": {
        "setting": "residential resale listings (Phnom Penh focus)",
        "stakeholders": "families, agents, and small developers",
        "why": "House ads mix currencies, vague room counts, and inconsistent location tags—clean data plus models improve trust.",
    },
    "job-analysis": {
        "setting": "Cambodian online job boards and salary listings",
        "stakeholders": "job seekers, career centers, and hiring managers",
        "why": "Knowing which skills correlate with higher pay guides training investments and hiring strategy.",
    },
    "khmer-riel-forecasting": {
        "setting": "USD/KHR foreign-exchange markets",
        "stakeholders": "importers, payroll teams, and finance students",
        "why": "Riel volatility affects costs priced in dollars; short-horizon forecasts support planning and risk awareness.",
    },
    "laptop-price-analysis": {
        "setting": "second-hand and retail laptop listings on Khmer24",
        "stakeholders": "students, freelancers, and SME buyers",
        "why": "Laptop SKUs differ by CPU generation, RAM, and storage—buyers need fair-price estimates for each configuration.",
    },
    "moto-price-streamlit": {
        "setting": "used motorbike classifieds",
        "stakeholders": "buyers and sellers negotiating on Facebook/Khmer24-style markets",
        "why": "Instant price quotes from year, brand, and mileage reduce unfair deals and support transparent resale.",
    },
    "movie-recommendation": {
        "setting": "digital entertainment and content discovery",
        "stakeholders": "streaming users and recommender-system learners",
        "why": "Users face choice overload; content-based recommendations surface relevant titles without rich collaborative history.",
    },
    "outlier-detection": {
        "setting": "messy scraped marketplace datasets used across PDS projects",
        "stakeholders": "student analysts and instructors grading capstones",
        "why": "A single bad price row can distort regression; systematic outlier treatment is a prerequisite for trustworthy models.",
    },
    "phone-price-analysis": {
        "setting": "smartphone resale and retail in Cambodia",
        "stakeholders": "consumers, phone shops, and importers",
        "why": "Flagship vs. budget brands and storage tiers create wide price spreads that buyers struggle to compare.",
    },
    "used-car-price-prediction": {
        "setting": "imported used-vehicle listings on Cambodian classified sites",
        "stakeholders": "buyers, dealers, and middlemen negotiating without standardized appraisals",
        "why": "Mileage, model year, brand, and condition should determine fair value—models make that relationship explicit and testable.",
    },
    "gold-price-forecasting": {
        "setting": "global gold markets as a macro indicator",
        "stakeholders": "students learning time-series methods and small investors tracking hedges",
        "why": "Gold prices react to macro shocks; forecasting exercises build intuition for trend, seasonality, and model risk.",
    },
    "home-loan-analysis": {
        "setting": "retail lending and credit approval analytics",
        "stakeholders": "applicants, loan officers, and risk analysts",
        "why": "Approval depends on income, credit history, and employment—EDA reveals which factors dominate decisions.",
    },
    "churn-prediction": {
        "setting": "subscription telecom and SaaS-style customer bases",
        "stakeholders": "retention marketers and customer-success teams",
        "why": "Churn destroys recurring revenue; early risk scores focus retention spend on likely leavers.",
    },
    "logistic-analysis": {
        "setting": "binary decision problems in business and public policy",
        "stakeholders": "managers who need probability and odds-ratio explanations",
        "why": "Logistic regression remains the interpretable baseline for yes/no outcomes with auditable coefficients.",
    },
}


def _para(*sentences):
    return " ".join(s.strip() for s in sentences if s.strip())


def expand_background(slug, base: str, title: str) -> str:
    if slug == "data-science-collection":
        return _para(
            "The **Data Science Projects Collection** on GitHub (account: **PaulChanCyber**) "
            "archives multi-year student capstones from Cambodia-focused data science coursework. "
            "Rather than synthetic textbook datasets alone, most teams work with **scraped marketplace "
            "and public records data**—Khmer24 listings, Bookshop catalogs, job boards, and FX series—"
            "so methods are tested on noisy, real-world tables.",
            base,
            "Across cohorts (approximately 2020–2023), projects share a common pedagogical arc even when "
            "domains differ: articulate a business question, collect and document data provenance, clean "
            "and explore, engineer features, train models, evaluate with appropriate metrics, and communicate "
            "findings in reports and slides. Several advanced teams extended notebooks into **Flask**, "
            "**Streamlit**, or **Docker** deployments, demonstrating that analytics prototypes can be shared "
            "as lightweight applications.",
            PDS_FOOTER,
        )

    ctx = DOMAIN.get(slug, {
        "setting": "applied data science in Cambodia",
        "stakeholders": "learners and local market participants",
        "why": "Structured analysis improves decisions over intuition alone.",
    })
    return _para(
        f"This study examines **{ctx['setting']}** in Cambodia—a context where digital classifieds and "
        f"e-commerce listings have accelerated price transparency but not necessarily price *understanding*. "
        f"Stakeholders include {ctx['stakeholders']}.",
        base,
        "The project folder on GitHub contains notebooks, and in many cases a formal **Project Guideline** "
        "PDF that records the instructor-approved objectives, timeline, and evaluation plan. That document "
        "is the contract between the student team and the course: it states what will be delivered, which "
        "algorithms will be compared, and how success will be measured.",
        PDS_FOOTER,
    )


def expand_motivation(slug, base: str, title: str) -> str:
    if slug == "data-science-collection":
        return _para(
            "Cambodia's economy is increasingly digitized: property, vehicles, electronics, and jobs are "
            "advertised online long before they appear in traditional channels. That shift creates an "
            "educational opportunity—students can practice the same workflows used by working data analysts "
            "(scraping, cleaning, modeling, deployment) on problems their families and communities recognize.",
            base,
            "Motivation for maintaining a **public collection** is threefold: (1) showcase student achievement "
            "for employers and graduate programs; (2) give future cohorts exemplar pipelines; (3) document "
            "instructor **CHAN Sophal**'s PDS curriculum impact across real estate, consumer goods, labor, and "
            "finance domains.",
            "For visitors to this portfolio, the collection demonstrates breadth: regression for prices, "
            "classification for churn and loan approval, time series for gold and FX, recommenders for movies, "
            "and dedicated modules on outlier treatment that underpin every other scrape-heavy project.",
        )

    ctx = DOMAIN.get(slug, {"why": base})
    return _para(
        f"**Why this topic matters:** {ctx['why']}",
        base,
        f"From an academic standpoint, **{title}** trains competencies employers list repeatedly: "
        "pandas data wrangling, visualization literacy, scikit-learn modeling, and clear written "
        "communication. From a practical standpoint, even a simple benchmark model helps "
        f"{ctx.get('stakeholders', 'users')} negotiate fairer deals and spot overpriced listings.",
        "The motivation is therefore both **social** (fairer, more informed transactions) and "
        "**pedagogical** (evidence that the team followed the guideline, compared models fairly, "
        "and can explain limitations such as sample bias, missing data, and temporal drift).",
    )


def expand_guidelines(text: str, title: str) -> str:
    return _para(
        "The following objectives and steps are taken from the team's **Project Guideline** "
        f"(see GitHub) and reflect how the instructor graded the capstone:",
        text.strip(),
        "Teams were expected to show intermediate artifacts—not only a final accuracy number. "
        "That includes data dictionaries, plots defending modeling choices, and a short conclusion "
        "on which model to deploy or recommend for the stated business question.",
    )


def expand_data(text: str, title: str) -> str:
    return _para(
        "Reliable conclusions depend on documenting **where data came from**, **how often it was collected**, "
        "and **what each column means**. For this project:",
        text.strip(),
        "Typical preparation steps across PDS scraping projects include deduplicating listings, "
        "standardizing currencies (USD vs. KHR), parsing text fields (e.g., '3+ bedrooms'), "
        "handling missing values with explicit rules, and flagging extreme prices before modeling. "
        "Those steps reduce leakage and prevent a single erroneous row from dominating metrics.",
    )


def expand_methodology(text: str, title: str) -> str:
    return _para(
        "Analytical work proceeded in reproducible notebook stages so instructors could rerun cells "
        "during defense sessions:",
        text.strip(),
        "Where applicable, teams compared multiple algorithms rather than reporting a single default model. "
        "Feature engineering was justified with plots (distributions, correlations, geographic breakdowns) "
        "so stakeholders could see *why* variables entered the model—not only *that* they improved error metrics.",
    )


def expand_evaluation(text: str, title: str) -> str:
    return _para(
        "Model evaluation followed train/validation/test discipline taught in PDS:",
        text.strip(),
        "Beyond scalar error, teams were encouraged to inspect **residuals** (regression), "
        "**confusion matrices** (classification), or **forecast overlays** (time series) to detect "
        "systematic bias—such as underpricing premium districts or overfitting rare categories.",
    )


def expand_outcomes(text: str, title: str) -> str:
    return _para(
        text.strip(),
        f"Completing **{title}** provides evidence of end-to-end data science execution: from raw scrape "
        "to defended conclusions. For portfolio readers, the GitHub repository contains the artifacts "
        "to verify claims—notebooks, and in many folders, slide decks and PDF reports.",
        "Limitations are worth stating explicitly: scraped data snapshots age quickly; models trained in "
        "2022–2023 may need retraining as market conditions shift. That honesty is part of professional practice.",
    )


def get_expanded(slug: str, title: str) -> dict:
    base = ENRICHED[slug]
    return {
        "background": expand_background(slug, base["background"], title),
        "motivation": expand_motivation(slug, base["motivation"], title),
        "guidelines": expand_guidelines(base["guidelines"], title),
        "data": expand_data(base["data"], title),
        "methodology": expand_methodology(base["methodology"], title),
        "evaluation": expand_evaluation(base["evaluation"], title),
        "outcomes": expand_outcomes(base["outcomes"], title),
    }
