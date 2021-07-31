import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


url="https://www.cricbuzz.com/cricket-match/live-scores"

r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
soup.prettify()
try:
    date=soup.find('span',class_="text-gray").text
    # print(date)
    
except AttributeError:
    # print('No live cricket matches are detected')
    exit()

place=soup.find('div',class_="text-gray").text
# print(place)



t1=soup.find_all('div',class_="cb-ovr-flo cb-hmscg-tm-nm")
s1=soup.find_all('div',class_="cb-ovr-flo")

# print(t1[0].text,'-->',s1[2].text)
# print(t1[1].text,'-->',s1[4].text)

try:
    comment=soup.find('div',class_="cb-text-live").text
    # print(comment)

    
except AttributeError:
    come=soup.find('div',class_="cb-text-complete").text
    # print('winner-->',come)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',comment=comment or come,t1=t1,t2=s1,date=date,place=place)

if __name__ == '__main__':
    app.run(debug=True)
