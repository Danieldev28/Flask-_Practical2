import os
from flask import Flask, render_template,request, flash, jsonify
import json

app = Flask(__name__)
app.secret_key="secure_code"

@app.route('/')
def index():
    with open("data/data.json", 'r') as file:
        contents_of_file = json.load(file)
        return render_template("index.html", title = "Home Page", content = contents_of_file)
    
@app.route('/contact', methods= ["GET", "POST"])
def contact():
    if request.method== "POST":
        # print(request.form["name"])
        flash("Thanks {}, we have recieved your message".format(request.form["name"]))
     
    return render_template("contact.html", title = "Contact Page")


@app.route('/about/what/')
def about():
       return render_template("about.html", title = "About Page")
    
@app.route('/post')
def post():
    return render_template("post.html", title = "Random Page")
    
@app.route('/about/<actor_name>')
def about_actors(actor_name):
    actor_return = {}
    with open("data/data.json", 'r') as file12:
        actors_file = json.load(file12)
        for actor in actors_file:
            if actor['url'] == actor_name:
                actor_return = actor
    if actor_return == {}:
        actor_return = {"message":"No Data Available"}
    return render_template("about_actors.html", content = actor_return)
    
    # api calling for python
@app.route('/checkword/api/v1/task', methods=['GET'])
def check_word():
    my_arg = request.args
    word_to_check = my_arg['word']
    print(word_to_check)
    if word_to_check in api_test_list:
        return jsonify({'result':True})
    else:
        return jsonify({'result':False})

if __name__ =='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
   