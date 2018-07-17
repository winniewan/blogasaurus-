import webapp2
import os
import jinja2


#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("home.html")
        self.response.write(template.render())
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("blog.html")
        self.response.write(template.render())
class AboutMe(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("AboutMe.html")
        self.response.write(template.render())
app = webapp2.WSGIApplication([
    ('/', MainHandler), ("/Blogs", BlogHandler),("/AboutMe",AboutMe)
], debug=True)
