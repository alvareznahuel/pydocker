# pydocker
Configuración para desarrollar y probar python sobre docker.

# Configuración launch.json

    "configurations": [
        ...
        {
            "name": "Python: Attach",
            "type": "python",
            "request": "attach",
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/usr/src/app",
            "port": 3000,
            "secret": "my_secret",
            "host": "localhost"
        },
        ...
    ]

# Mejoras al proceso de DEBUG.

Se incorpora una variable de entorno para habilitar el DEBUG remoto.
Inicialmente se definieron dos entornos posibles:

- normal.env: Ejecuta normalmente el script.
- debug.env: Espera la conexión del debugger y su posterior desconexión. Por el momento no soporta el reiniciar la ejecución desde el debugger.

A partir de estos cambios la forma correcta de ejecutar el docker es con:

./run.sh archivo.env

