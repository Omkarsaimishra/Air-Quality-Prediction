
# 🌫️ Air Quality Prediction Project

This project is a machine learning web application designed to predict air quality using various environmental factors. It provides a user-friendly interface for inputting air quality data and instantly seeing the predicted Air Quality Index (AQI) category.

## 🚀 Live Demo

Check out the live deployed app here:  
👉 [Air Quality Predictor on Hugging Face](https://huggingface.co/spaces/omkarsai/air_quality_project)

## 📌 Features

- ✅ Predicts Air Quality Index (AQI) based on user input
- ✅ Clean and simple interface using [Gradio](https://www.gradio.app/)
- ✅ Real-time predictions
- ✅ Deployment on Hugging Face Spaces
- ✅ Lightweight and fast — great for demos and learning

## 📊 Technologies Used

- Python
- Scikit-learn
- Pandas & NumPy
- Gradio (for UI)
- Hugging Face Spaces (for deployment)

## 🛠️ How to Use Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/air_quality_project.git
   cd air_quality_project
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally:**
   ```bash
   python app.py
   ```

   The app will start locally and provide a link to open it in your browser.

## 📁 Project Structure

```
├── app.py               # Main application file
├── model.pkl            # Trained ML model
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 📈 How It Works

- The app takes inputs like PM2.5, PM10, NO2, SO2, O3, CO, etc.
- The data is passed to a pre-trained ML model (RandomForest or similar).
- The model returns an AQI category such as "Good", "Moderate", or "Poor".
- The result is displayed instantly in the interface.

## ✨ Showcase

This project is live and accessible to everyone! Try it out and explore how machine learning can help monitor and predict air quality.

👉 [Try the App Now](https://huggingface.co/spaces/omkarsai/air_quality_project)

## 👥 Contributors

| Name                  | GitHub Profile                             |
|-------------------    |---------------------------------------------|
| Ommkar sai mishra     | [@omkarsai](https://github.com/omkarsai)   |
| Asit Kumar Barik      | [@username2](https://github.com/asitbarik88) |
| Contributor 3         | [@username3](https://github.com/username3) |
| Contributor 4         | [@username4](https://github.com/username4) |

> Want to contribute? Open a pull request or drop a star 🌟!

---

Feel free to fork, star, and contribute!
```
