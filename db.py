from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # Este método "orm" está dentro de una subsección de la librería

# Configurar engine:*********************************
# le dice a sqlalchemy a que motor de base de datos se va a conectar. Es lo que permite la comunicación con la base de datos.

# https://docs.sqlalchemy.org/en/20/core/engines.html
# En este caso la base de datos está en la ruta relativa, en la carpeta del proyecto.
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread':False}) #Si existe se conecta, si no, la crea la bd
#Connect args es para que la base de datos trabaje en segundo plano y no de conflictos con html
#Atención: crear el engine no conecta inmediatamente a la base de datos.
#Si algo me aparece en rojo, como apareció create_engine, posiciono el cursor y lo importo.
#Agregará una línea como las de arriba "from...."

# Configurar la sesión*******************************
#Para trabajar con la base de datos necesitamos crear una sesión, lo que nos permite realizar transacciones (operaciones) dentro de la bd
Session = sessionmaker(bind=engine) #Crea la sesión
session = Session() #Crear una instancia de la sesión

# Realizar la vinculación*****************************
#Transforma las clases en tablas. En el archivo models es donde le diremos que tablas
# queremos que se transformen y le añadiremos esta variable. Esto se encargará de mapear y vincular la clase a la tabla
Base = declarative_base()