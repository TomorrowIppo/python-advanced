

class Robot:

    '''
    [Robot Class]
    Author : 김병진
    Role : ???
    
    '''

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name    # 인스턴스 변수
        self.code = code    # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code ...

        print(f"Greetings, my master call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"{self.name} Counts : {Robot.population}")

    # 클래스 메서드
    @classmethod
    def how_many(cls):  # cls는 self랑 비슷하되 다름. self - instance / cls - class
        print(f"We have {cls.population} robots.")

    @staticmethod
    def this_is_robot_class():
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"
    
    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


bixby = Robot('bixby', 123123123123)

print(dir(bixby))

print(bixby) # <__main__.Robot object at 0x1005b5a90>

bixby()