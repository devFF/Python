--оконные функции
--отношение стоимости товаров к единице стоимости этих товаров
-- over открывает оконную функцию
-- partition by - группировка по индентификатору товара
-- distinct - удаляет дублирующиеся функции

select distinct p.product_id, sum(o.amount) over (partition by p.product_id) / price
from orders o 
join order_product_list opl on o.order_id = opl.order_id 
join product p on p.product_id = opl.product_id 

-- получим данные о каждом тысячном заказе

-- для начала напишем функцию запроса данных с группировкой по номеру заказа
-- оконная функция row_number, которая проставит порядковые номера для наших записей
select o.order_id, o.customer_id, o.amount ,
	row_number () over (order by order_id)
from orders o 

-- запишем ее как функцию и добавим условие
select *
from (select o.order_id, o.customer_id, o.amount ,
	row_number () over (order by order_id) 
from orders o) t
where t.row_number % 1000 = 0 -- без остатка делится на 1000

-- получим накопительную сумму платежей по каждому пользователю
select o.order_id, o.customer_id , o.amount,
	sum(amount) over (partition by customer_id order by order_id)
from orders o 

