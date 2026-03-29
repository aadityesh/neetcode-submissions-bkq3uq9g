-- Write your query below
SELECT distinct(customer_id)
from customers
where year='2020' and
revenue > 0;