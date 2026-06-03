# Data Dictionary - Bluestock Mutual Fund Capstone Project

## 1. dim_fund (Dimension Table)

| Column | Data Type | Description |
|--------|----------|-------------|
| amfi_code | INTEGER | Unique identifier for mutual fund scheme |
| fund_house | TEXT | Name of AMC (Asset Management Company) |
| scheme_name | TEXT | Full name of mutual fund scheme |
| category | TEXT | Fund category (Equity, Debt, Hybrid etc.) |
| sub_category | TEXT | Sub classification of fund |
| plan | TEXT | Direct / Regular plan type |
| launch_date | TEXT | Scheme launch date |
| benchmark | TEXT | Benchmark index of fund |
| expense_ratio_pct | REAL | Annual expense ratio in % |
| exit_load_pct | REAL | Exit load charges in % |
| min_sip_amount | INTEGER | Minimum SIP investment amount |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk level (Low/Moderate/High) |
| sebi_category_code | TEXT | SEBI classification code |

---

## 2. fact_nav (NAV History Table)

| Column | Data Type | Description |
|--------|----------|-------------|
| nav_id | INTEGER | Primary key (auto increment) |
| amfi_code | INTEGER | Fund identifier |
| date | TEXT | NAV record date |
| nav | REAL | Net Asset Value |

---

## 3. fact_transactions (Investor Transactions)

| Column | Data Type | Description |
|--------|----------|-------------|
| transaction_id | INTEGER | Primary key |
| investor_id | TEXT | Unique investor ID |
| amfi_code | INTEGER | Fund identifier |
| transaction_date | TEXT | Date of transaction |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification of city |
| age_group | TEXT | Age group of investor |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI / Net Banking / Cheque |
| kyc_status | TEXT | KYC verification status |

---

## 4. fact_performance (Scheme Performance)

| Column | Data Type | Description |
|--------|----------|-------------|
| perf_id | INTEGER | Primary key |
| amfi_code | INTEGER | Fund identifier |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | AMC name |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular |
| return_1yr_pct | REAL | 1-year return % |
| return_3yr_pct | REAL | 3-year return % |
| return_5yr_pct | REAL | 5-year return % |
| benchmark_3yr_pct | REAL | Benchmark 3-year return |
| alpha | REAL | Excess return over benchmark |
| beta | REAL | Market risk measure |
| sharpe_ratio | REAL | Risk-adjusted return |
| sortino_ratio | REAL | Downside risk adjusted return |
| std_dev_ann_pct | REAL | Volatility measure |
| max_drawdown_pct | REAL | Maximum loss from peak |
| aum_crore | REAL | Assets under management |
| expense_ratio_pct | REAL | Expense ratio |
| morningstar_rating | INTEGER | Fund rating (1–5) |
| risk_grade | TEXT | Risk classification |

---

## Source Notes
- Data derived from AMFI mutual fund datasets
- NAV data sourced via MFAPI
- Investor transaction simulation dataset provided for analytics training