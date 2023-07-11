import pandas as pd
import numpy as np

print(np.random.randn(20, 3))

print(np.array([10, 20]))

print(np.array([[10], [20]]))

# data = {"Homme": [10], "Femme": [20]}
data = {"Sexe": ["Homme", "Femme"], "Valeurs": [20, 10]}
df = pd.DataFrame(data)
print(df)
