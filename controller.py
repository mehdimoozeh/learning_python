import web


urls = (
    '/', 'home'
)

app = web.application(urls, globals())

# Classes / Routes
class home:
    def GET(self):
        return "home"

if __name__ == "__main__":
    app.run()