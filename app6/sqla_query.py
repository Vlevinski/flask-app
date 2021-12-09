from flask import jsonify
from app6 import create_app, db
from flask_admin import Admin
from flask_admin.menu import MenuLink  # https://flask-admin.readthedocs.io/en/latest/_modules/flask_admin/base/
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
#from app6.model import Post, Category
from app6.model import Post, Currency , Category

def is_db(name):
    """ Check User DB """
    import os.path
    if not os.path.isfile(name):
        db.drop_all()
        db.create_all()
        # py = Category(name='Python')
        # Post(title='Hello Python!', body='Python is pretty cool', category=py)

        # p = Post(title='The second post: Snakes', body='Ssssssss')
        # py.posts.append(p)
        # db.session.add(py)
        # db.session.commit()


class MyView(BaseView):
    @expose('/')
    def index(self):
        return 'Hello World!'


app = create_app()
app.config['FLASK_ADMIN_SWATCH'] = 'journal'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testn.db"

db.init_app(app)
app.app_context().push()
is_db('testn.db')


'''
admin = Admin(app, name='microblog', template_mode='bootstrap4')
#admin.add_view(MyView(name='My View'))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Currency, db.session))

#admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))

admin.add_view(ModelView(Currency, db.session))
admin.add_view(ModelView(TransferFrom, db.session))
admin.add_view(ModelView(Trustee, db.session))
admin.add_view(ModelView(Vehicle, db.session))
admin.add_view(ModelView(Company, db.session))
admin.add_view(ModelView(Transactions, db.session))
admin.add_view(ModelView(Investments, db.session))
admin.add_view(ModelView(Summary, db.session))
admin.add_view(ModelView(Settings, db.session))

@app.route("/")
def home_view():
    return "<div> Welcome Home. <br> <br> &nbsp &nbsp &nbsp -->  <a href='/admin'> admin</a></div>"


app.run()
'''

data_p = Post.query.all()
values = [{idx: k for idx, k in row.__dict__.items() if '_sa_' not in idx} for row in data_p]
print(data_p)
for item in values:
    print(item)
print(" ")
data_cur = Currency.query.all()
values_c = [{idx: k for idx, k in row.__dict__.items() if '_sa_' not in idx} for row in data_cur]


print(data_cur)
for item in values_c:
    print(item)
