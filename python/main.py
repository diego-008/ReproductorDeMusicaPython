import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import easygui
import xml.etree.ElementTree as ET

from pygame import mixer
ruta = ''; cancion = ''; pausa = False; botonReproducir = None; botonPausa = None; imgPausa = None; imgPlay = None
reproducir = True; botonNext = None; txtLabel = 'Cancion: \n Artista: \n Album:'
from tkinter import *
from ListaDobleAlbum import ListaDobleAlbum
from ListaDobleCancion import ListaDobleCancion
from ListaDobleArtista import ListaDobleArtista
from ListaDoble import ListaDoble
from Cancion import Cancion

listaAlbumes = ListaDobleAlbum()
listaCanciones = ListaDobleCancion()
listaArtistas = ListaDobleArtista()
listaC = ListaDobleCancion()
listaVar = ListaDoble()
def Play():
    global ruta, cancion, pausa, botonPausa, botonReproducir, imgPausa, imgPlay, reproducir
    mixer.init()
    cancion = '../Musica/heroes.mp3'
    if reproducir:
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        reproducir = False
        botonReproducir.configure(image=imgPausa)
        return
    if pausa:
        mixer.music.unpause()
        botonReproducir.configure(image=imgPausa)
        # botonReproducir.image = imgPausa
        pausa = False
    else:
        mixer.music.pause()
        botonReproducir.configure(image=imgPlay)
        # botonReproducir.image = imgPausa
        pausa = True

def Siguiente():
    global cancion
    mixer.music.stop()
    cancion = '../Musica/alone.mp3'
    mixer.music.load(cancion)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    

def Cargar():
    global ruta, cancion, pausa, botonReproducir, botonPausa, imgPausa
    ruta = easygui.fileopenbox()  
    print(ruta)
    cancion = '../Musica/Alone.mp3'
def Pausa(): 
    global pausa, botonPausa, botonReproducir, imgPausa
    mixer.music.pause()
    pausa = True
    
def Stop():
    global pausa, botonPausa, botonReproducir, imgPausa, reproducir
    mixer.music.stop()
    pausa = False
    reproducir = True
    botonReproducir.configure(image=imgPlay)

def obtenerOpcion():
    global var, listaC
    aux = listaC.primero
    aux2 = listaVar.primero
    print('*'*25)
    while aux != None:
        
        print(aux.dato.cget('text'), aux2.dato.get())
        aux = aux.siguiente
        aux2 = aux2.siguiente


