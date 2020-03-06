import web


urls = (
    '/', 'home',
    '/register', 'register'
)

render = web.template.render('Views/Templates/', base="MainLayout")
app = web.application(urls, globals())

# Classes / Routes
class home:
    def GET(self):
        return render.Home()

class register:
    def GET(self):
        return render.Register()

if __name__ == "__main__":
    app.run()