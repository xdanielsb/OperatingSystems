import pandas as pd
import matplotlib.pyplot as plt

def load(name_file, total =-1):
    df = pd.read_csv(name_file, names=["NUM_THREADS", "TIME"])
    return df[:total]

def plot(df):
    num_threads =  df["NUM_THREADS"]
    time= df["TIME"]

    speed_ups = []
    best_time_seq = 7.98094
    for a in df["TIME"]:
        speed_ups.append(best_time_seq/a)

    plt.plot(num_threads,time, 'b-', ms=1)
    plt.plot(num_threads,time, 'go', ms=5, label='Time')
    plt.plot(num_threads,speed_ups, 'rd', ms=5, label='Speed ups')

    for a,b in zip(num_threads,time):
        plt.text(a, b, "%.2f" % b)
        pass

    for a,b in zip(num_threads,speed_ups):
        plt.text(a, b, "%.2f" % b)
        pass

    plt.xlabel('X')  #Label
    plt.legend(loc='best') #Legenda
    plt.show()


if __name__ == "__main__":
    name_file = 'times2.csv'
    df = load(name_file, 100)
    plot(df)
