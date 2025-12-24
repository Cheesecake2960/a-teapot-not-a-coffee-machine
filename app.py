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
    """
    Return a JSON object with an emoji representing the requested drink, or raise HTTP 418 for "coffee".
    
    Parameters:
        drink (str): The drink name to look up; if the value is "coffee", the function aborts with HTTP 418.
    
    Returns:
        dict: JSON object with a single key `"content"` whose value is the drink's emoji from DRINKS, or `"🥤"` if the drink is not found.
    """
    if drink == "coffee":
        abort(418)
    
    return jsonify({"content": DRINKS.get(drink, "🥤")})

if __name__ == "__main__":
    app.run(debug=True)