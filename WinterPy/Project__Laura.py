import random
import math

screen = []  # 棋盘


def init():  # 创建空白棋盘
    for i in range(6):
        temp = []
        for j in range(8):
            temp.append(' ' + '|')
        screen.append(temp)


def screen_print():  # 打印棋盘
    print('', 1, 2, 3, 4, 5, 6, 7, 8, sep=' ')
    print('', 1, 2, 3, 4, 5, 6, 7, 8, sep=' ', file=file, flush=True)
    for i in range(6):
        print('|', end='')
        print('|', end='', file=file, flush=True)
        for j in range(8):
            print(screen[i][j], end='')
            print(screen[i][j], end='', file=file, flush=True)
        print('')
        print('', file=file, flush=True)
    print('-' * 17, '\n')
    print('-' * 17, '\n', file=file, flush=True)


def win():  # 判断输赢
    for i in range(6):  # 判断行
        for j in range(5):
            if screen[i][j][0] == screen[i][j + 1][0] == screen[i][j + 2][0] == screen[i][j + 3][0] and screen[i][j][
                0] != ' ':
                return 1
    for i in range(3):  # 判断列
        for j in range(8):
            if screen[i][j][0] == screen[i + 1][j][0] == screen[i + 2][j][0] == screen[i + 3][j][0] and screen[i][j][
                0] != ' ':
                return 1
    for i in range(3):  # 判断右下斜线
        for j in range(5):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == screen[i + 2][j + 2][0] == screen[i + 3][j + 3][0] and \
                    screen[i][j][0] != ' ':
                return 1
    for i in range(3):  # 判断左下斜线
        for j in range(3, 8):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == screen[i + 2][j - 2][0] == screen[i + 3][j - 3][0] and \
                    screen[i][j][0] != ' ':
                return 1
    return 0


def full():  # 判断棋盘是否已满
    for i in screen:
        for j in i:
            if j[0] == ' ':
                return 0
    return 1


def win_Laura():  # Laura获胜
    for i in range(6):  # 判断行
        for j in range(5):
            if screen[i][j][0] == screen[i][j + 1][0] == screen[i][j + 2][0] == screen[i][j + 3][0] == 'O':
                return 1
    for i in range(3):  # 判断列
        for j in range(8):
            if screen[i][j][0] == screen[i + 1][j][0] == screen[i + 2][j][0] == screen[i + 3][j][0] == 'O':
                return 1
    for i in range(3):  # 判断右下斜线
        for j in range(5):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == screen[i + 2][j + 2][0] == screen[i + 3][j + 3][0] == 'O':
                return 1
    for i in range(3):  # 判断左下斜线
        for j in range(3, 8):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == screen[i + 2][j - 2][0] == screen[i + 3][j - 3][0] == 'O':
                return 1
    return 0


def win_player():  # player获胜
    for i in range(6):  # 判断行
        for j in range(5):
            if screen[i][j][0] == screen[i][j + 1][0] == screen[i][j + 2][0] == screen[i][j + 3][0] == 'X':
                return 1
    for i in range(3):  # 判断列
        for j in range(8):
            if screen[i][j][0] == screen[i + 1][j][0] == screen[i + 2][j][0] == screen[i + 3][j][0] == 'X':
                return 1
    for i in range(3):  # 判断右下斜线
        for j in range(5):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == screen[i + 2][j + 2][0] == screen[i + 3][j + 3][0] == 'X':
                return 1
    for i in range(3):  # 判断左下斜线
        for j in range(3, 8):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == screen[i + 2][j - 2][0] == screen[i + 3][j - 3][0] == 'X':
                return 1
    return 0


