from dataclasses import dataclass
from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd


class TitanicService:

    model = TitanicModel()

    def process(self):
        print(f'프로세스 시작')
        train_model = self.new_model('train.csv')
        test_model = self.new_model('test.csv')
        print(f'트레인 컬럼 : {train_model.columns}')
        print(f'테스트 컬럼 : {test_model.columns}')

    def new_model(self, payload) -> object:
        this = self.model
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)




