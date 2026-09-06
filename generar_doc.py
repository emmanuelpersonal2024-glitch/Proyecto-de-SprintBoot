import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = Document()

# Configuración de Márgenes
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Paleta de Colores
COLOR_PRIMARY = RGBColor(30, 27, 75)      # Deep Indigo/Navy (#1E1B4B)
COLOR_SECONDARY = RGBColor(79, 70, 229)   # Royal Indigo Accent (#4F46E5)
COLOR_TEXT = RGBColor(30, 41, 59)         # Slate Dark (#1E293B)
COLOR_MUTED = RGBColor(100, 116, 139)     # Slate Gray (#64748B)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(24)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(20)
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_p(text, bold_prefix=None, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TEXT
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(11)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TEXT
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(11)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_callout(text, title='NOTA'):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, 'EEF2FF')
    set_cell_margins(cell, top=130, bottom=130, left=180, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="4F46E5"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f'{title}: ')
    r1.font.name = 'Calibri'
    r1.font.bold = True
    r1.font.size = Pt(10.5)
    r1.font.color.rgb = COLOR_SECONDARY
    
    r2 = p.add_run(text)
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = COLOR_TEXT
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_code_block(code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, 'F8FAFC')
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="12" w:space="0" w:color="CBD5E1"/><w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(15, 23, 42)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ==================== CONTENIDO ====================

add_title('MANUAL TÉCNICO Y ARQUITECTURA SPRING BOOT')
add_subtitle('Proyecto TiendaCarros - Guía Completa de Desarrollo, MVC, Anotaciones y Flujo HTTP')

# ----------------------------------------------------
# SECCIÓN 1
# ----------------------------------------------------
add_h1('1. Introducción al Proyecto')
add_p('El proyecto TiendaCarros representa la transformación integral de una aplicación de escritorio tradicional construida en Java Swing y JDBC nativo hacia una solución web empresarial moderna basada en Spring Boot 3.x.')

add_h2('1.1 Contexto y Objetivos de la Migración')
add_p('En la arquitectura previa de escritorio, las capas de presentación gráfica (JFrame/JPanel), la lógica de eventos y las consultas SQL directas se encontraban estrechamente vinculadas dentro del mismo hilo de ejecución local. Esto limitaba el acceso simultáneo de múltiples usuarios y dificultaba la integración con otros sistemas.')
add_p('Con la adopción de Spring Boot, el sistema alcanza los siguientes objetivos:')
add_bullet('Exposición de servicios web estándar (endpoints REST) que intercambian información en formato JSON con cualquier plataforma o aplicación externa.', 'Capacidad de API REST: ')
add_bullet('Generación de páginas web dinámicas y responsivas utilizando Thymeleaf como motor de plantillas, accesibles mediante cualquier navegador web.', 'Interfaz Web Dinámica: ')
add_bullet('Automatización de las operaciones a la base de datos MySQL eliminando sentencias SQL manuales mediante Spring Data JPA e Hibernate.', 'Capa de Persistencia ORM: ')
add_bullet('Inclusión del servidor Apache Tomcat dentro del propio empaquetado JAR, simplificando el despliegue a un único comando.', 'Servidor Web Embebido: ')

add_h2('1.2 Módulos Funcionales del Sistema')
add_bullet('Administración de la flota vehicular (placa, marca y modelo). Permite el registro, actualización y consulta de vehículos.', 'Módulo de Carros: ')
add_bullet('Control técnico y especificaciones de los motores (número de serie, tipo de combustible/sistema y cilindraje).', 'Módulo de Motores: ')
add_bullet('Registro de conductores y control de sus categorías de licencia de conducir (cédula, nombre completo y licencia).', 'Módulo de Choferes: ')
add_bullet('Padrón de pasajeros y clientes del servicio de transporte (cédula y nombre completo).', 'Módulo de Pasajeros: ')

