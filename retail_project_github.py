# ============================================================
# PYTHON ANALYSIS — STEP 1: LOAD AND VERIFY DATA
# Purpose: Load the retail dataset and verify its structure
# ============================================================

import pandas as pd
df = pd.read_csv("Project/retail_sales_data.csv")

# ============================================================
# PYTHON ANALYSIS — STEP 2: DATA UNDERSTANDING
# Purpose: Inspect the dataset structure, data types, and
# basic data quality before performing analysis
# ============================================================

# 1. DATASET DIMENSIONS [ROWS & COLUMNS]
print("\nShape:", df.shape)

# 2. COLUMN NAMES 
print("\nColumns:", df.columns)

# 3. DATATYPES 
print("\nDatatypes:", df.dtypes)

# 4. FIRST 5 RECORDS 
print("\nTop 5 Records:", df.head(5))

# ============================================================
# PYTHON ANALYSIS — STEP 3: DATA QUALITY CHECK
# Purpose: Check for missing values and duplicate records
# ============================================================

# 1. CHECK FOR MISSING VALUES
print("\nMissing Values:")
print(df.isnull().sum())

# 2. CHECK FOR DUPLICATES
print("\nDuplicate Rows:", df.duplicated().sum())


# ============================================================
# PYTHON ANALYSIS — STEP 4: DATE TYPE VALIDATION
# Purpose: Check whether date columns are stored as proper
# datetime values before performing date-based analysis
# ============================================================

print(df[['Date of Birth', 'Sales Date', 'Order Date', 'Ship Date']].dtypes)


# ============================================================
# PYTHON ANALYSIS — STEP 4: DATE TYPE CONVERSION
# Purpose: Convert date columns from string format to datetime
# format for accurate date-based analysis
# ============================================================

# 1. CONVERT DATE COLUMNS TO DATETIME
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
df['Sales Date'] = pd.to_datetime(df['Sales Date'])
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 2. VERIFY DATE COLUMN DATA TYPES
print(df[['Date of Birth', 'Sales Date', 'Order Date', 'Ship Date']].dtypes)


# ============================================================
# PYTHON ANALYSIS — STEP 5: CALCULATE SHIPPING DAYS
# Purpose: Calculate the number of days taken to ship each order
# ============================================================

# 1. CREATE SHIPPING DAYS COLUMN
shipping_days = df['Ship Date'] - df['Order Date']

# # 2. VERIFY THE RESULT
print(shipping_days)

# ============================================================
# PYTHON ANALYSIS — STEP 5: CALCULATE SHIPPING DAYS
# Purpose: Calculate the number of days taken to ship each order
# ============================================================

# 1. CALCULATE SHIPPING TIME

df['shipping_days'] = df['Ship Date'] - df['Order Date']


# 2. CONVERT SHIPPING TIME TO NUMERIC DAYS

df['shipping_days'] = df['shipping_days'].dt.days


# 3. VERIFY THE RESULT

print(df['shipping_days'].head())


# ============================================================
# PYTHON ANALYSIS — STEP 6: SHIPPING TIME SUMMARY
# Purpose: Calculate overall shipping time statistics
# ============================================================

# 1. CALCULATE AVERAGE SHIPPING TIME
avg_shipping_time = df['shipping_days'].mean()

# 2. CALCULATE MINIMUM SHIPPING TIME
min_shipping_time = df['shipping_days'].min()

# 3. CALCULATE MAXIMUM SHIPPING TIME
max_shipping_time = df['shipping_days'].max()

# 4. DISPLAY RESULTS
print("Average Shipping Time:",avg_shipping_time)
print("Minimum Shipping Time",min_shipping_time)
print("Maximum Shipping Time",max_shipping_time)



# ============================================================
# PYTHON ANALYSIS — STEP 7: SHIPPING TIME DISTRIBUTION
# Purpose: Understand how frequently different shipping durations
# occur across orders
# ============================================================


