def functionA(fn):
    print('Def A is working')
    fn()
    print('Def A is closing')

    return fn()


@functionA
def functionB():
    print('Def B is working')