# ----------------------------------------------------
# SECCIÓN 2
# ----------------------------------------------------
add_h1('2. Instalación y Configuración del Entorno (Paso a Paso)')
add_p('Para desplegar, desarrollar y ejecutar el proyecto TiendaCarros en cualquier estación de trabajo, se deben cumplir los siguientes pasos ordenados:')

add_h2('Paso 1: Verificación e Instalación de Java Development Kit (JDK 17+)')
add_p('Spring Boot 3 requiere Java 17 o superior. Para verificar la versión disponible en la terminal:')
add_code_block('java -version')
add_p('Si no se encuentra instalado o la versión es inferior a 17, descargar e instalar el JDK desde el portal oficial de Oracle o Eclipse Adoptium (Temurin).')

add_h2('Paso 2: Instalación y Configuración de Apache Maven en el PATH')
add_p('Maven administra las dependencias y el ciclo de vida de compilación del proyecto:')
add_bullet('Descargar el paquete binario de Apache Maven (archivo .zip) desde maven.apache.org y descomprimirlo (ejemplo: C:\\maven\\apache-maven-3.9.6).', '1. Descargar y Descomprimir: ')
add_bullet('Agregar la ruta del subdirectorio bin de Maven a la variable del sistema PATH (Variables de Entorno > Path > Nuevo > C:\\maven\\apache-maven-3.9.6\\bin).', '2. Configurar PATH: ')
add_bullet('Verificar en una nueva consola que Maven responda adecuadamente:', '3. Validar: ')
add_code_block('mvn -version')

add_h2('Paso 3: Configuración de la Base de Datos MySQL en XAMPP')
add_p('El aplicativo requiere el motor relacional MySQL activo:')
add_bullet('Iniciar el panel de control de XAMPP y presionar el botón "Start" en el módulo de MySQL.', '1. Iniciar Servicio: ')
add_bullet('Acceder a phpMyAdmin (http://localhost/phpmyadmin) o mediante cliente SQL y ejecutar la sentencia de creación de base de datos:', '2. Crear Base de Datos: ')
add_code_block('CREATE DATABASE IF NOT EXISTS tiendaparking;\nUSE tiendaparking;')
add_p('Nota: Gracias a la propiedad spring.jpa.hibernate.ddl-auto=update, Hibernate creará las tablas requeridas de forma automática al iniciar la aplicación.')

add_h2('Paso 4: Configuración del Archivo application.properties')
add_p('El archivo ubicado en src/main/resources/application.properties centraliza los parámetros de conexión y el puerto del servidor:')
add_code_block('# Conexion a la Base de Datos en MySQL (XAMPP)\nspring.datasource.url=jdbc:mysql://localhost:3306/tiendaparking?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true\nspring.datasource.username=root\nspring.datasource.password=\nspring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver\n\n# Hibernate y JPA\nspring.jpa.hibernate.ddl-auto=update\nspring.jpa.show-sql=true\nspring.jpa.properties.hibernate.format_sql=true\n\n# Puerto del servidor web (8081 evita colisiones con Apache en el 8080)\nserver.port=8081\n\nspring.application.name=tiendaCarros-spring')

add_callout('El puerto 8081 se seleccionó específicamente para prevenir colisiones con el servidor web Apache de XAMPP, el cual por defecto utiliza el puerto 8080.', 'RECOMENDACIÓN TÉCNICA')

add_h2('Paso 5: Compilación y Puesta en Marcha')
add_p('Desde la raíz del proyecto (donde reside el pom.xml), ejecutar:')
add_code_block('# Compilar el proyecto y descargar librerias necesarias\nmvn clean package -DskipTests\n\n# Levantar el servidor embebido Spring Boot\nmvn spring-boot:run')

# ----------------------------------------------------
# SECCIÓN 3
# ----------------------------------------------------
add_h1('3. Estructura del Proyecto Spring Boot')
add_p('El proyecto implementa la estructura estándar Maven con una segmentación limpia de responsabilidades por paquetes:')

