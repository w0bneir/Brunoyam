import sqlite3

connect = sqlite3.Connection("mydatabase.db")
cur = connect.cursor()
cur.execute('''create table users (user_id int PRIMARY KEY, username varchar(50), email varchar(50), password varchar(50))''')
connect.commit()
cur.execute('''insert into users (user_id, username, email, password) values
(1, 'John Doe', 'johndoe@example.com', 'password1'),
(2, 'Jane Smith', 'janesmith@example.com', 'password2'),
(3, 'Michael Johnson', 'michaeljohnson@example.com', 'password3'),
(4, 'Emily Brown', 'emilybrown@example.com', 'password4'),
(5, 'David Wilson', 'davidwilson@example.com', 'password5'),
(6, 'Sarah Taylor', 'sarahtaylor@example.com', 'password6'),
(7, 'Christopher Lee', 'christopherlee@example.com', 'password7'),
(8, 'Olivia Clark', 'oliviaclark@example.com', 'password8'),
(9, 'Matthew Anderson', 'matthewanderson@example.com', 'password9'),
(10, 'Sophia Martinez', 'sophiamartinez@example.com', 'password10');''')
cur.execute('''create table phones (phone_id int PRIMARY KEY, vendor varchar(50), model varchar(50), ram varchar(50))''')
connect.commit()
cur.execute('''insert into phones (phone_id, vendor, model, ram) values 
(1, 'Apple', 'iPhone 14', '128 ГБ'),
(2, 'Google', 'Pixel 7', '128 ГБ'),
(3, 'Huawei', 'P60 Pro', '256 Гб'),
(4, 'Xiaomi', 'Redmi Note 12 Pro+', '256 ГБ'),
(5, 'Samsung ', 'Galaxy S21 FE', '256 ГБ');''')
connect.commit()
cur.execute('''create table ratio (user_id int, phone_id int)''')
connect.commit()
cur.execute('''insert into ratio (user_id, phone_id) values 
(1,5),
(2,4),
(3,3),
(4,2),
(5,1),
(6,5),
(7,4),
(8,3),
(9,2),
(10,1);''')
connect.commit()