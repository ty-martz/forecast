import pandas as pd

class DataCollector:

    def __init__(self):
        self.full_train = None
        self.train = None
        self.test = None
        self.val = None

    
    def get_train_data(self, path='../data/train.csv', fill_method='ffill'):
        df = pd.read_csv(path, parse_dates=['datetime'])
        if fill_method is None:
            df = df.dropna().reset_index(drop=True)
        else:
            df['energy'] = df['energy'].fillna(method=fill_method)
        self.full_train = df.copy()
        return self.full_train

    
    def get_test_data(self, path='../data/test.csv'):
        self.test = pd.read_csv(path, parse_dates=['datetime'])
        return self.test
    

    def split_train(self, random=False, test_pct=0.2, train_path='../data/train.csv', train_fill='ffill'):
        if self.full_train is None:
            df = self.get_train_data(path=train_path)
        else:
            df = self.full_train
        
        if random:
            # split randomly
            pass
        else:
            cutoff_idx = int(len(self.full_train) * (1-test_pct))
            self.train = df.iloc[:cutoff_idx]
            self.val = df.iloc[cutoff_idx:]

    
    def collect_split_data(self, test_pct=0.2, path_to_train='../data/train.csv'):
        if (self.train is None) | (self.val is None):
            self.split_train(test_pct=test_pct, train_path=path_to_train)
        return self.train, self.val
