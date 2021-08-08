숫자처리함수
    abs(-5) # 5
    pow(4, 2) # 16
    max(5, 12) # 12
    min(5, 12) # 5
    round(3.14) # 3

math library
    from math import * # math lib 에 있는 모든 기능을 쓰겠다.
    floor(4.99) # 4
    ceil(3.14) # 4
    sqrt(16) # 4

랜덤함수 # 무작위로 숫자를 뽑아줌
    from random import *
    random() # 0.0 ~ 1.0 미만의 무작위 실수를 반환
    int() # 정수형으로 변환
    randrange(1, 46) # 1 ~ 46 미만의 무작위 실수를 반환
    randint(1, 45) # 1 ~ 45 이하의 무작위 정수를 반환
    suffle(lst) # lst 값의 위치를 무작위로 변경
    sample(lst, 1) # lst 에서 무작위 값을 1 개 반환

문자열처리함수
    var = 'Python is Amazing'
    var.lower() # 소문자 변환
    var.upper() # 대문자 변환
    var[0].isupper() # 대문자인지 확인 (True, False)
    len(var) # 문자열의 길이 반환
    var.replace('Python', 'Java') # 'Python' 을 'Java' 로 변환
    
    index = var.index('n')
    var.index('n') # 'n' 이라는 문자의 위치 반환
    var.index('n', inddx + 1) # 처음 찾은 index 다음에 나오는 'n' 문자 위치 반환
    var.find('Java') # 원하는 값이 없을 경우 -1 을 반환
    # .index 와 .find 의 차이 : 원하는 값이 없을 경우 index 는 에러 find 는 -1
    var.count('n') # 'n' 이 총 몇번 나오는지 반환
    
문자열포맷
    Method 1
        print('I am %d years old.' %20) # %d 는 정수만 반환 가능 decimal
        print('I like %s.' %'Python') # %s 는 문자열만 반환 가능 string
        print('Apple starts with %c. %'A') # %c 는 한문자만 반환 가능 character
        print('I like %s and %s.' %('blue', 'red')) # 뒷 부분에 소괄호를 이용하여 여러개 반환 가능
    Method 2
        print('I am {} years old.'.format(20)) # % 대신에 format 함수를 활용하여 {}로 같은 기능 활용 가능
        print('I like {0} and {1}.'.format('blue', 'red')) # {} 안에 index 를 부여함으로써 format 함수에 들어있는 값들을 순서에 맞게 반환 가능
        print('I am {age} and I like {color}.'.format(age=20, color='red')) # {} 안에 변수를 선언함으로써 format 함수에 들어있는 값들을 변수에 맞게 반환 가능
    Method 3
        age = 20
        color = 'red'
        print(f'I am {age} and I like {color}.') # .format() 대신 f 로도 사용 가능

탈출 문자
    \n # 줄바꿈
    \' # 작은 따옴표를 문자로 변환
    \\ # '\' 문자로 변환
    \r # 커서를 맨 앞으로 이동
    \b # 한 글자 삭제
    \t # 탭
    
리스트
    subway = ['유재석', '조세호', '박명수', '유재석']
    subway.index('조세호') # '조세호' 가 몇번째 자리에 있는지
    subway.append('하하') # '하하' 를 맨 마지막에 추가
    subway.insert(1, '정형돈') # '정형돈' 을 1번째 자리에 끼워넣음
    subway.pop() # 맨 마지막 원소를 반환 후 제거
    subwat.count('유재석') # '유재석' 이 몇번 나오는지 확인
    
정렬
    num = [5, 2, 4, 3, 1]
    num.sort() # 순서대로 정렬
    num.reverse() # 순서뒤집어서 정렬
    num.clear() # num 리스트를 초기화
    
    num.extend(subway) # num 에 subway 를 뒤에 붙힘

사전
    dict = {3:'three', 100:'hundred'} # key:value 패턴으로 자료 저장
    print(dict[3]) # key 가 3 인 value 를 출력
    print(dict.get(3)) # key 가 3 인 value 를 출력
    # [] 와 .get 의 차이 : 해당 key 가 없을 경우 [] 는 에러 후 프로그램 종료 .get 은 None 을 출력 (문자열처리함수에서 .index 와 .find 와 비슷한 내용)
    print(dict.get(5), '사용 가능') # key 가 5인 value 가 없을 경우 '사용 가능' 출력
    print(3 in dict) # 3 이라는 key 가 dict 에 있을 경우 True 출력 없을 경우 False
    dict['C-20'] = '이십' # 새로운 key 와 value 선언
    dict[3] = '삼' # 기존에 있던 key 를 update
    del dict[100] # key 가 100 인 k,v 를 삭제
    print(dict.keys()) # key 값들만 출력
    print(dict.values()) # value 값들만 출력
    print(dict.items()) # k,v 모두 출력
    dict.clear() # dict 의 모든 값 삭제
    
튜플 # 변경되지 않는 list, list 보다 속도가 빠름
    menu = ('돈까스', '치즈까스')

세트 # 집합, set, 중복 안됨, 순서 없음
    set = {1,2,3,3,3} # {1,2,3}
    java = {'유재석', '김태호', '양세형'}
    python = set(['유재석', '박명수'])

교집합 # java 와 python 을 할 수 있는 개발자
    print(java & python)
    print(java.intersection(python))

합집합 # java 혹은 python 을 할 수 있는 개발자
    print(java | python)
    print(java.union(python))

차집합 # java 는 할 수 있지만 python 은 모르는 개발자
    print(java - python)
    print(java.difference(python))

# python 을 배운 개발자
    python.add('김태호')

# java 를 까먹음
    java.remove('김태호')

자료구조의 변경
    menu = {'커피', '우유', '주스'}
    menu = list(menu) # set 이였던걸 list 로
    menu = tuple(menu) # list 였던걸 tuple 로
    menu = set(menu) # tuple 이였던걸 set 으로

continue 와 break
    반복문에서 continue 명령이 있을 경우 다음 iteration 으로 넘어감
    반복문에서 break 명령이 있을 경우 반복문 탈출

한 줄 for # List comprehension

함수
    def open_account():
        print('새로운 계좌가 생성되었습니다.')

전달값과 반환값
    def deposit(balance, money): # balance, money 는 전달값
        print('입금이 완료되었습니다. 잔액은 {}원입니다.'.format(balance + money))
        return balance + money # balance + money 는 반환값

기본값
    def profile(name, age=17, main_lang='파이썬'): # 전달값이 없을 경우 기본값 반환
        print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}' \
        .format(name, age, main_lang))

