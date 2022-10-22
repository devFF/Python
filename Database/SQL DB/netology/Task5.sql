-- отношение стоимости товаров к единице стоимости этих товаров 
-- сумма платежей в разрезе каждого товара
select opl.product_id, sum(o.amount)
from orders o 
join order_product_list opl on o.order_id = opl.order_id 
group by opl.product_id 

-- информация по сумме каждого продукта
select p.product_id, p.price 
from product p 

-- совместим две логики
select t1.product_id, sum / price
from (select opl.product_id, sum(o.amount)
from orders o 
join order_product_list opl on o.order_id = opl.order_id 
group by opl.product_id ) t1
join (select p.product_id, p.price 
from product p ) t2 on t1.product_id = t2.product_id

-- или
select t1.product_id, sum / (select p.price from product p where p.product_id = t1.product_id)
from (select opl.product_id, sum(o.amount)
from orders o 
join order_product_list opl on o.order_id = opl.order_id 
group by opl.product_id ) t1

