from enum import Enum

Color = Enum('Color',('red','blue','yellow'))

# Color = type('Color',(object,Enum),dict(red='red', blue='blue', yellow='yellow'))

for color in Color:
    print(color.name,color.value,type(color),'\n')

