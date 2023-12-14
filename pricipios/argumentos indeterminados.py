def indeterminados(*args):
    for i in args:
        print(i)


indeterminados(1,"wazaza",(1,2,3,4,),4.6)




def nombre_indeterminados(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])


nombre_indeterminados(n=2,z="hola",f=[1,2,3,4,5],t=True)