키워드값
    def profile(name, age, main_lang):
        print(name, age, main_lang)

    profile(name='유재석', main_lang='파이썬', age=20) # 키워드에 맞게 함수 호출

가변인자
    def profile(name, age, *language): # 서로 다른 갯수의 값을 사용할 때는 가변인자 *
        print('이름 : {0}\t나이 : {1}\t'.format(name, age), end=' ')
        for lang in language:
            print(lang, end=' ')
        print()

지역변수와 전역변수
    지역변수 : 함수내에서만 쓸 수 있는 변수
    전역변수 : 프로그램내에서 어디서든 쓸 수 있는 변수
    
    gun = 10 # 전역변수
    
    def checkpoint(soldiers):
        global gun # 전역 공간에 있는 gun 사용
        # gun = 20 # 지역변수
        gun = gun - soldiers
        print('[함수 내] 남은 총 : {0}'.format(gun))

    print('전체 총 : {0}'.format(gun))
    checkpoint(2)
    print('남은 총 : {0}'.format(gun))

    def checkpoint_ret(gun, soldiers):
        gun = gun - soldiers
        print('[함수 내] 남은 총 : {0}'.format(gun))
        return gun

    print('전체 총 : {0}'.format(gun))
    gun = checkpoint_ret(gun, 2)
    print('남은 총 : {0}'.format(gun))

표준입출력
    print('Python', 'Java', 'JavaScript', sep=' vs ') # sep 를 통해 출력간 사이에 어떤 문자가 들어갈 지 설정 가능
    print('Python', 'Java', 'JavaScript', end='?') # end 를 통해 출력문 마지막에 들어갈 문자를 설정 (기본값은 줄바꿈)
    
    score = {'수학':0, '영어':50, '코딩':100}
    for subject, score in scores.items():
        print(subject.ljust(8), str(score).rjust(4), sep=':')
        ljust() = 왼쪽 정렬
        rjust() = 오른쪽 정렬

    for num in range(1, 21):
        print('대기번호 : ' + str(num).zfill(3))
        zfill() = 세개 공간을 확보 후 남은 공간은 0 으로 채우기

다양한 출력포맷
    print('{0: >+10}'.format(500)) # 10칸 확보, 오른쪽 정렬, 양수음수 구분
    print('{0:_<+10}'.format(500)) # 10칸 확보, 왼쪽 정렬, 양수음수 구분, 빈칸은 밑줄로 채우기
    print('{0:+,}'.format(100000000)) # 3자리마다 콤마 찍어주고, 부호 구분
    print('{0:^<+30,}'.format(100000000)) # 3자리마다 콤마 찍어주고, 부호 구분, 30자리 확보, 왼쪽정렬, 빈자리 ^로 채우기
    print('{0:.2f}'.format(5/3)) # 소수점 2번째자리까지 출력

파일입출력
    score_file = open('score.txt', 'w', encoding='utf8')
    print('수학 : 0', file=score_file)
    print('영어 : 50', file=score_file)
    score_file.close() # 파일 닫기
    # open(파일이름, 목적, encoding='utf8')

    score_file = open('score.txt', 'a', encoding='utf8')
    score_file.write('과학 : 80')
    score_file.write('\n코딩 : 100')
    score_file.close()
    #'a' 를 통해 append
    # .write() 를 통해 내용 추가, 줄바꿈 필요

    score_file = open('score.txt', 'r', encoding='utf8')
    print(score_file.read())
    score_file.close()
    # 전체 파일 읽기

    score_file = open('score.txt', 'r', encoding='utf8')
    while True:
        line = score_file.readline() # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
        if not line:
            break
        print(line, end='') # realline() 과 print() 가 줄바꿈을 하기 때문에
    score_file.close()
    # 파일이 몇줄인지 모를 경우 while 문 사용

    score_file = open('score.txt', 'r', encoding='utf8')
    lines = score_file.readlines() # 모든 라인을 리스트 형태로 저장
    for line in lines:
        print(line, end='')
    score_file.close()

