from mymodule.depB import dep_funcB


def dep_funcA():
    print('Dependency function A.')
    dep_funcB()
