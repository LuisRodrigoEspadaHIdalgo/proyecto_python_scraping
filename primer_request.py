from bs4 import BeautifulSoup # BeautifulSoup es una biblioteca de Python para extraer contenido de ficheros HTML y XML. Resulta muy útil para obtener información de forma procesable (en un sistema de árbol fácil de manejar) de páginas web.
import requests 

#realizamos el request a la pagina que deseamos scrapear  
page = requests.get("https://scrapeme.live/shop/") 

#serializamos la informacion con BS$
soup = BeautifulSoup(page.content,'html.parser')

#filtramos la informacion que desamos con find
lista_products = soup.find(class_="products columns-4")

#filtramos aun mas con find_all para obtener datos mas especificos
products = lista_products.find_all(class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")

#hacemos un for para obtener la informacion de cada uno de los productos
#y la almacenamos en un json que luego podría se guardado en una base de datos.
_datos = []
for item in products:
    #limpiamos la informacion antes de ser guardada con get_text() para solo obtener el texto
    title = item.h2.get_text()
    price = item.span.get_text()
    image = item.img['src']

    #agregamos el json a la lista _datos
    _datos.append({
        "title":title,
        "price":price,
        "image":image
        })

print(_datos)

#result = lista_products

#print(soup.prettify())
  
#print(page.status_code) #muestra el código de respuesta del Request que realizamos.ej: 200 para una solicitud aceptada y 400 para una pagina que no existe
  
#print(page.content) #muestra el contenido html del cuerpo de la paguina que queríamos Scrapear.