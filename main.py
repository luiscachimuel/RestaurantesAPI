#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


# noinspection PyInterpreter
@app.route('/restaurants', methods=['GET'])
def getAllRestaurants():
    restaurantsList = []

    restaurante1 = {
                        "id": 1,
                        "Nombre": "Inka Burger Ecuador",
                        "Categoria": "Comida rapida",
                        "Direccion": "Av. Gaspar de Villarroel E3-83, Quito 170513",
                        "Review": "Somos la primera cadena ecuatoriana de hamburguesas mas querida del país. ¡Persíguenos en nuestras redes! ;)",
                        "Rating": 3.5,
                        "Imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQzhwsGfzRV56nwg054CCT3dS9XJywU5ZCLQ&usqp=CAU",
                        "Coordenada": "geo:0,0?q=-0.10704512475694013, -78.45508011232049(Inka Burguer)"
                   }
    restaurantsList.append(restaurante1)

    restaurante2 = {
        "id": 2,
        "Nombre": "VACO Y VACA",
        "Categoria": "Comida rapida",
        "Direccion": " AV. NACIONES UNIDAS Y 6 de DICIEMBRE",
        "Review": "Las mejores hamburguesas y alitas en un sólo click. Te llevamos en minutos la mejor sazón a tu hogar. ¡Pide de una y disfruta de Vaco y Vaca!",
        "Rating": 4,
        "Imagen": "https://elbosque.com.ec/vacoyvaca/wp-content/uploads/sites/242/2020/08/vaco-vaca.jpg",
        "Coordenada": "geo:0,0?q=-0.10100727708700387, -78.49031543451348(VACO Y VACA)"
    }
    restaurantsList.append(restaurante2)

    restaurante3 = {
        "id": 3,
        "Nombre": "Tac and Roll",
        "Categoria": "Comida mexicana",
        "Direccion": "Av. República de El Salvador, Quito 170135",
        "Review": "En TAC & ROLL, un mexicano puede comer tacos al estilo mexicano, y un ecuatoriano al estilo TAC&ROLL. Contamos con especialidades vegetarianas y veganas.",
        "Rating": 3.5,
        "Imagen": "https://tacandroll.com.ec/wp-content/uploads/2019/08/logo-tac-and-roll-retina.png",
        "Coordenada": "geo:0,0?q=-0.17987868176810667, -78.47983544751524(Tac and Roll)"
    }
    restaurantsList.append(restaurante3)
    restaurante4 = {
        "id": 4,
        "Nombre": "El Ventanal",
        "Categoria": "Cafetería",
        "Direccion": "Carchi, Quito 170130",
        "Review": """El Restaurante Mirador El Ventanal está situado en las faldas del
                     Pichincha en el tradicional barrio de San Juan, llevándonos un aire
                     refrescante y una vista espectacular del Centro Colonial de Quito y la
                     famosa Avenida de los Volcanes""",
        "Rating": 4.5,
        "Imagen": "http://www.elventanal.ec/imagenes/gallery/ventanal-gallery12.jpg",
        "Coordenada": "geo:0,0?q=-0.21353733832725827, -78.51293758984433(El Ventanal)"
    }
    restaurantsList.append(restaurante4)

    restaurante5 = {
        "id": 5,
        "Nombre": "Pizzeria El Hornero",
        "Categoria": "Pizza",
        "Direccion": "Av. de la Prensa N51-20 y, Quito 170512",
        "Review": "Disfruta de la mejor pizza del mundo a domicilio. Llámanos o pide tu pizza favorito desde tu computador.",
        "Rating": 4,
        "Imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0hnpNTNpbVcZIhrAe4kX_8foVbUZxpcq_Ug&usqp=CAU",
        "Coordenada": "geo:0,0?q=-0.19995470995090656, -78.4942803477948(Pizzeria El Hornero)"
    }
    restaurantsList.append(restaurante5)

    restaurante6 = {
        "id": 6,
        "Nombre": "Long Fong",
        "Categoria": "Comida China",
        "Direccion": "Perez Guerrero 422 entre Versalles y America, Quito 12345 Ecuador",
        "Review": "Comida China tradicional",
        "Rating": 3.5,
        "Imagen": "https://scontent.fuio1-1.fna.fbcdn.net/v/t39.30808-6/242043455_4323638714383826_5389788532553492368_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=e3f864&_nc_ohc=GYYw0kZYHMsAX9qbyzF&_nc_ht=scontent.fuio1-1.fna&oh=00_AT_-aYeGwKURO99eGaEM0gB1QJMaBpI5S7YscEOUdPR7ow&oe=6232E311",
        "Coordenada": "geo:0,0?q=-0.20267226693370624, -78.50081521683221(Inka Burguer)"
    }
    restaurantsList.append(restaurante6)

    restaurante7 = {
        "id": 7,
        "Nombre": "Inka Burger Ecuador",
        "Categoria": "Comida rapida",
        "Direccion": "Av. Gaspar de Villarroel E3-83, Quito 170513",
        "Review": "Somos la primera cadena ecuatoriana de hamburguesas mas querida del país. ¡Persíguenos en nuestras redes! ;)",
        "Rating": 3.5,
        "Imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQzhwsGfzRV56nwg054CCT3dS9XJywU5ZCLQ&usqp=CAU",
        "Coordenada": "geo:0,0?q=-0.10704512475694013, -78.45508011232049(Inka Burguer)"
    }
    restaurantsList.append(restaurante7)

    restaurante8 = {
        "id": 8,
        "Nombre": "Mayflower",
        "Categoria": "Comida china",
        "Direccion": "Centro Comercial Granados Plaza calle, Av. 6 de Diciembre, Quito",
        "Review": "Comida rica, comida sana. Fanpage oficial de Mayflower Ecuador. Pedidos a domicilio sin monto mínimo.",
        "Rating": 4,
        "Imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWVMlUq7alTwa0jXFEX3GZXw9h8NMtchMWRtWFf0yICOgOvG_vk28yupyujMiQWMTUFA&usqp=CAU",
        "Coordenada": "geo:0,0?q=-0.18787727813201674, -78.48745801945041(Mayflower)"
    }
    restaurantsList.append(restaurante8)

    response = {"restaurants": restaurantsList}

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='9095')
