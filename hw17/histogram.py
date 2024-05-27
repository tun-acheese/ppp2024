import matplotlib.pyplot as plt
import numpy as np

def main():
    dices= np.random.randint(1,7, size=100)

    print(dices)

    plt.hist(dices,bins=6,color="b")
    plt.savefig('hw17/hist.png')
    # plt.show()


if __name__=="__main__":
    main()