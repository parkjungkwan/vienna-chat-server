from dataclasses import dataclass
import pandas as pd
from icecream import ic


from app.api.titanic.model.titanic_model import TitanicModel


class TitanicService:

    def __init__(self) -> None:
        self.model = TitanicModel()

    def preprocess(self):
        ic(f'전처리 시작')
        self.model.preprocess('train.csv', 'test.csv')


    def modeling(self):
        ic(f'모델링 시작')
        this = self.model

    def learning(self):
        ic(f'학습 시작')
        ic(f'결정트리를 활용한 검증 정확도: ')
        ic(f'랜덤프레스트를 활용한 검증 정확도: ')
        ic(f'나이브베이즈를 활용한 검증 정확도: ')
        ic(f'KNN를 활용한 검증 정확도: ')
        ic(f'SVM를 활용한 검증 정확도: ')
        this = self.model


    def postprocessing(self):
        ic(f'후처리 시작')
        this = self.model

    def submit(self):
        ic(f'제출 시작')
        this = self.model

    
        





    
   
    




    

    






