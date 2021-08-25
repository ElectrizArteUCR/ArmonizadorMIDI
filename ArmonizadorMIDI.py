from midiutil import MIDIFile
import random

A = 9
A_SOSTENIDO = 10
B = 11
C = 12
C_SOSTENIDO = 1
D = 2
D_SOSTENIDO = 3
E = 4
F = 5
F_SOSTENIDO = 6
G = 7
G_SOSTENIDO = 8
   
def cambiar_a_sostenidos(nota_tonica):

    if nota_tonica == "Bb":
        return "A#"
    elif nota_tonica == "Db":
        return "C#"
    elif nota_tonica == "Eb":
        return "D#"
    elif nota_tonica == "Gb":
        return "F#"
    elif nota_tonica == "Ab":
        return "G#"
    else:
        return nota_tonica

def obtener_notas_acorde(acorde, octava):
          
    if acorde == "A":
        acorde = [A, C_SOSTENIDO, E]
    elif acorde == "A#":
        acorde = [A_SOSTENIDO, D, F]
    elif acorde == "B":
        acorde = [B, D_SOSTENIDO, F_SOSTENIDO]
    elif acorde == "C":
        acorde = [C, E, G]
    elif acorde == "C#":
        acorde = [C_SOSTENIDO, F, G_SOSTENIDO]
    elif acorde == "D":
        acorde = [D, F_SOSTENIDO, A]
    elif acorde == "D#":
        acorde = [D_SOSTENIDO, G, A_SOSTENIDO]
    elif acorde == "E":
        acorde = [E, G_SOSTENIDO, B]
    elif acorde == "F":
        acorde = [F, A, C]
    elif acorde == "F#":
        acorde = [F_SOSTENIDO, A_SOSTENIDO, C_SOSTENIDO]
    elif acorde == "G":
        acorde = [G, B, D]
    elif acorde == "G#":
        acorde = [G_SOSTENIDO, C, D_SOSTENIDO]
        
    elif acorde == "Am":
        acorde = [A, C, E]
    elif acorde == "A#m":
        acorde = [A_SOSTENIDO, C_SOSTENIDO, F]
    elif acorde == "Bm":
        acorde = [B, D, F_SOSTENIDO]
    elif acorde == "Cm":
        acorde = [C, D_SOSTENIDO, G]
    elif acorde == "C#m":
        acorde = [C_SOSTENIDO, E, G_SOSTENIDO]
    elif acorde == "Dm":
        acorde = [D, F, A]
    elif acorde == "D#m":
        acorde = [D_SOSTENIDO, F_SOSTENIDO, A_SOSTENIDO]
    elif acorde == "Em":
        acorde = [E, G, B]
    elif acorde == "Fm":
        acorde = [F, G_SOSTENIDO, C]
    elif acorde == "F#m":
        acorde = [F_SOSTENIDO, A, C_SOSTENIDO]
    elif acorde == "Gm":
        acorde = [G, A_SOSTENIDO, D]
    elif acorde == "G#m":
        acorde = [G_SOSTENIDO, B, D_SOSTENIDO]
        
    for i, nota in enumerate(acorde):
        acorde[i] = acorde[i] + 12*octava

    return acorde

def obtener_tonica(acorde):

    if acorde == "A" or acorde == "Am":
        return A
    elif acorde == "A#" or acorde == "A#m":
        return A_SOSTENIDO
    elif acorde == "B" or acorde == "Bm":
        return B
    elif acorde == "C" or acorde == "Cm":
        return C
    elif acorde == "C#" or acorde == "C#m":
        return C_SOSTENIDO
    elif acorde == "D" or acorde == "Dm":
        return D
    elif acorde == "D#" or acorde == "D#m":
        return D_SOSTENIDO
    elif acorde == "E" or acorde == "Em":
        return E
    elif acorde == "F" or acorde == "Fm":
        return F
    elif acorde == "F#" or acorde == "F#m":
        return F_SOSTENIDO
    elif acorde == "G" or acorde == "Gm":
        return G
    elif acorde == "G#" or acorde == "G#m":
        return G_SOSTENIDO
 


   
