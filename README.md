# FastAPI Application with Docker Compose

Este proyecto es una aplicación FastAPI configurada para ejecutarse con Docker Compose. Incluye servicios para PostgreSQL, Redis y Swagger UI para la documentación de la API.

## Requisitos

- Docker
- Docker Compose
- Make (opcional, pero recomendado para simplificar comandos)

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

    ```env
    DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
    REDIS_URL=redis://redis:6379/0
    ```

3. Instala las dependencias de Python (opcional, si deseas ejecutar la aplicación localmente sin Docker):

    ```sh
    pip install -r requirements.txt
    ```

## Uso

### Con Docker Compose

Para levantar los contenedores, ejecutar los siguientes comandos:

- Levantar los contenedores:

    ```sh
    make up
    ```

- Detener los contenedores:

    ```sh
    make down
    ```

- Reiniciar los contenedores:

    ```sh
    make restart
    ```

- Ver los logs de todos los contenedores:

    ```sh
    make logs
    ```

- Ver los logs del contenedor de la aplicación:

    ```sh
    make logs-app
    ```

- Ver los logs del contenedor de la base de datos:

    ```sh
    make logs-db
    ```

- Ver los logs del contenedor de Redis:

    ```sh
    make logs-redis
    ```

- Ver los logs del contenedor de Swagger UI:

    ```sh
    make logs-swagger
    ```

- Ver el estado de los contenedores:

    ```sh
    make ps
    ```

- Limpiar el sistema Docker:

    ```sh
    make clean
    ```

### Sin Docker Compose

Si prefieres ejecutar la aplicación localmente sin Docker, asegúrate de tener PostgreSQL y Redis instalados y configurados. Luego, ejecuta:

```sh
uvicorn app.main:app --reload
```