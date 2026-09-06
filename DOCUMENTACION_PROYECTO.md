# **DOCUMENTO DE EVALUACIÓN Y EXPOSICIÓN TÉCNICA**

## **GUÍA Y DOCUMENTACIÓN TÉCNICA DE EXPOSICIÓN PROYECTO: TIENDA CARROS**

---

**REPOSITORIO:** [https://github.com/emmanuelpersonal2024-glitch/Proyecto-de-SprintBoot](https://github.com/emmanuelpersonal2024-glitch/Proyecto-de-SprintBoot)  
**APRENDIZ:** *[Nombre del Aprendiz]*  
**INSTRUCTOR:** *Nelson Rincón*  
**PROGRAMA DE FORMACIÓN:** Análisis y Desarrollo de Software (ADSO)  
**FICHA:** *[Número de Ficha]*  

---

### **Tecnologías utilizadas:**

* **Lenguaje:** Java 17 (LTS) / compatible con Java 21  
* **Framework principal:** Spring Boot 3.3.4  
* **Módulos de Spring Boot:**  
  * **Spring Web:** Controladores MVC y API REST (`@Controller`, `@RestController`)  
  * **Spring Data JPA:** Capa de persistencia y abstracción de base de datos con Hibernate  
  * **Spring Boot Starter Thymeleaf:** Motor de plantillas HTML del lado del servidor  
  * **Spring Boot Starter Test:** Pruebas unitarias e integración  
* **Motor de plantillas:** Thymeleaf 3 — Renderizado de vistas HTML dinámicas  
* **Base de datos:**  
  * **MySQL:** Base de datos relacional principal (vía **XAMPP**, puerto `3306`, BD: `tiendaparking`)  
  * **MySQL Connector/J:** Driver oficial JDBC de conexión  
* **Herramienta de construcción:** Apache Maven 3.9+ — Gestión de dependencias y ciclo de vida del proyecto  
* **Patrones y conceptos aplicados:**  
  * **MVC (Model-View-Controller):** Arquitectura principal de la aplicación web  
  * **Repository Pattern (Spring Data JPA):** Capa de abstracción de acceso a datos sin SQL manual  
  * **Service Layer:** Capa intermedia de lógica de negocio y validación  
  * **RESTful API:** Endpoints JSON bajo `/api/carros`, `/api/motores`, `/api/choferes`, `/api/pasajeros`  
  * **Inyección de Dependencias (IoC):** Gestión automática de Beans con `@Autowired`  
  * **ORM (Object-Relational Mapping):** Mapeo objeto-relacional automático con Hibernate (`ddl-auto=update`)  
* **Frontend:**  
  * HTML5 semántico + CSS3 moderno (diseño dark responsive con panel lateral / sidebar de navegación)  
  * Plantillas modulares Thymeleaf en `src/main/resources/templates/`  
* **Herramientas de desarrollo:**  
  * **NetBeans IDE / VS Code / IntelliJ IDEA:** Entornos de desarrollo integrados  
  * **XAMPP:** Servidor local para MySQL y phpMyAdmin  
  * **Postman / Thunder Client:** Pruebas de endpoints de la API REST  

---

## **TABLA DE CONTENIDO**

1. **Introducción al Proyecto.**  
2. **Instalación y Configuración del Entorno (Paso a Paso).**  
3. **Estructura del Proyecto Spring Boot.**  
4. **El Patrón de Diseño MVC (Modelo-Vista-Controlador) y Capas.**  
5. **Explicación de Anotaciones Clave de Spring Boot.**  
6. **Rutas Fijas y Rutas Dinámicas.**  
7. **Flujo de Trabajo Completo de una Petición HTTP (Paso a Paso).**  

---

## **1. Introducción al proyecto**

**TiendaCarros** es una aplicación web empresarial desarrollada sobre el ecosistema **Java 17** y **Spring Boot 3**, diseñada para la administración integral, control de inventario vehicular y gestión del personal operativo asociado a una tienda y estacionamiento automotriz.

El sistema permite registrar, consultar, editar y eliminar cuatro entidades fundamentales:
1. **Carros:** Control de vehículos con Placa, Marca y Modelo.
2. **Motores:** Catálogo técnico de motores con Número de Serie, Tipo de Motor y Cilindraje.
3. **Choferes:** Registro de conductores autorizados con Cédula, Nombre Completo y Licencia de Conducción.
4. **Pasajeros:** Padrón de usuarios del servicio con Cédula y Nombre Completo.

### **¿Qué hace el proyecto?**
Desde el navegador web y a través de clientes externos, el usuario puede:
* **Dashboard Principal:** Visualizar una pantalla de inicio con accesos directos e indicadores interactivos para cada módulo.
* **Gestión Web Completa (CRUD):** Listar en tablas interactivas, registrar mediante formularios validados, modificar registros existentes y eliminar elementos con confirmación.
* **Consultas por Identificador Único:** Buscar y acceder a registros específicos mediante variables directas en la URL (`@PathVariable`).
* **API RESTful Integral:** Consumir todos los recursos del sistema en formato estándar **JSON** con soporte para peticiones cruzadas (`@CrossOrigin`), permitiendo integración con aplicaciones móviles, SPAs (React, Angular, Vue) o herramientas como Postman.

### **¿Por qué es importante?**
Este proyecto demuestra cómo construir una solución backend robusta y escalable aplicando los más altos estándares de la industria:
* **Separación de Responsabilidades:** Arquitectura desacoplada en capas (**Controlador $\rightarrow$ Servicio $\rightarrow$ Repositorio $\rightarrow$ Base de Datos**).
* **Persistencia Moderna con Spring Data JPA:** Eliminación de código SQL repetitivo gracias a `JpaRepository` y el motor Hibernate ORM.
* **Inversión de Control (IoC) e Inyección de Dependencias:** Gestión automatizada del ciclo de vida de los componentes mediante el contenedor de Spring.
* **Enrutamiento Limpio y Semántico:** URLs amigables que combinan rutas fijas para colecciones y rutas dinámicas para recursos puntuales.
* **Sincronización Automática con MySQL:** Creación y actualización transparente de tablas en base de datos mediante la configuración `spring.jpa.hibernate.ddl-auto=update`.

---

## **2. Instalación y configuración del entorno (PASO A PASO)**

### **Paso 1 — Instalar Java Development Kit (JDK 17+)**
1. Descargar el instalador de **Java 17 JDK** o superior desde Oracle o Eclipse Temurin:  
   🔗 [https://www.oracle.com/java/technologies/downloads/#java17](https://www.oracle.com/java/technologies/downloads/#java17)
2. Completar la instalación y configurar la variable de entorno `JAVA_HOME`.
3. Verificar la instalación abriendo una terminal (`cmd` o PowerShell):
   ```bash
   java -version
   ```
   *Debe mostrar: `java version "17.x.x"` o superior.*

---

### **Paso 2 — Instalar Apache Maven**
1. Ir al sitio oficial de descargas de Maven:  
   🔗 [https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi)
2. Descargar el archivo `Binary zip archive` (ej. `apache-maven-3.9.6-bin.zip`).
3. Descomprimir en una ruta local, por ejemplo: `C:\maven\apache-maven-3.9.6`.
4. Agregar `C:\maven\apache-maven-3.9.6\bin` a la variable del sistema `PATH`.
5. Verificar en terminal:
   ```bash
   mvn -version
   ```

---

### **Paso 3 — Instalar e Iniciar XAMPP (MySQL)**
1. Descargar e instalar XAMPP para Windows desde:  
   🔗 [https://www.apachefriends.org/](https://www.apachefriends.org/)
2. Abrir el **Panel de Control de XAMPP**.
3. Hacer clic en **Start** en el módulo **MySQL**.
4. Confirmar que el puerto `3306` quede resaltado en color verde.

---

### **Paso 4 — Configurar la Base de Datos en MySQL**
1. Con MySQL activo en XAMPP, abrir el navegador e ingresar a:  
   👉 `http://localhost/phpmyadmin`
2. Hacer clic en **Nueva** (panel lateral izquierdo).
3. Ingresar el nombre de la base de datos: `tiendaparking`.
4. Hacer clic en **Crear** (Cotejamiento recomendado: `utf8mb4_unicode_ci`).
5. *(Las tablas `carro`, `motor`, `chofer` y `pasajero` serán creadas y actualizadas automáticamente por Hibernate cuando la aplicación inicie).*

---

### **Paso 5 — Verificar el archivo `application.properties`**
Ubicado en `src/main/resources/application.properties`:
```properties
# ===================================================
# Configuración de Spring Boot - tiendaCarros
# ===================================================

# Conexión a MySQL (XAMPP)
spring.datasource.url=jdbc:mysql://localhost:3306/tiendaparking?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
spring.datasource.username=root
spring.datasource.password=
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# JPA / Hibernate - Actualización automática de tablas
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# Puerto del Servidor Web (8081 para no colisionar con Apache en 8080)
server.port=8081

spring.application.name=tiendaCarros-spring
```

---

### **Paso 6 — Compilar y Ejecutar el Proyecto**

#### **Opción A: Desde NetBeans IDE (Recomendado)**
1. Abrir NetBeans IDE $\rightarrow$ **File** $\rightarrow$ **Open Project** $\rightarrow$ Seleccionar la carpeta `tiendaCarros-spring`.
2. Hacer clic derecho sobre el proyecto y seleccionar **Run** (o presionar `F6`).
3. También se puede ejecutar directamente la clase principal: `src/main/java/com/tiendacarros/TiendaCarrosApplication.java` con `Shift + F6`.

#### **Opción B: Desde la Consola con Maven**
En la raíz del proyecto:
```bash
# Limpiar y empaquetar el proyecto
mvn clean package -DskipTests

# Iniciar la aplicación
mvn spring-boot:run
```

---

### **Paso 7 — Verificación y Accesos al Sistema**
Una vez aparezca en la consola el mensaje `Started TiendaCarrosApplication in X.XXX seconds`, el sistema estará operativo en:

* **Panel Web Principal (Dashboard):** [http://localhost:8081/](http://localhost:8081/)
* **Módulo Web de Carros:** [http://localhost:8081/carros](http://localhost:8081/carros)
* **Módulo Web de Motores:** [http://localhost:8081/motores](http://localhost:8081/motores)
* **Módulo Web de Choferes:** [http://localhost:8081/choferes](http://localhost:8081/choferes)
* **Módulo Web de Pasajeros:** [http://localhost:8081/pasajeros](http://localhost:8081/pasajeros)
* **API RESTful (JSON):** `http://localhost:8081/api/carros`, `/api/motores`, etc.

---

## **3. Estructura del Proyecto Spring Boot**

El proyecto implementa la convención estándar de Maven organizada en paquetes semánticos por capa de responsabilidad:

```text
tiendaCarros-spring/
├── pom.xml                                   # Descriptor de dependencias y plugins Maven
└── src/
    └── main/
        ├── java/com/tiendacarros/
        │   ├── TiendaCarrosApplication.java  # Clase principal de arranque (@SpringBootApplication)
        │   │
        │   ├── model/                        # Entidades JPA (Mapeo a tablas MySQL)
        │   │   ├── Carro.java
        │   │   ├── Chofer.java
        │   │   ├── Motor.java
        │   │   └── Pasajero.java
        │   │
        │   ├── repository/                   # Capa de Acceso a Datos (Spring Data JPA)
        │   │   ├── CarroRepository.java
        │   │   ├── ChoferRepository.java
        │   │   ├── MotorRepository.java
        │   │   └── PasajeroRepository.java
        │   │
        │   ├── service/                      # Capa de Lógica de Negocio y Transacciones
        │   │   ├── CarroService.java
        │   │   ├── ChoferService.java
        │   │   ├── MotorService.java
        │   │   └── PasajeroService.java
        │   │
        │   ├── controller/                   # Controladores API RESTful (Respuestas JSON)
        │   │   ├── CarroController.java
        │   │   ├── ChoferController.java
        │   │   ├── MotorController.java
        │   │   └── PasajeroController.java
        │   │
        │   └── web/                          # Controladores Web MVC (Vistas Thymeleaf)
        │       ├── InicioWebController.java
        │       ├── CarroWebController.java
        │       ├── ChoferWebController.java
        │       ├── MotorWebController.java
        │       └── PasajeroWebController.java
        │
        └── resources/
            ├── application.properties        # Configuración de base de datos, JPA y puerto
            ├── static/                       # Recursos estáticos web
            │   └── css/
            │       └── styles.css            # Estilos personalizados (Dark Modern Theme)
            └── templates/                    # Plantillas HTML procesadas por Thymeleaf
                ├── index.html                # Vista de inicio (Dashboard general)
                ├── sidebar.html              # Fragmento reutilizable de barra de navegación
                ├── carros/
                │   ├── lista.html            # Tabla de visualización de carros
                │   └── formulario.html       # Formulario de creación y edición
                ├── choferes/
                │   ├── lista.html
                │   └── formulario.html
                ├── motores/
                │   ├── lista.html
                │   └── formulario.html
                └── pasajeros/
                    ├── lista.html
                    └── formulario.html
```

### **Descripción de los Componentes:**
* **`model/`:** Contiene las clases anotadas con `@Entity` y `@Table`. Representan la estructura física de las tablas en MySQL, con sus campos, constructores, getters y setters.
* **`repository/`:** Interfaces que extienden de `JpaRepository<Entidad, ID>`. Heredan de forma inmediata métodos CRUD como `findAll()`, `findById()`, `save()`, `deleteById()` y `existsById()` sin necesidad de escribir sentencias SQL manuales.
* **`service/`:** Contiene las clases con la anotación `@Service`. Encapsulan la lógica operativa, orquestan las operaciones sobre los repositorios y aplican transformaciones de negocio.
* **`controller/`:** Controladores marcados con `@RestController` y `@CrossOrigin`. Exponen endpoints REST para devolver objetos Java serializados automáticamente en JSON.
* **`web/`:** Controladores marcados con `@Controller`. Atienden peticiones web del navegador, inyectan atributos al modelo (`org.springframework.ui.Model`) y retornan el nombre de la plantilla Thymeleaf a renderizar.
* **`resources/templates/`:** Vistas HTML estructuradas en módulos independientes con directivas Thymeleaf (`th:each`, `th:field`, `th:text`, `th:href`, `th:replace`).

---

## **4. El Patrón de Diseño MVC (Modelo-Vista-Controlador) y Capas**

### **Las 3 Capas Fundamentales del MVC en este Proyecto:**

```text
┌────────────────────────────────────────────────────────┐
│                        VISTA                           │
│  Plantillas HTML + Thymeleaf (resources/templates/)    │
│  - Renderiza datos dinámicos enviados por el Modelo    │
│  - Captura eventos y formularios del usuario           │
└───────────────────────────▲────────────────────────────┘
                            │ (Renderizado / Envío de Formularios)
                            ▼
┌────────────────────────────────────────────────────────┐
│                     CONTROLADOR                        │
│     WebControllers (@Controller) & REST (@RestController)     │
│  - Recibe y gestiona las solicitudes HTTP              │
│  - Invoca a la Capa de Servicio                        │
│  - Carga el 'Model' con datos para la Vista            │
└───────────────────────────▲────────────────────────────┘
                            │ (Inyección @Autowired)
                            ▼
┌────────────────────────────────────────────────────────┐
│                        MODELO                          │
│          Entidades JPA (com.tiendacarros.model)        │
│  - Representa las estructuras de datos del negocio     │
│  - Carro, Chofer, Motor, Pasajero                      │
└────────────────────────────────────────────────────────┘
```

#### **M — Modelo (`model/`):**
Representa la información y reglas estructurales del sistema:
* **Carro:** `placa_carro` (PK), `marca_carro`, `modelo_carro`.
* **Chofer:** `cedula_chofer` (PK), `nombre_completo_chofer`, `licencia_chofer`.
* **Motor:** `numero_serie_motor` (PK), `tipo_motor`, `cilindraje_motor`.
* **Pasajero:** `cedula_pasajero` (PK), `nombre_completo_pasajero`.

#### **V — Vista (`resources/templates/`):**
Es la interfaz gráfica que interactúa con el usuario. Emplea Thymeleaf para enlazar datos del servidor en el HTML sin necesidad de código Java incrustado.

#### **C — Controlador (`controller/` y `web/`):**
Es el coordinador central. Recibe las peticiones entrantes del navegador o de clientes API, procesa los parámetros de entrada, consulta al servicio y decide qué vista mostrar o qué JSON responder.

---

### **Más allá del MVC — Arquitectura Empresarial en Capas**

Para asegurar una alta mantenibilidad y bajo acoplamiento, el proyecto implementa una arquitectura multicapa:

```text
[ CLIENTE (Navegador Web / Postman / App Móvil) ]
                       │
                       ▼ Petición HTTP (GET, POST, PUT, DELETE)
┌──────────────────────────────────────────────────────────────┐
│  CAPA CONTROLADOR (controller/ & web/)                       │
│  - WebController: Retorna plantillas HTML Thymeleaf          │
│  - RestController: Retorna datos serializados en JSON        │
└──────────────────────────────┬───────────────────────────────┘
                               │ Inyección (@Autowired)
                               ▼
┌──────────────────────────────────────────────────────────────┐
│  CAPA DE SERVICIO (service/)                                 │
│  - Centraliza la lógica de negocio y validaciones            │
│  - Desacopla los controladores de la persistencia directa    │
└──────────────────────────────┬───────────────────────────────┘
                               │ Inyección (@Autowired)
                               ▼
┌──────────────────────────────────────────────────────────────┐
│  CAPA DE REPOSITORIO (repository/ - Spring Data JPA)         │
│  - Interfaces tipadas con JpaRepository<Entidad, ID>         │
│  - Métodos CRUD automáticos y consultas optimizadas          │
└──────────────────────────────┬───────────────────────────────┘
                               │ ORM (Hibernate)
                               ▼
┌──────────────────────────────────────────────────────────────┐
│  BASE DE DATOS (MySQL - tiendaparking)                       │
│  - Tablas: carro, chofer, motor, pasajero                    │
└──────────────────────────────────────────────────────────────┘
```

#### **¿Para qué sirve cada capa extra?**
1. **Capa Service (`service/`):** Evita que los controladores contengan lógica de negocio o acceso directo a datos. Si mañana se requiere agregar validaciones de placas, formatos de cédulas o enviar notificaciones, se realiza en el servicio sin alterar la vista ni el controlador.
2. **Capa Repository (`repository/`):** Aísla por completo el acceso a la base de datos. Gracias a Spring Data JPA, se eliminan cientos de líneas de código JDBC manual (`Connection`, `PreparedStatement`, `ResultSet`), delegando la persistencia a Hibernate.
3. **Base de Datos MySQL:** Proporciona integridad referencial, transaccionalidad y almacenamiento seguro y persistente.

---

## **5. Explicación de Anotaciones Clave de Spring Boot**

### **¿Qué es una anotación?**
Una anotación en Java es una directiva o metadato que comienza con el símbolo `@`. Le indica al compilador y al framework Spring cómo debe instanciar, configurar, inyectar o enrutar un componente sin necesidad de escribir extensos archivos XML de configuración.

---

### **A. Anotaciones de Configuración e Inicio**

#### **`@SpringBootApplication`**
* **Ubicación:** `TiendaCarrosApplication.java`
* **Propósito:** Es la anotación central del proyecto. Agrupa tres anotaciones esenciales:
  1. `@SpringBootConfiguration`: Declara la clase como fuente de beans de configuración.
  2. `@EnableAutoConfiguration`: Activa el motor de autoconfiguración de Spring Boot según las dependencias en `pom.xml`.
  3. `@ComponentScan`: Escanea recursivamente el paquete `com.tiendacarros` para registrar automáticamente componentes `@Controller`, `@RestController`, `@Service`, `@Repository`, etc.

---

### **B. Anotaciones de Entidades y Persistencia JPA**

#### **`@Entity`**
* **Ubicación:** `Carro.java`, `Chofer.java`, `Motor.java`, `Pasajero.java`
* **Propósito:** Informa a JPA/Hibernate que la clase representa una entidad mapeada a una tabla relacional en MySQL.

#### **`@Table(name = "...")`**
* **Ubicación:** Modelos JPA
* **Propósito:** Especifica el nombre exacto de la tabla física en la base de datos (ej. `@Table(name = "carro")`).

#### **`@Id`**
* **Ubicación:** Atributos identificadores en los modelos
* **Propósito:** Marca el campo como la Clave Primaria (*Primary Key*) de la tabla.

---

### **C. Anotaciones de Componentes e Inyección**

#### **`@Repository`**
* **Ubicación:** `CarroRepository.java`, `ChoferRepository.java`, etc.
* **Propósito:** Declara la interfaz como componente de acceso a datos. Spring Data JPA genera automáticamente la clase de implementación en tiempo de ejecución.

#### **`@Service`**
* **Ubicación:** `CarroService.java`, `ChoferService.java`, etc.
* **Propósito:** Registra la clase como un componente de servicio de negocio dentro del contenedor de Spring (IoC Container).

#### **`@Autowired`**
* **Ubicación:** Controladores y Servicios
* **Propósito:** Aplica **Inyección de Dependencias** automática. Spring busca el Bean correspondiente en memoria y lo inyecta sin requerir la palabra clave `new`.

---

### **D. Anotaciones de Controladores y Rutas HTTP**

#### **`@Controller`**
* **Ubicación:** `CarroWebController.java`, `InicioWebController.java`, etc.
* **Propósito:** Marca la clase como controlador web MVC tradicional. Sus métodos retornan nombres de plantillas HTML para ser renderizadas por Thymeleaf.

#### **`@RestController`**
* **Ubicación:** `CarroController.java`, `MotorController.java`, etc.
* **Propósito:** Combinación de `@Controller` y `@ResponseBody`. Transforma directamente los objetos devueltos por los métodos en formato **JSON** para clientes API.

#### **`@RequestMapping("/...")`**
* **Ubicación:** A nivel de clase en controladores
* **Propósito:** Define el prefijo base de las URLs atendidas por todos los métodos de la clase (ej. `@RequestMapping("/carros")` o `@RequestMapping("/api/carros")`).

#### **`@CrossOrigin(origins = "*")`**
* **Ubicación:** Controladores REST
* **Propósito:** Habilita el intercambio de recursos de origen cruzado (CORS), permitiendo que aplicaciones frontend en distintos dominios o puertos consuman la API.

#### **`@GetMapping`**
* **Propósito:** Mapea solicitudes HTTP de tipo **GET** (consultas, listados y despliegue de vistas).

#### **`@PostMapping`**
* **Propósito:** Mapea solicitudes HTTP de tipo **POST** (creación de registros o envío de formularios).

#### **`@PutMapping`**
* **Propósito:** Mapea solicitudes HTTP de tipo **PUT** (actualización completa de registros existentes en la API REST).

#### **`@DeleteMapping`**
* **Propósito:** Mapea solicitudes HTTP de tipo **DELETE** (eliminación de registros en la API REST).

---

### **E. Anotaciones de Parámetros**

#### **`@PathVariable`**
* **Propósito:** Extrae una variable incrustada directamente en la ruta de la URL (ej. `@GetMapping("/editar/{placa}")` $\rightarrow$ `@PathVariable String placa`).

#### **`@ModelAttribute`**
* **Propósito:** Mapea y vincula automáticamente los campos enviados desde un formulario HTML `<form th:object="${carro}">` a los atributos de un objeto Java.

#### **`@RequestBody`**
* **Propósito:** Deserializa el cuerpo JSON de una petición HTTP entrante y lo convierte en una instancia de un objeto Java en la API REST.

---

### **Tabla Resumen de Anotaciones del Proyecto:**

| Anotación | Capa / Ubicación | Propósito y Función |
|---|---|---|
| `@SpringBootApplication` | Clase Principal | Inicializa la aplicación, activa autoconfiguración y escaneo de componentes. |
| `@Entity` | Modelo (`model/`) | Define una entidad persistente gestionada por Hibernate/JPA. |
| `@Table` | Modelo (`model/`) | Asocia la clase con la tabla física correspondiente en MySQL. |
| `@Id` | Modelo (`model/`) | Define la Clave Primaria (Primary Key) de la entidad. |
| `@Repository` | Repositorio (`repository/`) | Marca la interfaz como componente DAO/Repository de persistencia. |
| `@Service` | Servicio (`service/`) | Registra la clase como componente con la lógica de negocio del sistema. |
| `@Controller` | Web (`web/`) | Controlador MVC que procesa peticiones y retorna vistas Thymeleaf. |
| `@RestController` | API REST (`controller/`) | Controlador RESTful que procesa peticiones y retorna respuestas en JSON. |
| `@Autowired` | Todas las capas | Inyecta dependencias automáticamente desde el contenedor de Spring. |
| `@RequestMapping` | Controladores | Establece la ruta base o prefijo para los endpoints de la clase. |
| `@CrossOrigin` | Controladores REST | Configura permisos de acceso CORS para clientes externos. |
| `@GetMapping` | Métodos | Enruta peticiones HTTP GET (Lectura y Vistas). |
| `@PostMapping` | Métodos | Enruta peticiones HTTP POST (Creación y Guardado). |
| `@PutMapping` | Métodos | Enruta peticiones HTTP PUT (Actualización en REST). |
| `@DeleteMapping` | Métodos | Enruta peticiones HTTP DELETE (Eliminación en REST). |
| `@PathVariable` | Parámetros | Captura parámetros dinámicos dentro de la URL. |
| `@ModelAttribute` | Parámetros | Vincula los datos de un formulario HTML al objeto del Modelo. |
| `@RequestBody` | Parámetros | Convierte el cuerpo JSON de la petición HTTP en un objeto Java. |

---

## **6. Rutas Fijas y Rutas Dinámicas**

### **¿Qué es una ruta?**
Una ruta (o endpoint) es la dirección URL que el cliente (navegador o Postman) envía al servidor web para solicitar una acción o recurso específico. En Spring Boot, estas rutas se configuran mediante anotaciones en los controladores.

---

### **A. Rutas Fijas (Estáticas)**
Una ruta fija es aquella cuya estructura URL es constante y no varía entre peticiones. Se utiliza para acceder a páginas generales, listas de elementos o formularios de creación.

* **Características:**
  * URL estática y predecible.
  * No incluye variables en la estructura de la ruta.
  * Retorna listados generales, paneles o formularios vacíos.

#### **Tabla de Rutas Fijas del Proyecto:**

| Módulo | Tipo | Método HTTP | URL | Controlador / Método | Descripción / Respuesta |
|---|---|---|---|---|---|
| **Inicio** | Web | `GET` | `/` | `InicioWebController.inicio()` | Carga el Dashboard general (`index.html`) |
| **Carros** | Web | `GET` | `/carros` | `CarroWebController.listar()` | Lista todos los carros (`carros/lista.html`) |
| **Carros** | Web | `GET` | `/carros/nuevo` | `CarroWebController.nuevo()` | Formulario de nuevo carro (`carros/formulario.html`) |
| **Carros** | Web | `POST` | `/carros/guardar` | `CarroWebController.guardar()` | Procesa y guarda el formulario de carro |
| **Carros** | REST | `GET` | `/api/carros` | `CarroController.listar()` | Retorna lista de carros en JSON |
| **Carros** | REST | `POST` | `/api/carros` | `CarroController.crear()` | Crea un nuevo carro desde cuerpo JSON |
| **Motores** | Web | `GET` | `/motores` | `MotorWebController.listar()` | Lista todos los motores |
| **Motores** | Web | `GET` | `/motores/nuevo` | `MotorWebController.nuevo()` | Formulario de nuevo motor |
| **Motores** | Web | `POST` | `/motores/guardar` | `MotorWebController.guardar()` | Guarda datos de motor desde formulario |
| **Motores** | REST | `GET` | `/api/motores` | `MotorController.listar()` | Retorna lista de motores en JSON |
| **Motores** | REST | `POST` | `/api/motores` | `MotorController.crear()` | Crea un nuevo motor desde JSON |
| **Choferes** | Web | `GET` | `/choferes` | `ChoferWebController.listar()` | Lista todos los choferes |
| **Choferes** | Web | `GET` | `/choferes/nuevo` | `ChoferWebController.nuevo()` | Formulario de nuevo chofer |
| **Choferes** | Web | `POST` | `/choferes/guardar` | `ChoferWebController.guardar()` | Guarda datos de chofer desde formulario |
| **Choferes** | REST | `GET` | `/api/choferes` | `ChoferController.listar()` | Retorna lista de choferes en JSON |
| **Choferes** | REST | `POST` | `/api/choferes` | `ChoferController.crear()` | Crea un nuevo chofer desde JSON |
| **Pasajeros** | Web | `GET` | `/pasajeros` | `PasajeroWebController.listar()` | Lista todos los pasajeros |
| **Pasajeros** | Web | `GET` | `/pasajeros/nuevo` | `PasajeroWebController.nuevo()` | Formulario de nuevo pasajero |
| **Pasajeros** | Web | `POST` | `/pasajeros/guardar` | `PasajeroWebController.guardar()` | Guarda datos de pasajero desde formulario |
| **Pasajeros** | REST | `GET` | `/api/pasajeros` | `PasajeroController.listar()` | Retorna lista de pasajeros en JSON |
| **Pasajeros** | REST | `POST` | `/api/pasajeros` | `PasajeroController.crear()` | Crea un nuevo pasajero desde JSON |

---

### **B. Rutas Dinámicas (Con Variables de Ruta)**
Una ruta dinámica contiene uno o más segmentos variables delimitados por llaves `{nombreVariable}`. Permite ejecutar operaciones sobre un recurso individual identificado por su clave primaria.

* **Características:**
  * La URL cambia según el identificador enviado (ej. `/carros/editar/ABC-1234`).
  * Spring captura el valor mediante `@PathVariable` y lo asigna al parámetro del método.
  * Se utiliza para buscar, editar o eliminar registros individuales.

#### **Tabla de Rutas Dinámicas del Proyecto:**

| Módulo | Tipo | Método HTTP | Patrón de URL | Variable | Método Controlador | Acción Realizada |
|---|---|---|---|---|---|---|
| **Carros** | Web | `GET` | `/carros/editar/{placa}` | `{placa}` | `CarroWebController.editar()` | Carga formulario con datos del carro a editar |
| **Carros** | Web | `GET` | `/carros/eliminar/{placa}` | `{placa}` | `CarroWebController.eliminar()` | Elimina el carro y redirige a la lista |
| **Carros** | REST | `GET` | `/api/carros/{placa}` | `{placa}` | `CarroController.buscar()` | Retorna el carro específico en JSON (200 / 404) |
| **Carros** | REST | `PUT` | `/api/carros/{placa}` | `{placa}` | `CarroController.actualizar()` | Actualiza los datos del carro por placa |
| **Carros** | REST | `DELETE` | `/api/carros/{placa}` | `{placa}` | `CarroController.eliminar()` | Elimina el carro por placa (200 / 404) |
| **Motores** | Web | `GET` | `/motores/editar/{numeroSerie}` | `{numeroSerie}` | `MotorWebController.editar()` | Carga formulario de edición de motor |
| **Motores** | Web | `GET` | `/motores/eliminar/{numeroSerie}` | `{numeroSerie}` | `MotorWebController.eliminar()` | Elimina el motor y redirige |
| **Motores** | REST | `GET` | `/api/motores/{numeroSerie}` | `{numeroSerie}` | `MotorController.buscar()` | Retorna el motor específico en JSON |
| **Motores** | REST | `PUT` | `/api/motores/{numeroSerie}` | `{numeroSerie}` | `MotorController.actualizar()` | Actualiza los datos del motor en JSON |
| **Motores** | REST | `DELETE` | `/api/motores/{numeroSerie}` | `{numeroSerie}` | `MotorController.eliminar()` | Elimina el motor por número de serie |
| **Choferes** | Web | `GET` | `/choferes/editar/{cedula}` | `{cedula}` | `ChoferWebController.editar()` | Carga formulario de edición de chofer |
| **Choferes** | Web | `GET` | `/choferes/eliminar/{cedula}` | `{cedula}` | `ChoferWebController.eliminar()` | Elimina el chofer y redirige |
| **Choferes** | REST | `GET` | `/api/choferes/{cedula}` | `{cedula}` | `ChoferController.buscar()` | Retorna el chofer específico en JSON |
| **Choferes** | REST | `PUT` | `/api/choferes/{cedula}` | `{cedula}` | `ChoferController.actualizar()` | Actualiza los datos del chofer |
| **Choferes** | REST | `DELETE` | `/api/choferes/{cedula}` | `{cedula}` | `ChoferController.eliminar()` | Elimina el chofer por cédula |
| **Pasajeros** | Web | `GET` | `/pasajeros/editar/{cedula}` | `{cedula}` | `PasajeroWebController.editar()` | Carga formulario de edición de pasajero |
| **Pasajeros** | Web | `GET` | `/pasajeros/eliminar/{cedula}` | `{cedula}` | `PasajeroWebController.eliminar()` | Elimina el pasajero y redirige |
| **Pasajeros** | REST | `GET` | `/api/pasajeros/{cedula}` | `{cedula}` | `PasajeroController.buscar()` | Retorna el pasajero específico en JSON |
| **Pasajeros** | REST | `PUT` | `/api/pasajeros/{cedula}` | `{cedula}` | `PasajeroController.actualizar()` | Actualiza los datos del pasajero |
| **Pasajeros** | REST | `DELETE` | `/api/pasajeros/{cedula}` | `{cedula}` | `PasajeroController.eliminar()` | Elimina el pasajero por cédula |

---

### **Diferencias Principales: Rutas Fijas vs. Dinámicas**

```text
┌───────────────────────────────────────┬───────────────────────────────────────┐
│              RUTA FIJA                │             RUTA DINÁMICA             │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ URL constante (ej. /carros)           │ URL variable (ej. /carros/editar/ABC) │
│ Aplica sobre colecciones completas    │ Aplica sobre un registro individual   │
│ No requiere @PathVariable             │ Requiere @PathVariable para capturar  │
│ Ejemplos: Listar, Crear, Dashboard    │ Ejemplos: Ver detalle, Editar, Borrar │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

---

## **7. Flujo de Trabajo Completo de una Petición HTTP (Paso a Paso)**

### **¿Qué es una petición HTTP?**
Es el mensaje estandarizado que el cliente (navegador o Postman) envía al servidor web cuando el usuario realiza una acción: acceder a una URL, presionar un botón o enviar un formulario. El servidor la procesa a través de todas sus capas y devuelve una respuesta con código de estado (ej. `200 OK`, `201 Created`, `302 Redirect`, `404 Not Found`).

---

### **Caso 1 — Petición GET de Listado Web (Ruta Fija)**
**Escenario:** El usuario ingresa en el navegador a `http://localhost:8081/carros`.

1. **Paso 1 — Envío de la Petición:** El navegador emite una solicitud `HTTP GET /carros` hacia el puerto `8081`.
2. **Paso 2 — Intercepción por DispatcherServlet:** El servlet frontal de Spring MVC recibe la petición y busca en el mapeo de controladores.
3. **Paso 3 — Ejecución en el Controlador:** Se ejecuta el método `listar(Model model)` de `CarroWebController`.
4. **Paso 4 — Llamada al Servicio:** El controlador invoca a `carroService.listar()`.
5. **Paso 5 — Consulta al Repositorio JPA:** `CarroService` llama a `carroRepository.findAll()`.
6. **Paso 6 — Generación y Ejecución de SQL:** Hibernate genera la sentencia `SELECT * FROM carro;` y la ejecuta en MySQL (`tiendaparking`).
7. **Paso 7 — Mapeo Objeto-Relacional:** Hibernate transforma las filas resultantes en una lista tipada `List<Carro>`.
8. **Paso 8 — Carga del Modelo:** El controlador recibe la lista y la inyecta al modelo con `model.addAttribute("carros", listaCarros)`.
9. **Paso 9 — Renderizado Thymeleaf:** El motor de plantillas toma `carros/lista.html`, itera la lista con `th:each="c : ${carros}"` y genera el HTML final.
10. **Paso 10 — Respuesta al Navegador:** El servidor responde con `HTTP 200 OK` y el usuario visualiza la tabla completa de carros en pantalla.

---

### **Caso 2 — Petición GET con PathVariable (Ruta Dinámica)**
**Escenario:** El usuario hace clic en el botón *Editar* del carro con placa `ABC-123` $\rightarrow$ `GET /carros/editar/ABC-123`.

1. **Paso 1 — Petición Dinámica:** El navegador solicita la URL con la variable incrustada.
2. **Paso 2 — Extracción del Parámetro:** Spring MVC detecta la coincidencia con `/carros/editar/{placa}` y extrae el valor `"ABC-123"` mediante `@PathVariable String placa`.
3. **Paso 3 — Consulta por ID:** `CarroWebController` llama a `carroService.buscar("ABC-123")` $\rightarrow$ `carroRepository.findById("ABC-123")`.
4. **Paso 4 — Recuperación del Registro:** MySQL devuelve la fila correspondiente y Hibernate instancia el objeto `Carro`.
5. **Paso 5 — Carga del Formulario:** El controlador inyecta el objeto encontrado en el modelo: `model.addAttribute("carro", carro)` y retorna `"carros/formulario"`.
6. **Paso 6 — Renderizado con Datos Previos:** Thymeleaf enlaza los atributos a los campos del formulario con `th:field="*{placa_carro}"`, etc.
7. **Paso 7 — Visualización:** El usuario visualiza el formulario precargado listo para modificar.

---

### **Caso 3 — Petición POST desde Formulario Web (Guardar Registro)**
**Escenario:** El usuario completa el formulario y presiona el botón **Guardar**.

1. **Paso 1 — Envío del Formulario:** El navegador envía una solicitud `HTTP POST /carros/guardar` con el cuerpo codificado del formulario.
2. **Paso 2 — Mapeo con `@ModelAttribute`:** Spring instancia un objeto `Carro` y asigna automáticamente los valores de los inputs.
3. **Paso 3 — Invocación del Servicio y Repositorio:** `CarroWebController` llama a `carroService.guardar(carro)` $\rightarrow$ `carroRepository.save(carro)`.
4. **Paso 4 — Ejecución del INSERT/UPDATE:** Hibernate ejecuta en MySQL:
   ```sql
   INSERT INTO carro (placa_carro, marca_carro, modelo_carro) VALUES (?, ?, ?);
   ```
5. **Paso 5 — Redirección (Patrón Post/Redirect/Get):** El controlador añade un mensaje flash y responde con `HTTP 302 Found` (`redirect:/carros`).
6. **Paso 6 — Recarga Limpia:** El navegador realiza automáticamente un nuevo `GET /carros`.
7. **Paso 7 — Resultado:** El usuario ve la lista de carros actualizada con el nuevo registro y una notificación de éxito.

---

### **Caso 4 — Petición a la API RESTful (Consumo JSON)**
**Escenario:** Postman o una aplicación móvil envía una solicitud `GET /api/carros/ABC-123`.

1. **Paso 1 — Solicitud API:** El cliente envía la petición con cabecera `Accept: application/json`.
2. **Paso 2 — Enrutamiento en `@RestController`:** Spring detecta el controlador REST `CarroController`.
3. **Paso 3 — Procesamiento:** El controlador busca el carro a través del servicio y repositorio.
4. **Paso 4 — Serialización JSON:** La librería **Jackson** (integrada en Spring Boot) convierte automáticamente la entidad `Carro` en texto JSON:
   ```json
   {
     "placa_carro": "ABC-123",
     "marca_carro": "Mazda",
     "modelo_carro": "CX-30"
   }
   ```
5. **Paso 5 — Respuesta HTTP:** El servidor retorna `HTTP 200 OK` con cabecera `Content-Type: application/json` y el cuerpo JSON. Si no existe, retorna `HTTP 404 Not Found`.

---

### **Resumen Visual de los 4 Flujos de Trabajo**

```text
========================================================================================
Caso 1: GET Lista Web      Cliente ──GET /carros──► Controller ──► Service ──► Repository ──► MySQL
                           Cliente ◄──HTML (200)── Thymeleaf ◄── Model ◄──────┘

Caso 2: GET Dinámico Web   Cliente ──GET /editar/ABC──► @PathVariable ──► Service ──► MySQL
                           Cliente ◄──Form HTML (200)── Thymeleaf ◄──────┘

Caso 3: POST Formulario    Cliente ──POST /guardar──► @ModelAttribute ──► Save ──► MySQL (INSERT)
                           Cliente ◄──Redirect 302──► GET /carros ──► Lista Actualizada (200)

Caso 4: API RESTful JSON   Postman ──GET /api/carros/ABC──► @RestController ──► Service ──► MySQL
                           Postman ◄──JSON Data (200 OK)── Jackson Converter ◄┘
========================================================================================
```

---

*Documentación técnica y pedagógica desarrollada para el proyecto TiendaCarros — Spring Boot 3 & MySQL.*