add_code_block('tiendaCarros-spring/\n├── pom.xml                                   (Gestor maestro de dependencias y plugins Maven)\n└── src/\n    ├── main/\n    │   ├── java/com/tiendacarros/\n    │   │   ├── TiendaCarrosApplication.java  (Clase Principal con @SpringBootApplication)\n    │   │   ├── model/                        (Entidades JPA / Modelos de datos)\n    │   │   │   ├── Carro.java\n    │   │   │   ├── Motor.java\n    │   │   │   ├── Chofer.java\n    │   │   │   └── Pasajero.java\n    │   │   ├── repository/                   (Interfaces de persistencia Spring Data JPA)\n    │   │   │   ├── CarroRepository.java\n    │   │   │   ├── MotorRepository.java\n    │   │   │   ├── ChoferRepository.java\n    │   │   │   └── PasajeroRepository.java\n    │   │   ├── service/                      (Servicios de logica de negocio transaccional)\n    │   │   │   ├── CarroService.java\n    │   │   │   ├── MotorService.java\n    │   │   │   ├── ChoferService.java\n    │   │   │   └── PasajeroService.java\n    │   │   ├── controller/                   (Endpoints API REST - Retorno de datos JSON)\n    │   │   │   ├── CarroController.java\n    │   │   │   ├── MotorController.java\n    │   │   │   ├── ChoferController.java\n    │   │   │   └── PasajeroController.java\n    │   │   └── web/                          (Controladores MVC Web - Retorno de Vistas)\n    │   │       ├── InicioWebController.java\n    │   │       ├── CarroWebController.java\n    │   │       ├── MotorWebController.java\n    │   │       ├── ChoferWebController.java\n    │   │       └── PasajeroWebController.java\n    │   └── resources/\n    │       ├── application.properties        (Configuracion de BD, JPA y Puerto)\n    │       ├── static/\n    │       │   └── css/style.css             (Hoja de estilos CSS3 moderna)\n    │       └── templates/                    (Vistas HTML dinámicas de Thymeleaf)\n    │           ├── sidebar.html              (Componente reutilizable de navegacion lateral)\n    │           ├── index.html                (Pagina de inicio y dashboard)\n    │           ├── carros/                   (lista.html, formulario.html)\n    │           ├── motores/                  (lista.html, formulario.html)\n    │           ├── choferes/                 (lista.html, formulario.html)\n    │           └── pasajeros/                (lista.html, formulario.html)\n    └── test/                                 (Pruebas automatizadas de integracion)')

# ----------------------------------------------------
# SECCIÓN 4
# ----------------------------------------------------
add_h1('4. El Patrón de Diseño MVC (Modelo-Vista-Controlador) y Capas')
add_p('El patrón arquitectónico MVC desacopla la lógica interna del sistema en tres capas principales, asegurando alta cohesión y bajo acoplamiento:')

add_h2('4.1 Los Tres Pilares del Patrón MVC')
add_bullet('Estructuras que representan los datos y el estado de la aplicación. En Spring Boot corresponde a las entidades JPA mapeadas a las tablas de la base de datos.', '1. Modelo (Model): ')
add_bullet('Capa de representación visual. En el proyecto se compone de plantillas Thymeleaf (.html) que procesan dinámicamente la información para presentarla al usuario final en el navegador.', '2. Vista (View): ')
add_bullet('Cerebro coordinador. Intercepta las solicitudes HTTP, solicita datos a la capa de servicios y selecciona qué vista presentar o qué respuesta serializada emitir.', '3. Controlador (Controller): ')

add_h2('4.2 Cuadro de Capas de la Aplicación')

