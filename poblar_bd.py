from miappweb.models import Proveedores, Productos, Clientes, Pedidos

proveedor1 = Proveedores(nombre = "Proveedor1", rut = "000000001", direccion = "Avenida1_numero001_Comuna1", telefono = "00000001")
proveedor1.save() 

proveedor2 = Proveedores(nombre = "Proveedor2", rut = "000000002", direccion = "Avenida2_numero002_Comuna2", telefono = "00000002")
proveedor2.save() 

proveedor3 = Proveedores(nombre = "Proveedor3", rut = "000000003", direccion = "Avenida3_numero003_Comuna3", telefono = "00000003")
proveedor3.save() 

proveedor4 = Proveedores(nombre = "Proveedor4", rut = "000000004", direccion = "Avenida4_numero004_Comuna4", telefono = "00000004")
proveedor4.save() 

producto1 = Productos(categoria = "Fruta", cantidad = "1_Kilo", nombre = "Manzana", codigo = "001", precio = "900", proveedores = proveedor1)
producto1.save()

producto2 = Productos(categoria = "Fruta", cantidad = "1_Kilo", nombre = "Naranja", codigo = "002", precio = "1000", proveedores = proveedor1)
producto2.save()

producto3 = Productos(categoria = "Fruta", cantidad = "1_Unidad", nombre = "Piña", codigo = "003", precio = "2000", proveedores = proveedor2)
producto3.save()

producto4 = Productos(categoria = "Fruta", cantidad = "1_Kilo", nombre = "Mango", codigo = "004", precio = "2800", proveedores = proveedor2)
producto4.save()

producto5 = Productos(categoria = "Verdura", cantidad = "1_Unidad", nombre = "Zapallo_Italiano", codigo = "005", precio = "300", proveedores = proveedor3)
producto5.save()

producto6 = Productos(categoria = "Verdura", cantidad = "1_Unidad", nombre = "Pimenton_Verde", codigo = "006", precio = "500", proveedores = proveedor3)
producto6.save()

producto7 = Productos(categoria = "Verdura", cantidad = "1_Paquete", nombre = "Zanahoria", codigo = "007", precio = "1000", proveedores = proveedor3)
producto7.save()

producto8 = Productos(categoria = "Verdura", cantidad = "1_Kilo", nombre = "Papas", codigo = "008", precio = "700", proveedores = proveedor4)
producto8.save()

producto9 = Productos(categoria = "Verdura", cantidad = "1_Unidad", nombre = "Lechuga", codigo = "009", precio = "700", proveedores = proveedor4)
producto9.save()

producto10 = Productos(categoria = "Verdura", cantidad = "1_Kilo", nombre = "Tomate", codigo = "0010", precio = "1600", proveedores = proveedor4)
producto10.save()

cliente1 = Clientes(nombreCompleto = "Cliente1", rut = "000000010", fechaNacimiento = "1993-04-17", direccion = "Avenida10_numero010_Comuna1", correo = "mail1@gmail.com", telefono = "99394837")
cliente1.save()

cliente2 = Clientes(nombreCompleto = "Cliente2", rut = "000000011", fechaNacimiento = "1995-07-07", direccion = "Avenida11_numero011_Comuna2", correo = "mail2@gmail.com", telefono = "93985832")
cliente2.save()

cliente3 = Clientes(nombreCompleto = "Cliente3", rut = "000000012", fechaNacimiento = "1993-10-08", direccion = "Avenida12_numero012_Comuna3", correo = "mail3@gmail.com", telefono = "94853894")
cliente3.save()

cliente4 = Clientes(nombreCompleto = "Cliente4", rut = "000000013", fechaNacimiento = "1985-01-25", direccion = "Avenida13_numero013_Comuna4", correo = "mail4@gmail.com", telefono = "96959892")
cliente4.save()

cliente5 = Clientes(nombreCompleto = "Cliente5", rut = "000000014", fechaNacimiento = "1980-01-31", direccion = "Avenida14_numero014_Comuna5", correo = "mail5@gmail.com", telefono = "94857982")
cliente5.save()

cliente6 = Clientes(nombreCompleto = "Cliente6", rut = "000000015", fechaNacimiento = "1995-12-04", direccion = "Avenida15_numero015_Comuna6", correo = "mail6@gmail.com", telefono = "98399483")
cliente6.save()

cliente7 = Clientes(nombreCompleto = "Cliente7", rut = "000000016", fechaNacimiento = "1992-06-05", direccion = "Avenida16_numero016_Comuna7", correo = "mail7@gmail.com", telefono = "26466378")
cliente7.save()

cliente8 = Clientes(nombreCompleto = "Cliente8", rut = "000000017", fechaNacimiento = "1991-08-15", direccion = "Avenida17_numero017_Comuna8", correo = "mail8@gmail.com", telefono = "63635164")
cliente8.save()

cliente9 = Clientes(nombreCompleto = "Cliente9", rut = "000000018", fechaNacimiento = "1990-09-18", direccion = "Avenida18_numero018_Comuna9", correo = "mail9@gmail.com", telefono = "75737744")
cliente9.save()

cliente10 = Clientes(nombreCompleto = "Cliente10", rut = "000000015", fechaNacimiento = "1997-03-25", direccion = "Avenida19_numero019_Comuna10", correo = "mail10@gmail.com", telefono = "55292812")
cliente10.save()

pedido1 = Pedidos(productos= producto3 , clientes = cliente1, fueEntregado = True , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido1.save()

pedido2 = Pedidos(productos= producto7 , clientes = cliente2, fueEntregado = True , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido2.save()

pedido3 = Pedidos(productos= producto1 , clientes = cliente3, fueEntregado = False , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido3.save()

pedido4 = Pedidos(productos= producto3 , clientes = cliente4, fueEntregado = False , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido4.save()

pedido5 = Pedidos(productos= producto9 , clientes = cliente5, fueEntregado = True , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido5.save()

pedido6 = Pedidos(productos= producto4 , clientes = cliente6, fueEntregado = False , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido6.save()

pedido7 = Pedidos(productos= producto7 , clientes = cliente7, fueEntregado = False , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido7.save()

pedido8 = Pedidos(productos= producto3 , clientes = cliente8, fueEntregado = True , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido8.save()

pedido9 = Pedidos(productos= producto2 , clientes = cliente9, fueEntregado = True , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido9.save()

pedido10 = Pedidos(productos= producto6 , clientes = cliente10, fueEntregado = False , fechaPedido = "2019-04-25", fechaDespacho = "2019-05-01")
pedido10.save()

