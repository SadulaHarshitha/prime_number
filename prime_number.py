from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', method=['GET'])
def input():
  if request.method == 'GET':
  return render_template(input.html)

@app.route("/submit", methods = ["POST"])

def is_prime():
  if request.method == "POST"
  num=request.form['number']
  have_factors=false
  if num>1:
     for divisor in range(2,(num**0.5)+1):
	      if (num%divisor)==0 :
		      return render_template(non_prime.html)	
		      have_factors=true
		      break
        
     if(!have_factors)
	     return render_template(prime.html)	

  else:
    return render_template(non_prime.html)	
  
if __name__ == '__main__'
    app.run(debud=True)
