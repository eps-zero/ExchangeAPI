from flask import Flask, request, jsonify
from data import get_data

app = Flask(__name__)

@app.route('/api/rates', methods=['GET'])
def convert_currency():
    try:
        from_currency = request.args.get('from')
        to_currency = request.args.get('to')
        value = float(request.args.get('value', 0))

        if not from_currency or not to_currency or value <= 0:
            raise ValueError('Invalid input')

        data = get_data(from_currency=from_currency, to_currency=to_currency)

        if not data:
            raise Exception('Failed to fetch exchange rates')

        result = data.get('result')
        if 'error' in result:
            raise Exception(result['error'])

        rate = result[to_currency]

        converted_value = value * rate

        return jsonify({'result': round(converted_value, 2)})

    except (ValueError, Exception) as e:
        return jsonify({'error': str(e)}), 400 if isinstance(e, ValueError) else 500


if __name__ == '__main__':
    app.run(debug=True)
