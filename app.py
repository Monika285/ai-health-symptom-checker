from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load symptoms CSV
data = pd.read_csv("model/symptoms.csv")
symptom_list = list(data.columns[:-1])  # all columns except 'condition'

# Precautions dictionary
precautions_dict = {
    "Flu": "Rest and drink fluids.",
    "Cold": "Stay hydrated and take OTC cold meds.",
    "COVID-19": "Isolate and consult a doctor.",
    "Food Poisoning": "Hydrate and rest.",
    "Migraine": "Rest in a dark room and avoid noise.",
    "Dengue": "Consult doctor immediately.",
    "Malaria": "Medical treatment required.",
    "Asthma": "Use inhaler and avoid triggers.",
    "Allergy": "Avoid allergens; take antihistamines.",
    "Typhoid": "Doctor prescribed medication.",
    "Pneumonia": "Consult doctor immediately."
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data_json = request.get_json()
        user_input = data_json.get("symptoms", "")

        # Normalize user input
        user_symptoms = [s.strip().lower().replace(" ", "_") for s in user_input.split(",")]

        # Overlap-based matching
        max_match = 0
        predicted_disease = "Unknown"

        for i, row in data.iterrows():
            match = sum([1 for s in symptom_list if row[s] == 1 and s in user_symptoms])
            if match > max_match:
                max_match = match
                predicted_disease = row["condition"]

        precaution = precautions_dict.get(predicted_disease, "Follow general health guidelines.")

        return jsonify({"prediction": predicted_disease, "precaution": precaution})

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
