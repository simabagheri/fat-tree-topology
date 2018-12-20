import networkx as nx
import matplotlib.pyplot as plt

k = int(input("enter K?"))
p = (k/2)**2    #number of servers in pod 
s = ((k/2)**2)*k
g = []
color_map = []
n = s+(k*k/2)+(k*k/2)+((k/2)**2)

edge=s+(k/2)*k
agg=(k/2)*k + edge


G1 = nx.Graph()

for i in range(int(n)):
   G1.add_node(i)
   g.append([])

for node in G1:
   if node<s:
      color_map.append('blue')
for node in G1:
   if node<edge and node>s:
      color_map.append('red')
for node in G1:
   if node<agg and node>edge:     
      color_map.append('green')
for node in G1:
   if node>agg:
      color_map.append('yellow')
      
      

#print(g)
i = 0
while i < s:
    for j in range(int(p)):
        top = s+int((i+j)/(k/2))
        g[int(i+j)].append(int(top))
        g[int(top)].append(int(i+j))
    i += p
#print(g)
e = s + (k*k/2)
i = 0
while i < (k*k/2):
    for j in range(int(k/2)):
        for l in range(int(k/2)):
            top = int(e+i+l)
            g[int(s+i+j)].append(top)
            g[top].append(int(s+i+j))
    i += k/2
#print(g)
a = e + (k*k/2)
i = 0

while i < (k*k/2):
    temp = int(i/(k/2))
    for j in range(int(k/2)):
        for l in range(int(k/2)):
            top = int(a+(temp%((k/2)*(k/2))))
            g[int(e+i+j)].append(top)
            g[top].append(int(e+i+j))
            temp += 1
    i += k/2
print(g)

f=open("result.txt","w+")

for i in range(int(n)):
    for l in range(int(n)):
        flag = False
        for j in range(len(g[i])): 
            if g[i][j]==l:
                flag = True
        if flag:
            f.write(f"{i} {l} ------>1\n")
            G1.add_edge(i,l)
        else:
            f.write(f"{i} {l} ------>9999\n")    

f.close()

#nx.draw(G1,node_color = color_map,with_labels=True, font_weight='bold')
nx.write_gml(G1,'g.gml')
nx.write_graphml(G1,'g.xml')

#plt.show()






