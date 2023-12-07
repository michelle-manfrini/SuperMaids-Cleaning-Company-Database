import sqlite3
import pandas as pd


# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('Project.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
cursor.execute("DROP TABLE IF EXISTS Employee")

query = """
    CREATE TABLE Employee(
    empNo NUMERIC(10, 0) NOT NULL,
    emp_firstname VARCHAR(15),
    emp_lastname VARCHAR(15),
    address VARCHAR(100),
    salary DECIMAL(10, 2),
    telNo NUMERIC(10, 0) UNIQUE NOT NULL,
    PRIMARY KEY(empNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)


cursor.execute("DROP TABLE IF EXISTS Client")

query = """
    CREATE TABLE Client(
    clientNo NUMERIC(10, 0) NOT NULL,
    client_fname VARCHAR(15),
    client_lname VARCHAR(15),
    client_address VARCHAR(100),
    client_te_No NUMERIC(10, 0) UNIQUE NOT NULL,
    PRIMARY KEY(clientNo)
    );
    """

cursor.execute(query)


cursor.execute("DROP TABLE IF EXISTS Equipment")

query = """
    CREATE TABLE Equipment(
    equipNo NUMERIC(10, 0) NOT NULL,
    description VARCHAR(200),
    usage VARCHAR(100),
    cost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY(equipNo)
    );
    """

cursor.execute(query)


cursor.execute("DROP TABLE IF EXISTS Service")

query = """
    CREATE TABLE Service(
    serviceID NUMERIC(10, 0) NOT NULL,
    clientNo NUMERIC(10, 0) NOT NULL,
    start_date DATE,
    start_time TIME,
    duration FLOAT,
    comments VARCHAR(100),
    PRIMARY KEY(serviceID),
    CONSTRAINT alternate_key_constraint UNIQUE (clientNo, start_date),
    FOREIGN KEY (clientNo) REFERENCES Client(clientNo) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE (start_date, start_time)
    );
    """

cursor.execute(query)

#Create EmployeeService Table
cursor.execute("DROP TABLE IF EXISTS EmployeeService")

query = """
    CREATE TABLE EmployeeService(
    empNo NUMERIC(10, 0) NOT NULL,
    serviceID NUMERIC(10,0) NOT NULL,
    PRIMARY KEY (empNo, serviceID),
    FOREIGN KEY (empNo) REFERENCES Employee(empNo) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (serviceID) REFERENCES Service(serviceID) ON UPDATE CASCADE ON DELETE CASCADE
    );
    """

cursor.execute(query)

#Create EquipmentService Table
cursor.execute("DROP TABLE IF EXISTS EquipmentService")

query = """
    CREATE TABLE EquipmentService(
    equipNo NUMERIC(10, 0) NOT NULL,
    serviceID NUMERIC(10,0) NOT NULL,
    PRIMARY KEY (equipNo, serviceID),
    FOREIGN KEY (equipNo) REFERENCES Equipment(equipNo) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (serviceID) REFERENCES Service(serviceID) ON UPDATE CASCADE ON DELETE CASCADE
    );
    """

cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Employee
    VALUES (682502, "John", "Smith", "123 Main St", 50000.00, "3055551234"),
            (936034, "Jane", "Kirkland", "456 Oak St", 100000.00, "3054219672"),
            (408452, "Tomas", "Diaz", "822 Third St", 70000.00, "3053859264"),
            (274932, "Emma", "Rodriguez", "734 Burrow Ave", 80000.00, "3059277283"),
            (172723, "Joseph", "Alcantara", "481 Collins Ln", 90000.00, "3052013621"),
            (672459, "Madeline", "Connor", "349 Douglas Ave", 60000.00, "4583492389");
    """

cursor.execute(query)


query = """
    INSERT INTO Client
    VALUES (103649, "Emily", "Garcia", "202 Elm St", "7865557890"),
            (028452, "David", "Lee", "101 Cedar Ln", "3052946192"),
            (826491, "Chloe", "Smith", "789 Pine Rd", "7862949901"),
            (618352, "Benjamin", "Button", "456 Oak Ave", "3058366629"),
            (630984, "Alice", "Johnson", "888 Maple Rd", "3054443908"),
            (234892, "John", "Batman", "349 Dixie Rd", "4697894567");
    """

cursor.execute(query)


# Insert row into table
query = """
    INSERT INTO Equipment
    VALUES (8273, "Dusting Cloths", "dusting surfaces", 10.99),
            (0182, "Pressure Washer", "exterior cleaning", 250.00),
            (3729, "Window Squeegee", "window cleaning", 20.00),
            (2947, "Mop", "floor cleaning", 30.50),
            (9201, "Vacuum", "general cleaning", 150.00),
            (6781, "rugDoctor", "rugs", 45.00);
    """

