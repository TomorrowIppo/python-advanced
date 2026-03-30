# decorator


def copyright(func):
    
    # 함수 재정의 후 리턴
    def new_func():
        print("@ amamove asdfwezsdfsafsdfwef")
        func()

    return new_func


@copyright
def smile():
    print(":smile")


@copyright
def angry():
    print(":angry")


@copyright
def love():
    print(":love")


# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)
# 이렇게 하지 않고, 위에 처럼 함수 바로 위에 @copyright를 하면 편하게 함수 재정의를 할 수 있다
# 개발에서의 유지보수 효율성을 위해 만들어짐

smile()
angry()
love()