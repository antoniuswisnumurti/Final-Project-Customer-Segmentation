
---

## ⚙️ Data Understanding
- Source: [Retail Analysis Large Dataset (Kaggle)](https://www.kaggle.com/datasets/sahilprajapati143/retail-analysis-large-dataset)  
- Period: March 2023 – February 2024  
- Size: 302,006 rows × 30 columns  
- After preprocessing: 95,205 rows × 26 columns  

---

## 🔄 Data Preprocessing
1. Convert `date` to datetime format  
2. Handle duplicates (dropped 18 duplicated values)  
3. Drop irrelevant columns (e.g., personal info, payment method)  
4. Filter USA transactions only  
5. Handle missing values using logical formulas:  
   - `Total Purchases = Total Amount / Amount`  
   - `Amount = Total Amount / Total Purchases`  
   - `Total Amount = Total Purchases × Amount`  
6. Apply **RFM analysis** (added 9 new columns for RFM scores & segmentation)

---

## 📊 RFM Segmentation
- **Recency (R):** Days since last purchase  
- **Frequency (F):** Number of transactions  
- **Monetary (M):** Total money spent  

**Segments Defined:**
- **Champions** (score = 12) → best customers, high in all RFM  
- **Loyal Customers** (score = 9–11) → frequent, valuable, engaged  
- **Potential Loyalists** (score = 6–8) → could become loyal with engagement  
- **Needs Attention** (score = 3–5) → inactive or at risk of churn  

---

## ✅ Results
- **Total Sales:** $130M  
- **Total Transactions:** ~95K  
- **Total Customers:** ~58K  

**Customer Distribution:**
- Potential Loyalists → **60% of customers** (~75M sales, 102K transactions)  
- Needs Attention → **27%** (~15M sales, 25K transactions)  
- Loyal Customers → **13%** (~38M sales, 78K transactions)  
- Champions → **<0.1%** (~500K sales, 2K transactions)  

**Trends (July 2023 – Feb 2024):**
- Potential Loyalists declined after July 2023  
- Needs Attention increased sharply since July 2023  
- Loyal Customers decreased gradually  
- Champions remained very low  

---

## 🎯 Recommendations
1. **Nurture Potential Loyalists** (largest & most profitable group)  
   - Launch loyalty programs, exclusive previews, and personalized offers  

2. **Re-engage Needs Attention Customers**  
   - Send win-back campaigns, feedback forms, and humanized communication  

3. **Investigate Decline of Loyal Customers**  
   - Run satisfaction surveys and check for service/product issues  

4. **Grow the Champions Segment**  
   - Study traits of Champions and upsell Loyal/Potential Loyalists  

5. **Set Up Early-Warning System**  
   - Monitor monthly customer movement across segments  
   - Trigger alerts when sharp declines occur  

---

## 🛠️ Tools & Technologies
- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- Google Colab  
- Power BI (Dashboard)  
- Streamlit (Deployment)  

---

## 👤 Author
**Antonius Wisnumurti Sulistyanto**  
- [LinkedIn](https://www.linkedin.com/in/antonius-wisnumurti-sulistyanto/)  
- 📧 antoniuswisnumurti@gmail.com  

---
