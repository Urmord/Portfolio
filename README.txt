# 🚀 Unified Business Intelligence (BI) & Data Analytics Portal

An enterprise-grade portfolio demonstrating end-to-end data capabilities—spanning Automated ETL pipelines, Relational Database (SQL) design, exploratory data analysis (EDA), and interactive web deployment. 

This repository centralizes three distinct analytical production workloads into a single, interactive **Streamlit** dashboard dashboard interface.

---

## 📊 Core Architecture Overview

The architecture of this portfolio models a modern corporate data infrastructure: raw, disparate data workloads (flat CSVs and relational database schemas) are processed via Python, optimized through structured SQL queries, and served directly to an interactive business intelligence tier.




              ┌──────────────────────┐
              │  Disparate Workloads         │
              └──────────┬───────────┘
                             │
        ┌──────────────┴──────────────┐
        ▼                                        ▼

┌────────────────────┐        ┌────────────────────┐
│ Relational DB Tier         │        │      Flat-File Tier       │
│  (SQLite/jobs.db)          │        │    (overwatch_data.csv    │
└──────────┬─────────┘        └──────────┬─────────┘
               │                                     │
               └────────────┬──────────────┘
                                 ▼
               ┌───────────────────────────┐
               │         Pandas Engine / Core        │
               └─────────────┬─────────────┘
                                  ▼
               ┌───────────────────────────┐
               │        Interactive BI Layer         │
               │            (Streamlit)              │
               └───────────────────────────┘


                                ---

## 🛠️ Integrated Projects & Technical Stack

### 💾 Tab 1: Relational Job Market Pipeline (SQL)
* **Objective:** Ingest, structure, and query corporate market salary metrics to discover optimization points.
* **Tech Stack:** `SQLite`, `SQLAlchemy`, `Pandas`
* **Engineering Highlights:** * Implemented structured relational schemas to transition business operations from volatile spreadsheet management to robust database infrastructure.
  * Utilized programmatic SQL aggregations (`GROUP BY`, `AVG`, `COUNT`) to reduce memory footprints during web rendering phases.
  * Connected live database connections directly into interactive **Plotly Express** data visualizations.

### 🎮 Tab 2: Algorithmic Game Analytics & Counter Logic
* **Objective:** Programmatically parse historical performance metrics for target profiles (`Anran`) to construct automated decision-making engines.
* **Tech Stack:** `Python 3`, `Pandas (DataFrames)`, `Vectorized Operations`
* **Engineering Highlights:**
  * Created an automated algorithmic rules engine utilizing looping structures to flag statistically significant win-rate anomalies.
  * Isolated operational bottlenecks (e.g., specific high-mobility constraints like a 24% performance drop against counter-picks such as Sombra).
  * Built dynamic conditional UI states within Streamlit to surface automated "tactical swap protocols" based on real CSV log inputs.

### 📈 Tab 3: Financial ETL Ingestion Engine
* **Objective:** Automate transactional data validation, cleansing, and normalization workflows.
* **Tech Stack:** `Python`, `ETL Design Patterns`
* **Engineering Highlights:**
  * Modeled an enterprise operational ingestion stream that programmatically handles dirty data, normalizes date types, drops redundant tracking schemas, and flags transaction anomalies.

---

## 🚀 Local Deployment and Replication

To replicate this environment locally and explore the interactive analytics engine, follow these steps:

### 1. Clone the Repository & Environment Setup
Ensure Python 3.10+ is installed on your local machine.
```powershell
git clone [https://github.com/YOUR_USERNAME/data-analyst-portfolio.git](https://github.com/YOUR_USERNAME/data-analyst-portfolio.git)
cd data-analyst-portfolio