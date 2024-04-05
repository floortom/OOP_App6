from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):

    def get(self):
        caloriesForm = CaloriesForm()

        return render_template("calories_form_page.html",
                               caloriesform=caloriesForm)

    def post(self):
        caloriesForm = CaloriesForm(request.form)

        temp = Temperature(caloriesForm.country.data,
                           caloriesForm.city.data).get()

        cal = Calorie(float(caloriesForm.weight.data),
                      float(caloriesForm.height.data),
                      float(caloriesForm.age.data),
                      temp)

        calories = cal.calculate()

        return render_template("calories_form_page.html",
                               caloriesform=caloriesForm,
                               calories=calories,
                               result=True)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default="28")
    country = StringField("Country: ", default="USA")
    city = StringField("City: ", default="San Francisco")
    button = SubmitField("Calculate")


app.add_url_rule("/",
                 view_func=HomePage.as_view("home_page"))
app.add_url_rule("/calories_form",
                 view_func=CaloriesFormPage.as_view("calories_form_page"))

app.run(debug=True)
