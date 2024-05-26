ringo_ans, sunuke_ans = input().split()
crimer_list = [1,2,3]
ringo_ans = int(ringo_ans)
sunuke_ans = int(sunuke_ans)


if ringo_ans == sunuke_ans:
    print(-1)
else:
    for i in crimer_list:
        if i != ringo_ans and i != sunuke_ans:
            print(i)
            break