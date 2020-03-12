import web
from Models import RegisterModel
import bcrypt

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
        registration = RegisterModel.RegisterModel()
        hashed_password = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        _id = registration.insert_user(data.username, hashed_password, data.fullname)
        return _id

if __name__ == "__main__":
    app.run()