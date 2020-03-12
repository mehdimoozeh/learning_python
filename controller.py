import web
from Models import UserModel
import bcrypt

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login'
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
        registration = UserModel.UserModel()
        hashed_password = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        _id = registration.insert_user(data.username, hashed_password, data.fullname)
        return _id

class Login:
    def GET(self):
        return render.Login()
    
    def POST(self):
        data = web.input()
        user_model = UserModel.UserModel()
        user = user_model.find_user(data.username)
        if user and bcrypt.checkpw(data.password.encode(), user["password"]):
            return user["fullname"]
        else:
            return "error"

            

if __name__ == "__main__":
    app.run()