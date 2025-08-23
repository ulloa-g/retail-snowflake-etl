# retail-snowflake-etl

Desde la página principal de **Snowsight**, vamos a crear una nueva carpeta para mantener el proyecto organizado. Le vamos a dar el nombre de *first_sf_etl*
![](img/00_create_folder.png)

Dentro de nuestra carpeta de proyecto vamos a crear un nuevo `SQL Worksheet`.
![](img/01_create_sql_worksheet.png)

Pegar el contenido del archivo `sql/01_init_objects.sql`. Aquí podemos renombrar los worksheets y luego ejecutamos todas las sentencias SQL. Abajo en "status" vemos que se ejecutó sin problemas.
![](img/02_run_init_objects_sql.png)

Repetimos el proceso para los archivos `sql/02_create_dim_tables.sql` y `sql/03_create_fact_table.sql`.
![](img/03_create_tables.png)

Si ingresamos desde el panel a **Databases** podemos observar nuestro trabajo hasta ahora.
![](img/04_results.png)
