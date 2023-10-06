import argparse
import pandas as pd
import numpy as np
from Utils import Preprocessor


def main() -> None:
    pareser = argparse.ArgumentParser(description='multilayer perceptron')

    pareser.add_argument(
        '--dataset',
        default='./data.csv',
        help='file of the dataset (default = data.csv)'
    )
    
    args = pareser.parse_args()
    print('Welcome to my first neural network implementation')

    df = pd.read_csv(args.dataset, header=None)

    y = np.array(df[1])
    X = df.iloc[:, 2:].values
    X = Preprocessor.min_max_scale(X)
    X_train, y_train, X_test, y_test = Preprocessor.split_data(X, y)
    
        
    
    

if __name__ == '__main__':
    main()