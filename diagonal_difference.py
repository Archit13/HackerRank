n = int(raw_input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in raw_input().strip().split(' ')]
   a.append(a_t)

sum_left = 0
sum_right = 0


def get_diagnoal_sum_r2l(n, a):
   sum = 0
   cur_x_index = 0
   cur_y_index = n - 1

   for i in range(len(a)):
       sum += (a[cur_x_index][cur_y_index])

       cur_x_index += 1
       cur_y_index -= 1

   return sum


def get_diagnoal_sum_l2r(n, a):
   sum = 0
   cur_x_index = 0
   cur_y_index = 0

   for row in range(len(a)):
       sum += (a[cur_x_index][cur_y_index])

       cur_x_index += 1
       cur_y_index += 1

   return sum


def diagonal_diff(s1, s2):
    return abs(s1 - s2)

sum_left = get_diagnoal_sum_l2r(n, a)
sum_right = get_diagnoal_sum_r2l(n, a)

abs_sums = diagonal_diff(sum_left, sum_right)
print str(abs_sums)
