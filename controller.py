import web
from Models import UserModel, PostModel
import bcrypt

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/post', 'Post'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer


render = web.template.render('Views/Templates/', base="MainLayout", globals={'session': session_data, 'currentUser': session_data["user"]})

# Classes / Routes
class Home:
    def GET(self):
        post_model = PostModel.PostModel()
        posts = []
        if session_data['user'] != None:
            posts = post_model.find_user_posts(session_data['user']['username'])
        return render.Home(posts)

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
            session_data["user"] = user
            return user["fullname"]
        else:
            return "error"

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"

class Post:
    def POST(self):
        data = web.input()
        user = session_data['user']['username']

        post_model = PostModel.PostModel()
        _id = post_model.insert_post(user, data["post-text"])
        if _id:
            return _id
        else:
            return 'error'



            

if __name__ == "__main__":
    app.run()