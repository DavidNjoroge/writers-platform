from flask import abort,request,redirect,url_for,render_template
from . import admin_view
from ..models import User,Article,Comment
from .. import db,admin
from flask_login import login_user,logout_user,login_required,current_user
# from .forms import RegistrationForm,LoginForm


from flask_admin.contrib.sqla import ModelView

# Flask and Flask-SQLAlchemy initialization here

# admin = Admin(app, name='microblog', template_mode='bootstrap3')


# admin.add_view(ModelView(User, db.session))
class AdminModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))



admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Article, db.session))
admin.add_view(AdminModelView(Comment, db.session))
