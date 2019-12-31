import pyccar


if __name__ == '__main__':
    mycar = pyccar.MyCar('PRIUS', 62053.738, 2560000)

    print(mycar.name)
    print(mycar.mileage)
    print(mycar.price)

    mycar.name = 'Lamborghini'
    mycar.mileage = 0.0
    mycar.price = 30160000

    mycar.introduction()
