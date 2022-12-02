# Write your MySQL query statement below
#select 
#sell_date,
#count(product) num_sold,
#group_concat(product order by product asc separator ',') products

#from 
#(select distinct * from Activities a) Activities
#group by sell_date
#order by sell_date

select 
    sell_date, 
    count(distinct(product)) as num_sold, 
    GROUP_CONCAT(distinct(product) SEPARATOR  ',') as products 
from Activities
group by sell_date 
order by sell_date, product;