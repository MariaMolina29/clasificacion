import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('Matriz_Final.csv', header=None)
data_no_headers = data.iloc[1:, :].reset_index(drop=True)

X = data_no_headers.iloc[:, 1:88].astype(float)  # Columns 2 to 89 (features)
Y = data_no_headers.iloc[:, 88].astype(int)      # Column 90 (labels)

X = X.to_numpy()
Y = Y.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5) 
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

conf_mat = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:")
print(conf_mat)
print(f"Accuracy: {accuracy * 100:.2f}%")

