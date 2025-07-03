from flask import Flask, render_template, request
from models.checkout import CheckoutSystem

app = Flask(__name__)
checkout = CheckoutSystem()

@app.route('/', methods=['GET', 'POST'])
def index():
    total = None
    messages=[]
    if request.method == 'POST':
        items = request.form.get('items','')
        # total ,messages = checkout.calculate_total(items) #ABBA
        if items:  # only calculate if input is non-empty
            total, messages = checkout.calculate_total(items)
        else:
            messages = []  # clear old messages if nothing was submitted
            total = None
            print("the message is ", messages)

    return render_template('index.html', total=total ,messages=messages )

if __name__ == '__main__':
    app.run(debug=True)
