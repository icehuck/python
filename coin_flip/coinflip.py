# coin flip python script
# nothing major, just flipping a coin
import random


def main():

    num_flip = 0
    num_of_heads = 0
    num_of_tails = 0
    
    while num_flip <= 50:
        flip = random.randint(1, 2)
        if flip == 1:
            print "Heads"
            num_of_heads += 1
        if flip == 2:
            print "Tails"
            num_of_tails += 1
        num_flip = num_flip +1



    print "Num of Heads:", num_of_heads, "Num of Tails:", num_of_tails


if __name__ == "__main__":
    main()
