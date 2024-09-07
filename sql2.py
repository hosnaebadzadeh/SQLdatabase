import sqlite3

connection = sqlite3.connect("sodaFactory.db")
curs = connection.cursor()
sql ="""


CREATE TABLE IF NOT EXISTS Warehouse(
id INTEGER PRIMARY KEY,
name VARCHAR(80),
pro_year INTEGER,
ex_year INTEGER,
bottle_number INTEGER
);
INSERT INTO Warehouse (id, name, pro_year, ex_year, bottle_number) VALUES (100,"coca", 2024, 2027, 100000),
(100, "coca", 2024, 2027, 100000),
(99,"pepsi", 2023, 2029, 50000),
(98, "sprite", 2023, 2029, 8600),
(97,"zam zam", 2019, 2024, 98);

SELECT * FROM Warehouse;
SELECT id, name FROM Warehouse;
SELECT pro_year FROM Warehouse WHERE pro_year > 1400 AND ex_year > 1402;
SELECT bottle_number FROM Warehouse WHERE bottle_number > 100;
SELECT name FROM Warehous ORDER BY name ASC;
SELECT bottle_number FROM Warehouse ORDER BY bottle_number DESC;
SELECT id FROM Warehouse ex_year = 1400 AND ex_year = 1402;

"""
curs.executescript(sql)

connection.commit()
connection.close()