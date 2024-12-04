CREATE TABLE marcas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
codigo integer NOT NULL,
nombre TEXT NOT NULL
);
CREATE TABLE proveedores (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL
);
CREATE TABLE productos (
id INTEGER PRIMARY KEY,
nombre TEXT NOT NULL,
marca_id integer NOT NULL,
proveedor_id INTEGER NOT NULL,
FOREIGN KEY(proveedor_id) REFERENCES proveedores(id), 
FOREIGN KEY(marca_id) REFERENCES marcas(id)
);
CREATE TABLE transacciones (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fecha TEXT NOT NULL,
producto_id INTEGER NOT NULL,
cantidad INTEGER NOT NULL,
proveedor_id INTEGER,
marca_id INTEGER,
precio REAL,
FOREIGN KEY(producto_id) REFERENCES productos(id),
FOREIGN KEY(proveedor_id) REFERENCES proveedores(id),
FOREIGN KEY(marca_id) REFERENCES marcas(id)
);