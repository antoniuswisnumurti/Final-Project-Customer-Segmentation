#import libaries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#sidebar menu
st.sidebar.header('Profile:')
st.sidebar.caption('''[Antonius Wisnumurti Sulistyanto](linkedin.com/in/antonius-wisnumurti-sulistyanto/)''')
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "❓ Questions",
    "📂 Data",
    "📈 Analysis",
    "📌 Conclusion"
])
st.sidebar.header("Source:")
st.sidebar.caption('''- [Github](https://github.com/antoniuswisnumurti/Final-Project-Customer-Segmentation)''')

#page 1: Home
if page == "🏠 Home":
    st.title("Final Project: Customer Segmentation")
    st.caption("This data orign from [Kaggle](https://www.kaggle.com/datasets/sahilprajapati143/retail-analysis-large-dataset), it represent transaction of retail company from 2023 - 2024. This data includes various attributes such as customer ID, name, email, phone, address, city, state, zipcode, country, age, gender, income, customer segment, last purchase date, total purchases, amount spent, product category, product brand, product type, feedback, shipping method, payment method, and order status.")

    st.subheader("Data Dictionary")
    dictionary = '''- Transaction_ID: it represent customers transactions id
- Customer_ID: this is a customers id without it nothing possible
- Name: customers names here
- Email: customers and users emails
- Phone: cust. phone no
- Address: their address
- City: cust. city
- State: their state
- Zipcode: their zipcode
- Country: customer country
- Age: their age
- Gender: gender
- Income: cust. income like : high , low
- Customer_Segment: segment like : regular ,vip like
- Date: dates of purchase
- Year: year
- Month: month of purchase
- Time: time for purchasing
- Total_Purchases: total how many purchase
- Amount: amount spend
- Total_Amount: total amount spended here
- Product_Category: products category
- Product_Brand: brand
- Product_Type: their type
- Feedback: customer feedback
- Shipping_Method: shipping type : like : same day etc.
- Payment_Method: payment method like : cash
- Order_Status: order status : pending , completed
- Ratings: product ratings
- products: products names'''
    st.caption(dictionary)

    #business understanding
    st.subheader("Business Understanding")
    st.caption("Retail company have great total transactions in USA, and want to analyze their own transactions to understand their customers behavior like how much they spend their own money, how often they come to bought in our company, and how long they want to come back to our company. I will analyze with RFM method. With that understanding company can know  what kind of type of their customers, and can give them specific promotion, treat, benefit, voucher, etc and end up with incrased sales")
#page 2: Qustions
elif page == "❓ Questions":
    st.title("Questions")
    questions = '''1. How much total sales, transactions, and customers that company have?
2. Which segments are the largest by number of customers?
3. Which segments are have highest frequency?
4. Trend customer segment over time, are there any change over months?
5. What type of promotions should be assigned to each segment?'''
    st.caption(questions)

#page 3 = Data
elif page == "📂 Data":
    st.title("Data")
    st.subheader("Dataset Preview")

    #load dataset
    url = "https://raw.githubusercontent.com/antoniuswisnumurti/Final-Project-Customer-Segmentation/refs/heads/main/data_usa.csv"
    data_usa = pd.read_csv(url)
    st.dataframe(data_usa.head())
    st.caption('''This data set have been through alot of cleaning steps like:
- Filterd by USA Country
- Altered Data Type
- Dropped few columns
- Duplicate Handling
- Missing Values Handling''')
    
    #RFM terms
    st.subheader("Customers Segmentation Class")
    data = {
    "Segment": ["Champions", "Loyal Customers", "Potential Loyalist", "Needs Attention"],
    "Score Range": ["12", "9 – 11", "6 – 8", "3 – 5"],
    "Description": [
        "The best customers – purchase often, spend big, very engaged. High in all RFM metrics.",
        "Regular and valuable customers. Not perfect in all 3 metrics, but very good.",
        "Average performance – could become loyal with proper engagement. Usually good in 1 or 2 metrics.",
        "Low scores – inactive, low spenders, or not recently engaged. At risk of churn."
    ]
    }
    df_rfm = pd.DataFrame(data)
    st.table(df_rfm)

