import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


data = {
    'Hours_Studied': [2.0, 3.5, 5.0, 1.0, 4.0, 6.0, 1.5, 3.0, 2.5, 4.5],
    'Hours_Slept': [7.0, 6.0, 8.0, 5.0, 6.5, 8.5, 6.0, 7.0, 5.0, 7.5],
    'Prior_Grade': [70, 65, 80, 50, 78, 85, 60, 75, 55, 82],
    'Result': ['fail', 'fail', 'pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'fail', 'pass']
}
df = pd.DataFrame(data)


df.to_csv('student_data.csv', index=False)


print("First few rows of the dataset:")
print(df.head())


print("\nMissing values:")
print(df.isnull().sum())


df['Result'] = df['Result'].map({'fail': 0, 'pass': 1})


scaler = StandardScaler()
features = ['Hours_Studied', 'Hours_Slept', 'Prior_Grade']
df[features] = scaler.fit_transform(df[features])


X = df[features]
y = df['Result']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=['fail', 'pass'])

print(f"\nAccuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)


k_values = [1, 3, 5]
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nk={k}, Accuracy: {accuracy:.2f}")


best_k = 3
print(f"\nBest k: {best_k}")
print(f"Overall Accuracy: {accuracy:.2f}")


new_student = np.array([[3, 6.5, 77]])
new_student_scaled = scaler.transform(new_student)
prediction = knn.predict(new_student_scaled)
print(f"\nPrediction for new student: {'pass' if prediction[0] == 1 else 'fail'}")
