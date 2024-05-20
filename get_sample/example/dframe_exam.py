import random
import string

import pandas as pd
from icecream import ic
import numpy as np

from context.model.data_model import DataModel
from context.service.data_service import DataService
from example.utils import memberlist



class Quiz30:
    '''
        데이터프레임 문제 Q-1
    ic| df:     A   B   C
            1   1   2   3
            2   4   5   6
            3   7   8   9
            4  10  11  12
    '''
    def df_range(self) -> str:
        df = pd.DataFrame([[1,2,3],
                          [4,5,6],
                          [7,8,9],
                          [10,11,12]], index=range(1,5), columns=['A','B','C'])
        # 위 식을 리스트결합 형태로 분해해서 조립하시오

        d = {'1':range(1,4),
             '2':range(4,7),
             '3':range(7,10),
             '4':range(10,13)}
        df2 = pd.DataFrame.from_dict(d,orient="index",columns=['A','B','C'])
        ic(df2)
        return None

    '''
        데이터프레임 문제 Q-2
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''
    def rand_2_by_3(self) -> str:
        '''
        기본 해체
        l1 = [[myRandom(0,100) for i in range(3)] for i in range(2)]
        l2 = [i for i in range(2)]
        columns = [i for i in range(3)]
        # df = pd.DataFrame([],index=[], columns=[]) 구조
        df = pd.DataFrame(l1,index=l2, columns=columns)
        '''
        # 넘파이사용한 예제
        df = pd.DataFrame(np.random.randint(10,100,size=(2,3)))
        print(df)
        return None

    '''
            데이터프레임 문제 Q-3
            국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
             단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
             
              ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    def df_grade(self) -> object:
        data1 = np.random.randint(0,100,(10,4))
        idx = [self.id(chr_size=5) for i in range(10)]
        col1 = ['국어', '영어', '수학', '사회']
        df1 = pd.DataFrame(data1,index=idx,columns=col1)
        print('------------------------------------------------------')
        # data2 = {i:j for i,j in zip(idx,data1)} 은 아래와 같이 줄인다
        data2 = dict(zip(idx,data1))
        col2 = ['국어', '영어', '수학', '사회']
        df2 = pd.DataFrame.from_dict(data2,orient="index", columns=col2)
        ic(df1)
        print('*'*100)
        ic(df2)
        return None

    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz33_df_loc(self) -> str:

        '''
        데이터프레임 생성 예제
        d = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
             {'a': 100, 'b' : 200, 'c' : 300, 'd' : 400},
             {'a' : 1000, 'b' : 2000, 'c' : 3000, 'd' : 4000}]

        df = self.createDf(keys=['a','b','c','d'],
                           vals=np.random.randint(0,100,4),
                           len=3)
        '''
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        subjects = ['자바', '파이썬', '자바스크립트', 'SQL']
        scores = np.random.randint(0, 100, (24, 4))
        students = memberlist()
        students_scores = {student:score for student,score in zip(students, scores)}
        students_scores_df = pd.DataFrame.from_dict(students_scores, orient="index", columns=subjects)
        service = DataService()
        # model.save_model(fname='grade.csv', dframe=students_scores_df)
        grade_df = service.new_dframe_idx(fname='grade.csv')
        ic(grade_df)
        print('Q1. 파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:,'파이썬']
        ic(type(python_scores))
        ic(python_scores)
        print('Q2. 조현국의 점수만 출력하시오')
        cho_scores = grade_df.loc['조현국']
        ic(type(cho_scores))
        ic(cho_scores)
        print('Q3. 조현국의 과목별 점수를 출력하시오')
        cho_subjects_scores = grade_df.loc[['조현국']]
        ic(type(cho_subjects_scores))
        ic(cho_subjects_scores)



        return None
    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys,vals)) for _ in range(len)])


    def quiz34_df_iloc(self) -> str:
        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a    61
                b    57
                c    63
                d    19
                Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a   b  c   d
                            0  36  24  2  12
        '''
        # ic(df.iloc[[0,1]])
        '''
        ic| df.iloc[[0,1]]:     a   b   c   d
                            0  27  73  90  71
                            1  27  73  90  71
        '''
        # ic(df.iloc[:3])
        '''
        ic| df.iloc[:3]:     a   b   c   d
                         0  92  28  64  62
                         1  92  28  64  62
                         2  92  28  64  62
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:     a  b   c   d
                                          0  96  6  77  28
                                          2  96  6  77  28
        '''
        # ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                                 0  65  40  32  69
                                                 2  65  40  32  69
        '''
        # ic(df.iloc[0, 1])
        '''ic| df.iloc[0, 1]: 32'''
        # ic(df.iloc[[0, 2], [1, 3]])
        '''
        ic| df.iloc[[0, 2], [1, 3]]:     b   d
                                     0  12  10
                                     2  12  10
        '''
        # ic(df.iloc[1:3, 0:3])
        '''
        ic| df.iloc[1:3, 0:3]:     a  b   c
                                1  82  9  12
                                2  82  9  12
        '''
        # ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                    0  86  99
                                                    1  86  99
                                                    2  86  99
        '''
        # ic(df.iloc[:, lambda df: [0, 2]])
        '''
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                            0  59  58
                                            1  59  58
                                            2  59  58
        '''
        return None