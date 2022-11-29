"""
Exercise No. 03

Use the stochastic gradient descent algorithm to find the minimum of the loss function given by the formula: L(w) = w2
- 4w.

The derivate of function L: dl / dw = 2 * w - 4

Algorithm:

    1. We start from the starting point, let's take:

        w_0 = -1

    2. We define in advance the maximum number of iterations:

        max_iters = 10000

    3. We define a variable that will help us control the size of the step towards the minimum, let's set this value to 1:

        previous_step_size = 1

    4. We define the learning rate:

        learning_rate = 0.01

    5. We define the precision that is enough to find the minimum:

        precision = 0.000001

    6. We define the derivative of a function:

        derivative = lambda w: 2 * w - 4

    To find the minimum of the L function, move along the opposite direction to the direction of the gradient by
    updating the value w_0 as follows:

        w_0 = w_0 - learning_rate * derivative(w_prev)

    Where w_prev is the point from the previous iteration. For the first point is just w_0.

Create a while loop that will stop the algorithm when the minimum is found with the precision we assumedor if we exceed
the maximum number of iterations. Print the result to the console as shown below.

Tip: Conditions in a while loop:

    while previous_step_size > precision and iters < max_iters:

Expected result:

    A local minimum in point: 2.00
"""
max_iters = 10000
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_0 - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1
print(f'A local minimum in point: {w_0:.2f}')
