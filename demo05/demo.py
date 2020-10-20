a=7
b=8
def add(a: float, b: float) -> float:
    '''Calculates sum of two arguments'''
    print(a, '+', b, '=', a + b)
    return a + b
def calc_pipeline(
   a: float =0,
   b: float =7
):
    #Passing pipeline parameter and a constant value as operation arguments
    add_task = add_op(a, 4) #Returns a dsl.ContainerOp class instance. 
    
    #You can create explicit dependency between the tasks using xyz_task.after(abc_task)
    add_2_task = add_op(a, b)
    
    add_3_task = add_op(add_task.output, add_2_task.output)
