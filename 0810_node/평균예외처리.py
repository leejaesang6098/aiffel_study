def aver():
    total = 0
    count = 0
    nums = input('Enter a number: (input "q" to quit) ')

    while nums != "q":
        try:
            x = float(nums)
            total += x
            count += 1
        except ValueError:
            print('Not a number! please input just number')

        nums = input('Enter a number: (input "q" to quit) ')

    avg = total / count

    return print(f'\n average: {avg}')


aver()
