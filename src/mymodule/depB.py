from mymodule.depA import dep_funcA


def dep_funcB():
    print('Dependency function B.')
    dep_funcA()
