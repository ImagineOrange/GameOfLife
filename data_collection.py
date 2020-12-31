import mysql.connector
from mysql.connector import errorcode

x_coords = []
y_coords = []

# cnx = mysql.connector.connect(user='meyercts_meyerct', password=',{xHc6evSy-b',
#                               host='gator3315.hostgator.com', database='meyercts_particle_data')

try:
    cnx = mysql.connector.connect(user='meyercts_meyerct', password='WS_ZVp^sI)x@',
                                  host='gator3315.hostgator.com', database='meyercts_particle_data')

    selector = cnx.cursor()

    query = ("SELECT x_coord FROM `data_table`")

    selector.execute(query)

    for x_coord in selector:
        print(x_coord[0])
        x_coords.append(x_coord[0])

    selector.close()

    selector = cnx.cursor()

    query = ("SELECT y_coord FROM `data_table`")

    selector.execute(query)

    for y_coord in selector:
        print(y_coord[0])
        y_coords.append(y_coord[0])

    print(x_coords)
    print(y_coords)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
