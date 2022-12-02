# Write your MySQL query statement below
select 
employee_id, 
if(mod(employee_id, 2) <> 0, if(left(name, 1) <> 'M', salary, 0 ), 0) bonus

from 
Employees
order by employee_id