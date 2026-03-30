

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


bixby = Robot('bixby')

print(bixby.this_is_robot_class())  # staticmethod 데코레이터를 통해 인스턴스도 접근 가능 (전역)
print(Robot.this_is_robot_class())  # 기본적으로 위의 데코레이터가 없어도 접근 가능 