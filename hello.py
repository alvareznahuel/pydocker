# Inicio del DEBUG REMOTO.
import time
import os
if os.environ.get('PYTHON_REMOTE_DEBUG') == "ON":
    import ptvsd
    ptvsd.enable_attach("my_secret", address = ('0.0.0.0', 3000))
    print("Esperando conexion del debbuger...")
    ptvsd.wait_for_attach()
    ptvsd.break_into_debugger()
    
# Inicio de la logica del programa.
for i in range(10):
    print("Hola mundo %d!" % i)
for j in range(20):
    print("Chau mundo %d!" % j)

if os.environ.get('PYTHON_REMOTE_DEBUG') == "ON":
    # Finalizacion del DEBUG REMOTO.
    print("Esperando desconexion del debbuger...")
    while ptvsd.is_attached():
        time.sleep(0.5)