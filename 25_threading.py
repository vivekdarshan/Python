import threading


class ViveksMessenger(threading.Thread):
	def run(self):
		for _ in range(10):
			print(threading.currentThread().getName())

x = ViveksMessenger(name = 'Send out Messages')
y = ViveksMessenger(name = 'Receive Messages')
x.start()
y.start()