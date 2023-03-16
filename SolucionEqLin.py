import numpy as np
import time

n=int(input('¿Cuantas columnas?  '))
m=int(input('¿Cuantas filas?  '))

eleccion=input('\n¿Qué sistema deseas resolver? Pulsa el número de la eleccción\n1 Generar matriz aleatoria\n2 Ingresar todos los coeficientes\n')
while eleccion not in ('1','2'):
    eleccion=input('\nRespuesta no reconocida. ¿Qué sistema deseas resolver? Pulsa el número de la eleccción\n1 Generar matriz aleatoria\n2 Ingresar todos los coeficientes\n')

if eleccion=='1':
    matr=np.random.rand(m,n)
    vector_result=np.random.rand(m,1)
    print('Matriz generada y vector de resultados:\n', matr,vector_result)
if eleccion=='2':
    matr=np.zeros((m,n))
    vector_result=np.zeros((m,1))

    _m,_n=0,0
    for fila in range(m):
        for columna in range(n):
            value=eval(input(f'Valor del coeficiente {_m}{_n}:  '))
            matr[_m,_n]=value
            _n+=1
        val=eval(input(f'Valor independiente de la ecuacion {_m}°:  '))
        vector_result[_m,0]=int(val)
        _m+=1
        _n=0

tiempo_inicial=time.time()
matr_or,vector_or=matr,vector_result

sobredeterminado=False
inconsistente=False
for column in range(n):
    m_pivot,n_pivot=column,column
    try:
        if matr[m_pivot,n_pivot]!=1:
            matr[m_pivot],vector_result[m_pivot]=matr[m_pivot]/matr[m_pivot,n_pivot],vector_result[m_pivot]/matr[m_pivot,n_pivot]
            print('Normalizacion:\n',matr,'\n',vector_result)
    except IndexError:
        print('Matriz sobredeterminada (Mayor cantidad de varables que de ecuaciones)\nSolución no exacta')
        sobredeterminado=True
        break

    for row in range(m):
        print('\n',column,row)
        if row==m_pivot:continue
        matr[row],vector_result[row]=matr[row]+(matr[m_pivot]*matr[row,column]*-1),vector_result[row]+(vector_result[m_pivot]*matr[row,column]*-1)
        print(2,matr,'\n',vector_result)
        if np.all(matr[row]==0):inconsistente=True;print('Ojo aquí')
    
    if inconsistente==True:print('Se llegó a un a solución que demuestra que el sistema es inconsistente');break



print(3, matr,vector_result)

print('-'*40,'PROCESO FINALIZADO','-'*40)
Ab = np.hstack((matr_or, vector_or))     #Para juntar el vector resultado con la matriz de coeficientes
if inconsistente:
    print('\n\nEL SISTEMA INGRESADO ES INCONSISTENTE.')
if sobredeterminado:
    print('\n\nEL SISTEMA INGRESADO ES SOBREDETERMINADO (MAS VARIABLES QUE ECUACIONES)\nPOR LO QUE NO HAY UNA SOLUCIÓN EXACTA')
else:
    iterator=1
    for i in vector_result:
        print(f'X{iterator}=',i[0])
        iterator+=1


print('\n\nMatriz resultado:\n\n',Ab)
print(f'\n\nTIEMPO DE EJECUCIÓN: {time.time()-tiempo_inicial} segundos')
print('-'*(80+len('PROCESO FINALIZADO')))