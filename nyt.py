#imports
import requests
import pandas as pd

#in this string i save the url of the API and then make the request of the url
url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=LrbCeftsODrEyj8rBZsT37Jd5mJk8Lt0'
r = requests.get(url)

#in this if i look if the request of the url was successful
if r.status_code == 200:
    json= r.json()
    json.keys()
    jsonResults = json['results']
    #pass the information to a dataframe 
    df = pd.DataFrame(jsonResults)
    #filter the data
    dfClean = df[['title','description','author','publisher']]
    #sort the data alphabetically
    dfClean =dfClean.sort_values('title',ascending=True)
    #create the csv with the data
    dfClean.to_csv('nyt.csv')
    print("El csv se ha creado")
else:
    print("La conexion ha fallado")

