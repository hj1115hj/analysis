import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
from numpy.random import randn


def ex1():
    #plt.plot([1, 2, 3, 4], [10, 20, 30, 40]) #가로,세로
    plt.plot([10, 20, 30, 40])#세로
    plt.show()


def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot([1, 2, 3, 4], [10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [100, 200, 300, 400])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(1000), bins=30, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()


def ex4():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([10, 20, 30, 40])
    plt.show()


def ex5():
    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(100), bins=20, color='k', alpha=0.3)

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


def ex6():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([1, 2, 3, 4], [10, 20, 30, 40], 'go--') #color ,maker, linestile
    plt.show()


def ex7():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot(
        [1, 2, 3, 4],
        [10, 20, 30, 40],
        color='r',
        linestyle='--',
        marker='v' # y축 점들에서 마커표시가됨
        )
    plt.show()


def ex8():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot(
        [1, 2, 3, 4],
        [10, 20, 30, 40],
        color='#335599',
        linestyle='solid',
        marker='v')
    plt.show()


def ex9():
    fig, subplot = plt.subplots(1, 1)

    #cumsum() 넘파이함수 , 누적합을 구해줌
    data = randn(50).cumsum()
    subplot.plot(data, color='black', linestyle='dashed', label='AAA')
    subplot.plot(data, color='blue', drawstyle='steps-mid', label='BBB')

    #help(plt.legend)
    plt.legend(loc='upper right')
    plt.show()


def ex10():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) #x눈금 리스트를 변경한다
    plt.show()


def ex11():
    fig, subplot = plt.subplots(1, 1)

    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

    subplot.set_xticklabels( #x눈금 이름을 정한다
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplot.set_xlabel('Points') #x라벨 정하기
    subplot.set_title('Matplotlib Test') #제목적하기

    plt.show()


def ex12():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='one')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='two')
    subplots.plot(randn(1000).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()


def ex13():
    # font_filename = 'c:/Windows/fonts/malgun.ttf'
    # font_name = font_manager.FontProperties(fname=font_filename).get_name()
    # print(font_name)

    # font_options = {'family': 'Malgun Gothic'}
    # plt.rc('font', **font_options)
    # plt.rc('axes', unicode_minus=False)

    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='기본') #그래프 라벨
    subplots.plot(randn(1000).cumsum(), 'k--', label='대시')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')


    plt.legend(loc='best')

    plt.show()


if __name__ == '__main__':
    #ex1()
    #ex2()
    #ex3()
    #ex4()
    #ex5()
    #ex6()
    #ex7()
    #ex8()
    #ex9()
    #ex10()
    #ex11()
    #ex12()
    ex13()