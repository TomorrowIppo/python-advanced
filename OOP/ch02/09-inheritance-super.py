"""
* [클래스 상속]

* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

* 3. 메서드 오버라이딩

* 4. super()

* 5. Python의 모든 클래스는 object를 상속한다. : 모든 것은 객체다

* 6. MyClass.mro() --> 상속 관계를 보여준다.
"""

class Robot:

    '''
    [Robot Class]
    Author : 김병진
    Role : ???
    
    '''

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name    # 인스턴스 변수
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


class Siri(Robot):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b
    
    def cal_flexable(self, a, b):
        super().say_hi()
        return self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)

    @classmethod
    def hello_apple(cls):   # Siri를 가리킴.
        print(f"{cls}")     # staticmethod 였다면 부모인 로봇을 가리킴

    def say_hi(self):
        # code ...
        print(f"Greetings, my master call me {self.name}. by apple.")

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"


siri = Siri("iphone14", 17)

print(siri.age)
print(siri.name)

print(Siri.how_many())

siri.say_hi()
print(siri.cal_flexable(10, 17))