from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class NewArticle(FlaskForm):
    title=StringField('Title',validators=[Required()])
    body=TextAreaField('body',validators=[Required()])
    submit=SubmitField('Submit')
