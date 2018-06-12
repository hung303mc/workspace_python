# How to use jupyter notebook

## test plot on Jupyter
```python
import numpy as np 
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

```

## test clip
<iframe width="560" height="315" src="https://www.youtube.com/watch?v=_g-dyXWUov8&t=251s"></iframe>