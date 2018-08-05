array = [10,20,30,40,50,60,70];
arrayLength = len(array);
print('The length of the array is %f' %arrayLength);
iter = input("Enter the number: ");

if iter > arrayLength-1:
    print("Number cannot be larger than the array");
elif iter < 0:
    print("Index cannot be smaller than 0");
else:
    print("Content inside the array are:");
    for x in range(0,arrayLength):
        print(array[x]);