def LeerXml():
    global ruta, listaAlbumes, listaCanciones, listaArtistas, ventana, var, listaC, listaVar
    tree = ET.parse("../archivos/1.xml")
    root = tree.getroot()
    for i in range(len(root)): #root.tag es biblioteca
        nombreCancion = (root[i].attrib) #Por cada iteracion guadar el nombre de cada cancion en un dicc
                                        #el tag es cancion
        nombreCancion = nombreCancion["nombre"] #Esto devuelve solo el nombre de la cancion sin la etiqueta
        nuevaCancion = Cancion()
        
        nuevaCancion.nombre = nombreCancion
        #nombre
        #Posicion 0 de la lista es la etiqueta cancion
        # print(root[0][0].text)
        # print(nombreCancion)
        #Recorriendo etiqueta cancion
        for j in range(len(root[0])):
            if root[i][j].tag== 'album':
                nuevaCancion.album = root[i][j].text
            elif root[i][j].tag == 'ruta':
                nuevaCancion.ruta = root[i][j].text
            elif root[i][j].tag == 'imagen':
                nuevaCancion.imagen = root[i][j].text
            elif root[i][j].tag == 'artista':
                nuevaCancion.artista = root[i][j].text.strip(' ')
        
        listaCanciones.agregarFinal(nuevaCancion)

    aux = listaCanciones.primero #Esta es la primera lista aux cancion
    #Recorriendo la lista de canciones
    while aux != None:
        if listaAlbumes.vacia():
            listaAlbumAux = ListaDobleAlbum()
            listaAlbumAux.agregarFinal(aux.dato)
            listaAlbumAux.artista = aux.dato.artista
            listaAlbumAux.album = aux.dato.album
            # print(aux.dato.album, aux.dato.artista)
            
            listaAlbumes.agregarFinal(listaAlbumAux)

            # print(aux.dato.nombre)
            #seguir creando las listas album cuando ya hay elementos,
            #recorrer la lista 
            aux2 = listaAlbumes.primero

        else:
            albumEncontrado = False
            # print(aux.dato.album, aux.dato.artista)
            aux3 = listaAlbumes.primero
            while aux3 != None:
                # print(aux3.dato)
                aux4=aux3.dato #aux4 tiene la lista album aux
                # print(aux4.primero.dato.nombre) # Esto es el objeto cancion
                # print(aux4.album)
                aux3 = aux3.siguiente
                if aux4.album == aux.dato.album: #Recorremos para ver si el album ya existe
                    aux4.agregarFinal(aux.dato) #Le agregamos la cancion a ese album
                    albumEncontrado = True
                    break
            
            if albumEncontrado:
                pass
            else:
                listaAlbumAux = ListaDobleAlbum()
                listaAlbumAux.agregarFinal(aux.dato)
                listaAlbumAux.artista = aux.dato.artista
                listaAlbumAux.album = aux.dato.album
                # print(listaAlbumAux.primero.dato.nombre) Con esto se accede a los atributos de la lista
                #de canciones desde la lista aux album
                listaAlbumes.agregarFinal(listaAlbumAux)

                # print(aux.dato.nombre)



        #print(aux.dato.ruta)#asi se accede a los atrubutos desde el auxiliar
        aux=aux.siguiente

    #Recorriendo listas albumes
    aux = listaAlbumes.primero


    #Aqui solo se obtienen datos, no se crea nada
    while aux!=None:
        aux2 = aux.dato #Esto es la lista album auxiliar
        aux3 = aux.dato.primero
        # print('*'*25)
        # print('Canciones del album', aux.dato.album, 'artista', aux.dato.artista) #Aqui se imprime la info
        #Descomentar para ver
        while aux3 !=None:
            # print(aux3.dato.nombre) descomentar para obtener atrib de la cancion
            aux3=aux3.siguiente

        # print(aux2.primero.dato.nombre) #Imprimo nombre de la cancion
        aux = aux.siguiente


    #Aqui se anidan listasArtista y listaALbum
    aux = listaAlbumes.primero
    # print(aux.dato) #esto es un album auxiliar
    artistaEncontrado = False
    while aux != None: #Aqui recorro los 5 albumes
        aux2 = aux.dato #Aqui estan los atributos de cada album
        aux2 = aux2.artista
        # print(aux.dato.size)
        if listaArtistas.vacia():
            listaAuxArtistas = ListaDobleArtista()
            listaAuxArtistas.agregarFinal(aux.dato) #aux dato contiene el album a agregar
            listaAuxArtistas.artista = aux2
            listaArtistas.agregarFinal(listaAuxArtistas)
            aux3 = listaArtistas.primero

        else:
            #aqui recorro las listas artistas
            aux3 = listaArtistas.primero
            while aux3 != None:
                # print(aux2+aux3.dato.artista+'valores') #esta es una lista artista con atributos
                #Verificamos si ya existe el artista y solo le agregamos el album
                #aux 3 es lista artista
                # print(aux2 == aux3.dato.artista, 'comparacion')
                if aux2 == aux3.dato.artista:
        
                    aux3.dato.agregarFinal(aux.dato)

                    artistaEncontrado = True
                    

                    # print('iguales', aux2)
                    break
                aux3 = aux3.siguiente
                    
                
            #Si el artista no existe creamos una nueva instancia
            if artistaEncontrado == False:
                # print('no existe')
                listaAuxArtistas = ListaDobleArtista()
                listaAuxArtistas.agregarFinal(aux.dato) #aux dato contiene el album a agregar
                listaAuxArtistas.artista = aux2
                listaArtistas.agregarFinal(listaAuxArtistas)
            artistaEncontrado = False
                    
        # print('sxsx')
                


            
        

        aux = aux.siguiente

    #Verificando los datos en la lista artista
    aux = listaArtistas.primero
    print(listaArtistas.size)
    while aux != None:
        print('*'*25)
        # print('artista', aux.dato.artista, )
        # print(aux.dato.primero.dato)
        aux2 = aux.dato.primero 
        # aux4 = aux.dato.primero
        # print('albumes', end='   ')
        #Recorriendo albumes de los artistas para obtener solo los albumes
        # while aux4 != None:
            
        #     print(aux4.dato.album, end='   ')
        #     aux4 = aux4.siguiente


        #Recorremos los albumes del artista para obtener las canciones
        
        while aux2 != None:
            
            # print('album', aux2.dato.album)
            aux3 = aux2.dato.primero
            #Recorriendo el album para pbtener las canciones
            # print('CANCIONES')
            while aux3 != None:
                # print(aux3.dato.nombre)
                aux3 = aux3.siguiente

            aux2 = aux2.siguiente
            # print(aux2)
        


        
        aux = aux.siguiente

    aux = listaCanciones.primero
    posy = 0
    
    while aux != None:
        var = tk.BooleanVar()
        # var = aux.dato.nombre
        opcionCancion = tk.Checkbutton(ventana, text=aux.dato.nombre, variable=var)
        opcionCancion.pack
        opcionCancion.place(x=20, y=160+posy)
        listaAux = ListaDoble()
        listaAux.agregarFinal(opcionCancion)
        listaVar.agregarFinal(var)

        listaC.agregarFinal(opcionCancion)
        # print(var.get())
        
        posy+=20
        aux = aux.siguiente
    




    
        

    


    
        
            

