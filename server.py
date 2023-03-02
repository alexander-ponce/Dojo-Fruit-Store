from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    selectedFruit = []
    selectedAmount = 0
    for fruit in ["strawberry", "raspberry", "apple"]:
        quantity = int(request.form.get(fruit, 0))
        if quantity > 0:
            selectedFruit.append({"name":fruit, "quantity":int(quantity)})
            selectedAmount+= int(quantity)

    first_name= request.form["first_name"]        
    last_name= request.form["last_name"]        
    student_id= request.form["student_id"]

    print(f'{first_name} for {selectedAmount}') 


    return render_template("checkout.html", selectedAmount=selectedAmount, selectedFruit=selectedFruit, first_name=first_name, last_name= last_name, student_id=student_id)




@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    


