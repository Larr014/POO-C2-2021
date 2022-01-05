import requests
from Post import *
import crud

url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)
data = r.json()

for pub in data:
    p = Post(pub['userId'],pub['id'],pub['title'],pub['body'])
    #p.mostrar()
    #crud.registrar_post(p)
    
publicaciones = crud.mostrar_posts()
for pub in publicaciones:
    pub.mostrar()
    
