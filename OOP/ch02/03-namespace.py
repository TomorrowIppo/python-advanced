"""

#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다
#* dir() : 네임스페이스의 key값을 확인할 수 있다
#* __doc__: class의 주석을 확인한다
#* __class__: 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.

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


print(f"Robot Counts : {Robot.population}")

siri = Robot('siri', 21039788127)
jarvis = Robot('jarvis', 12312312323)
bixby = Robot('bixby', 32132132132)

print(Robot.__dict__)

print(siri.__dict__)

print(jarvis.__dict__)

print(siri.population)

siri.how_many()

# 파이썬은 유저가 사용하기 편하게, 인스턴스 내부에서 접근하려는데 없으면 클래스에서 찾는다
# 이러한 네임스페이스 설계 때문에 위에처럼 인스턴스에서 원본 클래스로의 접근이 가능하다. 
# 하지만 반대로 클래스에서 인스턴스로는 안된다.

# Robot.say_hi() # 이건 안됨
Robot.say_hi(siri) # 이건 됨 근데 이건
siri.say_hi() # 이거와 같으며 사실 이 코드의 원본은 바로 위의 코드이다.

print(siri.__dir__)
print(dir(siri))    # siri 인스턴스를 통해 접근할 수 있는 key value를 얻음

print(dir(Robot))   # 원본 클래스에 비해 인스턴스가 더 접근할 수 있는 key value가 많음

print(Robot.__doc__)    # 주석을 통한 클래스 정보 확인

print(siri.__class__)

