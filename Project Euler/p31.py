pennys = [200,100,50,20,10,5,2,1]
total = 1
for p100 in range(3):
    for p50 in range(5):
        for p20 in range(11):
            for p10 in range(21):
                for p5 in range(41 - 10 * p10 - 20 * p20 - 50 * p50 - 100 * p100):
                    for p2 in range(101 - 5 * p5 - 10 * p10 - 20 * p20 - 50 * p50 - 100 * p100):
                        for p1 in range(201 - 2 * p2  - 5 * p5 - 10 * p10 - 20 * p20 - 50 * p50 - 100 * p100):
                            if p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 + p1 * 1 == 200:
                                print(201 - 2 * p2  - 5 * p5 - 10 * p10 - 20 * p20 - 50 * p50 - 100 * p100)
                                total += 1
                                print("100 * {0} + 50 * {1} + 20 * {2} + 10 * {3} + 5 * {4} + 2 * {5} + 1 * {6} = 200".format(p100, p50, p20, p10, p5, p2, p1))
print(total)
