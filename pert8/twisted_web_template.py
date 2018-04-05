from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import cgi
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader( searchpath="./templates" ))

# class HomePage extend class Resource 
class HomePage(Resource):
	# Fungsi untuk menangani request GET
	def render_GET(self, request):
		# Render dari template home.html
		template = env.get_template('home.html')
		templateVars = { "username" : "Bhawiyuga", "alamat" : "Malang"
        }
		return str(template.render(templateVars))

# Root resource
root = Resource()
# Akses ke /
root.putChild("", HomePage())
# Jalankan server
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()