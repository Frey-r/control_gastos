import sqlite3
from util import logger_config


logger = logger_config.get_logger(__name__)

def get_connection_sqlite():
    """
        Función que se encarga de conectar a la base de datos
        y de retornar una conección para realizar operaciones  
        Returns:
            Connection : sqlite3.Connection
    """
    conn = None
    tables = []
    try:
        conn = sqlite3.connect('database/main_db.db')
        logger.info("Conexión establecida")
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")
    return conn

def create_tables():
    """
        Función que se encarga de:
            - verificar si las tablas ya existen
            - crear las tablas de la base de datos. Las tablas son:
                - productos
                - marcas
                - transacciones
                - proveedores
        Returns:
            None
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    tables = ['productos', 'marcas', 'transacciones', 'proveedores']
    for table in tables:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        if cursor.fetchone() is None:
            try:
                cursor.executescript(open('database/CREATE_TABLES.sql').read())
                conn.commit()
                conn.close()
                logger.info(f"Tablas creadas desde CREATE_TABLES.sql SCRIPT") 
                return
            except sqlite3.Error as err:
                logger.error(f"{err} - {err.with_traceback} - {err.args}")
        else:
            logger.info(f"las tablas ya existen")
            return
    

def insert_producto(producto):
    """
        Función que se encarga de insertar un producto en la base de datos
        Args:
            producto (dict): diccionario con los datos del producto {\n
            'id': int,\n
            'nombre': str,\n
            'marca_id': int,\n
            'proveedor_id': int\n
            }
        Returns:
            None
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO productos (id, nombre, marca_id, proveedor_id) VALUES (?,?,?,?)",
                       (producto['id'], producto['nombre'], producto['marca_id'], producto['proveedor_id']))
        conn.commit()
        conn.close()
        logger.info(f"Producto {producto['nombre']} insertado en la base de datos.")
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def insert_marca(marca):
    """
        Función que se encarga de insertar una marca en la base de datos
        Args:
            marca (dict): diccionario con los datos de la marca
        Returns:
            None
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO marcas (nombre) VALUES (?)", (marca['nombre'],))
        conn.commit()
        conn.close()
        logger.info(f"Marca {marca['nombre']} insertada en la base de datos.")
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def insert_proveedor(proveedor):
    """
        Función que se encarga de insertar un proveedor en la base de datos
        Args:
            proveedor (dict): diccionario con los datos del proveedor
        Returns:
            None
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO proveedores (nombre) VALUES (?)", (proveedor['nombre'],))
        conn.commit()
        conn.close()
        logger.info(f"Proveedor {proveedor['nombre']} insertado en la base de datos.")
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def insert_transaccion(transaccion):
    """
        Función que se encarga de insertar una transacción en la base de datos
        Args:
            transaccion (dict): diccionario con los datos de la transacción
        Returns:
            None
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO transacciones (fecha, producto_id, cantidad, proveedor_id, marca_id, precio) VALUES (?,?,?,?,?,?)",
                       (transaccion['fecha'], transaccion['producto_id'], transaccion['cantidad'], transaccion['proveedor_id'], transaccion['marca_id'], transaccion['precio']))
        conn.commit()
        conn.close()
        logger.info(f"Transacción {transaccion['fecha']} insertada en la base de datos.")
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def get_productos():
    """
        Función que se encarga de retornar los productos de la base de datos
        Returns:
            list : lista de productos
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()
        logger.info(f"Productos obtenidos desde la base de datos.")
        return productos
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def get_marcas():
    """
    Obtiene las marcas de los productos de la base de datos.
    Returns:
            list : lista de marcas
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM marcas")
        marcas = cursor.fetchall()
        conn.close()
        logger.info(f"Marcas obtenidos desde la base de datos.")
        return marcas
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def get_proveedores():
    """
    Obtiene los proveedores de los productos de la base de datos.
    Returns:
        list : lista de proveedores
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        conn.close()
        logger.info(f"Proveedores obtenidos desde la base de datos.")
        return proveedores
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")

def get_transacciones():
    """
    Obtiene las transacciones de la base de datos.
    Returns:
        list : lista de transacciones
    """
    conn = get_connection_sqlite()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM transacciones")
        transacciones = cursor.fetchall()
        conn.close()
        logger.info(f"Transacciones obtenidos desde la base de datos.")
        return transacciones
    except sqlite3.Error as err:
        logger.error(f"{err} - {err.with_traceback} - {err.args}")