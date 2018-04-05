from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
import cgi

main_html = "<html><body>%s</body></html>"

# class HomePage extend class Resource 
class HomePage(Resource):
	# Fungsi untuk menangani request GET
	def render_GET(self, request):
		return main_html % "Hello World Selamat Siang"

# class UserPage extend class Resource
class UserPage(Resource):
	isLeaf = True
	# Fungsi untuk menangani request GET dengan parameter "username"
	def render_GET(self, request):
		try :
			username = request.args["username"][0]
		except KeyError :
			username = ""
		return main_html % "Username anda adalah : "+username

# class FormPage extend class Resource
class FormPage(Resource):
	# Fungsi untuk menangani request GET
    def render_GET(self, request):
        return '<html><body><form method="POST"><input name="data" type="text" /> <input type="submit" value="Submit" /></form></body></html>'

    # Fungsi untuk menangani request POST
    def render_POST(self, request):
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["data"][0]),)

# Root resource
root = Resource()
# Akses ke /
root.putChild("", HomePage())
# Akses ke /user
root.putChild("user", UserPage())
# Akses ke /form
root.putChild("form", FormPage())
# Akses ke /file, list static file
root.putChild("file", File('./'))
# Jalankan server
factory = Site(root)
reactor.listenTCP(80, factory)
reactor.run()
