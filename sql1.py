import sqlite3


connection = sqlite3.connect("storeBank.db")
curs = connection.cursor()
sql ="""


CREATE TABLE IF NOT EXISTS Product(
id INTEGER PRIMARY KEY ,
name  VARCHAR(80),
price  INTEGER,
type VARCHAR(80)
);

CREATE TABLE IF NOT EXISTS Provider(
id INTEGER PRIMARY KEY ,
name  VARCHAR(80),
city VARCHAR(80)
);

ALTER TABLE Provider ADD COLUMN last_name VARCHAR(80);
ALTER TABLE Product ADD COLUMN CITY VARCHAR(80) DEFAULT 'Mashhad';
ALTER TABLE Provider ALTER COLUMN name VARCHAR(15) NOT NULL;
ALTER TABLE Product ALTER COLUMN name VARCHAR(15) UNIQUE;
ALTER TABLE Product DROP COLUMN type;

INSERT INTO Product (id, name, price, type, city) VALUES 
(100, 'PHONE', 10000, 'TECHNO', 'TEHRAN'),
(99, 'PC', 365000, 'TECHNO', 'MASHAHD'),
(98, 'HEADPHONE', 5000, 'EARPHONE','TEHRAN');
INSERT INTO Provider(id, name, city) VALUES
(100,'ASGHAR', 'MASHHAD'),
(99, 'MOHAMMAD', 'KERMAN'),
(98, 'HOSNA', 'TEHRAN'),
(97, 'HELIA', 'TEHRAN'),
(96, 'ELI', 'MASHHAD');

DROP TABLE Provider;
DROP TABLE Product;
DROP DATABASE 'storeBank.db';

"""
curs.executescript(sql)



connection.commit()
connection.close()
