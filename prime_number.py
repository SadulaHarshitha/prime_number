from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def input():
        return render_template('input.html')

@app.route('/submit', methods=['POST'])
def is_prime():
    num=request.form['number']
    k=0
    if num>1:
        for divisor in range(2,(num**0.5)+1):
            if((num%divisor)==0):	
                k=1
                return render_template(non_prime.html)
                break
        
        if(k==0):
            return render_template('prime.html')	

    else:
        return render_template('non_prime.html')	
  
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')
