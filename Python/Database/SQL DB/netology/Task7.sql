-- представления

-- нужно постоянно получать данные по последнему заказу пользователя
-- для начала реализуем логику по последнему зазказу пользователя 
-- (обратная сортировка по убыванию, берем только 1 элемент)
select *
from (
select o.order_id , o.customer_id , o.amount ,
	row_number() over (partition by o.customer_id order by order_id desc)
from orders o) t
where row_number = 1

-- создадим представление на основе предыдущей логики
create view task7 as 
select *
from (
select o.order_id , o.customer_id , o.amount ,
	row_number() over (partition by o.customer_id order by order_id desc)
from orders o) t
where row_number = 1

-- вызовем представление 
select * from task7

-- создадим материализованное представление (таблица запишется в память на жесткий диск)
create materialized view task7m as 
select *
from (
select o.order_id , o.customer_id , o.amount ,
	row_number() over (partition by o.customer_id order by order_id desc)
from orders o) t
where row_number = 1
with no data -- но данными не заполняем 

-- запросим данные из матер представления, но получим ошибку, 
-- так как не заполнена разметка на диске (нет данных)
select * from task7m

--обновим данные в материализованном представлении
refresh materialized view task7m 

-- удалим материализованное представление
drop materialized view task7m 
