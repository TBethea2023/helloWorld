from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Tamara Bethea! I am adding m first code change.'


@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/favorite-course')
def favorite_course():  # put application's code here
    print('Subject:' + request.args.get('subject'))
    print('Course_number:' + request.args.get('course_number'))

    return render_template('favorite_course.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():  # put application's code here
    if request.method == "POST":
        return render_template('contact.html', form_submitted= True)
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run()
