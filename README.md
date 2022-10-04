# Blog - Django
---

**Integrantes:**
- Bocchieri Matias
- Lorenzatti Matias


<b>En la carpeta MEDIA > README van a poder encontrar un **VIDEO**, en el cual se explica el funcionamiento de la app.</b>


<div style="text-align: justify">

¡Hola a todos! Les presentamos nuestro primer proyecto hecho con Python, Django, HTML y CSS.

Se trata de un blog, pensado para que cualquier usuario de internet pueda leer los distintos posts sin necesidad de registrarse y hacer un login. En el caso de que quieran colaborar con el blog, ya sea agregando nuevos posts o modificando los existentes, pueden registrarse en la app y luego ingresar a la misma, para que se le habiliten las opciones correspondientes a edición.

Este readme esta dividido en 2 secciones:
- ¿Como se creo la app?
- ¿Como se usa la app?

**¿Como se creo la app?**

En esta sección, se explicara de forma simple, que conceptos y herramientas se utilizaron, para poder desarrollar la app. Recordando que estamos en GitHub, pueden ver el código y comprobar por ustedes mismos, el nivel de detalle, prolijidad y conocimientos que se tuvieron en cuenta para tal fin.

Se trabajo con el modelo MVT de Django (Model - View - Template), el cual utiliza un **Model** para la DB, un **Template** para el frontend (con el cual nos comunicarnos con el usuario y este se comunica con la lógica del programa) y una **View**, que se encarga de la lógica del backend, conectando el Model con el Template. Una ventaja de trabajar con este patron, es que los componentes tienen un acoplamiento débil entre si, es decir, cada pieza de la aplicación web que funciona sobre Django, tiene un único propósito clave, que puede ser modificado independientemente, sin afectar a las otras piezas. Por ultimo, es necesario aclarar que gracias a las URL´s, podemos vincular un template a una view, la cual a su vez esta vinculada a un model. Es por esto, que cada vez que el usuario accede a una URL, internamente esta realizando una petición GET a la view, la cual procesa la misma y devuelve un RESPONSE con la información necesaria para que el usuario pueda visualizarla en el template (esto se logra por medio de la arquitectura REST y el protocolo HTTP, el cual es proveído por Django).

Sabiendo como funciona Django, nuestra forma de trabajo se amolda a ello, creando Views para controlar la lógica de la app, Templates para poder comunicarnos con el usuario, y que a su vez este se comunique con nosotros, Models para crear las tablas y campos necesarios en la DB, y URL´s, para poder vincular al usuario con las views necesarias.

Se trabajo tanto con:
- Clases Basadas en Vistas (CBV), las cuales viene por defecto en Django y nos permiten realizar ciertas acciones puntuales (CRUD, seguridad, autenticación, registro, login, etc).
- Vistas creadas para un fin determinado (no viene por defecto en Django, fueron creadas).

Por medio de estas views, podemos controlar el CRUD de los post, registros de usuarios, etc. como asi también la autenticación de usuarios (gestión de sesiones) para asegurarnos de que solo usuarios registrados y logueados, puedan acceder a ciertas funcionalidades de edición.

Estas Clases Basadas en Vistas, requieren de una estructura de archivos puntual (formularios + templates para listar datos), la cual se conoce y se atendió con éxito, creando los templates, urls y views necesarias. Se trabajo con formularios de Django, los cuales fueron modificados estéticamente para aportar armonía y prolijidad a la web.

Por ultimo, se realizaron pruebas unitarias de ciertas funcionalidades y modelos, para verificar que todo ande a la perfección, y ajustar detalles en caso de ser necesario. Estas pruebas unitarias (Unit Test) crean una DB temporal, en la cual se realizan transacciones tal cual se realizarían sobre la DB original, testeando que todo ande a la perfección, y eliminando la DB una vez que el unit test finalice y nos comunique los resultados.
De esta forma, nos aseguramos de que dicha app este en condiciones de utilizarse.


**¿Como se usa la app?**

A continuación, se explicara el funcionamiento de la app.

Como bien dijimos, no es necesario que un usuario se registre y/o loguee para poder visualizar los posts, pero como la intension es explicar el funcionamiento de la app, vamos a comenzar desde 0, explicando los pasos que debe seguir un usuario si desea utilizar la app.

<h2>Pagina inicial:</h2>

La pagina inicial que visualizaremos al acceder a la app es la siguiente:

Como podemos ver, todavía no hay posts creados, pero no se preocupen, ahora crearemos uno.

![1](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/1.png?raw=true)    

<h2>Registrarse y acceder a la app:</h2>

Al hacer clic en el botón de "Registrarse", se nos abre el siguiente formulario, el cual debemos completar con nuestros datos y listo, nos hemos registrado con éxito (esto lo podemos ver al observar que nos redirecciona a la pagina principal y nos muestra dicho mensaje).

![3](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/3.png?raw=true)  

![4](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/4.png?raw=true)

Una vez que nos registramos, debemos iniciar sesión con los datos que hemos ingresado anteriormente. Al iniciar sesión, vemos que nos aparece un nuevo botón en el menu de navegación, que es el "Editar post". Esto solo pueden verlo los usuarios registrados y logueados. También podemos ver que el botón de registrarse desaparece, y nos aparece nuestro nombre de usuario en el botón superior, el cual nos muestra un pequeño avatar y nos da la opción de modificar nuestros datos, modificar la contraseña, agregar un avatar o cerrar sesión (todo esto lo veremos mas adelante).

![6](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/6.png?raw=true)

![7](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/7.png?raw=true)

<h2>Crear un post:</h2>

Para crear un post, debemos ir a la sección de **Editar post**, hacer clic en **Crear nuevo post** y listo, completamos los campos y seguimos el proceso de creación que es bastante intuitivo.

![8](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/8.png?raw=true)


![10](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/10.png?raw=true)

![11](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/11.png?raw=true)

![12](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/12.png?raw=true)

<h2>Modificar un post:</h2>

Para modificar un post, debemos ir a **Editar post** y seleccionar la opción de Editar. Luego seguimos los pasos que nos indica y listo, hemos podido modificar nuestro post con éxito.

![13](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/13.png?raw=true)

![14](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/14.png?raw=true)

![15](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/15.png?raw=true)

<h2>Eliminar un post:</h2>

Para eliminar un post, debemos seguir los siguientes pasos:

![16](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/16.png?raw=true)

![17](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/17.png?raw=true)

<h2>Modificar datos varios del usuario:</h2>

En el botón de inicio, el cual tiene nuestro nombre y avatar (no tiene ningún avatar asociado si nunca se lo hemos creado), vamos a poder seleccionar la opción que deseemos. Contamos con 4 funcionalidades/opciones (modificar datos, cambiar contraseña, agregar un avatar o cerrar sesión). Observemos esto:

![18](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/18.png?raw=true)

![19](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/19.png?raw=true)

![20](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/20.png?raw=true)

![21](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/21.png?raw=true)

![23](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/23.png?raw=true)

<h2>Cerrar sesión:</h2>

Finalmente, cuando deseemos dejar de utilizar la app, debemos **Cerrar Sesión** y listo.

![24](https://github.com/matilorenzatti/django_blog/blob/main/media/readme/24.png?raw=true)



</div>