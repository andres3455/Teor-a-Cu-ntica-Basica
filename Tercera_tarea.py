import numpy as np
import primera_tarea
import segunda_tarea as lol

def matriz(m1, v1):
    return m_mul(m1, v1)

def m_diagonal(x):
    y = [[(0, 0) for j in range(x)] for i in range(x)]
    for i in range(x):
        for j in range(x):
            if i == j:
                y[i][j] = (1, 0)
    return y

def longitud(Vector1, Vector2):
    if len(Vector1) == len(Vector2):
        return True
    else:
        return False
#1
def probabilidad(ket, po):
    n = lol.norma_de_un_vector(ket)
    p2 = op.modulo(ket[p]) ** 2
    result = round((p2/n ** 2) * 100, 2)
    return result

def amplitud(Ket1, Ket2):
    v1 = []
    for index in range(len(Ket2)):
        auxiliar = [Ket2[index]]
        v1 += [auxiliar]
    K2 = lol.matriz_conjugada(v1)
    v2 = []
    for index in range(len(ket2)):
        v2 += ket2[index]
    norma_1 = lol.norma_de_un_vector(Ket1)
    norma_2 = lol.norma_de_un_vector(ket2)
    norma = norma_1 * norma_2
    probabilidad = [lol.longitud_vector(v2, Ket1)]
    check = lol.vector_scalar((1/norm, 0), probabilidad)[0]
    point = (round(check[0], 2), round(check[1], 2))
    return point
# 2
def matriz_hermitiana(x):
"""Recibe una matriz y determina si es hermitiana o no es hermitiana
    (x)---> (x)
    """
    longitud = len(x)
    k = [[(0,0) for i in range (longitud)] for i in range (longitud)]
    adj = lol.matriz_adjunta(x)
    h = adj == x
    return x
def media(observable, Ket):
    Ket_aux = []
    for index in range(len(Ket)):
        a = [Ket[index]]
        Ket_aux += [a]
    if matriz_hermitiana(observable):
        B = lol.matriz_conjugada(K_aux)
        psp = matriz(observable, Ket_aux)
        check = lol.longitud_vector(psp, B)
        point = (round(check[0], 2), round(check[1], 2))
        return point
    else:
        return "El observable es invalido"

def varianza(observable, Ket):
    Ket_aux = []
    for index in range(len(Ket)):
        a = [Ket[index]]
        K_aux += [a]
    B = lol.matriz_conjugada(K_aux)
    media = media(observable, Ket)
    m = [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
    for i in range(len(observable)):
        for j in range(len(observable[i])):
            if i == j:
                m[i][j] = op.multiplicacion((-1, 0), media)
    m = lol.añadir(m, observable)
    square = lol.producto(m, m)
    ac = lol.matriz(square, K_aux)
    return lol.longitud_vector(ac, B)
#3
def val_vectores(observable):
    val, vectores = np.linalg.eig(observable)
    l_val = []
    l_vectores = []
    for index in range(len(val)):
        l_val += [(val[index].real, val[index].imag)]
    for index in range(len(vectores)):
        V = []
        for index_2 in range(len(vectores[0])):
            V += [(vectores[index][index_2].real, vectores[index][index_2].imag)]
        l_vectores += [V]
    return l_valores, l_vectores
def probabilidades_vectores(i, observable, po):
    vectores = va_vectores(observable)[1]
    return amplitud(i, vectores[po])

#4
def unitaria(m1):
    if length(m1, m1[0]):
        mI = diagonal((len(m1)))
        m2 = lol.matriz_adjunta(m1)
        product = op.m_mul(m1, m2)
        flag = True
        aux = Spaces.f_aux(product)
        for i in range(len(m1)):
            for j in range(len(m1)):
                if product[i][j] != mI[i][j]:
                    flag = False
        if flag:
            return True
        else:
            return False
    else:
        return False

def dinamica(mat_u, v1, t):
    if m_unitaria(mat_u):
        for index in range(t):
            v1 = Spaces.m_action(mat_u, v1)
        return v1
    else:
        return "Matriz no valida"

print(dinamica([[(0, 1), (0, 0)], [(0, 0), (0, 1)]], [(1, 0), (0, 0)], 1))
