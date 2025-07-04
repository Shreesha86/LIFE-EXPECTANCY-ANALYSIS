# 🌍 Life Expectancy Analysis – Data Analytics Project

## 📌 Project Overview
This project analyzes global health, economic, and social indicators to understand their impact on life expectancy across countries from 2000 to 2015. The goal was to clean raw data, visualize key patterns using Power BI, and extract meaningful insights to support public health and development strategies.

---

## 🎯 Project Goals
- Analyze global health and economic indicators affecting life expectancy
- Clean and preprocess raw data using Python (pandas)
- Build an interactive Power BI dashboard with key KPIs and visual comparisons
- Identify key influencing factors like GDP, alcohol use, HIV/AIDS, education, and infant mortality
- Compare life expectancy across developed and developing countries
- Extract insights to support public health and policy decisions

---

## 📁 Dataset Overview
- **Rows:** 2,928
- **Columns:** 22
- **Years Covered:** 2000 to 2015
- **Target Variable:** `Life expectancy`
- **Key Features:**
  - Economic: GDP, Income composition of resources
  - Health: HIV/AIDS, Alcohol, infant deaths, Hepatitis B, Measles
  - Social: Schooling, Status (Developed/Developing)
- **Source:** Cleaned from raw CSV using Python

---

## 🧹 Data Cleaning Summary
- Removed an unnamed empty column
- Handled missing values using column means
- Stripped extra spaces from column names
- Converted all data to consistent formats
- Saved cleaned data as `Life_cleaned.csv`

---

## 📊 Dashboard Overview (Power BI)

### Page 1: Life Expectancy Overview
- KPI cards: Avg Life Expectancy, Adult Mortality, Schooling, Health Expenditure
- Bar: Top 10 countries by Life Expectancy
- Pie: Status (Developed vs Developing)
- Line: Life Expectancy trend by Year
- Map: Life Expectancy by Country

### Page 2: Health & Economic Impact
- Scatter: Life Expectancy vs GDP (bubble = Population)
- Bar: Life Expectancy by Alcohol level
- Stacked Column: Life Expectancy by HIV/AIDS levels
- Bar: Education (Schooling) impact
- Slicers: Year, Country, Status

---

## 📐 DAX Measures Used

```DAX
Avg Life Expectancy = AVERAGE('Life_cleaned'[Life expectancy])
Avg GDP = AVERAGE('Life_cleaned'[GDP])
Avg Alcohol = AVERAGE('Life_cleaned'[Alcohol])
Avg HIV = AVERAGE('Life_cleaned'[HIV/AIDS])
Avg Schooling = AVERAGE('Life_cleaned'[Schooling])
Avg Infant Deaths = AVERAGE('Life_cleaned'[infant deaths])
```

---

## 📈 Key Insights

- Countries with higher GDP generally have higher life expectancy
- HIV/AIDS and infant mortality rates are strong negative indicators
- Better schooling and income composition correlate with longer lives
- Developing nations show consistently lower life expectancy
- Global life expectancy has steadily improved from 2000 to 2015

---
## 📌 Project Status

✅ Completed 

---

## 🔗How to Use

1. Download the `.pbix` file from this repository
2. Open it using **Microsoft Power BI Desktop**
3. Interact with filters and visuals to explore trends

---
## 👤 Author

**Shreesha – Data Analyst Intern**  
[LinkedIn Profile](https://www.linkedin.com/in/shreesha-poojary85)


