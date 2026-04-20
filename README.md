# Customer Classification using Machine Learning

---

## English Version

## Project Overview
This project demonstrates a complete end-to-end machine learning workflow to classify customers into **high-value** and **low-value** segments based on their purchasing behavior.

In addition to model training, the project includes **model deployment basics** with a reusable prediction script that allows user interaction.

---

## Objectives
- Build a classification model to identify high-value customers
- Compare multiple machine learning models
- Evaluate model performance using different metrics
- Implement a simple deployment-ready prediction system

---

## Dataset
A synthetic dataset was generated to simulate customer behavior, including:

- Total orders
- Total spending
- Average order value
- Country

A target variable (`high_value`) was created based on customer spending.

---

## Workflow

### 1. Data Creation
A dataset of 200 customers was generated using NumPy and Pandas.

---

### 2. Feature Engineering
- Created average order value
- Generated categorical variable (country)

---

### 3. Data Preprocessing
- Label Encoding applied to categorical data
- Train-test split (80/20)

---

### 4. Models Used

#### Decision Tree
- Rule-based model
- No scaling required

#### K-Nearest Neighbors (KNN)
- Distance-based model
- Requires feature scaling

---

### 5. Feature Scaling
StandardScaler was applied for the KNN model to normalize feature values.

---

### 6. Evaluation Metrics
- Accuracy
- Confusion Matrix

---

## Results

### Decision Tree
- Accuracy: 77.5%
- Better performance in identifying high-value customers

### KNN
- Accuracy: 67.5%
- Lower performance and missed more high-value customers

---

## Key Insights
- Decision Tree outperformed KNN in this dataset
- KNN struggled with detecting high-value customers
- Identifying high-value customers is critical for business decisions

---

## Model Deployment

The trained model was saved using `pickle` and reused in a standalone Python script.

---

## Prediction Script (app/predict.py)

The project includes a reusable prediction script that:

- Loads the trained model and encoder
- Accepts user input from the terminal
- Outputs customer classification

---

## How to Use

1. Clone the repository

2. Install dependencies:
pip install -r requirements.txt
3. Run the prediction script:
cd app
python predict.py
4. Enter customer data when promoted:
Enter total orders:
Enter total spent:
Enter average order value:
Enter country:
5. Get prediction result: 
Prediction: High Value / Low Value

---

## Tools & Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle (model persistence)

---

## Project Structure
customer-classification-ml/

│── model/
│   ├── model.pkl
│   ├── encoder.pkl

│── app/
│   ├── predict.py

│── notebooks/
│   ├── customer_classification.ipynb

│── requirements.txt
│── README.md

---

## Author
Yara Shartooh

---

## Deutsche Version

## Projektübersicht
Dieses Projekt demonstriert einen vollständigen Machine-Learning-Workflow zur Klassifizierung von Kunden in **wertvolle** und **weniger wertvolle** Segmente basierend auf ihrem Kaufverhalten.

Zusätzlich zur Modellentwicklung enthält das Projekt eine einfache **Deployment-Lösung** mit einem interaktiven Vorhersageskript.

---

## Ziel
- Entwicklung eines Klassifikationsmodells zur Identifikation wertvoller Kunden
- Vergleich mehrerer Machine-Learning-Modelle
- Bewertung der Modellleistung mit verschiedenen Metriken
- Implementierung eines wiederverwendbaren Vorhersagesystems

---

## Datensatz
Ein synthetischer Datensatz wurde erstellt, um Kundenverhalten zu simulieren, einschließlich:

- Anzahl der Bestellungen
- Gesamtausgaben
- Durchschnittlicher Bestellwert
- Land

Eine Zielvariable (`high_value`) wurde basierend auf den Ausgaben definiert.

---

## Workflow

### 1. Datenerstellung
Ein Datensatz mit 200 Kunden wurde mithilfe von NumPy und Pandas erstellt.

---

### 2. Feature Engineering
- Berechnung des durchschnittlichen Bestellwerts
- Erstellung einer kategorialen Variable (Land)

---

### 3. Datenvorverarbeitung
- Label-Encoding für kategoriale Daten
- Aufteilung in Trainings- und Testdaten (80/20)

---

### 4. Verwendete Modelle

#### Entscheidungsbaum
- Regelbasiertes Modell
- Keine Skalierung erforderlich

#### K-Nearest Neighbors (KNN)
- Distanzbasiertes Modell
- Benötigt Skalierung

---

### 5. Skalierung
StandardScaler wurde für das KNN-Modell verwendet.

---

### 6. Bewertungsmetriken
- Genauigkeit
- Konfusionsmatrix

---

## Ergebnisse

### Entscheidungsbaum
- Genauigkeit: 77,5 %
- Bessere Erkennung wertvoller Kunden

### KNN
- Genauigkeit: 67,5 %
- Schwächere Leistung und mehr übersehene wertvolle Kunden

---

## Wichtige Erkenntnisse
- Der Entscheidungsbaum liefert bessere Ergebnisse
- KNN erkennt wertvolle Kunden schlechter
- Die Identifikation wertvoller Kunden ist geschäftskritisch

---

## Model Deployment

Das trainierte Modell wurde mit `pickle` gespeichert und in einem separaten Python-Skript wiederverwendet.

---

## Vorhersageskript (app/predict.py)

Das Projekt enthält ein Skript, das:

- Das trainierte Modell lädt
- Benutzereingaben im Terminal verarbeitet
- Eine Klassifikation ausgibt

---

## Verwendung

1. Repository klonen

2. Abhängigkeiten installieren:
pip install -r requirements.txt
3. Skript ausführen:
cd app
python predict.py
4. Eingaben machen:
Anzahl der Bestellungen:
Gesamtausgaben:
Durchschnittlicher Bestellwert:
Land:
5. Ergebnis:
Vorhersage: High Value / Low Value

---

## Tools & Bibliotheken

- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## Projektstruktur

(siehe oben)

---

## Autorin
Yara Shartooh