def progresion_de_acordes(nota_tonica, tipo_de_base):

    progresion = []
    if tipo_de_base == 1:
        if nota_tonica == "C":
            progresion = ["C", "Am", "F", "G" ]
            
        if nota_tonica == "C#":
            progresion = ["C#","A#m", "F#", "G#"]
            
        if nota_tonica == "D":
            progresion = ["D", "Bm", "G", "A"]
            
        if nota_tonica == "D#":
            progresion = ["D#", "Cm", "G#", "A#"]
            
        if nota_tonica == "E":
            progresion = ["E", "C#m", "A", "B"]
            
        if nota_tonica == "F":
            progresion = ["F", "Dm", "A#", "C"]
            
        if nota_tonica == "F#":
            progresion = ["F#", "D#m", "B", "C#"]
            
        if nota_tonica == "G":
            progresion = ["G", "Em", "C", "D"]
            
        if nota_tonica == "G#":
            progresion = ["G#", "Fm", "C#", "D#"]
            
        if nota_tonica == "A":
            progresion = ["A", "F#m", "D", "E"] 
            
        if nota_tonica == "A#":
            progresion = ["A#", "Gm", "D#", "F"]
            
        if nota_tonica == "B":
            progresion = ["B", "G#m", "E", "F#"]
            
        return progresion
    
    elif tipo_de_base == 0:
        if nota_tonica == "C":
            progresion = ["C", "G", "Am", "Em" ]
            
        if nota_tonica == "C#":
            progresion = ["C#","G#", "A#m", "Fm"]
            
        if nota_tonica == "D":
            progresion = ["D", "A", "Bm", "F#m"]
            
        if nota_tonica == "D#":
            progresion = ["D#", "A#", "Cm", "Gm"]
            
        if nota_tonica == "E":
            progresion = ["E", "B", "C#m", "G#m"]
            
        if nota_tonica == "F":
            progresion = ["F", "C", "Dm", "Am"]
            
        if nota_tonica == "F#":
            progresion = ["F#", "C#", "D#m", "A#m"]
            
        if nota_tonica == "G":
            progresion = ["G", "D", "Em", "Bm"]
            
        if nota_tonica == "G#":
            progresion = ["G#", "D#", "Fm", "Cm"]
            
        if nota_tonica == "A":
            progresion = ["A", "E", "F#m", "C#m"]
                          
        if nota_tonica == "A#":
            progresion = ["A#", "F", "Gm", "Dm"]
            
        if nota_tonica == "B":
            progresion = ["B", "F#", "G#m", "D#m"]
        
        return progresion
    
    elif tipo_de_base == 2:
        if nota_tonica == "C":
            progresion = ["Cm", "A#", "Gm", "G#" ]

        if nota_tonica == "C#":
            progresion = ["C#m","B", "G#m", "A"]

        if nota_tonica == "D":
            progresion = ["Dm", "C", "Am", "A#"]

        if nota_tonica == "D#":
            progresion = ["D#m", "C#", "A#m", "B"]

        if nota_tonica == "E":
            progresion = ["Em", "D", "Bm", "C"]

        if nota_tonica == "F":
            progresion = ["Fm", "D#", "Cm", "C#"]

        if nota_tonica == "F#":
            progresion = ["F#m", "E", "Bm", "D"]

        if nota_tonica == "G":
            progresion = ["Gm", "F", "Cm", "D#"]

        if nota_tonica == "G#":
            progresion = ["G#m", "F#", "D#m", "E"]

        if nota_tonica == "A":
            progresion = ["Am", "G", "Em", "F"] 

        if nota_tonica == "A#":
            progresion = ["A#m", "G#", "Fm", "F#"]

        if nota_tonica == "B":
            progresion = ["Bm", "A", "F#m", "G"]
        
        return progresion
    
    elif tipo_de_base == 3:
        if nota_tonica == "C":
            progresion = ["D#", "A#", "Cm", "G#" ]

        if nota_tonica == "C#":
            progresion = ["E","B", "C#m", "A"]    

        if nota_tonica == "D":
            progresion = ["F", "C", "Dm", "A#"]  

        if nota_tonica == "D#":
            progresion = ["F#", "C#", "D#m", "B"]  

        if nota_tonica == "E":
            progresion = ["G", "D", "Em", "C"]  

        if nota_tonica == "F":
            progresion = ["G#", "D#", "Fm", "C#"]   

        if nota_tonica == "F#":
            progresion = ["A", "E", "F#m", "D"] 

        if nota_tonica == "G":
            progresion = ["A#", "F", "Gm", "D#"]     

        if nota_tonica == "G#":
            progresion = ["B", "F#", "G#m", "E"]   

        if nota_tonica == "A":
            progresion = ["C", "G", "Am", "F"]    

        if nota_tonica == "A#":
            progresion = ["C#", "G#", "A#m", "F#"] 

        if nota_tonica == "B":
            progresion = ["D", "A", "Bm", "G"]
        
        return progresion
    
def bajos(progresion, octava):
    
    bajos = []
    for i, acorde in enumerate(progresion):
        bajo = obtener_tonica(progresion[i]) + 12*octava
        bajos.append(bajo)
    return bajos

