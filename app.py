from flask import Flask
from app.routes.transaction import transaction_bp

app = Flask(__name__)
app.register_blueprint(transaction_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Uniswap Transaction Fee API"

if __name__ == "__main__":
    app.run(debug=True)