# 1. CALCULATE SHIPPING TIME DISTRIBUTION
# Count the number of orders for each shipping duration
# (1 day, 2 days, 3 days, etc.)
shipping_distribution = df['shipping_days'].value_counts()

# 2. SORT THE RESULT
# Arrange shipping durations in ascending order
shipping_distribution = shipping_distribution.sort_index()

# 3. DISPLAY RESULTS
# Print the shipping duration and corresponding order count
print("\nShipping Time Distribution:")
print(shipping_distribution)


# ============================================================
# PYTHON ANALYSIS — STEP 8: REGIONAL SALES & PROFIT ANALYSIS
# Purpose: Analyze total sales and profit across different regions
# ============================================================


# 1. GROUP DATA BY REGION
# Group the dataset based on the Region column
data_by_region = df.groupby('Region')

# 2. CALCULATE TOTAL SALES
# Calculate the total Sales for each region
total_Sales_by_region = data_by_region['Sales'].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate the total Profit for each region
total_profit_by_region = data_by_region['Profit'].sum()

# 4. SORT RESULTS
# Arrange regions from highest to lowest total sales
total_Sales_by_region = total_Sales_by_region.sort_values(ascending=False)

# 5. DISPLAY RESULTS
# Print the regional sales and profit summary
print("\nTotal Sales By Region:")
print(total_Sales_by_region)

print("\nTotal Profit By Region:")
print(total_profit_by_region)


# # ============================================================
# # PYTHON ANALYSIS — STEP 9: SEGMENT SALES & PROFIT ANALYSIS
# # Purpose: Compare total sales and profit across customer segments
# # ============================================================


# 1. GROUP DATA BY SEGMENT
# Group the dataset based on the Segment column
group_by_Segment = df.groupby('Segment')

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each segment
total_sales_by_segment = group_by_Segment['Sales'].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate total Profit for each segment
total_profit_by_segment = group_by_Segment['Profit'].sum()

# 4. SORT RESULTS
# Arrange segments from highest to lowest total Sales
total_sales_by_segment = total_sales_by_segment.sort_values(ascending=False)

# 5. DISPLAY RESULTS
# Print the segment-wise Sales and Profit summary
print("\nTotal Sales By Segment:")
print(total_sales_by_segment)

print("\nTotal Profit By Segment:")
print(total_profit_by_segment)


# ============================================================
# PYTHON ANALYSIS — STEP 10: YEAR-WISE SALES ANALYSIS
# Purpose: Analyze total sales across different years
# ============================================================

# 1. GROUP DATA BY YEAR
# Group the dataset based on the Year column
group_by_year = df.groupby('Year')

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each year
total_Sales_by_year = group_by_year['Sales'].sum()

# 3. SORT RESULTS
# Arrange years in chronological order
total_Sales_by_year = total_Sales_by_year.sort_index()

# 4. DISPLAY RESULTS
# Print the year-wise Sales summary
print("\nTotal Sales By Year:")
print(total_Sales_by_year)


# ============================================================
# PYTHON ANALYSIS — STEP 11: DISCOUNT ANALYSIS
# Purpose: Identify the highest discount and the number of
# records receiving the highest discount
# ============================================================

# 1. FIND THE HIGHEST DISCOUNT
# Calculate the maximum value in the Discount column
max_discount = df['Discount'].max()

# 2. COUNT RECORDS AT THE HIGHEST DISCOUNT
# Count how many records have the maximum discount
records_highest_discount = (df['Discount'] == max_discount).sum()

# 3. DISPLAY RESULTS
# Print the highest discount and corresponding record count
print("\n Max Discount:")
print(max_discount)

print("\nRecords Of Highest Discount:")
print(records_highest_discount)


# ============================================================
# PYTHON ANALYSIS — STEP 12: SUB-CATEGORY DEMAND ANALYSIS
# Purpose: Analyze order frequency and total quantity across
# different sub-categories
# ============================================================

