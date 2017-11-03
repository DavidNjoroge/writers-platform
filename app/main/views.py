from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from .. import db
from .forms import NewArticle


@main.route('/')
def index():
    """
    view function for the landing page
    """

    return render_template('index.html')
@main.route('/new-article')
def new_article():
    '''
    view function for new article
    '''
    form=NewArticle()
    if form.validate_on_submit():
        title=form.title.data
        body=form.body.data
        new_pitch=Pitch(title=title,body=body,user=current_user)

    return render_template('new-article.html',form=form)
