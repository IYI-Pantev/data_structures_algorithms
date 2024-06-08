def func_three():
    print('three')

def func_two():
    func_three()
    print('two')

def func_one():
    func_two()
    print('one')

func_one()