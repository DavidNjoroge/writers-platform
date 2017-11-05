from flask import abort,request,redirect,url_for,render_template
from . import admin_view
from ..models import User,Article,Comment
from .. import db,admin
from flask_login import login_user,logout_user,login_required
# from .forms import RegistrationForm,LoginForm


from flask_admin.contrib.sqla import ModelView

# Flask and Flask-SQLAlchemy initialization here

# admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Comment, db.session))


# admin.add_view(ModelView(User, db.session))
