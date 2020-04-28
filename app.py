from flask import Flask, jsonify
import pandas
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Nothing'

@app.route('/users')
def users():
    
    excel_data_df = pandas.read_excel("users.xlsx", sheet_name="Sheet1")

    users = excel_data_df.to_dict("records")

    j = json.dumps(users, ensure_ascii=False)

    return jsonify(users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)