data_capas = [
    ('Presentación (Vistas)', 'Thymeleaf (.html), CSS3', 'Renderizar la interfaz gráfica, mostrar tablas, formularios y capturar entradas del usuario.'),
    ('Controladores Web', 'CarroWebController, etc. (@Controller)', 'Atender peticiones del navegador, enviar datos a las vistas HTML y procesar formularios.'),
    ('Controladores REST', 'CarroController, etc. (@RestController)', 'Exponer endpoints HTTP para intercambio puro de datos en formato JSON.'),
    ('Lógica de Negocio', 'CarroService, etc. (@Service)', 'Validar reglas de negocio, coordinar transacciones e interactuar con los repositorios.'),
    ('Persistencia / Acceso', 'CarroRepository (@Repository / JPA)', 'Ejecutar operaciones CRUD en MySQL mediante Spring Data JPA sin escribir SQL manual.')
]

t_capas = doc.add_table(rows=len(data_capas) + 1, cols=3)
t_capas.alignment = WD_TABLE_ALIGNMENT.CENTER
t_capas.autofit = False
for col, w in zip(t_capas.columns, [Inches(1.4), Inches(2.2), Inches(2.9)]):
    col.width = w

headers = ['Capa', 'Tecnología / Clase', 'Responsabilidad Principal']
for i, h in enumerate(headers):
    cell = t_capas.cell(0, i)
    set_cell_background(cell, '1E1B4B')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    r = p.add_run(h)
    r.font.name = 'Calibri'
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

for row_idx, data in enumerate(data_capas, start=1):
    bg_hex = 'F8FAFC' if row_idx % 2 == 1 else 'FFFFFF'
    for col_idx, text in enumerate(data):
        cell = t_capas.cell(row_idx, col_idx)
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, 70, 70, 90, 90)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(9.5)
        r.font.color.rgb = COLOR_TEXT

doc.add_paragraph().paragraph_format.space_after = Pt(6)

# ----------------------------------------------------
# SECCIÓN 5
# ----------------------------------------------------
add_h1('5. Explicación de Anotaciones Clave de Spring Boot')
add_p('Las anotaciones son metadatos declarativos que instruyen al contenedor de Spring sobre el rol de cada clase, facilitando la Inversión de Control (IoC) y la Inyección de Dependencias (DI).')

data_annot = [
    ('@SpringBootApplication', 'Principal (Main)', 'Marca la clase de arranque. Activa autoconfiguracion, escaneo de paquetes y configuracion de Spring.'),
    ('@Entity', 'Modelo (JPA)', 'Declara que la clase Java (ej: Carro) representa una tabla relacional en la base de datos.'),
    ('@Table(name="...")', 'Modelo (JPA)', 'Especifica el nombre exacto de la tabla en MySQL (ej: @Table(name="carro")).'),
    ('@Id', 'Modelo (JPA)', 'Define el atributo que actua como Clave Primaria (Primary Key) de la entidad.'),
    ('@Repository', 'Persistencia', 'Indica que la interfaz es un DAO gestionado por Spring para operaciones sobre la base de datos.'),
    ('@Service', 'Negocio', 'Declara una clase de servicio que concentra la logica de negocio y reglas de validacion.'),
    ('@Controller', 'Controlador Web', 'Marca una clase que procesa peticiones web y retorna el nombre de una vista HTML (Thymeleaf).'),
    ('@RestController', 'Controlador REST', 'Combina @Controller y @ResponseBody. Retorna directamente objetos en formato JSON.'),
    ('@Autowired', 'Inyeccion (DI)', 'Inyecta automaticamente dependencias (ej: inyectar CarroRepository dentro de CarroService).'),
    ('@RequestMapping', 'Controlador', 'Define el prefijo base de las URLs atendidas por la clase (ej: @RequestMapping("/carros")).'),
    ('@GetMapping', 'Enrutamiento HTTP', 'Mapea solicitudes HTTP GET para consultar datos o solicitar una pagina web.'),
    ('@PostMapping', 'Enrutamiento HTTP', 'Mapea solicitudes HTTP POST para registrar nuevos datos o procesar formularios.'),
    ('@PathVariable', 'Parametros', 'Extrae valores dinamicos contenidos en la URL (ej: /carros/editar/{placa} -> @PathVariable String placa).'),
    ('@ModelAttribute', 'Formularios Web', 'Vincula los campos de un formulario HTML directamente con un objeto Java del modelo.')
]

