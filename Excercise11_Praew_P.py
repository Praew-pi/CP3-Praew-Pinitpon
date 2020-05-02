inputpyramid = int(input("Please input layer of pyramid:"))
for x in range (inputpyramid):
        print(" "*(inputpyramid - x - 1), "*"*(x+(x+1)))


