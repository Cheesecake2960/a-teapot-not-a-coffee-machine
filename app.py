from flask import Flask, render_template, abort, jsonify

app = Flask(__name__)

DRINKS = {
    "tea": "🍵",
    "wine": "🍷",
    "juice": "🧃",
    "beer": "🍺",
    "tapioca": "🧋",
    "milk": "🥛",
}

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/api/teapot/<drink>')
def api_teapot(drink: str):
    if drink == "coffee":
        abort(418)
    
    return jsonify({"content": DRINKS.get(drink, "🥤")})

if __name__ == "__main__":
    app.run(debug=True)