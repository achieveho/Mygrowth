# import scipy as sp
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# x = sp.stats.mode(speed)
x = stats.mode(speed)

print(x)