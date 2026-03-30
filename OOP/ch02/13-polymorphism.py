"""
polymorphism
여러 형태를 가질 수 있도록 한다.


"""


class Robot:

    '''
    [Robot Class]
    '''

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    __population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.__name = name    # 인스턴스 변수
        self.__age = age      # 언더바를 한쪽에만 두번 쓰면 private
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property   # Getter
    def age(self):
        return self.__age
    
    @age.setter # Setter
    def age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age
        else:
            raise ValueError()
        
    # 인스턴스 메서드
    def __say_hi(self):
        # code ...
        print(f"Greetings, my master call me {self.__name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 클래스 메서드
    @classmethod
    def how_many(cls):  # cls는 self랑 비슷하되 다름. self - instance / cls - class
        print(f"We have {cls.__population} robots.")


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class Siriko(Robot):
    def say_apple(self):
        print("안녕하세요.")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요")