# 1. GROUP DATA BY SUB-CATEGORY
# Group the dataset based on the Sub-Category column
group_by_sub_category = df.groupby('Sub-Category')

# 2. CALCULATE ORDER COUNT
# Count the number of orders for each sub-category
records_of_orders = group_by_sub_category['Order ID'].count()

# 3. CALCULATE TOTAL QUANTITY
# Calculate the total quantity sold for each sub-category
records_of_quantity = group_by_sub_category['Quantity'].sum()

# 4. COMBINE THE RESULTS
# Create one summary table containing order count and total quantity
sub_category_summary = pd.DataFrame({
    'Order Count': records_of_orders,
    'Total Quantity': records_of_quantity
})

# 5. SORT RESULTS
# Arrange sub-categories from highest to lowest order count
sub_category_summary = sub_category_summary.sort_values('Order Count', ascending=False)

# 6. DISPLAY RESULTS
# Print the sub-category demand summary
print("\nSub-category Demand:")
print(sub_category_summary)


# ============================================================
# PYTHON ANALYSIS — STEP 13: CUSTOMER PROFITABILITY ANALYSIS
# Purpose: Identify customers generating the highest total profit
# ============================================================

# 1. GROUP DATA BY CUSTOMER NAME
# Group the dataset based on the Customer Name column
group_by_customer_name =  df.groupby('Customer Name')

# 2. CALCULATE TOTAL PROFIT
# Calculate total Profit generated by each customer
record_of_profit = group_by_customer_name['Profit'].sum()

# 3. SORT RESULTS
# Arrange customers from highest to lowest total Profit
sorted_profit =  record_of_profit.sort_values(ascending = False)

# 4. DISPLAY RESULTS
# Print the customer-wise profit summary
print("\nCustomers Generating Highest Profit")
print(sorted_profit)


# ============================================================
# PYTHON ANALYSIS — STEP 14: SHIPPING TIME BY SUB-CATEGORY
# Purpose: Analyze average shipping time across sub-categories
# ============================================================

# 1. GROUP DATA BY SUB-CATEGORY
# Group the dataset based on the Sub-Category column
group_by_sub_category = df.groupby('Sub-Category')

# 2. CALCULATE AVERAGE SHIPPING TIME
# Calculate the average shipping days for each sub-category
avg_shipping_time = group_by_sub_category['shipping_days'].mean()

# 3. SORT RESULTS
# Arrange sub-categories from highest to lowest average shipping time
sorted_time = avg_shipping_time.sort_values(ascending=False)

# 4. DISPLAY RESULTS
# Print the sub-category-wise average shipping time
print("\nAverage Shipping Time")
print(sorted_time)


# ============================================================
# PYTHON ANALYSIS — STEP 15: SHIP MODE & SHIPPING TIME
# Purpose: Analyze average shipping time across different
# ship modes
# ============================================================

# 1. GROUP DATA BY SHIP MODE
# Group the dataset based on the Ship Mode column
group_by_ship_mode = df.groupby('Ship Mode')

# 2. CALCULATE AVERAGE SHIPPING TIME
# Calculate the average shipping days for each ship mode
avg_shipping_days = group_by_ship_mode['shipping_days'].mean()

# 3. SORT RESULTS
# Arrange ship modes from highest to lowest average shipping time
sorted_shipping_time = avg_shipping_days.sort_values(ascending=False)

# 4. DISPLAY RESULTS
# Print the ship-mode-wise average shipping time
print("\nAverage Shipping Time Based on Ship Mode")
print(sorted_shipping_time)



# ============================================================
# PYTHON ANALYSIS — STEP 16: DISCOUNT & PROFIT ANALYSIS
# Purpose: Analyze the relationship between discount levels
# and average profit
# ============================================================

# 1. GROUP DATA BY DISCOUNT
# Group the dataset based on the Discount column
group_by_discount =  df.groupby('Discount')

