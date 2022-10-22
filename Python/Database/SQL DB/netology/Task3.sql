-- получить данные по сумме платежей, минимальному, максимальному платежу и количеству платежей
-- по каждому пользователю
select c.last_name , c.first_name , sum(amount), min(amount), max(amount), avg(amount)
from customer c 
join orders o on o.customer_id = c.customer_id 
group by c.customer_id 

-- получить данные по сумме платежей, минимальному, максимальному платежу и количеству платежей
-- по каждому пользователю, при этом размер платежа должен быть более 100 и сумма платежей
-- должна быть более 2000
select c.last_name , c.first_name , sum(amount), min(amount), max(amount), avg(amount)
from customer c 
join orders o on o.customer_id = c.customer_id 
where amount > 100
group by c.customer_id 
having sum(amount) > 20000

--Какое количество платежей было совершено
select count(o.order_id) 
from orders o 

-- Какое количество товаров находится в категории “Игрушки”?
select count(product_id) 
from product p 
join category c on c.category_id  = p.category_id 
where c.category = 'Игрушки'
group by p.product_id 

--Вывести категории товаров и количество товаров для этих категорий?
select c.category , count(p.product_id)
from product p 
join category c on c.category_id  = p.category_id 
where p.category_id = c.category_id 
group by c.category 

--В какой категории находится больше всего товаров?
select c.category 
from category c
join product p on c.category_id = p.category_id 
where p.category_id = c.category_id 
group by c.category 
order by count(p.product_id) desc -- сортировка с убыванием по количествую продуктов с категорией category_id 
limit 1 -- выведем один элемент из списка

-- Что вообще и в каком количестве покупала Williams Linda?
select p.product , sum(opl.amount)
from orders o
join customer c on o.customer_id = c.customer_id 
join order_product_list opl on opl.order_id = o.order_id 
join product p on p.product_id = opl.product_id 
where c.first_name = 'Linda' AND c.last_name = 'Williams' and p.product = 'Черепаха'
group by p.product 
--Сколько “Черепах” купила Williams Linda? = 3




