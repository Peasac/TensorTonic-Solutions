import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    y=[]
    for new_x in x:
        
        if new_x>0:
            y.append(new_x)
        else:
             y.append(alpha*(math.exp(new_x)-1))
    return y
    pass