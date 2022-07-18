#!/usr/bin/env python
# coding: utf-8

# # <center> Ikiam
# ## <center> Facultad Ciencias de la Vida
# ### <center> Bioinformatica 
# **Tarea N°6**
# - Crear el modulo que se llame poblacionmendeliana.
# - Guardar las 3 funciones de: 
#  * Generacion de la poblacion.
#  * conteo de frecuencia de alelos.
#  * reproduccion de la poblacion en el modulo del poblacionmendeliana.
# - Generar una explicación para cada función.
# - Generar las poblaciones 500 generaciones. 
# - Calcular las proporciones de AA, Aa, aA, aa de todas las generaciones.
# - Generar el repositorio tarea N°6 con un readme.
# 
# <center> **DESAROLLO DEL MÓDULO**

# In[3]:


# FUNCIÓN 1. Generación de la población

import scipy # for random numbers

def build_population(N, p):
    """
    N = La entrada del tamaño de la población. Cada individuo tiene dos cromosomas.
    p = Es la probabilidad de tener un alelo "A"
    1-p = Es la probabilidad de tener un alelo "a"
    population = Es una lista de las posibles duplas.
    
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population


# In[4]:


# FUNCIÓN 2. Conteo de frecuencia de alelos
def compute_frequencies(population):
    """ 

    Cuenta genotipos 
    Devuelve un diccionario de freciencias genotipicas
    
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})


# In[5]:


# FUNCIÓN 3. Reproduccion de la poblacion en el modulo del poblacionmendeliana.

def reproduce_population(population):
    """
    Crear nueva generación a través de la reproducción.
    Para cada uno de N nuevos descendientes:
    - elegir a los padres al azar.
    - la descendencia recibe un cromosoma de cada uno de los padres.

    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation


# In[ ]:




