-- Remove duplicates from customers table
WITH duplicates AS (
  SELECT 
    user_id, 
    event_time, 
    user_session, 
    product_id, 
    price, 
    event_type,
    ROW_NUMBER() OVER (PARTITION BY user_id, event_time, user_session, product_id, price, event_type ORDER BY ctid) AS row_num
  FROM 
    customers
)
DELETE FROM customers
WHERE (user_id, event_time, user_session, product_id, price, event_type) IN (
  SELECT 
    user_id, 
    event_time, 
    user_session, 
    product_id, 
    price, 
    event_type
  FROM 
    duplicates
  WHERE 
    row_num > 1
);