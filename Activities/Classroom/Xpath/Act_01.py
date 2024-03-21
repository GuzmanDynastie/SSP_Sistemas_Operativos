from lxml import etree

tree = etree.parse("Activities/Classroom/Xpath/Act_01.xml")

# • Mostrar el nombre del instituto. 
nombre_instituto = tree.xpath("/ies/nombre/text()") 
print(nombre_instituto[0], '\n')

# • Mostrar la página web del instituto sin etiquetas.
pagina_web_instituto = tree.xpath("/ies/web/text()")
print(pagina_web_instituto[0], '\n')

# • Mostrar el nombre de los ciclos formativos sin etiquetas.
nombres_ciclos = tree.xpath("/ies/ciclos/ciclo/nombre/text()")
print(nombres_ciclos, '\n')

# • Mostrar las siglas por las que se conocen los ciclos formativos.
siglas_ciclos = tree.xpath("//@id")
print(siglas_ciclos, '\n')

# • Mostrar los años en los que se publicaron los decretos de los ciclos formativos.
anio_decreto = tree.xpath("//@año")
print(anio_decreto, '\n')

# • Mostrar toda la información de los ciclos formativos de grado medio.
ciclos_grado_medio = tree.xpath("/ies/ciclos/ciclo[grado='Medio']")
for ciclo in ciclos_grado_medio:
    ciclo_id = ciclo.get("id")
    nombre = ciclo.find("nombre").text
    grado = ciclo.find("grado").text
    decreto_año = ciclo.find("decretoTitulo").get("año")
    
    print("id:", ciclo_id)
    print("nombre:", nombre)
    print("grado:", grado)
    print("Año del decreto del título:", decreto_año, '\n')

# • Mostrar los nombres de los ciclos formativos de grado superior.
nombres_grados_superior = tree.xpath("/ies/ciclos/ciclo[grado='Superior']/nombre/text()")
print(nombres_grados_superior, '\n')

# • Mostrar los nombres de los ciclos formativos anteriores a 2010 sin etiquetas.
ciclos_formativos = tree.xpath("/ies/ciclos/ciclo[decretoTitulo/@año < '2010']")
for ciclo_f in ciclos_formativos:
    decreto_anio = ciclo_f.xpath("decretoTitulo/@año")[0]
    print(decreto_anio)
print('\n')

# • Mostrar los nombres de los ciclos formativos de 2008 o de 2010. 
nombres_ciclos_formativos = tree.xpath("/ies/ciclos/ciclo[(decretoTitulo/@año='2008') or (decretoTitulo/@año='2010')]/nombre/text()")
for nombre in nombres_ciclos_formativos:
    print(nombre)