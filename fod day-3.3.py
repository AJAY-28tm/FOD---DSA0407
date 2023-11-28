# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text

# Create a sample dataset
data = pd.DataFrame({
    'income': [50000, 80000, 60000, 75000, 90000, 55000, 72000, 85000],
    'credit_score': [600, 750, 700, 720, 780, 620, 700, 760],
    'debt_to_income_ratio': [0.4, 0.2, 0.3, 0.2, 0.1, 0.5, 0.3, 0.2],
    'employment_duration': [1, 3, 2, 2, 4, 1, 2, 3],
    'risk': ['high', 'low', 'low', 'low', 'low', 'high', 'low', 'low']
})

# Display the first few rows of the dataset to understand its structure
print(data)

# Preprocess the data
X = data[['income', 'credit_score', 'debt_to_income_ratio', 'employment_duration']]
y = data['risk']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CART classifier
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Display the decision tree rules
tree_rules = export_text(classifier, feature_names=list(X.columns))
print("Decision Tree Rules:\n", tree_rules)

# Example: Predict credit risk for a new loan applicant
new_applicant = pd.DataFrame({
    'income': [60000],
    'credit_score': [700],
    'debt_to_income_ratio': [0.3],
    'employment_duration': [2]
})

prediction = classifier.predict(new_applicant)
print(f'Predicted Credit Risk for the new applicant: {prediction[0]}')
