from flask import Flask, render_template, request, jsonify
from crypto_social_sage.crypto_social_sage import CryptoSocialSage
import os

app = Flask(__name__)

# Initialize CryptoSocialSage
css = CryptoSocialSage()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_crypto_data', methods=['POST'])
def get_crypto_data():
    symbol = request.form['symbol']
    data = css.get_crypto_data(symbol)
    return jsonify(data)

@app.route('/get_social_sentiment', methods=['POST'])
def get_social_sentiment():
    symbol = request.form['symbol']
    sentiment = css.get_social_sentiment(symbol)
    return jsonify(sentiment)

@app.route('/get_trading_signals', methods=['POST'])
def get_trading_signals():
    symbol = request.form['symbol']
    signals = css.get_trading_signals(symbol)
    return jsonify(signals)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))