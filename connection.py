
user = " root"
database = "testing"
url = " localhost"

try:
    connection_string = f'mysql+pymysql://{user}:@{url}/{database}'



except ValueError as e:
    print("Error al conectar a la base de datos: ",e)