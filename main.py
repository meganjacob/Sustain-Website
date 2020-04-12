from flask import Flask, url_for, render_template, redirect, request
app = Flask(__name__)

#name = input("Enter your name: ")
#rating = str(input("Please rate the product you are writing about out of 10. If this doesn't apply to you, please enter a '-'."))        
#user_input = input('Start writing here: ')
#   

comment_list = []

def aesthetic():
    global user_input
    if len(user_input) <= 5:
        print(len(user_input))
        print("please write a longer comment")
        user_input = input('Start writing here: ')
    if len(user_input) < 15:
        print(name + " rates this product as a " + rating + " out of 10. They said ' " + user_input + "'")
    if len(user_input) >= 15:
        print(name + " rates this product as a " + rating + " out of 10. They said ' " + user_input + "'")

@app.route('/', methods=['GET', 'POST'])      
def mainFunc():
    if request.method == 'GET':
        return render_template("new3_comment.html")
    
    name = request.form.get("comment_author")
    email = request.form.get("email")
    rating = request.form.get("rating")
    comment = request.form.get("comment")
    
    
    comment_list.append("{} entered {} and gave it a rating of {} out of 10".format(name, comment, rating))
    return "<br>".join(comment_list)

@app.route('/new', methods=['GET', 'POST'])
def newFunc():
    if request.method == 'GET':
        return render_template("website.html")
    
    name = request.form.get("comment_author")
    email = request.form.get("email")
    rating = request.form.get("rating")
    comment = request.form.get("comment")
    
    comment_list.append("{} entered ' {} ' and gave it a rating of {} out of 10".format(name, comment, rating))
    return render_template("comments.html", comments=comment_list)



#    aesthetic()
#    another = input("Would you like to submit another review? Please say 'Yes', or 'No'.")
#    while another == 'Yes':
#        name = input("Enter your name:")
#        rating = str(input("Please rate the product you are writing about out of 10."))
#        user_input = input("Start writing here: ")
#        aesthetic()
#        another = input("Would you like to submit another review? Please say 'Yes', or 'No'.")
#





app.run('0.0.0.0',8080)