def win2():  # Laura两连子（且能四连子）
    score = 0
    for i in range(6):  # 判断行
        if screen[i][0][0] == screen[i][1][0] == 'O' and screen[i][2][0] == screen[i][3][0] == ' ':
            score += 1
        if screen[i][1][0] == screen[i][2][0] == 'O' and screen[i][3][0] == ' ' and (
                screen[i][0][0] == ' ' or screen[i][4][0] == ' '):
            score += 1
        if screen[i][5][0] == screen[i][6][0] == 'O' and screen[i][4][0] == ' ' and (
                screen[i][3][0] == ' ' or screen[i][7][0] == ' '):
            score += 1
        if screen[i][6][0] == screen[i][7][0] == 'O' and screen[i][4][0] == screen[i][5][0] == ' ':
            score += 1
        for j in range(2, 5):
            if screen[i][j][0] == screen[i][j + 1][0] == 'O' and (
                    screen[i][j - 2][0] == screen[i][j - 1][0] == ' ' or screen[i][j - 1][0] == screen[i][
                j + 2] == ' ' or screen[i][j + 2][0] == screen[i][j + 3][0] == ' '):
                score += 1
    for j in range(8):  # 判断列
        if screen[0][j][0] == screen[1][j][0] == 'O' and screen[2][j][0] == screen[3][j][0] == ' ':
            score += 1
        if screen[1][j][0] == screen[2][j][0] == 'O' and screen[3][j][0] == ' ' and (
                screen[0][j][0] == ' ' or screen[4][j][0] == ' '):
            score += 1
        if screen[2][j][0] == screen[3][j][0] == 'O' and (
                screen[0][j][0] == screen[1][j][0] == ' ' or screen[1][j][0] == screen[3][j][0] == ' ' or screen[4][j][
            0] == screen[5][j][0] == ' '):
            score += 1
        if screen[3][j][0] == screen[4][j][0] == 'O' and screen[2][j][0] == ' ' and (
                screen[1][j][0] == ' ' or screen[5][j][0] == ' '):
            score += 1
        if screen[4][j][0] == screen[5][j][0] == 'O' and screen[2][j][0] == screen[3][j][0] == ' ':
            score += 1
    for i in range(3):  # 判断右下斜线
        for j in range(5):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == 'O' and screen[i + 2][j + 2] == screen[i + 3][
                j + 3] == ' ':
                score += 1
    for i in range(1, 4):
        for j in range(1, 6):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == 'O' and screen[i - 1][j - 1] == screen[i + 2][
                j + 2] == ' ':
                score += 1
    for i in range(2, 5):
        for j in range(2, 7):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == 'O' and screen[i - 1][j - 1] == screen[i - 2][
                j - 2] == ' ':
                score += 1
    for i in range(3):  # 判断左下斜线
        for j in range(3, 8):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == 'O' and screen[i + 2][j - 2] == screen[i + 3][
                j - 3] == ' ':
                score += 1
    for i in range(1, 4):
        for j in range(2, 7):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == 'O' and screen[i + 2][j - 2] == screen[i - 1][
                j + 1] == ' ':
                score += 1
    for i in range(2, 5):
        for j in range(1, 6):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == 'O' and screen[i - 1][j + 1] == screen[i - 2][
                j + 2] == ' ':
                score += 1
    return score


def win3():  # Laura三连子（且能四连子）
    score = 0
    for i in range(6):  # 判断行
        if screen[i][0][0] == screen[i][1][0] == screen[i][2][0] == 'O' and screen[i][3][0] == ' ':
            score += 3
        if screen[i][5][0] == screen[i][6][0] == screen[i][7][0] == 'O' and screen[i][4][0] == ' ':
            score += 3
        for j in range(1, 5):
            if screen[i][j][0] == screen[i][j + 1][0] == screen[i][j + 2][0] == 'O' and screen[i][j - 1][0] == \
                    screen[i][j + 1][0] == ' ':
                score += 3
    for j in range(8):  # 判断列
        if screen[0][j][0] == screen[1][j][0] == screen[2][j][0] == 'O' and screen[3][j][0] == ' ':
            score += 3
        if screen[3][j][0] == screen[4][j][0] == screen[5][j][0] == 'O' and screen[2][j][0] == ' ':
            score += 3
        for i in range(1, 3):
            if screen[i][j][0] == screen[i + 1][j][0] == screen[i + 2][j][0] == 'O' and screen[i - 1][j][0] == \
                    screen[i + 3][j][0] == ' ':
                score += 3
    for i in range(3):  # 判断右下斜线
        for j in range(5):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == screen[i + 2][j + 2][0] == 'O' and screen[i + 3][j + 3][
                0] == ' ':
                score += 3
    for i in range(1, 4):
        for j in range(1, 6):
            if screen[i][j][0] == screen[i + 1][j + 1][0] == screen[i + 2][j + 2][0] == 'O' and screen[i - 1][j - 1][
                0] == ' ':
                score += 3
    for i in range(3):  # 判断左下斜线
        for j in range(3, 8):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == screen[i + 2][j - 2][0] == 'O' and screen[i + 3][j - 3][
                0] == ' ':
                score += 3
    for i in range(1, 4):
        for j in range(2, 7):
            if screen[i][j][0] == screen[i + 1][j - 1][0] == screen[i + 2][j - 2][0] == 'O' and screen[i - 1][j + 1][
                0] == ' ':
                score += 3
    return score


def position():  # 找到每一列最小的空余位置
    blank = []
    for j in range(8):
        for i in range(5, -1, -1):
            if screen[i][j][0] == ' ':
                blank.append(i)
                break
            if i == 0 and screen[0][j][0] != ' ':
                blank.append(-1)
                break
    return blank


