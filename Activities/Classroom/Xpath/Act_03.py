from lxml import etree

tree = etree.parse("Activities/Classroom/Xpath/Act_03.xml")

# • Mostrar los nombres de los módulos del ciclo de "Sistemas Microinformáticos y Redes".
nombres_modulos_SMR = tree.xpath("/ies/modulos/modulo[ciclo='SMR']/nombre/text()")
print(nombres_modulos_SMR, '\n')

# • Mostrar los nombres de los ciclos formativos que incluyen el módulo "Lenguajes de marcas y sistemas de gestión de información".
nombres_ciclos_formativos = tree.xpath("/ies/modulos/modulo[nombre='Lenguajes de marcas y sistemas de gestión de información']/ciclo/text()")
print(nombres_ciclos_formativos, '\n')

# • Mostrar los nombres de los módulos de ciclos de Grado Superior.
nombres_modulos_ciclos_GS = tree.xpath("/ies/ciclos/ciclo[grado='Superior']/nombre/text()")
print(nombres_modulos_ciclos_GS, '\n')

# • Mostrar los nombres de los módulos de los ciclos formativos cuyo título se aprobó en 2008.
nombres_modulos_ciclos_formativo = tree.xpath("//ciclo[decretoTitulo/@año='2008']/nombre/text()")
print(nombres_modulos_ciclos_formativo, '\n')

# • Mostrar los grados de los ciclos formativos con módulos de primer curso. 
ciclos_con_primer_curso = tree.xpath("//modulo[curso=1]/ciclo")
for ciclo_id in ciclos_con_primer_curso:
    ciclo = tree.xpath(f"//ciclo[@id='{ciclo_id.text}']")
    grado = ciclo[0].find("grado").text
    print(grado)