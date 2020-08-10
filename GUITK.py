from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = Tk()
root.title("Embedding in Tk")
root.geometry("600x600")

# fig1=Figure(figsize=(5, 4), dpi=100)
    #j=fig1.add_subplot(111)
#fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
#root2= Tk()
#root2.title("No.of Installs")
fig=Figure(figsize=(10,12),dpi=100)
k=fig.add_subplot(221)
l=fig.add_subplot(222)
m=fig.add_subplot(223)
data_my=pd.read_csv("C:\\Datasheets\\data.csv")
Categorys=data_my.Category.unique()
#category_column=list(data_my.Category)

category_installs1={}
category_installs2={}
category_installs3={}

sum6=0.0
sum7=0.0
sum8=0.0
sumo=0.0

for category in Categorys:
    
    Art_Design=data_my.loc[data_my['Category']==category]#loc function is used for returning rows
    Art_Design=Art_Design.sort_values('Last Updated')
    installs = [ float(i.replace('+','').replace(',', '')) if '+' in i or ',' in i else float(0) for i in Art_Design["Installs"] ]
    
    dates=list(Art_Design['Last Updated'])
    dates=[i.replace(',', '') if ',' in i else float(0) for i in Art_Design["Last Updated"] ]

    list_sum=[]
    

    for year in ['2016','2017','2018']:
            dic={}
            
            sum=0.0
            for i in range(len(dates)):
                j=dates[i].split()
                if(j[2]==year):
                    sum=sum+installs[i]
            
                
            list_sum.append(sum)
    category_installs1.update({category:list_sum[0]})
    category_installs2.update({category:list_sum[1]})
    category_installs3.update({category:list_sum[2]})
    sum6=sum6+list_sum[0]
    sum7=sum7+list_sum[1]
    sum8=sum8+list_sum[2]
    sumo=sumo+list_sum[0]+list_sum[1]+list_sum[2]
  
#print("Year 2016") 
def g2016():
    k.bar(category_installs1.keys(),category_installs1.values(),color='yellow')
    k.set_xlabel("Category")
    k.set_ylabel("No.of Installs")
    inverse=[(value,key) for key, value in category_installs1.items()]
    canvas = FigureCanvasTkAgg(k,master=root2)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack()
    canvas.draw()
#print("Highest no.of Installs in year 2016 is ",max(inverse)[1])
#print("Lowest no.of installs in year 2016 is ",min(inverse)[1])
#print("Year 2017")
def g2017():
    l.bar(category_installs2.keys(),category_installs2.values(),color='Red')
    l.set_xlabel("Category")
    l.set_ylabel("No.of Installs")
    canvas = FigureCanvasTkAgg(l,master=root2)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack()
    canvas.draw()

def g2018():   
    invers=[(value,key) for key, value in category_installs2.items()]
    print("Highest no.of Installs in year 2017 is ",max(invers)[1])
    print("Lowest no.of installs in year 2017 is ",min(invers)[1])
    print("Year 2018")
    m.bar(category_installs3.keys(),category_installs3.values(),color='Green')
    m.set_xlabel("Category")
    m.set_ylabel("No.of Installs")
    canvas = FigureCanvasTkAgg(m,master=root2)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack()
    canvas.draw()
#root2.mainloop()
   
inver=[(value,key) for key, value in category_installs3.items()]
#print("Highest no.of Installs in year 2018 is ",max(inver)[1])
#print("Lowest no.of installs in year 2018 is ",min(inver)[1])
'''diff67=sum7-sum6
per67=(diff67/sumo)*100
diff78=sum8-sum7
per78=float((diff78/sumo)*100)
if per67>0:
    print("Increase by percent of Installs of apps from year 2016 to 2017 is ",per67)
else:
    print("Decrease by percent",per67)
if per78>0:
    print("Increase by percent of Installs of apps from year 2017 to 2018 is",per78)
else:
    print("Decrease by percent",per78)'''
        
def graph():
    root1= Tk()
    root1.title("No.of Installs")
    fig1=Figure(figsize=(5, 4), dpi=100)
    j=fig1.add_subplot(111)
    
    data_my=pd.read_csv("C:\\Datasheets\\data.csv")
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in data_my['Installs']:
        
        t=i.replace(',','')
        x=int(t.replace('+',''))
        
       
        if 10000<=x<50000 :
            a=a+1
        elif 50000<=x<150000 :
            b=b+1
        elif 150000<= x <500000:
            c=c+1
        elif 500000<=x<5000000 :
            d=d+1
        else:
            e=e+1
    dic_data={"10000-50000":a,"50000-150000":b,"150000-500000":c,"500000-5000000":d,"5000000+":e}
    j.bar(dic_data.keys(),dic_data.values(),color='yellow')
    j.set_xlabel("Range")
    j.set_ylabel("No.of Installs")
    
    
    canvas = FigureCanvasTkAgg(fig1,master=root1)  # A tk.DrawingArea.
   
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    root1.mainloop()
Butt=Button(root,text="No.of Installs",width=20,command=graph).pack()   
Button1=Button(root,text="Insstalls 2016",width=20,command=g2016).pack() 
Button2=Button(root,text="Insstalls 2017",width=20,command=g2017).pack() 
Button3=Button(root,text="Insstalls 2018",width=20,command=g2018).pack()  
root.mainloop()

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
