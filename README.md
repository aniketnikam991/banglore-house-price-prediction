Bangalore House Price Prediction

Project Overview
Real estate prices are often unpredictable. This project is a Machine Learning solution that predicts house prices in Bangalore, India based on key factors like location, square footage, number of bedrooms (BHK), and bathrooms.

The goal was to build a model that can provide accurate price estimates to help buyers and sellers make informed decisions.

Tech Stack & Tools
- Python: Core programming language.
- Pandas & NumPy: For data manipulation and cleaning.
- Matplotlib: For data visualization.
- Scikit-Learn: For building the Linear Regression model.
- Jupyter Notebook: Used for experimentation and analysis.

 Key Steps in the Project
1.  Data Cleaning: Handled missing values and standardized format.
2.  Feature Engineering:
    - Created new features like `price_per_sqft`.
    - Applied Dimensionality Reduction to group less frequent locations as "Other".
3.  Outlier Removal: Removed logical errors (e.g., houses with extreme sqft per bedroom ratios) to improve accuracy.
4.  Model Building: Used Linear Regression and evaluated performance using K-Fold Cross Validation.
5.  Hyperparameter Tuning: Used `GridSearchCV` to find the best model parameters.


## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/aniketnikam991/banglore-house-price-prediction.git](https://github.com/aniketnikam991/banglore-house-price-prediction.git)
