from flask import Flask, render_template
import db_functions as db


#vytvořila jsem novou aplikaci s názvem ivuška ve Flasku
application = Flask('ivuska')


@application.route('/')
def show_index():
    return render_template('title.html')

@application.route('/acitivities')
def show_activities():
    activities = db.get_activities()
    return render_template('activities.html', activities = activities)