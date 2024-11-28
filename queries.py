#Import libraries
import pymysql
import locale

#Import function from the file 'connect_mysql'
from  connect_mysql import connect_mysql as cm 

#Create and connect the query that we're going to use. The one that I'm showing is an example that I used when I was testing the code.
def amounts_quantity():

    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    cursor = cm().cursor(pymysql.cursors.DictCursor)

    cursor.execute('''SELECT DISTINCT 
                    tv.TIPO_VEHICULO AS "Vehicle Type",
                    tv.CATEGORIA AS "Category",
                    CAST(pc.MONTO_PAGADO AS UNSIGNED) AS "Total Amount",
                    v.A_FABRICACION AS "Year of Manufacture",
                    v.MARCA AS "Brand",
                    v.PATENTE AS "License Plate",
                    v.COLOR AS "Color",
                    tp.TIPO_PAGO AS "Payment Type",
                    ma.MODULO_ATENCION AS "Service Module"

                    FROM tipo_vehiculo tv
                    LEFT JOIN vehiculo v ON v.TIPO_VEHICULO = tv.ID
                    LEFT JOIN permiso_circulacion pc ON pc.PATENTE = v.PATENTE
                    LEFT JOIN tipo_pago tp ON tp.ID = pc.TIPO_PAGO
                    LEFT JOIN modulo_atencion ma ON ma.ID = pc.MODULO_ATENCION

                    ORDER BY v.PATENTE DESC;''')
    registros = cursor.fetchall()

    cm().close()
    
    return registros