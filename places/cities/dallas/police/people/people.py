
import pandas as pd

if __name__ == '__main__':


    import os

    for filename in os.listdir('./'):
        if filename.endswith(".htm"):
            df = pd.read_html(filename, match='Dallas Police Department')
            print (df)
            continue
        else:
            continue