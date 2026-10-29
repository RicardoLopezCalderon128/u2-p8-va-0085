import matplotlib.pyplot as plt
import numpy as np
diasX=["lun","mar","mie","jue","vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("califas en VA de Ricardo Lopez NC 0085") 
plt.xlabel("dias de la semana habil")
plt.ylabel("califas en VA")
plt.grid()
plt.show()