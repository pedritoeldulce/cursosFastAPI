# FASTAPI

- Interfaces de programacion de aplicaciones.

## ¿Què es FastApi?
- Es un marco web moderno y de alto rendimineto para crear API con Python.

- Caracterìsticas:
    - Rapido de Ejecutar: rendimiento muy alto, a la par de NodeJS y Go, gracias a Starlette y pydantic.
    - Rapido de COdificar:
    - Nùmero reducido de errores: reduce los errores inducidos por humanos.
    - Intuitivo: Ofrece un soporte de editor.
    - Sencillo: Documentacion fàcil de leer.
    - Short: Minimiza la ducplicacion de còdigo.
    - Robusto: Proporciona còdigo listo para la produccion con documentacion interactica automatica.
    . Basada en standares: se basa en standares API, OpenAPi, y Json Schema.


## Instalar FastAPi

- Primer paso instalar FastAPI yu Uvicorn usando pip:

        python -m pip install fastapi uvicorn[standar]

## Primeros Pasos
- crea una aplicacion FastApi minima, la ejecutarà en un servidor usando Uvicorn y luego aprenderà todas las partes que interactuan.

### Crear una primara API
- Un archivo bàsico FastAPI se ve asì:

        from fastapi import FastAPI

        app = FastAPI()

        @app.get('/')
        async def root():
        return {"message":"HOLA MUNDO!!!"}

- para ejecutarlo necesita un servidor.

### Ejecuta la aplicacion con Uvicorn

        # uvicorn main:app --reload

- -- reload: usado para desarrollo, se actualiza cada que ay un cambio, el servidor se recargarà automaticamente.


### Verifique su respuesta

Abra su navegador en http://127.0.0.1, su navegador enviarà una solicitud a la aplicaciòn. luego se recibe una respues JSON con lo siquiente:

        {"message": "HOLA NOA!!!"}

### Consulta la Documentaciòn de la API interactiva

- Abrir http://127.0.0.1:8000/docs en el navegador (pòr defecto FastAPI funciona en el puerto 8000).
. Verà la documentacion de la API interactiva automatica proporcionada por SwaggerUI:

### Documentacion de la API interactiva alternativa.

- Abrir http://127.0.0.1:8000/redoc en el navegador.

## La Primera API, paso a paso

- Paso 1: importar FastAPI:

        from fastapi import FastAPI

FastAPI es una clase de Python que proporciona toda la funcionalidad para su API.

- Paso 2: crear una instancia FastAPI.

        app = FastAPI()

la variable `app` serà una instancia de la clase FastAPI, serà el punto principal de interaccion para creat la API.

`app` es el mismo al que se refirio en el comando para ejecutar el servidor con uvicorn.

        # uvicorn main:app --reload

- Algunos tèrminos para familiarizarse.

* ruta: se refiere a la ùltima parte de la URL. en una URL http://example.com/items/foo, la ruta serìa `/items/foo`. 

- La ruta es la forma principal para separar los recursos.

- Otros tèrminos que se debe conocer es son las operaciones, que se usan como referencia a cualquiera de los `metodos de solicitudes HTTP`:
    - POST, GET, PUT, DELETE, OPTIONS, HEAD, PATCH, TRACE.

- Con HTTP puede comunicarse con cada ruta usando una (o màs) de esas operaciones.

- PASO 3: Definir un __decorador de operacion de  ruta__

        @app.get('/')
        async def root():
            return {"message": "HOLA NOA!!!"}

- El `@app.get('/')` le dice a FAstAPI que la funciòn debajo està a cargo  de manejar las solicitudes que van a la ruta `/` usando una operaciòn `get`
- Este es un decorador relacionado con una operacion de ruta o un decorador de opracion de ruta.

- otras operaciones mencionadas:
    @app.post(), ......@app.trace()

- Paso 4: Definir __funciòn de operaciòn de ruta__, o la funciòn de va debajo del decorador de operacion de ruta.

        async def root():

- FastAPI llamarà a esta funcion cada vez que reciba una solictud a la URL espeficica(/) mediante una operacion GET. en este caso es una funciòn `async`.

- Tambien podrìa definirlo como una funcion normal en lugar de usar async: def.

- Paso 5: __devolver__ el contenido:

        return {"message":"HOLA NOA!!!"}

- Puede devolver un diccionario, una lista o valores singulares como cadenas, enteros, etc. Tambien puede devolver modelos `pydantic`.
- Hay otros objetos y modelos que se convertiran automaticamente en JSON.