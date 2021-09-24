class Rectangle():
    #長方形（ちょうほうけい）
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #長方形の周囲長(しゅういちょう)
    def get_perimeter(self):
        return (self.x + self.y) * 2
    #長方形の面積（めんせき）
    def get_area(self):
        return self.x * self.y
    
class Vehicle:
    def __init__(self, fuelInTank, consumption, roadDistance):
        self.fuelInTank = fuelInTank
        self.consumption = consumption
        self.roadDistance = roadDistance
    
    def get_fuel_in_tank(self):
        return self.fuelInTank #L
    
    def get_consumption(self):
        return self.consumption #L/100km
    
    def get_roadDistance(self):
        return self.roadDistance #道路の長さ(どうろのながさ)

    def get_used_fuel(self):
        return self.roadDistance / 100 * self.consumption

    def get_drivable_distance(self):
        return round(self.fuelInTank / self.consumption * 100)

    def get_remaining_fuel(self):
        if self.fuelInTank - self.get_used_fuel() <= 0:
            return 0
        else:
            return self.fuelInTank - self.get_used_fuel()


def task1():
    englishGrade = float(input("英語の学年末の成績を入力してください"))
    mathGrade = float(input("数学の学年末の成績を入力してください"))
    itGrade = float(input("プログラミングの学年末の成績を入力してください"))

    print("その三つの成績の平均は{0}".format((englishGrade + mathGrade + itGrade)//3))

def task2():
    currentTime = int(input("今の時を入力してください"))
    alarmTime = int(input("アラームが鳴る時を入力してください"))

    if alarmTime < currentTime:
        alarmRingTime = 24 - currentTime + alarmTime

    else:
        alarmRingTime = alarmTime - currentTime
    
    print("アラームが{0}時間後が鳴ります".format(alarmRingTime))

def task3():
    exchangeRate = int(input("現在のEUR/HUFの為替レートを入力してください(１ユーロはXフォリントような形式で)"))
    currentlyHeldEuros = int(input("今の持っていますユーロを入力してください"))
    print("{0}ユーロは{1}フォリントです".format(currentlyHeldEuros, currentlyHeldEuros*exchangeRate))

def task4():
    a_side = int(input("長方形のA辺CMでを入力してください"))
    b_side = int(input("長方形のB辺CMでを入力してください"))

    rectangle = Rectangle(a_side, b_side)

    print("長方形の周囲兆は{0}cmです".format(rectangle.get_perimeter()))
    print("長方形の面積は{0}cm2です".format(rectangle.get_area()))

def task5():
    #道路の長さ分からないので０を使ったいます。
    fuelInTank = int(input("燃料の量はどれくらい持っていますか？"))
    consumption = int(input("車の消費量を入力してください(L/100km)"))

    car = Vehicle(fuelInTank, consumption, 0)
    print("{0}kmぐらいの走行が可能です。".format(car.get_drivable_distance()))


def main():
    task1()
    task2()
    task3()
    task4()
    task5()

if __name__ == '__main__':
    main()