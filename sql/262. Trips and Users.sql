# Write your MySQL query statement below
select 
t.request_at Day,
(count(t.id)) 'Cancellation Rate'

from Trips t
left join Users clients on t.client_id = clients.users_id
left join Users drivers on t.driver_id = drivers.users_id
# 
where 
clients.banned = 'No' and drivers.banned = 'No' 
# and t.Status = 'completed'
group by t.request_at