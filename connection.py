import pyodbc




server = "FACU\SQLEXPRESS"
user = "FACU\Chevrolet"
database = "Testing"


try:
    connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={user}; Trusted_Connection=yes;'
    connection = pyodbc.connect(connection_string)
    



except pyodbc.Error as e:
    print("Error al conectar a la base de datos: ",e)