def player():  # 玩家输入
    global screen
    nextstep = position()
    while True:
        try:
            temp = input('>>>轮到你了,你放X棋子,请选择列号(1-8):')
            print('>>>轮到你了,你放X棋子,请选择列号(1-8):', temp, file=file, flush=True)
            temp = int(temp) - 1
            while temp not in range(0, 8):
                temp = int(input('列号应该在1～8之间，请重新选择...\n你放X棋子,请选择列号(1-8):')) - 1
                print('列号应该在1～8之间，请重新选择...\n你放X棋子,请选择列号(1-8):', temp, file=file, flush=True)
            while nextstep[temp] == -1:
                temp = int(input('这列满了，请另选一列...\n你放X棋子,请选择列号(1-8):')) - 1
                print('这列满了，请另选一列...\n你放X棋子,请选择列号(1-8):', temp, file=file, flush=True)
            break
        except ValueError:
            print('你输入的不是数字！')
            print('你输入的不是数字！', file=file, flush=True)
    num = nextstep[temp]
    screen[num][temp] = 'X' + '|'
    screen_print()


def AlphaBeta(nPlay, nAlpha, nBeta):
    global screen
    if win_Laura():
        return 100
    if win_player():
        return -100
    if nPlay == 0:
        temp = win3() + win2()
        return temp
    if nPlay % 2 == 1:  # 极小值节点,此处递归层数应为奇数，若递归层数为偶数，将此处改为nPlay % 2 == 0
        nextstep = position()
        for j in range(8):
            i = nextstep[j]
            if i != -1:
                screen[i][j] = 'X' + '|'
                score = AlphaBeta(nPlay - 1, nAlpha, nBeta)
                screen[i][j] = ' ' + '|'
                if score < nBeta:
                    nBeta = score
                    if nAlpha >= nBeta:
                        return nAlpha
        return nBeta
    else:  # 极大值节点
        nextstep = position()
        for j in range(8):
            i = nextstep[j]
            if i != -1:
                screen[i][j] = 'O' + '|'
                score = AlphaBeta(nPlay - 1, nAlpha, nBeta)
                screen[i][j] = ' ' + '|'
                if score > nAlpha:
                    nAlpha = score
                    if nAlpha >= nBeta:
                        return nBeta
        return nAlpha


def laura():
    global screen
    nextstep = position()
    nextstep_score = []
    for j in range(8):
        if nextstep[j] == -1:  # -1表示此列已满，赋值-9999，Laura选择最大值，不可能选到此列
            nextstep_score.append(-9999)
        else:  # 得到当前所有可以选择的列的分数
            temp = nextstep[j]
            screen[temp][j] = 'O' + '|'
            score = AlphaBeta(5, -10000, 10000)  # 递归层数不能太大，否则运行时间过长，经测试递归层数为5时，Laura智能程度很高，且运行时间在可接受范围内
            nextstep_score.append(score)
            screen[temp][j] = ' ' + '|'
    # 可添加print(nextstep_score)观测下一步的得分
    score_max = max(nextstep_score)
    nextstep_max = []
    for j in range(8):  # 找到值最大的列
        if nextstep_score[j] == score_max:
            nextstep_max.append(j)
    l = len(nextstep_max)
    choice = random.randint(0, l - 1)  # 如果有多列的值为最大值，则随机选出一列
    next_j = nextstep_max[choice]
    next_i = nextstep[next_j]
    print('>>>轮到我了,我把O棋子放在第%d列...' % (next_j + 1))
    print('>>>轮到我了,我把O棋子放在第%d列...' % (next_j + 1), file=file, flush=True)
    screen[next_i][next_j] = 'O' + '|'
    screen_print()


if __name__ == '__main__':
    file = open('四连环Log--%d.txt' % random.randint(10000, 99999), 'w', encoding='utf-8')
    print('''Hi,我是劳拉，我们来玩一局四连环。我用O型棋子，你用X型棋子。
游戏规则：双方轮流选择棋盘的列号放进自己的棋子，
        若棋盘上有四颗相同型号的棋子在一行、一列或一条斜线上连接起来，
        则使用该型号棋子的玩家就赢了!''')
    print('''Hi,我是劳拉，我们来玩一局四连环。我用O型棋子，你用X型棋子。
游戏规则：双方轮流选择棋盘的列号放进自己的棋子，
          若棋盘上有四颗相同型号的棋子在一行、一列或一条斜线上连接起来，
          则使用该型号棋子的玩家就赢了!''', file=file, flush=True)
    init()
    print('开始了！这是棋盘的初始状态:')
    print('开始了！这是棋盘的初始状态:', file=file, flush=True)
    screen_print()
    while win() == 0 and full() == 0:
        laura()
        if win() == 1 or full() == 1:
            break
        player()
    if full():
        print('******* 难分胜负！@_@')
        print('******* 难分胜负！@_@', file=file, flush=True)
    elif win_Laura():
        print('******* 耶，我赢了！^_^')
        print('******* 耶，我赢了！^_^', file=file, flush=True)
    elif win_player():
        print('******* 好吧，你赢了！^_*')
        print('******* 好吧，你赢了！^_*', file=file, flush=True)