pickle
    import pickle
    profile_file = open('profile.pickle', 'wb')  # wb = write binary
    profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
    print(profile)
    pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
    profile_file.close()

    profile_file = open('profile.pickle', 'rb')
    profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
    print(profile)
    profile_file.close()

with # 파일을 읽고 쓰는데 있어서 코드가 간결해지고 매번 파일을 닫아줄 필요가 없음
    import pickle
    with open('profile.pickle', 'rb') as profile_file:
        print(pickle.load(profile_file))
    # 위에 파일을 읽기 정보를 가져오는 과정이랑 같지만 파일을 다시 닫아줄 필요가 없음
    # pickle 없이 파일 쓰기
    with open('study.txt', 'w', encoding='utf8') as study_file:
        study_file.write('파이썬을 열심히 공부하고 있어요')
    # pickle 없이 파일 읽기
    with open('study.txt', 'r', encoding='utf8') as study_file:
        print(study_file.read())

클래스
    # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
    name = '마린'
    hp = 40
    damage = 5
    
    print('{} 유닛이 생성되었습니다.'.format(name))
    print('체력 {0}, 공격력 {1}\n'.format(hp, damage))

    # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반모드/시즈모드
    tank_name = '탱크'
    tank_hp = 150
    tank_damage = 35

    print('{} 유닛이 생성되었습니다.'.format(tank_name))
    print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

    def attack(name, location, damage):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(name, location, damage))

    attack(name, '1시', damage)
    attack(tank_name, '1시', tank_damage)

    # Class 는 붕어빵틀 과 같음

    class Unit:
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage
            print('{0} 유닛이 생성되었습니다.'.format(self.name))
            print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

    marine1 = Unit('마린', 40, 5)
    marine2 = Unit('마린', 40, 5)
    tank1 = Unit('탱크', 150, 35)

__init__ # 생성자, 객체는 어떤 클래스로부터 만들어지는것들, 마린과 탱크는 Unit 클래스의 인스턴스라고함

멤버변수 # self.name, self.hp, self.damage, 클래스 내에서 정의된 변수, 클래스내에서 초기화할수도 있고 쓸수도 있음

    wraith1 = Unit('레이스', 80, 5)
    print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage)) # 클래스 외부에서 .name 과 같은 멤버변수에 접근 가능

    wraith2 = Unit('빼앗은 레이스', 80, 5)
    wraith2.clocking = True # clocking 이라는 변수는 외부에서 선언
    
    if wraith2.clocking == True:
        print('{0} 는 현재 클로킹 상태입니다.'.format(wraith2.name))
    # 클래스 외부에서 변수 확장 가능, 그 변수는 내가 확장한 객체에만 적용이 됨
    # 파이썬에서는 외부에서 어떤객체에 추가로 변수를 만들어서 사용 가능

메소드
    class AttackUnit(Unit):
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage

        def attack(self, location):
            print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))

        def damaged(self, damage):
            print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
            self.hp -= damage
            print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
            if self.hp <= 0:
                print('{0} : 파괴되었습니다.'.format(self.name))

    firebat1 = AttackUnit('파이어뱃', 50, 16)
    firebat1.attack('5시')
    firebat1.damaged(25)
    firebat1.damaged(25)

상속
    class Unit:  # 부모 클래스
        def __init__(self, name, hp, speed):
            self.name = name
            self.hp = hp
            self.speed = speed

        def move(self, location):
            print('[지상 유닛 이동]')
            print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

    class AttackUnit(Unit):  # 자식 클래스
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)  # 다른 클래스에 비슷한 구문이 있을 경우 상속시켜줌
            self.damage = damage

다중 상속
    class Flyable:
        def __init__(self, flying_speed):
            self.flying_speed = flying_speed

        def fly(self, name, location):
            print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))

    class FlyableAttackUnit(AttackUnit, Flyable):  # 여러가지 클래스를 상속
        def __init__(self, name, hp, damage, flying_speed):
            AttackUnit.__init__(self, name, hp, 0, damage)
            Flyable.__init__(self, flying_speed)

        def move(self, location):
            print('[공중 유닛 이동]')
            self.fly(self.name, location)

연산자 오버로딩  # 자식클래스에서 정의한 메소드를 쓰고싶을때 메소드를 새롭게 정의해서 사용하는 것을 오버로딩이라고 함
    vulture = AttackUnit('벌쳐', 80, 10, 20)
    battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

    vulture.move('11시')
    battlecruiser.move('9시')



















