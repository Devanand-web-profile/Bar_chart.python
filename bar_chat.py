
import matplotlib.pyplot as plt
x=[12,56,40,80]
y=["Mahindra","infosis","tata","wipro"]

#plt.bar(y,x)
#plt.show()

#plt.bar(y,x,color=["green","red","yellow","gold"])
#plt.show()

#plt.barh(y,x,color=["green","red","yellow","gold"])
#plt.show()      #print ( horizontly )

plt.bar(y,x,color=["green","red","yellow","gold"])
plt.plot(y,x,color="blue")
plt.grid(True)
plt.show()      