ventana = tk.Tk()
var = tk.StringVar()

fuente = tkFont.Font(family="Arial", size=15)
fuenteLabel = tkFont.Font(family="Arial", size=35)

ventana.geometry('1500x1000+170+10')
ventana.title('Manejo Grid')
ventana.configure(bg='white')

botonCargar = tk.Button(ventana, text="Seleccionar Archivo", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonCargar.pack()
botonCargar.place(x=25, y=10)

botonRHtml = tk.Button(ventana, text="Reporte HTML", command=LeerXml, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonRHtml.pack()
botonRHtml.place(x=250, y=10)

botonRGraphviz = tk.Button(ventana, text="Reporte Graphviz", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonRGraphviz.pack()
botonRGraphviz.place(x=475, y=10)

imgPlay = PhotoImage(file=f'../Img/play1.png')
botonReproducir = tk.Button(ventana, command=Play, image=imgPlay)
botonReproducir.pack()
botonReproducir.place(x=750, y=100)

imgNext = PhotoImage(file='../Img/next.png')
botonNext = tk.Button(ventana, command=Siguiente, image=imgNext)
botonNext.pack()
botonNext.place(x=1300, y=800)

imgAnterior = PhotoImage(file='../Img/anterior.png')
botonAnterior = tk.Button(ventana, command=Play, image=imgAnterior)
botonAnterior.pack()
botonAnterior.place(x=750, y=800)

imgStop = PhotoImage(file='../Img/stop.png')
botonStop = tk.Button(ventana, command=Stop, image=imgStop)
botonStop.pack()
botonStop.place(x=1300, y=100)

imgPausa = PhotoImage(file=f'../Img/pausa1.png')



label = tk.Label(ventana, fg='black', bg='thistle', text=txtLabel, font=fuenteLabel)
label.pack()
label.place(x=820, y=270, width=600, height=500)
label.configure(justify="left")

imgCancion = PhotoImage(file='../Img/alone.png')
labelImgCancion = tk.Label(ventana, image=imgCancion)
labelImgCancion.pack()
labelImgCancion.place(x=500, y=350)

labelCanciones = tk.Label(ventana, text='Canciones Disponibles', font=fuente, bg='red', fg = 'white')
labelCanciones.pack()
labelCanciones.place(x=20, y =100)

botonCrearListaReproduccion = tk.Button(ventana, command=obtenerOpcion, text='Crear Lista de Reproduccion', font=fuente, bg='midnightblue', fg = 'white', activebackground="powderblue")
botonCrearListaReproduccion.pack()
botonCrearListaReproduccion.place(x=20, y=900)
LeerXml()
ventana.mainloop()
# opcionCancion = tk.Radiobutton(ventana, text='cancion 1', value=1, variable=var)
# opcionCancion.pack
# opcionCancion.place(x=20, y=200)






