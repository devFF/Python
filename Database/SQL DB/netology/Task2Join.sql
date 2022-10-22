-- из каких городов какие заказы совершались. Выведем идентификатор заказа и название города
-- используем алиасы (сокращенное название объектов, ex. orders = o)
select o.order_id , c.city 
from orders o
inner join delivery d on o.delivery_id = d.delivery_id -- идентификатор заказов должен быть одинаковый 
join address a on a.address_id = d.address_id -- присоединим таблицу адрес, соединяем по условию, что идентификаторы совпадают
join city c on c.city_id = a.city_id -- присоединяем таблицу город

-- получим все возможны комбинации имен таких, что имя А не было равно имени А
select c.first_name , c2.first_name 
from customer c 
cross join customer c2 
where c.first_name != c2.first_name 

-- получим список заказов, для которых отсутствует доставка
select o.order_id 
from orders o 
where o.delivery_id isnull 
