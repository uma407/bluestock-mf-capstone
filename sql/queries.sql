-- 1. Top 5 funds by AUM
SELECT amfi_code, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. SIP vs Lumpsum transaction count
SELECT transaction_type, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. High expense ratio funds (>1%)
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct > 1;

-- 6. Monthly transaction volume
SELECT substr(transaction_date, 1, 7) AS month,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY month
ORDER BY month;

-- 7. Average Sharpe ratio by category
SELECT category, AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance
GROUP BY category;

-- 8. Funds with highest returns (5 year)
SELECT amfi_code, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 9. Average expense ratio by fund house
SELECT fund_house, AVG(expense_ratio_pct) AS avg_expense
FROM fact_performance
GROUP BY fund_house;

-- 10. Risk distribution of funds
SELECT risk_grade, COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;