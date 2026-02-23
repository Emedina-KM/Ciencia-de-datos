# Control de Versiones

## GIT

'''Objetivos principales

1. Descemtralización.
es que cada desarrollador tiene una copia del proyecto y del historico que se esta realizando. esto le facilita el trabajo sin conexión.
2. Velocidad
Todas las operaciones locales como los comentarios, ramas. Todo eso debia ser una gestión rapida. ASpi podias trabajar de manera local sin tener que depender del internet.
3. Manejo eficiente de ramas
muchos colaboradores trabajan a la vez un mismo proyecto.
cada uno trabaja con una copia difernete de manera local.
una vez terminan podran subir sus cambios al servidor es decir a su carpeta principal. pero antes de subirse para por un periodo de revisión
si uno subio los cambios antes que el otro partiendo de la misma copia base, al segundo no lo dejara subir sus cambios sin antes descargar la última versión.
así se evitan los errores que pueden suceder con el trabajo colaborativo.'''

### Comandos GIT
'''
1. **git init**, empezar un proyecto de git (localmente).
cuando tengamos un proyecto abrimos terminal y ejectuamos git init. asi inicamos git en el proyecto que nos encontramos

2. **git status**, verificar cualquier cambio hecho en el proyecto (creación de nuevos archivos, editar archivos, etc.)

3. **git add**, añadir nuevos elementos para nuestra versión.
cada elementos que le agregamos es un cambio considerable para subir a nuestro proyecto
nosotros antes de subir cambios los agrupamos y una vez estamos seguros lo que hacmoes es empezar a tagerarlo.
y para poder taguearlo usamos el siguiente comando:

git add:
    a. Puedo agrupar cada cambio de manera independiente.
    b. puedo enviar todos los cambios de golpe (git add .)

4. **git commit**, añadir un comentos en los elementos que se agregaron previamente.

aca debemos ser no muy explicitos. algo simple:
git commit -m "inicio de proyecto"

ojo: cada comentario que hagamos debe estar autenticado por alguien, es deecir debe haber un autor de ese comentario.
asi vemos en el historico quien lo hizo.
cuando recien instalamos git tneemos que setearlo con nuestra cuenta:
git config --global user.email "emedina112233@gmail.com"

despúes colocamos el nombre que saldra en nuestro comentarios:
git config --global user.name "emedina"

ahora si puedes mandar tu commit.

5. **git remote**, da referencia a una rama remota.
hasta ahora hemos añadido cambios a nuestra rama local.
pero ahora haremos que esto se suba a nuetro repositorio de github, gitlab, bitbucket, etc. (rama remota.

para eso utilizamos el siguietne comando para añadir un proyecto remoto:

6. **git remote add**, añair un proyeto remoto

es git remote add origin (url de respositorio)

el origin es como se llamara nuestra rama remota. ahi podemos obtener todo lo que eta en el proyecto de git.
copiamos la url que sale en nuestro repositorio


7. **git push**, subir todos nuestros commits locales al servidor remoto.
git push origin main

**extra**
ssh-keygen
lo que hara esto es crear una llave publica que nos sirve como seguridad para poder autenticuar nuestro equipo hacia nuestra cuenta de git hub
esto sirve para colocar nuestro dispositivo seguro hacia nuestra cuenta.
esto nos puede pasar en algun momento.

8. **git pull**, traer todos los cambios de una rama remota a una rama local.

hola mundo!
'''