t_annot = doc.add_table(rows=len(data_annot) + 1, cols=3)
t_annot.alignment = WD_TABLE_ALIGNMENT.CENTER
t_annot.autofit = False
for col, w in zip(t_annot.columns, [Inches(1.8), Inches(1.8), Inches(2.9)]):
    col.width = w

headers_annot = ['Anotación', 'Capa / Contexto', 'Función y Caso de Uso en el Proyecto']
for i, h in enumerate(headers_annot):
    cell = t_annot.cell(0, i)
    set_cell_background(cell, '1E1B4B')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    r = p.add_run(h)
    r.font.name = 'Calibri'
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

for row_idx, data in enumerate(data_annot, start=1):
    bg_hex = 'F8FAFC' if row_idx % 2 == 1 else 'FFFFFF'
    for col_idx, text in enumerate(data):
        cell = t_annot.cell(row_idx, col_idx)
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(9.5)
        if col_idx == 0:
            r.font.bold = True
            r.font.color.rgb = COLOR_SECONDARY
        else:
            r.font.color.rgb = COLOR_TEXT

doc.add_paragraph().paragraph_format.space_after = Pt(6)

# ----------------------------------------------------
# SECCIÓN 6
# ----------------------------------------------------
add_h1('6. Rutas Fijas y Rutas Dinámicas')
add_p('El sistema de enrutamiento de Spring MVC asocia las solicitudes que ingresan al servidor hacia los métodos correspondientes en las clases controladoras.')

add_h2('6.1 Rutas Fijas (Estáticas)')
add_p('Son direcciones URL constantes que no varían en su estructura y no dependen de parámetros posicionales. Se emplean principalmente para cargar vistas globales, menús o formularios vacíos:')
add_bullet('http://localhost:8081/  → Página principal de navegación (Dashboard general).', 'Inicio: ')
add_bullet('http://localhost:8081/carros  → Lista general de todos los carros registrados en el sistema.', 'Listado de Carros: ')
add_bullet('http://localhost:8081/carros/nuevo  → Despliega el formulario para registrar un vehículo nuevo.', 'Formulario Nuevo Carro: ')
add_bullet('http://localhost:8081/api/motores  → Endpoint REST que retorna el arreglo JSON de todos los motores.', 'Endpoint REST Motores: ')

add_p('Ejemplo de implementación en código:')
add_code_block('@GetMapping("/carros/nuevo")\npublic String mostrarFormularioNuevo(Model model) {\n    model.addAttribute("carro", new Carro());\n    model.addAttribute("titulo", "Nuevo Carro");\n    return "carros/formulario"; // Resuelve a templates/carros/formulario.html\n}')

add_h2('6.2 Rutas Dinámicas (Con Variables de Ruta)')
add_p('Son URLs que incorporan valores variables dentro de su estructura delimitados por llaves {parametro}. Se utilizan para realizar operaciones sobre un recurso específico determinado por su identificador único:')
add_bullet('http://localhost:8081/carros/editar/ABC-1234  → Carga los datos del carro cuya placa sea "ABC-1234".', 'Editar Carro: ')
add_bullet('http://localhost:8081/carros/eliminar/XYZ-9876  → Elimina el registro del vehículo identificado con dicha placa.', 'Eliminar Carro: ')
add_bullet('http://localhost:8081/api/choferes/10203040  → Endpoint REST que retorna exclusivamente el JSON del chofer con esa cédula.', 'API REST Chofer: ')

