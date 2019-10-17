from flask import Flask, render_template

#vytvořila jsem novou aplikaci s názvem ivuška ve Flasku
application = Flask('ivuska')


@application.route('/')
def show_index():
    return render_template('title.html')