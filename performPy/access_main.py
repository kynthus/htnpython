import pycaccess


if __name__ == '__main__':
    mycar = pycaccess.MyCar('PRIUS', 62053.738, 2560000)

    print(mycar.name)
    print(mycar.mileage)
    print(mycar.price)

    mycar.name = 'Lamborghini'
    mycar.mileage = 0.0
    mycar.price = 9999

    mycar.introduction()

    mycar.price = -1