#page 4 = Analysis
elif page == "📈 Analysis":
    st.title("Analysis")

    #Question 1
    st.subheader('How much total sales, transactions, and customers that company have?')
    url = "https://raw.githubusercontent.com/antoniuswisnumurti/Final-Project-Customer-Segmentation/refs/heads/main/data_usa.csv"
    data_usa = pd.read_csv(url)

    # Calculate key metrics
    total_sales = data_usa['Total_Amount'].sum()
    total_transactions = data_usa['Transaction_ID'].nunique()
    total_customers = data_usa['Customer_ID'].nunique()



    # Create columns for the cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Total Sales**")
        st.markdown(f"<h2 style='color:navy;'>{total_sales/1_000_000:.0f}M</h2>", unsafe_allow_html=True)

    with col2:
        st.markdown("**Total Transactions**")
        st.markdown(f"<h2 style='color:navy;'>{total_transactions/1_000:.0f}K</h2>", unsafe_allow_html=True)

    with col3:
        st.markdown("**Total Customers**")
        st.markdown(f"<h2 style='color:navy;'>{total_customers/1_000:.0f}K</h2>", unsafe_allow_html=True)

    st.caption('''- Total Sales from all segment Customers is $130 million 
- Total Transaction in our company id 95.000 transaction
- Total Customers for all segment is around 58.000 Customers''')

    #Question 2
    st.subheader('Which segments are the largest by number of customers?')
    unique_customers = data_usa[['Customer_ID', 'Customer_Segment']].drop_duplicates()

    #count number of customers per segment
    total_customer_segment = unique_customers['Customer_Segment'].value_counts().reset_index()
    total_customer_segment.columns = ['Customer_Segment', 'Total_Customers']

    ##visualize total customers segment
    fig, ax = plt.subplots(figsize=(3,3))
    ax.pie(
    total_customer_segment['Total_Customers'],
    labels=total_customer_segment['Customer_Segment'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('coolwarm')
    )
    ax.set_title('Customer Segment Percentage')
    ax.axis('equal')

    st.pyplot(fig)
    st.caption('''- Potential Loyalist: The largest segment, accounting for almost 60% of all customers.
- Needs Attention: Makes up 27%.
- Loyal Customers: Around 13%.
- Champions: Very small group < 0.1% 

Most of customers fall into Potential Loyalist segment, this segment can be shift to Loyal if we tried to know their want''')

    #Question 3
    st.subheader('Which segments are have highest frequency?')
    #frequency total per segment
    frequency_total = data_usa.groupby('Customer_Segment')['Frequency'].sum().reset_index()
    frequency_total = frequency_total.rename(columns = {'Frequency':'Frequency_Total'})
    frequency_total = frequency_total.sort_values('Frequency_Total', ascending = False)

    #visualization of frequency total
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(
        data=frequency_total,
        x='Frequency_Total',
        y='Customer_Segment',
        palette='Blues_d',
        ax=ax
    )

    ax.set_title('Frequency Total by Customer Segment', fontsize=14)
    ax.set_xlabel('Frequency Value')
    ax.set_ylabel('Customer Segment')

    st.pyplot(fig)
    st.caption('''- Potential Loyalist contributes the most in sales (75M), followed by:
- Loyal Customers: 38M
- Needs Attention: 15M
- Champions: < 500K

Potential Loyalists generate the highest revenue, likely because they have large population and decent engagement''')

    #Question 4
    st.subheader('Trend customer segment over time, are there any change over months?')
    #extract Month-Year from your date column
    data_usa['Month'] = pd.to_datetime(data_usa['Date']).dt.to_period('M').astype(str)

    monthly_segment_trend = data_usa.groupby(['Month', 'Customer_Segment'])['Customer_ID'].nunique().reset_index()
    monthly_segment_trend = monthly_segment_trend.rename(columns={'Customer_ID': 'Customer_Count'})

    #visualize customer segment over time
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(
        data=monthly_segment_trend,
        x='Month', y='Customer_Count', hue='Customer_Segment',
        marker='o',
        ax=ax
    )

    ax.set_title('Trend of Customer Segments Over Time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Customers')
    ax.set_xticklabels(monthly_segment_trend['Month'], rotation=45)
    ax.legend(title='Customer Segment')

    st.pyplot(fig)
    st.caption('''- Potential Loyalist segment is declining since July 2023, after staying strong earlier in the year.
- Needs Attention has been increasing sharply since July 2023, becoming the most dominant segment by early 2024.
- Loyal Customers are dropping slowly, especially since July 2023.
- Champions remain consistently low, showing no recovery trend.

There’s a shift from active engagement (Loyal Customers & Potential Loyalists) to less engaged or at-risk behavior (Needs Attention''')

#page 5 =  Conclusion
elif page == "📌 Conclusion":
    st.title("Conclusion")
    st.subheader("Nurture the “Potential Loyalist” Segment Aggressively")
    st.caption('''Because They are largest customer group almost 60%, have the highest sales ($75M), and most frequent transactions (102K), but are declining in trend.
Action:
- Launch personalized campaigns or loyalty programs.
- Offer exclusive previews, discounts, or limited time rewards.
- Analyze their buying behavior to predict and suggest relevant products''')
    
    st.subheader("Pay attention to the “Needs Attention” Segment")
    st.caption('''This group is growing quickly (from July 2023) and might include previously loyal customers who are disengaging. They make up 27% of customers and generate a decent $15M in sales.
Action:
- Identify reasons for their reduced engagement delivery delays? pricing?
- Send re-engagement emails, feedback forms, or limited-time win-back offers.
- Prioritize humanized communication ask what they need or what went wrong.''')
    
    st.subheader("Investigate the Decline of “Loyal Customers”")
    st.caption('''Their numbers and engagement are dropping sharply despite historically strong performance ($38M sales, 78K transactions)
Action:
- Conduct satisfaction surveys or customer interviews.
- Check for any product, service, or pricing changes that might have affected this group.
- Create exclusive VIP benefit for this segment (faster support, loyalty tiers).''')
    
    st.subheader("Analyze Why “Champions” Are So Few”")
    st.caption('''Champions represent less rah 0.1% of customers but are likely the highest value per customer segment. You need more of them.
Action:
- Study the behavior and traits of existing Champions: what makes them loyal?
- Apply segmentation models to find more “look-alikes.”
- Upsell and offer premium service to high-value “Loyal Customers” and “Potential Loyalists” to move them into this tier.''')

    st.subheader("Set Up an Early Warning System Using Trend Data")
    st.caption('''We already observed that Potential Loyalists are declining and Needs Attention is increasing. We need to respond to changes proactively.
Action:
- Monitor monthly customer movement across segments.
- Set up alerts when a sharp shift happens (e.g. 10% drop in Loyal Customers).
- Combine RFM scores with satisfaction/feedback data for deeper insight.''')