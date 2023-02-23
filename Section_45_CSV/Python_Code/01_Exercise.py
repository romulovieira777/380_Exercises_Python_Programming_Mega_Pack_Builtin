"""
Exercise No. 01

The apple.csv file containing Apple's quotes is given. Using the built-in csv module load this file and print each line
to the console as shown below.

Expected result:

    Date,Open,High,Low,Close,Volume
    1984-09-07,0.41583,0.42087,0.41079,0.41583,23669718
    1984-09-10,0.41583,0.41708,0.40581,0.41334,18371562
    1984-09-11,0.41708,0.42839,0.41708,0.42087,43321235
    1984-09-12,0.42087,0.42337,0.40828,0.40828,37844792
    1984-09-13,0.43093,0.43215,0.43093,0.43093,58941865
    1984-09-14,0.43215,0.44723,0.43215,0.43719,70181304
    1984-09-17,0.44849,0.45477,0.44849,0.44849,54796306
    1984-09-18,0.44849,0.45228,0.43215,0.43215,27662429
    1984-09-19,0.43215,0.43719,0.42337,0.42337,30215978
    1984-09-20,0.42463,0.42839,0.42463,0.42463,18810964
"""
import csv

with open('../Files/apple.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(','.join(row))
