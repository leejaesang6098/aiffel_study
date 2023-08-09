import random


def game_go():
    x = 1

    while len(user_point) < 3:
        user_input = int(input("{}번째 숫자를 입력하세요: ".format(x)))
        if user_input not in user_point and user_input <= 9:
            user_point.append(user_input)
            x += 1
        else:
            print("잘못된 값이거나, 중복된 값입니다. 다시 입력하세요")
            continue


def get_score(user, computer):
    strike_count = 0
    ball_count = 0

    for i in range(0, 3):
        if user[i] == computer[i]:
            strike_count += 1
        elif user[i] in computer:
            ball_count += 1

    return strike_count, ball_count


computer_point = []

while len(computer_point) < 3:
    x = random.randint(0, 9)
    if x not in computer_point:
        computer_point.append(x)

print("0에서 9까지의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
game_count = 1

while True:
    print("숫자 3개를 차례대로 입력하세요")

    user_point = []

    game_go()

    strike, ball = get_score(user_point, computer_point)
    print("S: {}, B: {}".format(strike, ball))

    if strike == 3:
        print("{}번째 시도에 정답을 맞췄습니다".format(game_count))
        break

    game_count += 1
