import web


urls = (
    '/', 'Home',
    '/register', 'Register'
)

render = web.template.render('Views/Templates/', base="MainLayout")
app = web.application(urls, globals())

# Classes / Routes
class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register("")
    
    def POST(self):
        data = web.input()
        return data

if __name__ == "__main__":
    app.run()