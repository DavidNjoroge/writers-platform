from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Article
from .. import db
from .forms import NewArticle
from flask_login import login_required,login_user,current_user


@main.route('/')
def index():
    """
    view function for the landing page
    """
    articles=Article.query.all()
    return render_template('index.html',articles=articles)
@main.route('/new-article',methods = ['GET', 'POST'])
def new_article():
    '''
    view function for new article
    '''
    form=NewArticle()
    if form.validate_on_submit():
        title=form.title.data
        body=form.body.data
        new_article=Article(title=title,body=body,user=current_user)
        new_article.save_article()
        return render_template('index.html')

    return render_template('new-article.html',form=form)


@main.route('/article/<int:id>')
def article(id):
    '''
    view function for an article
    '''
    article=Article.query.filter_by(id=id).first()
    return render_template('article.html',article=article)

@main.route('/comment/<int:id>',methods=['GET','POST'])
