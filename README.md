# OpenWebinars

Esto es una taller para subir un paquete a Pypi

## 1 - Nombre de tu paquete

Todos los paquetes en PyPi han de ser únicos, puedes usar el [buscador](https://pypi.org/search) para ver si tu nombre esta disponible.

Los nombres deberían tener un formato de todo minúsculas separado por - como el de este paquete.

## 2 - Estructura de un paquete

El directorio del proyecto ha de estar organizado de la siguiente manera:

```tree
taller-openwebinar/
│
├── package_a/
│   ├── config.txt
│   ├── __init__.py
│   ├── __main__.py
│   └── functionality_a.py
│
├── package_b/
│   ├── __init__.py
│   └── functionality_b.py
│
├── tests/
│   ├── test_functionality_a.py
│   └── test_functionality_b.py
│
├── MANIFEST.in
├── README.md
└── setup.py
```

### 2.1 - package_a, package_b, test, etc

Cada paquete con cada utilidad que queramos, incluido el test, deberán estar dentro de la carpeta, aqui usamos dos 3 paquetes pero pueden agregarse más.

### 2.2 - Manifest.in

Aquí se indicarán archivos que no sean .py

En caso de usarlo en el setup.py teneis que poner el siguiente atributo: ```include_package_data``` a ```True```

Los comandos que acepta el manifest están disponibles [aquí](https://docs.python.org/3/distutils/commandref.html#creating-a-source-distribution-the-sdist-command)

### 2.3 - Readme.md

Aquí podeis poner la documentación de vuestro paquete, podeis usar vuestra propia plantilla o usar alguna existente:

* https://github.com/othneildrew/Best-README-Template
* https://github.com/dbader/readme-template

### 2.4 - setup.py

La definicion de los atributos es la siguiente:

* ```name```: Nombre público del paquete que no deberá estar en Pypi
* ```version```: Versión del paquete
* ```description```: Pequeña descripción del paquete
* ```long_description```: Descripción larga con los detalles del paquete
* ```long_description_content_type```: Formato de la ```long_description``` en caso de tenerla
* ```classifiers```: Información relevante del paquete como licencia o versiones de python soportadas
* ```packages```: paquetes que se incluiran
* ```include_package_data```: Si incluye archivos que no sean .py
* ```install_requires```: Dependencias que el paquete necesita para funcionar
* ```entry_points```: Comandos de consola que dispondra el paquete

#### 2.4.1 Plantillas

Disponeis de plantillas para el setup.py una bastante conocida es la siguiente:

https://github.com/navdeep-G/setup.py

## 3 - Publicando nuestro paquete

Lo primero que tienes que hacer es crear una cuenta en [Pypi](https://pypi.org) y en [Pypi para test](https://test.pypi.org/)

Después deberemos seguir los pasos indicados en el video del taller para obtener un token y guardarlo en el archivo ```.pypirc```

Una vez que este eso configurado usaremos [Twine](https://twine.readthedocs.io/en/latest/) para poder subir el paquete.

Twine se instala con pip de la siguiente manera:

```pip install twine```

Para distribuir un paquete es necesario convertirlo a un fichero de tipo wheels, que no es mas que un fichero zip. Para hacer esto basta con usar el siguiente comando:

```python3 -m pip install --user --upgrade setuptools wheel```

Finalmente para crear el paquete ejecutaremos el siguiente comando

```python setup.py sdist bdist_wheel```

Esto nos creará una carpeta llamada  ```dist/``` entre otras que será la que usemos para subir al repositorio.

Para subir el paquete lo podemos hacer especificando el repositorio con: ```--repository-url```

```twine upload --repository-url https://test.pypi.org/legacy/ dist/*```

o con el alias del repositorio del fichero ```.pypirc```

```twine upload --repository testpypi dist/*```

Aunque si no vamos a subir a test no es necesario poner nada

```twine upload dist/*```

## 4 - Instalando desde un repositorio privado

Para tener nuestro propio repositorio pip privado podemos hacer un servidor git como github y subir ahí nuestro paquete en un repositorio privado.

Después para instalarlo solo será necesario usar el siguiente comando:

```pip install git+ssh://git@github.com/Tlaloc-Es/taller-openwebinar.git```

En este caso se hace uso de ssh y por lo tanto tendremos que tener la clave ssh instalada en el equipo y reconocida por git.

Un fallo que podras ver, es que cuando hagas ```pip freeze > requiremetns.txt``` es que no vas a ver la url sino el nombre del paquete, lo que hará que cuando instales desde ```requirements.txt``` vaya al repositorio Pypi en vez de al privado para ello bastara con poner otra vez ```git+ssh://git@github.com/Tlaloc-Es/taller-openwebinar.git``` en el fichero en vez del nombre del paquete.

Una vez tengas el código listo podrás instalarlo
