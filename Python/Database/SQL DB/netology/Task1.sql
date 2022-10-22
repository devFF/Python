-- создадим таблицу с доставками
create table delivery(
	delivery_id serial primary key,
	address_id int references address(address_id) not null,
	delivery_date date not null, 
	time_range text[] not null, 
	staff_id int references staff(staff_id) not null,
	status del_status not null default 'в обработке', 
	last_update timestamp, 
	create_date timestamp default now(),
	deleted boolean not null default false
	)

select * from delivery 

-- добавим (add) в таблицу с заказами ограничение(constraint) внешнего ключа для стобца с доставкой
-- название ограничения orders_delivery_fkey
-- тип ограничения forign key с указанием на столбец ()
-- указываем таблицу и стобец в ссылке, куда обращаемся references
alter table orders add constraint orders_delivery_fkey foreign key (delivery_id)
	references delivery(delivery_id)
	
-- изменим данные в заказах, добавив данные по идентификатору доставки
insert into delivery (address_id, delivery_date, time_range, staff_id)
values(102, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(34, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(12, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(78, '2022.02.25', array['10:00:00', '18:00:00'], 2),
(55, '2022.02.25', array['10:00:00', '18:00:00'], 2)

-- после внесений изменений в таблицу delivery нам нужно обновить таблицу orders и проставить идентификаторы доставки:
update orders 
set delivery_id = 1
where order_id = 1

update orders 
set delivery_id = 2
where order_id = 2

update orders 
set delivery_id = 3
where order_id = 3

update orders 
set delivery_id = 4
where order_id = 4

update orders 
set delivery_id = 5
where order_id = 5

select * from orders 

-- попробуем удалить запись из таблицы delivery