add_p('Ejemplo de captura del parámetro dinámico con @PathVariable:')
add_code_block('@GetMapping("/carros/editar/{placa}")\npublic String mostrarFormularioEditar(@PathVariable("placa") String placa, Model model) {\n    Carro carro = carroService.buscar(placa);\n    if (carro == null) {\n        return "redirect:/carros"; // Redirige si el recurso no existe\n    }\n    model.addAttribute("carro", carro); // Adjunta el objeto al modelo para la vista\n    model.addAttribute("titulo", "Editar Carro");\n    return "carros/formulario";\n}')

# ----------------------------------------------------
# SECCIÓN 7
# ----------------------------------------------------
add_h1('7. Flujo de Trabajo Completo de una Petición HTTP (Paso a Paso)')
add_p('A continuación se documenta el recorrido secuencial que realiza una petición desde el cliente hasta la respuesta final.')

add_h2('7.1 Diagrama del Ciclo de Vida de una Petición')
add_code_block('[1. Navegador / Cliente HTTP]\n             │ (Envia peticion GET http://localhost:8081/carros)\n             ▼\n[2. Servidor Tomcat Embebido]\n             │ (Acepta conexion TCP en el puerto 8081)\n             ▼\n[3. DispatcherServlet (Front Controller)]\n             │ (Consulta HandlerMapping para ubicar el controlador adecuado)\n             ▼\n[4. CarroWebController (Capa de Control)]\n             │ (Ejecuta metodo listar(), invoca al servicio)\n             ▼\n[5. CarroService (Capa de Negocio)]\n             │ (Aplica reglas y llama al repositorio)\n             ▼\n[6. CarroRepository / Hibernate (Capa de Persistencia)]\n             │ (Traduce a consulta SQL: SELECT * FROM carro)\n             ▼\n[7. Base de Datos MySQL (tiendaparking)]\n             │ (Retorna filas de la tabla)\n             ▼\n[8. Hibernate convierte filas en objetos List<Carro>]\n             ▼\n[9. CarroWebController agrega lista al objeto Model]\n             ▼\n[10. Thymeleaf procesa templates/carros/lista.html y combina el HTML con los datos]\n             ▼\n[11. Se envia el documento HTML final renderizado con codigo 200 OK al Navegador]')

add_h2('7.2 Análisis Detallado de los Dos Escenarios de Uso')

add_p('1. Caso de Flujo Web (MVC con Thymeleaf):', 'Escenario A: ')
add_p('Cuando el usuario ingresa a "http://localhost:8081/carros", el método listar() de CarroWebController recibe una instancia de org.springframework.ui.Model. El controlador solicita la lista de registros a CarroService, la deposita en el modelo mediante model.addAttribute("carros", lista) y retorna el nombre lógico "carros/lista". El motor Thymeleaf localiza el archivo templates/carros/lista.html, itera la colección con la directiva th:each="carro : ${carros}" rellenando la tabla HTML con los datos de la base de datos, y despacha el documento HTML completo al navegador.')

add_p('2. Caso de Flujo REST (API JSON):', 'Escenario B: ')
add_p('Cuando un cliente externo o aplicación móvil envía una petición POST a "http://localhost:8081/api/carros" con un cuerpo JSON como {"placa_carro":"XYZ-999","marca_carro":"Mazda","modelo_carro":"CX-30"}, Spring activa el convertidor de mensajes Jackson. Éste deserializa el JSON transformándolo en un objeto Java Carro, el cual es transferido al método crear(@RequestBody Carro carro) en CarroController. El servicio y el repositorio ejecutan la inserción en MySQL y devuelven un objeto ResponseEntity con código de estado HTTP 201 Created y el recurso en formato JSON.')

# Guardar documento
doc_path = os.path.abspath('Manual_Proyecto_Spring_Boot_TiendaCarros.docx')
doc.save(doc_path)
print(f'EXITO: Documento creado en {doc_path}')