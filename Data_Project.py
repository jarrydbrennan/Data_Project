import statistics
file = "sample_grades.csv"
spring = []
fall = []

def stats(list):
    print("Mean: ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD: ", statistics.stdev(list))

for line in open(file):
    list = line.strip().split(",")
    #print(list)
    if list[1] == 'Fall 2016':
        spring.append(eval(list[2]))
    else:
        fall.append(eval(list[2]))

stats(fall)
stats(spring)