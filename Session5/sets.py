st = {}
st2 = set()

st = {'elemento1','elemento2','elemento3','elemento4'}

#todo adicionar elementos al conjunto
st.add('item5')
st.update(['item6','item7','item8'])

#todo removiendo elementos del conjunto
st.remove('item8')
st.add('item5') #todo no permite elementos duplicados

#st[0]="item6" #todo no se puede actualizar un elemento del set

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}

st3=st1.union(st2)
#print(st3)

#todo pensemos en matematicas y conjuntos

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2))

#todo diferencia entre conjuntos
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
#print(st2.difference(st1))
#print(st1.difference(st2))

#todo 

"""
Un conjunto puede ser un subconjunto o superconjunto de otros 
conjuntos:
Subconjunto: issubset()
Súper conjunto: issuperset
"""

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}

print(st2.issubset(st1))




