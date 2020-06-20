
import pandas as pd


if __name__ == '__main__':


    import os

    dataframes = []

    for filename in os.listdir('./'):
        if filename.endswith(".htm"):
            dataframes.extend(pd.read_html(filename, match='Dallas Police Department'))
            continue
        else:
            continue

    master = pd.concat(dataframes, ignore_index=True)

    print (master)