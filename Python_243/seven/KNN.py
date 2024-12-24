import pandas as pd
import numpy as np
import sklearn as skl 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from collections import  Counter
from sklearn.datasets import make_classification




df = pd.DataFrame({
  'columnA' : [10,np.nan,50,100],
  'columnB' : ['A','B','B','A'],
  'columnC' : [True,False, True, True]
}

)


x,y = make_classification(
      n_samples = 200,
      n_features = 2,
      n_informative=2,
      n_redundant=0,
      n_clusters_per_class=1,
      random_state = 42
)

plt.figure(figsize=(6,4))
plt.scatter(x[:,0],x[:,1], c = y, cmap = plt.cm.coolwarm, edgecolors= 'k')
plt.show()


x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=10)


def eucledian_distance(a,b):
  return np.sqrt(np.sum(a-b**2))



def knn_predict(x_train,y_train,x_query,k=3):
  distance = [[eucledian_distance(x_query,x_train) for X_train in x_train]]
  k_indices = np.argsort(distance)[:k]
  k_neighbor_labels = [y_train[i] for i in k_indices]
  label_counter = Counter(k_neighbor_labels)
  predicted_label = label_counter.most_common(1)[0][0]
  return predicted_label


def knn_predict_all(x_train,y_train,x_test,k=3):
  predictions = []
  for x in x_test:
    label = knn_predict(x_train,y_train,x,k)
    predictions.append(label)

  return np.array(predictions)


k =3
y_pred = knn_predict_all(x_train,y_train,x_test,k=k)
print(f"Predicted label(first 10): {y_pred[:10]}")
