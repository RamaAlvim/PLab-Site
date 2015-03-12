
def write(cmd):
	import visa;
	rm = visa.ResourceManager("@py")
	inst = rm.open_resource("TCPIP::192.168.134.102")

	inst.write(cmd)

