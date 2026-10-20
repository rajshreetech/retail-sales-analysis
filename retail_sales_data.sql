CREATE TABLE retail_sales (
    customer_id TEXT,
    customer_name TEXT,
    last_name TEXT,
    date_of_birth DATE,
    sales NUMERIC,
    year INTEGER,
    outlet_type TEXT,
    city_type TEXT,
    category_of_goods TEXT,
    region TEXT,
    country TEXT,
    segment TEXT,
    sales_date DATE,
    order_id TEXT,
    order_date DATE,
    ship_date DATE,
    ship_mode TEXT,
    state TEXT,
    postal_code TEXT,
    product_id TEXT,
    sub_category TEXT,
    product_name TEXT,
    quantity INTEGER,
    discount NUMERIC,
    profit NUMERIC
);

-- =================================================================================
   -- INITIAL DATA VERIFACATION 
-- =================================================================================

-- =================================================================================
   -- ANALYSIS 1: VERIFY TOTAL NUMBER OF RECORDS
   -- Purpose: Confirm that all records were imported successfully
-- ===================================================================================
SELECT 
     COUNT(*) AS total_rows 
FROM retail_sales;

-- =================================================================================
   -- ANALYSIS 2: PREVIEW IMPORTED DATA
   -- Purpose: Verify that the imported data is correctly aligned with the table 
   -- columns.
-- =================================================================================
SELECT * 
FROM retail_sales 
LIMIT 5;

-- ===================================================================================
-- DATA QUALITY
-- ===================================================================================

-- ===================================================================================
   -- ANALYSIS 1: CHECK FOR NULL VALUES
   -- Purpose: Check missing values in important columns
-- ===================================================================================

SELECT
    COUNT(*) AS total_rows,
    COUNT(*) - COUNT(customer_id) AS customer_id_nulls,
    COUNT(*) - COUNT(customer_name) AS customer_name_nulls,
    COUNT(*) - COUNT(sales) AS sales_nulls,
    COUNT(*) - COUNT(order_date) AS order_date_nulls,
    COUNT(*) - COUNT(product_id) AS product_id_nulls,
    COUNT(*) - COUNT(profit) AS profit_nulls
FROM retail_sales;

-- ===================================================================================
   -- ANALYSIS 2: CHECK FOR DUPLICATE ROWS
   -- Purpose: Identify completely duplicated records
-- ===================================================================================
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT (
        customer_id,
        customer_name,
        last_name,
        date_of_birth,
        sales,
        year,
        outlet_type,
        city_type,
        category_of_goods,
        region,
        country,
        segment,
        sales_date,
        order_id,
        order_date,
        ship_date,
        ship_mode,
        state,
        postal_code,
        product_id,
        sub_category,
        product_name,
        quantity,
        discount,
        profit
    )) AS unique_rows
FROM retail_sales;

-- ===================================================================================
   -- ANALYSIS 3: VALIDATE SALES DATE RANGE
   -- Purpose: Verify the earliest and latest sales dates
-- ===================================================================================
SELECT
     MIN(sales_date) AS earliest_date,
     MAX(sales_date) AS latest_date
FROM retail_sales;

-- ===================================================================================
   --  ANALYSIS 4: UNIQUE VALUES
   -- Purpose: Verify the number of distinct values in key categorical columns
-- ===================================================================================
SELECT
     COUNT(DISTINCT region) AS region_unique,
     COUNT(DISTINCT segment) AS segment_unique,
     COUNT(DISTINCT ship_mode) AS ship_mode_unique,
     COUNT(DISTINCT category_of_goods) AS category_of_goods_unique,
     COUNT(DISTINCT city_type) AS city_type_unique
FROM retail_sales;

-- ===================================================================================
   -- ANALYSIS 5: CHECK FOR NEGATIVE PROFIT
   -- Purpose: Identify records with negative profit
-- ===================================================================================
SELECT 
     COUNT(*) AS negative_profit_records,
     MIN(profit) AS minimum_profit
FROM retail_sales WHERE profit < 0;

-- ===================================================================================
-- BUSINESS ANALYSIS 
-- ===================================================================================

-- ===================================================================================
   -- ANALYSIS 1: REGION PERFORMANCE
   -- Purpose: Compare total sales and profit across regions
-- ===================================================================================
SELECT
     region, 
	 SUM(sales) AS total_sales,
     SUM(profit) AS total_profit
FROM retail_sales 
GROUP BY region;

-- ===================================================================================
   -- ANALYSIS 2: SEGMENT PERFORMANCE
   -- Purpose: Compare sales and profit across customer segments
-- ===================================================================================
SELECT
     segment, 
	 SUM(sales) AS total_sales,
     SUM(profit) AS total_profit
FROM retail_sales
GROUP BY segment;

-- ===================================================================================
   -- ANALYSIS 3: YEARLY SALES PERFORMANCE
   -- Purpose: Analyze total sales across different years
-- ===================================================================================

SELECT 
     year, 
     SUM(sales) AS year_wise_sales 
FROM retail_sales 
GROUP BY year 
ORDER BY year ASC;

-- ===================================================================================
   -- ANALYSIS 4: DISCOUNT ANALYSIS
   -- Purpose: Identify the highest discount offered and the number of records receiving 
   -- that discount.
-- ===================================================================================
SELECT
     MAX(discount) AS highest_discount,
     COUNT(*) AS records_at_highest_discount
FROM retail_sales
WHERE discount = (SELECT MAX(discount) FROM retail_sales);

-- ===================================================================================
   -- ANALYSIS 5: SUB-CATEGORY DEMAND ANALYSIS
   -- Purpose: Identify which sub-categories have the highest and lowest order frequency 
   -- and quantity sold.
-- ===================================================================================
SELECT
     sub_category, 
	 COUNT(order_id) AS order_count,
	 SUM(quantity) AS total_quantity
FROM retail_sales 
GROUP BY sub_category
ORDER BY order_count DESC;

-- ===================================================================================
   -- ANALYSIS 6: CUSTOMER PROFITABILITY ANALYSIS
   -- Purpose: Identify customers generating the highest and lowest total profit.
-- ===================================================================================
SELECT
     customer_name,
	 SUM(profit) AS total_profit
FROM retail_sales
GROUP BY customer_name
ORDER BY total_profit DESC;

-- ===================================================================================
   -- ANALYSIS 7: SHIPPING TIME ANALYSIS
   -- Purpose: Calculate the average shipping time for each sub-category and identify the 
   -- sub-category with the shortest average shipping time.
-- ===================================================================================
SELECT
     sub_category,
	 ROUND(AVG(ship_date - order_date), 2) AS avg_shipping_time
FROM retail_sales
GROUP BY sub_category
ORDER BY avg_shipping_time ASC;

-- ===================================================================================
   -- ANALYSIS 8: SHIP MODE VS SHIPPING TIME
   -- Purpose: Compare the average shipping time across different ship modes.
-- ===================================================================================
SELECT 
     ship_mode,
	 ROUND(AVG(ship_date - order_date), 2) AS avg_shipping_time
FROM retail_sales
GROUP BY ship_mode
ORDER BY avg_shipping_time DESC;



