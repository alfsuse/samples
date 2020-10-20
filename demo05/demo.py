import kfp
import kfp.dsl as dsl
from kfp import compiler
from kfp import components

EXPERIMENT_NAME = 'Simple notebook pipeline'        # Name of the experiment in the UI
BASE_IMAGE = 'tensorflow/tensorflow:2.0.0b0-py3' 
a= 7
b= 8

@dsl.python_component(
    name='add_op',
    description='adds two numbers',
    base_image=BASE_IMAGE  # you can define the base image here, or when you build in the next step. 
)
def add(a: float, b: float) -> float:
    '''Calculates sum of two arguments'''
    print(a, '+', b, '=', a + b)
    return a + b
    
add_op = components.func_to_container_op(
    add,
    base_image=BASE_IMAGE, 
)
@dsl.pipeline(
   name='Calculation pipeline',
   description='A toy pipeline that performs arithmetic calculations.'
)
def calc_pipeline(
   a: float =0,
   b: float =7
):
    #Passing pipeline parameter and a constant value as operation arguments
    add_task = add_op(a, 4) #Returns a dsl.ContainerOp class instance. 
    
    #You can create explicit dependency between the tasks using xyz_task.after(abc_task)
    add_2_task = add_op(a, b)
    
    add_3_task = add_op(add_task.output, add_2_task.output)
 
