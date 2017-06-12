from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

OPEN_JOBS = ["Software Engineer", "QA Engineer", "Product Manager"]

@app.route('/')
def homepage():
	"""Renders the homepage."""

	return render_template("index.html")


@app.route('/application-form')
def application_form():
	"""Allows user to apply for open jobs."""

	return render_template("application-form.html",
							OPEN_JOBS=OPEN_JOBS)

@app.route('/application-success', methods=["POST"])
def success():
	"""Confirms that user applied to specified job."""

	first_name = request.form.get("first-name")
	last_name = request.form.get("last-name")
	salary = request.form.get("salary")
	position = request.form.get("position")

	return render_template("application-response.html",
							first_name=first_name,
							last_name=last_name,
							salary=salary,
							position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
