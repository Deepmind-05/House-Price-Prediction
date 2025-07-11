from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "HI"
#defining a new subroutine that gives us a list of locations availabel
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price() :
    try:
        print("Form data:", request.form)
        sqft = float(request.form['sqft'])
        location = request.form['location']
        bhk = float(request.form['bhk'])
        bath = float(request.form['bath'])

        price = util.get_estimated_prices(location, sqft, bhk, bath)
        print("Predicted price:", price)

        response = jsonify({'estimated_price': price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__" :
    print("Starting Python Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run()