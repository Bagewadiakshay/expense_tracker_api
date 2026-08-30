from flask import Flask 

from flask import jsonify 
from flask import request

from models import add_expense, get_allexp,del_exp,upd_exp

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"msg":"Expense tracker API is running.."})

@app.route("/expenses",methods=["POST"])
def create_exp():
    data= request.args
    results = add_expense(data["title"],float(data["amount"]),data["category"],data["date"])
    return jsonify({"msg": results})

@app.route("/expenses",methods=["GET"])
def read_exp():
    data = get_allexp()
    return jsonify({"expenses ": data})


@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def remove_expense(expense_id):
    result = del_exp(expense_id)
    return jsonify({"message": result})



@app.route("/expenses/<int:expense_id>", methods=["PUT"])
def modify_expense(expense_id):
    data = request.args
    result = upd_exp(expense_id, float(data["amount"]))
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(debug=True)