from flask import Flask, render_template, url_for
app = Flask(__name__)




@app.route("/")



@app.route("/home")
def home():
    return render_template('home6.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
	return render_template('contact2.html')

@app.route("/clients")
def clients():
	return render_template('clients.html')

@app.route("/sticker")
def stickerlabel():
	return render_template('stickers6.html')

@app.route("/largeformatprints")
def lfp():
	return render_template('largeformat.html')

@app.route("/architecturalprints")
def architecturalprints():
	return render_template('architectural.html')


if __name__ == '__main__':
    app.run(debug=True)

    
