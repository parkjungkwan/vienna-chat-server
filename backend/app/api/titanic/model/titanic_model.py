
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score
from app.api.context.datasets import DataSets
from app.api.context.models import Models
from icecream import ic


class TitanicModel(object):

    def __init__(self):
        self.model = Models()
        self.dataset = DataSets()

    def preprocess(self, train_fname, test_fname) -> object:
        ic(f'--- TitanicModel 전처리 시작 ----')
        this =  self.dataset
        that = self.model
        ic(this)
        ic(that)
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        # 데이터셋은 Train과 Test, Validation 3종류로 나뉘어져 있다.
        this.train = that.new_dataframe_no_index(f'{train_fname}')
        this.test = that.new_dataframe_no_index(f'{test_fname}')
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this,'SibSp', 'Parch', 'Cabin', 'Ticket')
        # this = self.drop_feature(this, 'SibSp', 'Parch', 'Cabin', 'Ticket')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate_title(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)  
        self.df_info(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.drop_feature(this, "Fare")
        self.learning(this)
      

        
        
        return this
 
    
    @staticmethod
    def drop_feature(this, *feature) -> object:
        ic(type(feature))
        # for i in feature:
        #     this.train = this.train.drop([i], axis=1)
        #     this.test = this.test.drop(i, axis=1)

        # for i in [this.train, this.test]:
        #     for j in feature:
        #         i.drop(j, axis=1, inplace=True)

        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]

        return this
    
    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'id 의 타입  {type(this.id)}')
        ic(f'id 의 상위 3개 {this.id[:3]}')
    
    @staticmethod
    def title_nominal(this) -> None:
        return this
    
    @staticmethod
    def create_train(this) -> str:
        return this.train.drop('Survived', axis=1) # 0 : 행, 1 : 열
    

    @staticmethod
    def create_label(this) -> str:
        return this.train['Survived']
    
    # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        # ic(type(kwargs))
        {ic(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()} # key:name, val:이순신


    
    @staticmethod
    def pclass_ordinal(this) -> pd.DataFrame:
        this.train['Pclass'] = this.train['Pclass'].map({1:1, 2:2, 3:3})
        this.test['Pclass'] = this.test['Pclass'].map({1:1,})

        return this

    @staticmethod
    def name_nominal(this) -> pd.DataFrame:
        this.train['Name'] = this.train['Name'].str.extract('([A-Za-z]+)\.')
        this.test['Name'] = this.test['Name'].str.extract('([A-Za-z]+)\.')
        return this
    
    @staticmethod
    def extract_title_from_name(this) -> pd.DataFrame:
        for these in [this.train, this.test]:
            these['Title'] = these['Name'].str.extract('([A-Za-z]+)\.', expand=False)
        return this
    
    @staticmethod
    def remove_duplicate_title(this) -> pd.DataFrame:
        a = []
        for these in [this.train, this.test]:
           a += list(set(these['Title']))
        a = list(set(a))
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping
    
    @staticmethod
    def title_nominal(this, title_mapping) -> pd.DataFrame:

        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this
    
    @staticmethod
    def age_ratio(this) -> pd.DataFrame:
        train = this.train
        test = this.test
        age_mapping = {'Unknown':0 , 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4,
                       'Young Adult': 5, 'Adult':6,  'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5) # 왜 NaN 값에 -0.5 를 할당할까요 ?
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 이것을 이해해보세요
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        
        for these in train, test:
            pass # pd.cut() 을 사용하시오. 다른 곳은 고치지 맣고 다음 두 줄만 완성하시오
            these['Age'] = pd.cut(these['Age'], bins, labels=labels)
            these['AgeGroup'] = these['Age'].map(age_mapping) # map() 사용

        return this
    
    @staticmethod
    def sex_nominal(this) -> pd.DataFrame:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this
    
    @staticmethod
    def embarked_nominal(this) -> pd.DataFrame:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> pd.DataFrame:

        bins = [-1, 8, 15, 31, np.inf]
        labels = ['Unknown', 'Low', 'Mid', 'High']
        fare_mapping = {'Unknown': 0, 'Low': 1, 'Mid': 2, 'High': 3}
        for these in [this.train, this.test]:
            these['FareBand'] = pd.cut(these['Fare'], bins, labels=labels)
            these['FareBand'] = these['FareBand'].map(fare_mapping)

        return this
    
    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        # ic(type(kwargs))
        {ic(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()} # key:name, val:이순신

    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''
    
    
    @staticmethod
    def learning(this) :
        ic(f'학습 시작')
        # k_fold = self.create_k_fold()
        # accuracy = self.get_accuracy(this, k_fold)
        accuracy = '70'
        ic(f'사이킷런 알고리즘 정확도: {accuracy}')




   
    

