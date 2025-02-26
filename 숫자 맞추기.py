import sys  # sys 모듈을 불러옴

def number_correct(game):   # number_correct 함수 정의
    low, high = 1, 10  # 숫자의 최소, 최대 범위 설정

    for num, response in game:  # num과 response를 game에서 하나씩 가져옴
        if response == 'too high':   
            high = min(high, num - 1)  # high를 num-1과 high 중 작은 값으로 설정
        elif response == 'too low':  
            low = max(low, num + 1)  # low를 num+1과 low 중 큰 값으로 설정                    
        elif response == 'right on':  
            if not (low <= num <= high):  # 숫자가 올바른 범위에 있는지 확인
                return 'Stan is dishonest'
            return 'Stan may be honest'

    return 'Stan is dishonest'  # 기본적으로 "Stan is dishonest" 반환        

def main():
    game = []  # 게임 데이터 저장 리스트
    num = None  # 숫자를 저장할 변수 초기화

    for line in sys.stdin:  # 한 줄씩 입력을 받도록 변경
        line = line.strip()  # 공백 제거

        if line == "0":  # 입력이 "0"이면 프로그램 종료
            if game:  # 남아 있는 게임이 있다면 마지막 결과 출력
                print(number_correct(game))
            break  # 프로그램 종료

        if line.isdigit():  # 숫자가 입력된 경우
            num = int(line)  # 숫자 저장
        else:  # 응답이 입력된 경우
            response = line  
            if num is not None:  # 숫자가 존재할 때만 추가
                game.append((num, response))  
            
            if response == 'right on':  # 게임 종료 조건
                print(number_correct(game))  # 결과 출력
                game = []  # 게임 초기화
                num = None  # num 초기화
    
if __name__ == '__main__':
    main()  # main 함수를 실행
