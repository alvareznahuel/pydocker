import ptvsd
ptvsd.enable_attach("my_secret", address = ('0.0.0.0', 3000))
#Enable the below line of code only if you want the application to wait untill the debugger has attached to it
ptvsd.wait_for_attach()
for i in range(10):
    print("Hola mundo %d!" % i)