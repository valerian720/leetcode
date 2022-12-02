-- # write your mysql query statement below
-- select 
-- t.request_at day,
-- (count(t.id)) 'cancellation rate'

-- from trips t
-- left join users clients on t.client_id = clients.users_id
-- left join users drivers on t.driver_id = drivers.users_id
-- # 
-- where 
-- clients.banned = 'no' and drivers.banned = 'no' 
-- # and t.status = 'completed'
-- group by t.request_at

select request_at day,
round(sum(if(status = 'cancelled_by_driver' or status = 'cancelled_by_client', 1,0)) / count(*),2) as "cancellation rate"
from trips
where client_id not in (select users_id from users where banned = "yes") and
driver_id not in (select users_id from users where banned = "yes") and
request_at between "2013-10-01" and "2013-10-03"
group by request_at