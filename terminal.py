import os
import requests
from tqdm import tqdm
from clint.textui import progress

class mainterminal:
	def init(self):
		pass

	def helpc(self,*args):
			print("-help -download <url> <prtocol> -show")

	def show(self,*args):
		if len(os.listdir(os.getcwd() + "/download")) == 0:
				print("no download was found")
		else:
			for x in os.listdir(os.getcwd() + "/download"):
				print(x)
		
			

	def download(self,url,protocol):
		if protocol not in ('http', 'https', 'ftp', 'sftp', 'scp', 'tftp'):
			raise ValueError('Invalid protocol specified.')

		self.r = requests.get(f"{protocol}://" + url, stream=True)
		self.path = os.getcwd() + "/download" + "/file.jpg"
		with open(self.path, 'wb') as f:
			self.total_length = int(self.r.headers.get('content-length'))
			for chunk in progress.bar(self.r.iter_content(chunk_size=1024), expected_size=(self.total_length/1024) + 1): 
					if chunk:
						f.write(chunk)
						f.flush()

		print('download finished successfully')



	def loop(self):
		self.commands = {
    	"help": self.helpc,
    	"download": self.download,
    	"show": self.show
		}
		while True:
			self.user_input = input(": ")

 
			self.parts = self.user_input.split()
			self.command = self.parts[0]
			if not self.user_input == 'help' or self.user_input == 'show':
				self.args1 = self.parts[1:]
				self.args2 = self.parts[2:]

			if self.command == "exit":
				break
        		

			if self.command not in self.commands:
				print("Invalid command")
				continue
			try:
				if  self.user_input == 'help' or self.user_input == 'show':
					self.commands[self.command]()
				else:
					self.commands[self.command](self.args1[0],self.args2[0])
			except IndexError:
				print(f"not enough arguments were given for {self.command}")
