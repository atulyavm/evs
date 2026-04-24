# Water Quality Prediction System (EVS Project)

An AI-powered web application for analyzing water quality, predicting potential diseases, and recommending treatments based on water parameters like pH and the presence of specific chemicals.

## Features

- **Water Quality Analysis**: Input pH levels and select present chemicals (e.g., Lead, Mercury, Arsenic, Fluoride, Pesticides, Bacteria) to get instant analysis.
- **Disease Prediction**: Utilizes Machine Learning to predict potential diseases that could arise from the given water profile.
- **Treatment Recommendation**: Suggests appropriate water treatment methods to make the water safer.
- **Interactive Interface**: A premium, modern, and user-friendly web interface with smooth animations and responsive design.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn (Random Forest / Decision Trees), Pandas, Joblib

## Project Structure

- `backend/`: Contains the Flask server, machine learning models, and training scripts.
  - `app.py`: Main Flask application.
  - `generate_data.py` & `train_water_model.py`: Scripts to generate synthetic dataset and train the ML models.
  - `*.pkl`: Pickled models and feature encoders.
- `index.html`: The landing page of the web app.
- `analysis.html`: The main analysis interface where users input data.
- `styles.css` & `script.js`: Frontend styling and logic.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/atulyavm/evs.git
   cd evs
   ```

2. **Set up the backend environment:**
   Make sure you have Python installed. Install the required dependencies:
   ```bash
   pip install flask flask-cors pandas scikit-learn joblib
   ```

3. **Run the Application:**
   Start the Flask development server:
   ```bash
   cd backend
   python app.py
   ```
   The server will start on `http://127.0.0.1:5000`.

4. **Access the App:**
   Open your browser and navigate to `http://127.0.0.1:5000` to view the application.

## Usage

1. Navigate to the Analysis section.
2. Enter the pH value of the water sample.
3. Select any chemicals or contaminants detected in the water from the provided list.
4. Click on "Analyze" to receive predictions on potential diseases and recommended treatments.

## License

This project is created for educational purposes.