def obtener_base(iteraciones, progresion, bajos, tipo_de_base, nombre_archivo):
    
    mid = MIDIFile()
    track = 0
    canal = 0
    tiempo = 0
    volumen_acorde = 100
    if tipo_de_base == 1:
        duracion_acorde = 4
        for i in range(iteraciones):
            for acorde in range(len(progresion)):
                for nota in range(len(progresion[acorde])):
                    
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo, duracion_acorde, volumen_acorde + random.randint(-10, 10))
                    
                mid.addNote(track, canal, bajos[acorde], tiempo, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde]+12, tiempo+0.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde], tiempo+1, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde]+12, tiempo+1.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde], tiempo+2, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde]+12, tiempo+2.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde], tiempo+3, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde]+12, tiempo+3.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                tiempo += duracion_acorde
        with open(nombre_archivo, "wb") as output:
            mid.writeFile(output)

    if tipo_de_base == 0:
        tempo = 130
        mid.addTempo(track, tiempo, tempo)
        duracion_acorde = 8
        for i in range(iteraciones):
            for acorde in range(len(progresion)):
                for nota in range(len(progresion[acorde])):
                    
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo, duracion_acorde/2, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 4, duracion_acorde/2, volumen_acorde + random.randint(-10, 10))
                    
                mid.addNote(track, canal, bajos[acorde], tiempo, duracion_acorde/4, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde]-5, tiempo + 2, duracion_acorde/4, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde], tiempo + 4, duracion_acorde/4, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde]-5, tiempo + 6, duracion_acorde/4, volumen_acorde + random.randint(-10, 10))
                tiempo += duracion_acorde
        with open(nombre_archivo, "wb") as output:
            mid.writeFile(output)
            
    if tipo_de_base == 2:
        tempo = 89
        mid.addTempo(track, tiempo, tempo)
        duracion_acorde = 4
        for i in range(iteraciones):
            for acorde in range(len(progresion)):
                for nota in range(len(progresion[acorde])):
                    
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 0, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 0.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 1, duracion_acorde/4, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 2, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 2.5, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 2.75, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 3.25, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 3.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))

                mid.addNote(track, canal, bajos[acorde], tiempo + 2, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde] + 7, tiempo + 2.5, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde] + 7, tiempo + 3, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde], tiempo + 3.5, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                tiempo += duracion_acorde                        
        with open(nombre_archivo, "wb") as output:
            mid.writeFile(output)
            
    if tipo_de_base == 3:
        tempo = 89
        mid.addTempo(track, tiempo, tempo)
        duracion_acorde = 4
        for i in range(iteraciones):
            for acorde in range(len(progresion)):
                for nota in range(len(progresion[acorde])):
                    
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 0, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 0.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 1, duracion_acorde/4, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 2, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 2.5, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 2.75, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 3.25, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                    mid.addNote(track, canal, progresion[acorde][nota], tiempo + 3.5, duracion_acorde/8, volumen_acorde + random.randint(-10, 10))

                mid.addNote(track, canal, bajos[acorde], tiempo + 2, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde] + 7, tiempo + 2.5, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde] + 7, tiempo + 3, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                mid.addNote(track, canal, bajos[acorde], tiempo + 3.5, duracion_acorde/16, volumen_acorde + random.randint(-10, 10))
                tiempo += duracion_acorde
        with open(nombre_archivo, "wb") as output:
            mid.writeFile(output)


print("Ingrese la nota tónica sobre la que desea generar la improvisación: ")
## Nota tónica ingresada por el usuario
nota_tonica = str(input())
nota_tonica = cambiar_a_sostenidos(nota_tonica)

print("Elija una base del 0 al 3: ")
## Tipo de base ingresado por el usuario
tipo_de_base = int(input())

print("Ingrese la octava en la que desea generar la progresión base: ")
## Octava ingresada por el usuario
octava = int(input())

print("Ingrese la cantidad de iteraciones de la progresión base: ")
## Cantidad de iteraciones deseadas por el usuario
iteraciones = int(input())

print("Ingrese el nombre del archivo de salida: ")
## Nombre del archivo deseado por el usuario
nombre = str(input())

nombre = nombre + ".mid"

## Progresión de acordes obtenida a partir de los parámetros suministrados por el usuario  
progresion = progresion_de_acordes(nota_tonica, tipo_de_base)

## Notas MIDI de los acordes de la progresión
notas_progresion = []

for index, acorde in enumerate(progresion):
    ## Notas MIDI individuales para cada acorde de la progresión
    notas = obtener_notas_acorde(progresion[index], octava)
    notas_progresion.append(notas)    

if tipo_de_base == 1:
    ## Bajos o notas tónicas de la progresión de acordes.
    bajos = bajos(progresion, octava - 2)
elif tipo_de_base == 2 or tipo_de_base == 3:
    bajos = bajos(progresion, octava + 1)
else:
    bajos = bajos(progresion, octava - 1)

base = obtener_base(iteraciones, notas_progresion, bajos, tipo_de_base, nombre)