def add(x , y):
    return x + y


def concatenate(x,y):
    return str(x) + str(y)


def operate(operation , x,y):
    """

        :param This is a operation that needs to be preformed:
        :param x The first operand :
        :param y The second operand :
        :return The result of the operation:
        """
    return operation(x,y)

result_sum = operate(add,3,4)
result_concatenate = operate(concatenate , 3 , 4)
print("Result of sum " ,result_sum)
print( "Result of :" ,result_concatenate)