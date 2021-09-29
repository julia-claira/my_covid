from flask import Flask, render_template, redirect



#create app
graph = Flask(__name__)

#passes db results into html   
@graph.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    graph.run(debug=True)