# 2. CALCULATE AVERAGE PROFIT
# Calculate the average Profit for each discount level
avg_profit = group_by_discount['Profit'].mean()

# 3. SORT RESULTS
# Arrange discount levels from lowest to highest
sorted_discount = avg_profit.sort_index()

# 4. DISPLAY RESULTS
# Print the discount-wise average profit
print("\nAverage Profit Based on Discount")
print(sorted_discount)



# ============================================================
# PYTHON ANALYSIS — STEP 17: DISCOUNT VS SALES & PROFIT
# Purpose: Compare average sales and average profit across
# different discount levels
# ============================================================

# 1. GROUP DATA BY DISCOUNT
# Group the dataset based on the Discount column
group_by_discount =  df.groupby('Discount')

# 2. CALCULATE AVERAGE SALES
# Calculate the average Sales for each discount level
avg_sales = group_by_discount['Sales'].mean()

# 3. CALCULATE AVERAGE PROFIT
# Calculate the average Profit for each discount level
avg_profit = group_by_discount['Profit'].mean()

# 4. COMBINE RESULTS
# Create a summary table containing average Sales and Profit
summary = pd.DataFrame({
    'Sales' : avg_sales,
    'Profit' : avg_profit
})

# 5. SORT RESULTS
# Arrange discount levels from lowest to highest
summary =  summary.sort_index()

# 6. DISPLAY RESULTS
# Print the discount-wise Sales and Profit summary
print("\nDiscount Wise Sales")
print(summary)



# ============================================================
# PYTHON ANALYSIS — STEP 18: PROFIT MARGIN ANALYSIS
# Purpose: Analyze profitability of each sub-category
# by comparing total profit with total sales
# ============================================================

# 1. GROUP DATA BY SUB-CATEGORY
# Group the dataset based on the Sub-Category column
group_by_sub_category = df.groupby("Sub-Category")

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each sub-category
total_sales = group_by_sub_category["Sales"].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate total Profit for each sub-category
total_profit = group_by_sub_category["Profit"].sum()

# 4. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales) * 100