cursor.execute(query)


# Insert row into EmployeeService table
query = """
    INSERT INTO EmployeeService
    VALUES (682502, 274927),
            (936034,472926),
            (408452, 503900),
            (274932, 127490),
            (172723, 394021),
            (936034, 394021),
            (682502, 472926),
            (172723, 127490)
            ;
    """

cursor.execute(query)

# Insert row into Service table
query = """
    INSERT INTO Service
    VALUES (274927, 103649, '2023-05-25', '14:30:00', 2.5, 'Special event cleaning'),
            (472926, 028452, '2023-04-10', '09:15:00', 1.5, 'Apartment cleaning'),
            (503900, 826491, '2023-03-20', '13:45:00', 2.0, 'Office cleaning'),
            (127490, 618352, '2023-01-15', '08:00:00', 2.5, 'Regular cleaning'),
            (394021, 630984, '2023-02-05', '10:30:00', 3.0, 'Deep cleaning'),
            (459829, 902786, '2023-09-04', '14:45:00', 4.0, 'Kitchen cleaning');
    """

cursor.execute(query)

# Insert row into EquipmentService table
query = """
    INSERT INTO EquipmentService
    VALUES (8273, 274927),
            (0182, 472926),
            (3729, 503900),
            (2947, 127490),
            (9201, 394021),
            (8273, 472926),
            (0182, 127490),
            (2947, 394021);
    """

cursor.execute(query)

# Display Employee Table
query = '''
    SELECT *
    FROM employee;'''

cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
Employee = pd.DataFrame(table_data, columns=column_names)
print("Employee Table \n")
print(Employee)

# Display Client Table
query = '''
    SELECT *
    FROM client;'''

cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
Client = pd.DataFrame(table_data, columns=column_names)
print("Client Table \n")
print(Client)

# Display Employee Service Table
query = '''
    SELECT *
    FROM EmployeeService;'''

cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
empser = pd.DataFrame(table_data, columns=column_names)
print("Employee Service Table")
print(empser)

# Display Equipment Table
query = '''
    SELECT *
    FROM equipment;'''

cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
Equipment = pd.DataFrame(table_data, columns=column_names)
print("Equipment Table \n")
print(Equipment)

# Display Service Table
query = '''
    SELECT *
    FROM Service;'''

cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
Service = pd.DataFrame(table_data, columns=column_names)
print("Service Table \n")
print(Service)

# Display Equipment Service Table
query = '''
    SELECT *
    FROM EquipmentService;'''

cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
Equipserv = pd.DataFrame(table_data, columns=column_names)
print("Equipment Service Table \n")
print(Equipserv)

#List employee IDs and the number of services that they are assigned to
query = '''
    SELECT empNo, COUNT(serviceID)
    FROM EmployeeService 
    GROUP BY empNo;
'''
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
query1 = pd.DataFrame(table_data, columns=column_names)
print("Query 1")
print(query1)

#List client names that have a 305 area code phone number
query = '''
    SELECT client_fname, client_lname, client_te_no
    FROM Client
    WHERE client_te_no LIKE '305%';
'''
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
query2 = pd.DataFrame(table_data, columns=column_names)
print("Query 2")
print(query2)


#List Employee names that are assigned to more than one service

query = '''
    SELECT t1.emp_firstname, t1.emp_lastname, count(t2.serviceID)
    FROM employee t1, EmployeeService t2
    WHERE t1.empNo = t2.empNo
    GROUP BY t1.emp_firstname, t1.emp_lastname
    HAVING COUNT(t2.serviceID) >1;
'''
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
query3 = pd.DataFrame(table_data, columns=column_names)
print("Query 3")
print(query3)


#List the details of services assigned to a named employee.

query4 = '''
   SELECT S.serviceID, S.clientNo, S.start_date, S.start_time, S.duration, S.comments, E.empNo
        FROM Service S
        JOIN EmployeeService ES ON S.serviceID = ES.serviceID
        JOIN Employee E ON ES.empNo = E.empNo
        WHERE E.emp_firstname = "John" AND E.emp_lastname = "Smith"
        ;
'''
cursor.execute(query4)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
query4 = pd.DataFrame(table_data, columns=column_names)
print("Query 4")
print(query4)

#List the details of equipment assigned to a service.

query5 = '''
   SELECT S.serviceID, E.equipNo, E.description, E.usage, E.cost
        FROM Service S
        JOIN EquipmentService ES ON S.serviceID = ES.serviceID
        JOIN Equipment E ON ES.equipNo = E.equipNo
        ;
'''
cursor.execute(query5)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
query5 = pd.DataFrame(table_data, columns=column_names)
print("Query 5")
print(query5)


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()