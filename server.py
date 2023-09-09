from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_intro():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    capitalized_name = name.capitalize()
    return "Hi, " + capitalized_name + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat_hello(num, word):
    message = f"{word} " * num
    return message

# @app.route('/play')
# def level_one():
#     return render_template("index.html", num=3, color="blue")

# @app.route('/play/<int:num>')
# def level_two(num):
#     return render_template("index.html", num=num, color="blue")

# @app.route('/play/<int:num>/<string:color>')
# def level_three(num, color):
#     return render_template("index.html", num=num, color=color)


if __name__=="__main__":
    app.run(debug=True, port=5001)
    