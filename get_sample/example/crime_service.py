import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from example.crime_model import CrimeModel
import pandas as pd
'''
문제정의 !
서울시의 범죄현황과 CCTV현황을 분석해서
정해진 예산안에서 구별로 다음해에 배분하는 기준을 마련하시오.
예산금액을 입력하면, 구당 할당되는 CCTV 카운터를 자동으로
알려주는 AI 프로그램을 작성하시오.
'''
class CrimeService:
    def __init__(self):
        self.data = CrimeModel()
        self.data.dname = 'C:\\Users\\bitcamp\\kubernetes\\chat-server\\get_sample\\example\\data\\'
        self.data.sname = 'C:\\Users\\bitcamp\\kubernetes\\chat-server\\get_sample\\example\\save\\'
        self.data.crime = 'crime_in_seoul.csv'
        self.data.cctv = 'cctv_in_seoul.csv'
       

    def crime_dataframe(self) -> pd.DataFrame:
        # index_col=0 해야 기존 index 값이 유지된다
        # 0 은 컬럼명 중에서 첫번째를 의미한다(배열구조)
        # pd.read_csv(f'경로/파일명/csv', index_col=0 = '인덱스로 지정할 column 명') Index 지정
     
        return pd.read_csv(f'{self.data.dname}{self.data.crime}', index_col=0)
    
    def cctv_dataframe(self) -> object:
        # pd.read_csv('경로/파일명.csv') Index 를 지정하지 않음
        return pd.read_csv(f'{self.data.dname}{self.data.cctv}', index_col=0)
    

    def save_model(self, fname, dframe: pd.DataFrame) -> pd.DataFrame:
        '''
        풀옵션은 다음과 같다
        df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
        '''
        return dframe.to_csv(f'{self.ds.sname}{fname}', sep=',', na_rep='NaN')
    
if __name__ == "__main__":
    service = CrimeService()
    crime_df = service.crime_dataframe()
    cctv_df = service.cctv_dataframe()
    print(crime_df)
    print(cctv_df)
    


        

