from example.utils import myRandom


class LeapYear:

    def __init__(self) -> None:
        print(f'utils.py myRandom() 를 이용하여 윤년계산기 객체를 생성합니다')
        print ('(ex) 2020년은 윤년입니다. 단 컴프리헨션을 사용합니다')

    def is_leap_year(self):
        y = myRandom(2000, 2024)
        # Python style s = '윤년' if () else '평년'
        # Java style => String s = () ? "윤년" : "평년";
        s = '윤년' if (y % 4 == 0 and y % 100) or (y % 400 == 0) else '평년'
        print(f'{y}는 {s}이다')

        