# 5. COMBINE RESULTS
# Create a summary table containing Sales, Profit and Profit Margin
summary = pd.DataFrame({
    "Sales" : total_sales,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 6. SORT RESULTS
# Arrange sub-categories based on Profit Margin
sorted_summary = summary.sort_values("Profit Margin", ascending=False)

# 7. DISPLAY RESULTS
# Print the sub-category-wise profitability summary
print("\nSub_Category Wise Profitability")
print(sorted_summary)


# ============================================================
# PYTHON ANALYSIS — STEP 19: DISCOUNT & PROFIT MARGIN ANALYSIS
# Purpose: Analyze how Profit Margin varies across
# different discount levels
# ============================================================

# 1. GROUP DATA BY DISCOUNT
# Group the dataset based on the Discount column
group_by_discount = df.groupby("Discount")

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each discount level
total_sales = group_by_discount["Sales"].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate total Profit for each discount level
total_profit = group_by_discount["Profit"].sum()

# 4. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales) *100

# 5. COMBINE RESULTS
# Create a summary table containing Sales, Profit and Profit Margin
summary = pd.DataFrame({
    "Sales" : total_sales,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 6. SORT RESULTS
# Arrange discount levels from lowest to highest
summary_sorted = summary.sort_index(ascending=True)

# 7. DISPLAY RESULTS
# Print the discount-wise profitability summary
print("\nDiscount Wise Profitability")
print(summary_sorted)



# ============================================================
# PYTHON ANALYSIS — STEP 20: CUSTOMER PROFIT CONCENTRATION
# Purpose: Analyze how much total profit is contributed
# by the highest-profit customers
# ============================================================

# 1. GROUP DATA BY CUSTOMER NAME
# Group the dataset based on the Customer Name column
group_by_customer_name =  df.groupby("Customer Name")

# 2. CALCULATE TOTAL PROFIT
# Calculate total Profit generated by each customer
total_profit = group_by_customer_name["Profit"].sum()

# 3. SORT CUSTOMERS BY PROFIT
# Arrange customers from highest to lowest total Profit
customer_sorted = total_profit.sort_values(ascending=False)

# 4. CALCULATE TOTAL BUSINESS PROFIT
# Calculate the total Profit generated by all customers
overall_profit = df["Profit"].sum()

# 5. CALCULATE CUMULATIVE PROFIT
# Calculate the running total of Profit from highest-profit
# customer to lowest-profit customer
cumulative_profit = customer_sorted.cumsum()

# 6. CALCULATE CUMULATIVE PROFIT PERCENTAGE
# Calculate what percentage of total business Profit has been
# contributed cumulatively
cumulative_profit_percentage = (cumulative_profit / overall_profit) * 100

# 7. COMBINE RESULTS
# Create a summary table containing customer-wise Profit,
# Cumulative Profit and Cumulative Profit Percentage
customer_profit_summary = pd.DataFrame({
    "Profit" : customer_sorted,
    "Cumulative Profit" : cumulative_profit,
    "Cumulative Profit %" : cumulative_profit_percentage
})

# 8. DISPLAY RESULTS
# Print the customer profit concentration summary
print("\nCustomer Profit Concentration Summary")
print(customer_profit_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 21: CATEGORY-WISE PROFITABILITY
# Purpose: Analyze total Sales and total Profit across
# different categories of goods
# ============================================================

# 1. GROUP DATA BY CATEGORY
# Group the dataset based on the Category of Goods column
group_category_of_goods = df.groupby("Category of Goods")

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each category
total_sales = group_category_of_goods["Sales"].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate total Profit for each category
total_profit = group_category_of_goods["Profit"].sum()

# 4. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales) * 100

# 5. COMBINE RESULTS
# Create a summary table containing Sales, Profit and Profit Margin
summary = pd.DataFrame({
    "Sales" : total_sales,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 6. SORT RESULTS
# Arrange categories from highest to lowest Profit Margin
sorted_summary = summary.sort_values("Profit Margin", ascending=False)

# 7. DISPLAY RESULTS
# Print the category-wise profitability summary
print("\nCategory-Wise Profitability")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 22: REGIONAL PROFITABILITY ANALYSIS
# Purpose: Analyze total Sales, total Profit and Profit Margin
# across different regions
# ============================================================

# 1. GROUP DATA BY REGION
# Group the dataset based on the Region column
group_by_region = df.groupby("Region")

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each region
total_sales = group_by_region["Sales"].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate total Profit for each region
total_profit = group_by_region["Profit"].sum()

# 4. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales)* 100

# 5. COMBINE RESULTS
# Create a summary table containing Sales, Profit and Profit Margin
summary = pd.DataFrame({
    "Sales" : total_sales,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 6. SORT RESULTS
# Arrange regions from highest to lowest Profit Margin
sorted_summary = summary.sort_values("Profit Margin", ascending=False)

# 7. DISPLAY RESULTS
# Print the regional profitability summary
print("\nRegional Profitability")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 23: YEAR-WISE PROFITABILITY ANALYSIS
# Purpose: Analyze total Sales, total Profit and Profit Margin
# across different years
# ============================================================

# 1. GROUP DATA BY YEAR
# Group the dataset based on the Year column
group_by_year = df.groupby("Year")

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each year
total_sales = group_by_year["Sales"].sum()

# 3. CALCULATE TOTAL PROFIT
# Calculate total Profit for each year
total_profit = group_by_year["Profit"].sum()

# 4. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales)* 100

# 5. COMBINE RESULTS
# Create a summary table containing Sales, Profit and Profit Margin
summary = pd.DataFrame({
    "Sales" : total_sales,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 6. SORT RESULTS
# Arrange years in ascending order
sorted_summary = summary.sort_index(ascending=True)


# 7. DISPLAY RESULTS
# Print the year-wise profitability summary
print("\nYear-Wise Profitability")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 24: AVERAGE ORDER VALUE BY SEGMENT
# Purpose: Compare the average value of orders across
# different customer segments
# ============================================================

# 1. GROUP DATA BY SEGMENT
# Group the dataset based on the Segment column
group_by_segment = df.groupby("Segment")

# 2. CALCULATE TOTAL SALES
# Calculate total Sales for each segment
total_sales = group_by_segment["Sales"].sum()

# 3. COUNT ORDERS
# Count the number of orders for each segment
order_count = group_by_segment["Order ID"].count()

# 4. CALCULATE AVERAGE ORDER VALUE
# Calculate AOV using total Sales divided by number of Orders
averag_order_value = total_sales / order_count

# 5. COMBINE RESULTS
# Create a summary table containing Sales, Order Count and AOV
summary = pd.DataFrame({
    "Sales" : total_sales,
    "Order Count" : order_count,
    "AOV" : averag_order_value
})

# 6. SORT RESULTS
# Arrange segments from highest to lowest Average Order Value
sorted_summary = summary.sort_values("AOV", ascending=False)

# 7. DISPLAY RESULTS
# Print the segment-wise Average Order Value summary
print("\n Average Order Value By Segment")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 25: DISCOUNT EXPOSURE BY SEGMENT
# Purpose: Compare average discount levels across
# different customer segments
# ============================================================

# 1. GROUP DATA BY SEGMENT
# Group the dataset based on the Segment column
group_by_segment = df.groupby("Segment")

# 2. CALCULATE AVERAGE DISCOUNT
# Calculate the average Discount for each segment
avg_discount = group_by_segment["Discount"].mean()

# 3. CALCULATE AVERAGE PROFIT
# Calculate the average Profit for each segment
avg_profit = group_by_segment["Profit"].mean()

# 4. COMBINE RESULTS
# Create a summary table containing Average Discount
# and Average Profit
summary = pd.DataFrame({
    "Average Discount" : avg_discount,
    "Average Profit" : avg_profit
})

# 5. SORT RESULTS
# Arrange segments from highest to lowest Average Discount
sorted_summary = summary.sort_values("Average Discount", ascending=False)

# 6. DISPLAY RESULTS
# Print the segment-wise discount summary
print("\n Segment Wise Discount")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 26: PRODUCT DEMAND VS PROFITABILITY
# Purpose: Compare demand and profitability across
# different sub-categories
# ============================================================

# 1. GROUP DATA BY SUB-CATEGORY
# Group the dataset based on the Sub-Category column
group_by_sub_category = df.groupby("Sub-Category")

# 2. CALCULATE ORDER COUNT
# Count the number of orders for each sub-category
order_count = group_by_sub_category["Order ID"].count()

# 3. CALCULATE TOTAL QUANTITY
# Calculate total Quantity sold for each sub-category
total_quantity = group_by_sub_category["Quantity"].sum()

# 4. CALCULATE TOTAL SALES
# Calculate total Sales for each sub-category
total_sales = group_by_sub_category["Sales"].sum()

# 5. CALCULATE TOTAL PROFIT
# Calculate total Profit for each sub-category
total_profit = group_by_sub_category["Profit"].sum()

# 6. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales)* 100

# 7. COMBINE RESULTS
# Create a summary table containing demand and profitability metrics
summary = pd.DataFrame({
    "Order Count" : order_count,
    "Quantity" : total_quantity,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 8. SORT RESULTS
# Arrange sub-categories from highest to lowest Profit Margin
sorted_summary = summary.sort_values("Profit Margin", ascending=False)

# 9. DISPLAY RESULTS
# Print the demand and profitability summary
print("\nProfitability Summary")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 27: DISCOUNT VS DEMAND
# Purpose: Compare customer demand across different discount
# levels using order count and quantity sold
# ============================================================

# 1. GROUP DATA BY DISCOUNT
# Group the dataset based on the Discount column
group_by_discount = df.groupby("Discount")

# 2. CALCULATE ORDER COUNT
# Count the number of orders for each discount level
order_count = group_by_discount["Order ID"].count()

# 3. CALCULATE TOTAL QUANTITY
# Calculate total Quantity sold for each discount level
total_quantity = group_by_discount["Quantity"].sum()

# 4. COMBINE RESULTS
# Create a summary table containing demand metrics
summary = pd.DataFrame({
    "Order Count" : order_count,
    "Quantity" : total_quantity
})

# 5. SORT RESULTS
# Arrange discount levels from highest to lowest demand
sorted_summary = summary.sort_values("Order Count", ascending=False)

# 6. DISPLAY RESULTS
# Print the discount-wise demand summary
print("\nDemand Discount Summary")
print(sorted_summary)



# ============================================================
# PYTHON ANALYSIS — STEP 28: SHIPPING TIME VS PROFITABILITY
# Purpose: Compare shipping time and profitability across
# different sub-categories
# ============================================================

# 1. GROUP DATA BY SUB-CATEGORY
# Group the dataset based on the Sub-Category column
group_by_sub_category = df.groupby("Sub-Category")

# 2. CALCULATE AVERAGE SHIPPING TIME
# Calculate the average shipping days for each sub-category
avg_shipping_days = group_by_sub_category["shipping_days"].mean() 

# 3. CALCULATE TOTAL SALES
# Calculate total Sales for each sub-category
total_sales = group_by_sub_category["Sales"].sum()

# 4. CALCULATE TOTAL PROFIT
# Calculate total Profit for each sub-category
total_profit = group_by_sub_category["Profit"].sum()

# 5. CALCULATE PROFIT MARGIN
# Calculate Profit Margin using total Profit and total Sales
profit_margin = (total_profit / total_sales)* 100

# 6. COMBINE RESULTS
# Create a summary table containing shipping and profitability metrics
summary = pd.DataFrame({
    "Average Shipping Time" : avg_shipping_days,
    "Sales" : total_sales,
    "Profit" : total_profit,
    "Profit Margin" : profit_margin
})

# 7. SORT RESULTS
# Arrange sub-categories from highest to lowest average shipping time
sorted_summary = summary.sort_values("Average Shipping Time", ascending=False)

# 8. DISPLAY RESULTS
# Print the shipping and profitability summary
print("\n Shipping & Profitability Summary")
print(sorted_summary)


# ============================================================
# PYTHON ANALYSIS — STEP 29: OVERALL BUSINESS PERFORMANCE
# Purpose: Summarize the key business performance indicators
# from the retail sales dataset
# ============================================================

# 1. CALCULATE OVERALL SALES
# Calculate total Sales for the entire dataset
total_sales = df["Sales"].sum()

# 2. CALCULATE OVERALL PROFIT
# Calculate total Profit for the entire dataset
total_profit = df["Profit"].sum()

# 3. CALCULATE OVERALL PROFIT MARGIN
# Calculate overall Profit Margin
profit_margin = (total_profit / total_sales)* 100

# 4. FIND HIGHEST SALES REGION
# Identify the region with the highest total Sales
group_by_region = df.groupby("Region")
total_sales_by_region = group_by_region["Sales"].sum()
highest_sales_region = total_sales_by_region.idxmax()

# 5. FIND HIGHEST SALES CATEGORY
# Identify the category with the highest total Sales
group_by_good_category = df.groupby("Category of Goods")
total_sales_by_good_category = group_by_good_category["Sales"].sum()
highest_sales_good_category = total_sales_by_good_category.idxmax()

# 6. FIND HIGHEST SALES SEGMENT
# Identify the segment with the highest total Sales
group_by_segment = df.groupby("Segment")
total_sales_by_segment = group_by_segment["Sales"].sum()
highest_sales_segment = total_sales_by_segment.idxmax()

# 7. FIND HIGHEST PROFIT SUB-CATEGORY
# Identify the sub-category with the highest total Profit
group_by_sub_category = df.groupby("Sub-Category")
total_profit_by_sub_category = group_by_sub_category["Profit"].sum()
highest_profit_sub_category = total_profit_by_sub_category.idxmax()

# 8. FIND HIGHEST SALES YEAR
# Identify the year with the highest total Sales
group_by_year = df.groupby("Year")
total_sales_by_year = group_by_year["Sales"].sum()
highest_sales_year = total_sales_by_year.idxmax()

# 9. COMBINE RESULTS
# Create a summary table containing the overall business performance
summary = pd.DataFrame({
    "Overall Sales" : [total_sales],
    "Overall Profit" : [total_profit],
    "Profit Margin" : [profit_margin],
    "Highest Sales Region" : [highest_sales_region],
    "Highest Sales Category" : [highest_sales_good_category],
    "Highest Sales Segment" : [highest_sales_segment],
    "Highest Profit Sub-Category" : [highest_profit_sub_category],
    "Highest Sales Year" : [highest_sales_year]
})

# 10. DISPLAY RESULTS
# Print the overall business performance summary
print("\nOverall Business Performance")
pd.set_option('display.max_columns', None)
print(summary)



# ============================================================
# PYTHON ANALYSIS — STEP 30: FINAL BUSINESS INSIGHTS & RECOMMENDATIONS
# Purpose: Summarize key business findings and recommendations
# ============================================================

# 30.1 OVERALL BUSINESS PERFORMANCE
# The business generated approximately ₹250.84 crore in total sales
# and ₹37.55 crore in total profit, with an overall profit margin
# of 14.97% during 2019–2023.

# 30.2 REGIONAL PERFORMANCE
# The East region generated the highest total sales and profit,
# while the West region achieved the highest profit margin.

# 30.3 SEGMENT PERFORMANCE
# Corporate generated slightly higher total sales and Average Order Value,
# while Consumer generated slightly higher total profit. The differences
# between the two segments were relatively small.

# 30.4 YEAR-WISE BUSINESS PERFORMANCE
# Sales reached the highest level in 2021 and declined in the following
# years. Profit also declined over the period, while the overall profit
# margin remained relatively stable at around 15%.

# 30.5 PRODUCT DEMAND & PROFITABILITY
# Mops showed the highest demand based on order count and quantity,
# while Microwaves had the highest profit margin. Carrots showed a
# combination of strong demand and profitability. Overall, profit
# margins across sub-categories were relatively similar.

# 30.6 DISCOUNT ANALYSIS
# Higher discount levels were generally associated with lower average
# profit and profit margin. The highest discount of 50% was not associated
# with the highest demand, indicating that higher discounts did not
# consistently correspond to higher demand in this dataset.

# 30.7 SHIPPING & OPERATIONAL PERFORMANCE
# The average shipping time was approximately 3.99 days, with shipping
# durations ranging from 1 to 7 days. Average shipping times were very
# similar across ship modes, and no clear relationship between shipping
# time and profitability was observed across sub-categories.

# 30.8 CUSTOMER PROFITABILITY & CONCENTRATION
# Michael generated the highest aggregated profit among customer names.
# However, the top five customer names contributed only about 8.43% of
# total profit, indicating that profit was not heavily concentrated among
# a small number of customer names.

# 30.9 BUSINESS RECOMMENDATIONS
# 1. Review discount strategies, especially at higher discount levels,
#    because higher discounts were associated with lower profit margins.
#
# 2. Monitor sales performance after 2021 to understand the reasons
#    behind the decline in sales and total profit.
#
# 3. Continue monitoring high-demand and profitable sub-categories,
#    such as Mops, Microwaves, and Carrots, to support inventory and
#    sales planning.