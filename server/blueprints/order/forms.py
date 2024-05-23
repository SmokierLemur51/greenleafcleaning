from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


"""
class NewEmployeeForm(FlaskForm):

    f_name = StringField("First Name", validators=[DataRequired()])
    m_name = StringField("Middle Name", validators=[DataRequired()])
    l_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    # role = select field for all roles
    phone = StringField("Phone Number", validators=[DataRequired()])
    street = StringField("Street", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    zip = StringField("Zip Code", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
    # hotel select field

"""

