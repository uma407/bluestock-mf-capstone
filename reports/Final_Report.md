# Mutual Fund Analytics Platform

## Bluestock Fintech Pvt. Ltd.

### Final Project Report

**Prepared By:** Boppana Uma Maheswari
**Internship:** Data Analyst Intern
**Project:** Mutual Fund Analytics Platform
**Duration:** 7-Day Capstone Project

---

# 1. Executive Summary

This project focuses on building a complete Mutual Fund Analytics Platform using publicly available Indian mutual fund data. The platform integrates data engineering, financial analytics, risk measurement, investor behavior analysis, and business intelligence reporting. The objective was to design an end-to-end solution capable of ingesting, processing, analyzing, and visualizing mutual fund data for decision-making purposes.

The project includes ETL pipelines, database design, exploratory data analysis, performance analytics, advanced risk metrics, investor analytics, and an interactive Power BI dashboard.

---

# 2. Project Objectives

The primary objectives of this project were:

* Build an automated ETL pipeline.
* Create a normalized database schema.
* Perform exploratory data analysis.
* Calculate mutual fund performance metrics.
* Analyze investor transaction behavior.
* Build advanced risk analytics.
* Develop an interactive Power BI dashboard.
* Present actionable business insights.

---

# 3. Data Sources

The project utilized the following datasets:

1. Fund Master Data
2. NAV History Data
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance Data
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

Data was sourced from AMFI India, mfapi.in, and public market references.

---

# 4. ETL Pipeline Design

The ETL process consisted of:

### Extract

* Import CSV datasets.
* Load NAV history records.
* Validate file structure.

### Transform

* Handle missing values.
* Standardize column names.
* Convert date columns.
* Remove duplicates.
* Create derived metrics.

### Load

* Store processed data.
* Load into SQLite database.
* Create analytical tables.

The ETL pipeline was implemented using Python, Pandas, NumPy, and SQLAlchemy.

---

# 5. Database Design

A star schema approach was implemented.

Main tables:

* dim_fund
* fact_nav
* fact_aum
* fact_sip
* fact_transactions
* dim_investor

Relationships were designed to support reporting and dashboard requirements.

---
# 6. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted to understand trends, distributions, and relationships within the mutual fund ecosystem.

Key analyses performed:

* NAV growth trends across schemes.
* AUM distribution across fund houses.
* SIP inflow growth trends.
* Category-wise fund inflows.
* Folio growth analysis.
* Investor transaction distribution.
* Risk versus return relationships.

### Major Findings

* Industry AUM showed consistent growth from 2022 to 2025.
* SIP inflows reached record levels during the study period.
* Large-cap and flexi-cap funds attracted significant investor interest.
* Investor participation increased substantially across multiple states.

---

# 7. Performance Analytics

Performance metrics were calculated for all mutual fund schemes.

### Metrics Computed

* Daily Returns
* CAGR (1 Year, 3 Year, 5 Year)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Tracking Error
* Maximum Drawdown

### Observations

* Several large-cap funds demonstrated stable risk-adjusted performance.
* Sharpe Ratio rankings highlighted funds with superior return-to-risk characteristics.
* Alpha values identified funds outperforming benchmark expectations.
* Maximum Drawdown analysis revealed periods of market stress and recovery.

---

# 8. Advanced Analytics & Risk Metrics

Advanced analytics techniques were applied to evaluate risk and investor behavior.

### Historical Risk Metrics

* Historical VaR (95%)
* Conditional VaR (CVaR)

### Rolling Performance

* Rolling 90-Day Sharpe Ratio

### Investor Analytics

* Investor Cohort Analysis
* SIP Continuity Analysis
* At-Risk Investor Detection

### Portfolio Analysis

* Sector HHI Concentration
* Portfolio Diversification Assessment

### Fund Recommendation Engine

A rule-based recommendation system was developed using Sharpe Ratio rankings and risk grades to recommend suitable funds based on investor risk appetite.

---

# 9. Dashboard Development

A four-page Power BI dashboard was developed.

## Page 1 – Industry Overview

Features:

* Industry AUM
* SIP Inflows
* Folio Count
* Scheme Count
* AUM Trends

## Page 2 – Fund Performance

Features:

* Return vs Risk Scatter Plot
* Fund Scorecard
* Fund Ranking
* Interactive Slicers

## Page 3 – Investor Analytics

Features:

* State-wise Transaction Analysis
* SIP vs Lumpsum Distribution
* Age Group Analysis
* Monthly Transaction Trends

## Page 4 – SIP & Market Trends

Features:

* CAGR Analysis
* Category Distribution
* Fund Rankings
* Market Trend Insights

---

# 10. Key Findings

1. Industry AUM expanded significantly between 2022 and 2025.
2. SIP inflows continued to increase, reflecting growing retail participation.
3. Moderate-risk funds demonstrated strong risk-adjusted performance.
4. The 2024 investor cohort contributed the largest investment volume.
5. Several investors were identified as at-risk based on SIP continuity analysis.
6. Certain funds exhibited higher concentration risk based on HHI analysis.

---

# 11. Limitations

* Analysis is dependent on available historical data.
* Market conditions may change over time.
* Recommendation outputs are educational and not financial advice.
* Public datasets may contain reporting delays.

---

# 12. Recommendations

* Improve portfolio diversification in highly concentrated funds.
* Monitor SIP continuity to reduce investor churn.
* Expand investor education programs.
* Enhance dashboard automation through scheduled ETL execution.
* Integrate real-time market data feeds in future versions.

---

# 13. Conclusion

The Mutual Fund Analytics Platform successfully delivered an end-to-end analytics solution covering data ingestion, transformation, storage, analysis, risk measurement, investor behavior assessment, and dashboard reporting. The project demonstrates practical applications of Data Analytics, Financial Analytics, Business Intelligence, and Risk Management within the Fintech domain.

The platform provides meaningful insights for investors, analysts, and financial institutions while showcasing a complete analytics workflow from raw data to decision-ready dashboards.
