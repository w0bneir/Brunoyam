import sqlite3 as sql
con = sql.connect('soc.db')
cur = con.cursor()
cur.execute('''create table Users (user_id integer primary key, 
                                   username text unique not null,
                                   email text unique not null, 
                                   password text not null, 
                                   first_name text not null, 
                                   last_name text, 
                                   registration_date datetime default current_timestamp)''')
con.commit()
cur.execute('''create table Posts (post_id integer primary key,
                                   user_id integer not null,
                                   content text not null,
                                   creation_date datetime default current_timestamp,
                                   location text,
                                   private boolean default false,
                                   foreign key (user_id) references Users(user_id))''')
con.commit()
cur.execute('''create table Friends (relation_id integer primary key,
                                     user_id integer not null,
                                     friend_id integer not null,
                                     status text,
                                     foreign key (user_id) references Users(user_id),
                                     foreign key (friend_id) references Users(user_id))''')
con.commit()
cur.execute('''create table Messages (message_id integer primary key,
                                      sender_id integer not null,
                                      receiver_id integer not null,
                                      content text not null,
                                      send_date datetime default current_timestamp,
                                      is_read boolean default false,
                                      foreign key (sender_id) references Users(user_id),
                                      foreign key (receiver_id) references Users(user_id))''')
con.commit()
con.execute('''create table Notifictions (notification_id integer primary key,
                                          user_id integer not null,
                                          content text not null,
                                          creation_date datetime default current_timestamp,
                                          is_read boolean default false,
                                          foreign key (user_id) references Users(user_id))''')
con.commit()
con.close
