import pycinherit


if __name__ == '__main__':
    car = pycinherit.F1Car('AAA', 70212.6, 15840000, 120)
    car.introduction()
    car.run()
    print(car.name)
    print(car.mileage)
    print(car.price)
    print(car.speed)
    car.name = 'BBB'
    car.mileage = 64554.3512
    car.price = 16200000
    car.speed = 150
    car.introduction()
    car.run()
