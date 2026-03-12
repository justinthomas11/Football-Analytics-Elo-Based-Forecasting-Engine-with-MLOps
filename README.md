# Football Analytics & Elo-Based Forecasting Engine

An end-to-end football analytics pipeline that applies machine learning and Elo ratings to historical match data — surfacing team performance patterns, predicting match outcomes, and visualizing insights through an interactive Tableau dashboard.

---

## Results

- 59% prediction accuracy on unseen match data
- 30+ versioned models managed via MLflow registry
- Statistically significant home advantage patterns identified (+15% win rate) across 10,000+ matches

---

## Project Overview

The pipeline combines historical match statistics with Elo rating snapshots to perform feature engineering, model training, and dashboard visualization. The system predicts match outcomes (Home / Draw / Away) using regime-aware ML models trained on form, strength differentials, and match context.

---

## Dataset

**Matches Dataset**
Match-level data including league division, date, home/away teams, Elo ratings, team form (last 3 and 5 games), goals, shots, fouls, corners, cards, betting odds, and full/half-time results.

**Elo Ratings Dataset**
Club Elo snapshots including club name, country, snapshot date, and Elo rating — used as the primary strength indicator across time.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Data Processing | Python, Pandas, NumPy |
| Machine Learning | Scikit-learn, MLflow |
| Visualization | Tableau, Matplotlib, Seaborn |
| Workflow | Jupyter Notebook, Git, GitHub Actions |
| Deployment | Docker |

---

## ML Pipeline

- Encoding categorical variables and handling missing values
- Feature engineering — form metrics, Elo differentials, match context
- Model training — Logistic Regression, Random Forest
- Evaluation — accuracy, classification report, confusion matrix
- Outcome prediction — Home win / Draw / Away win
- Model versioning via MLflow registry

---

## Getting Started

### 1. Clone and Install
```bash
git clone https://github.com/justinthomas11/football-analytics-elo-forecasting.git
cd football-analytics-elo-forecasting
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 2. Run
```bash
jupyter notebook
```

Open and run `FootballAnalytics.ipynb`

---

## Project Structure
```
├── FootballAnalytics.ipynb      # Main analysis and modeling notebook
├── data/                        # Match and Elo datasets
├── models/                      # Saved model artifacts
├── requirements.txt
└── README.md
```

---

## Future Scope

- Player-level feature integration
- Live match prediction via API
- Web app deployment
