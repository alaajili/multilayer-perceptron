import argparse
import pandas as pd
import numpy as np
from Preprocessing import Preprocessor

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
    
    

if __name__ == '__main__':
    main()