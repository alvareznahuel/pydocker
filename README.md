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
            "remoteRoot": "${workspaceFolder}",
            "port": 3000,
            "secret": "my_secret",
            "host": "localhost"
        },
        ...
    ]
      