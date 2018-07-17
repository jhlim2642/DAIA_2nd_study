# 계산기
class Calc:
    classLog = []
    # 생성자 : 클래스로 객체를 만들 때 사용자가 호출하지 않아도 자동으로 호출되는 함수
    def __init__(self, id):
        print("계산기를 시작합니다. 아이디는 " + str(id) + " 입니다.")
        self.log = []
        Calc.classLog.append(id)

    def add(self, op1, op2):
        print(op1 + op2)
        self.log.append(str(op1) + "+" + str(op2))

    def mul(self, op1, op2):
        print(op1 * op2)
        self.log.append(str(op1) + "*" + str(op2))

    def div(self, op1, op2):
        #if (op2 == 0):
        #    return -1
        #예외처리
        # try : 오류가 있을 수도있느 코드 검사
        # except : try구문안에서 발생한 오류 처리
        # raise : 사용자가 오류를 일부러 일으킬때 사용
        # finally : 구분없이 실행되는 부분
        try:
            print(op1 / op2)
            self.log.append(str(op1) + "/" + str(op2))
        except ZeroDivisionError:
            print("error")

    def printLog(self):
        print(self.log)

calc1 = Calc(1)
calc2 = Calc(2)

calc1.add(1, 2)
calc2.mul(3, 4)
calc1.div(3,0)
print(Calc.classLog)

# Naming Convention
# (1) 클래스 첫글자는 대문자
# (2) 함수와 변수의 첫 글자는 소문자
# (3) 연결된 단어의 경우 대문자로 구분 (e.g ClassName, variableName (camel case))

# 클래스 변수와 객체 변수
# 클래스 변수 : 해당 클래스로 만들어진 모든 객체가 서로 공유하는 변수
# a = ClassName()
# b = ClassName()
# 객체 변수
# a.result = 0
# b.result = 23

# class ClassName:
# 클래스 변수
#   classVariable1 = 20
#   classVariable2 = 30

#    def __init__(self,param1, param2):
# 객체변수
#        self.instanceVariable1 = param1
#        self.instanceVariable2 = param2
