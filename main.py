from flask import Flask, render_template, request
from app.utils import Prediction
import CONFIG

# Initialize Flask app
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for prediction
@app.route('/predict', methods=["POST", "GET"])
def predict_price():
    try:
        # Get the data from the form
        data = request.form

        # Create an instance of the Prediction class
        pred_obj = Prediction()

        # Predict the price
        predicted_price = pred_obj.predict_price(data)

        # Render the result on the HTML page
        return render_template("index.html", value=predicted_price)
    except Exception as e:
        # Handle errors and display error message
        print(f"Error: {e}")
        return render_template("index.html", error="An error occurred during prediction. Please check your inputs.")

# Main execution
if __name__ == "__main__":
    app.run(host=CONFIG.HOST, port=CONFIG.PORT, debug=CONFIG.DEBUG)
