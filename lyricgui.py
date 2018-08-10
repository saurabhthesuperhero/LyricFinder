import bs4
import requests
import webbrowser
from tkinter import *
def lyricservice():
    #lstring='Perfect ed sheeran'
    lstring=e1.get()
    res=requests.get('https://search.azlyrics.com/search.php?q=%s'%lstring)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    result=soup.find_all('td',{"class":"text-left"})
    i=1
    global x
    x=['0']*10
    t1.delete(1.0,END)

    for link in result [0:5]:
        #print(link.text)
        t1.insert(END,link.text)
        x[i]=link.find('a').get('href')
    
        i=i+1
def show():
    global x
    #linkss=int(input("Enter song number ........"))
    linkss=int(e2.get())
    linksss=x[linkss]
    lres=requests.get(linksss)
    lsoup=bs4.BeautifulSoup(lres.text,'lxml')

    lresult=lsoup.find_all('div',{'class':'col-xs-12'})
    check='<!-- MxM banner -->'
    for lyric in lresult [1:2]:
        lyricss=lyric.text
    t1.delete(1.0,END)
    t1.insert(END,"********************Saurabh Lyrical service***********")
    lindex=lyricss.find('Android')
    t1.insert(END,lyricss[10:lindex])
    t1.insert(END,"********************Saurabh Lyrical service***********")
##
##GUI
##
##
window=Tk()
window.geometry("500x800")
window.title("Awesome Lyric finder")
l1=Label(text='Awesome Lyric Finder',font=('Times',18),fg='white',bg='purple')
l1.pack(fill=X)
l2=Label(window,text='Enter Song name here :',font=('Century gothic',17))
l2.pack()
e1=Entry(window,font=('Lucida calligraphy',10))
e1.pack()
b1=Button(window,text="Go",font=('Times',16),command=lyricservice)
b1.pack()
e2=Entry(width=15)
e2.pack(side=TOP)
b2=Button(text='Go',font=('Times',11),command=show)
b2.pack(side=TOP,ipady=1)

t1=Text(height=90,font=('Comic sans ms',12),bg='brown',fg='white')
t1.pack(fill=X)
window.mainloop()














