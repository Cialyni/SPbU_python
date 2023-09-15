import sys
from Vector import Vector, vectors_angle
from Matrix import Matrix


def disclaimer():
    print('.............................................................................\n'
          'Hellow\n'
          'In this program Vectors will be set with COORDINATES in 2 Rational numbers with space\n'
          'Matrix will be set as n-string with line break\n'
          'If you want to go back - enter ESC\n'
          'Calculations take place in two-dimensional space\n'
          '.............................................................................'
          )


def vector():
    key = 1
    while key != 0:
        print('\nChoose option: ', '    Go back - 0', '    Find len - 1', '    Find angle - 2',
              '    Scalar multiplication - 3\n', sep='\n')
        key = int(input())
        if key == 3:
            vec1 = Vector.vec_input(Vector(), 1)
            vec2 = Vector.vec_input(Vector(), 2)
            print('\033[1m{}{}\033[0m'.format('\nScalar multiplication of this vector = ', vec1 * vec2))
        if key == 1:
            vec = Vector.vec_input(Vector())
            print('\033[1m{}{}\033[0m'.format('\nLen of this vector = ', vec.len()))
        if key == 2:
            vec1 = Vector.vec_input(Vector(), 1)
            vec2 = Vector.vec_input(Vector(), 2)
            print('\033[1m{}{}\033[0m'.format('\nAngle of this vector = ', vectors_angle(vec1, vec2)))


def matrix():
    key = 1
    while key != 0:
        print('\nChoose option: ', '    Go back - 0', '    Addition - 1', '    Multiplication - 2',
              '    Transponirovanie - 3\n', sep='\n')
        key = int(input())
        if key == 1:
            matr1 = Matrix.input(Matrix(), 1)
            matr2 = Matrix.input(Matrix(), 2)
            if matr1.n != matr2.n or matr1.m != matr2.m:
                print('\033[1m{}\033[0m'.format('\n!!! Incorrect Data: expected equal matrix size !!!\n'))
                break
            print('\033[1m{}\033[0m'.format('\nResult of addition: '))
            matr3 = matr1 + matr2
            matr3.output()

        if key == 2:
            matr1 = Matrix.input(Matrix(), 1)
            matr2 = Matrix.input(Matrix(), 2)
            if matr1.n != matr2.m or matr1.m != matr2.n:
                print('\033[1m{}\033[0m'.format('\n!!! Incorrect Data: expected N1 = M2 !!!\n'))
                break
            print('\033[1m{}\033[0m'.format('\nResult of multiplicaltion: '))
            matr3 = matr1 * matr2
            matr3.output()

        if key == 3:
            matr = Matrix.input(Matrix(), 1)
            matr.transponirovanie()
            print('\033[1m{}\033[0m'.format('\nResult of Transponirovanie: '))
            matr.output()


def UI():
    key = 1
    while key != 0:
        print('\nEnter 0 to end program', 'Enter 1 to work with vectors', 'Enter 2 to work matrixs\n', sep='\n')
        key = int(input())
        if key == 1:
            vector()
        if key == 2:
            matrix()


if __name__ == '__main__':
    disclaimer()
    UI()
