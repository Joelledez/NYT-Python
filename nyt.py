import requests
import pandas as pd

url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=LrbCeftsODrEyj8rBZsT37Jd5mJk8Lt0'
r = requests.get(url)

if r.status_code == 200:
    json= r.json()
    json.keys()
    jsonResults = json['results']
    df = pd.DataFrame(jsonResults)
    dfClean = df[['title','description','author','publisher']]
    dfClean =dfClean.sort_values('title',ascending=True)
    dfClean.to_csv('nyt.csv')
    print("El csv se ha creado")
else:
    print("La conexion ha fallado")

