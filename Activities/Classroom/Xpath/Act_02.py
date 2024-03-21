from lxml import etree

tree = etree.parse("Activities/Classroom/Xpath/Act_02.xml")

# • Mostrar el nombre sin etiquetas de los módulos que se imparten en el instituto.
nombres_modulos = tree.xpath("/ies/modulos/modulo/nombre/text()")
print(nombres_modulos, '\n')

# • Mostrar el nombre de los módulos que se imparten en ciclo formativo ASIR.
nombres_modulo_ASIR = tree.xpath("/ies/modulos/modulo[ciclo='ASIR']/nombre/text()")
print(nombres_modulo_ASIR, '\n')

# • Mostrar el nombre de los módulos que se imparten en segundo curso de cualquier ciclo formativo.
nombres_modulos_curso2 = tree.xpath("/ies/modulos/modulo[curso='2']/nombre/text()")
print(nombres_modulos_curso2, '\n')

# • Mostrar el nombre de los módulos que tengan menos de 5 horas semanales.
nombres_modulos_menor_5hr = tree.xpath("/ies/modulos/modulo[horasSemanales < '5']/nombre/text()")
print(nombres_modulos_menor_5hr, '\n')

# • Mostrar el nombre de los módulos que se imparten en el primer curso del ciclo formativo ASIR.
nombres_modulos_ciclo1_ASIR = tree.xpath("/ies/modulos/modulo[curso='1' and ciclo='ASIR']/nombre/text()")
print(nombres_modulos_ciclo1_ASIR, '\n')

# • Mostrar las horas semanales sin etiquetas de los módulos que se imparten en más de 3 horas semanales.
horas_semanales = tree.xpath("/ies/modulos/modulo[horasSemanales > '3']/horasSemanales/text()")
print(horas_semanales, '\n')