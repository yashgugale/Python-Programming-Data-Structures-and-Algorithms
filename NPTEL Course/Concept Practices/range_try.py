"""
# prints numbers from i = 1 to j-1 = 10
>>> for i in range(1,11):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
---------------------------------------------------------
# prints numbers starting from i = 0 to j-1 = 19
>>> for i in range(20):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
---------------------------------------------------------
# prints numbers from i = 1 to j-1 = 29, but increments by k = 2
>>> for i in range(1,30,2):
	print("Odd nos:", i)

	
Odd nos: 1
Odd nos: 3
Odd nos: 5
Odd nos: 7
Odd nos: 9
Odd nos: 11
Odd nos: 13
Odd nos: 15
Odd nos: 17
Odd nos: 19
Odd nos: 21
Odd nos: 23
Odd nos: 25
Odd nos: 27
Odd nos: 29
-------------------------------------------------------------
# similarly prints for reverse. Here, i > j
>>> for i in range(29,0,-2):
	print("Odd nos in reverse order:", i)

	
Odd nos in reverse order: 29
Odd nos in reverse order: 27
Odd nos in reverse order: 25
Odd nos in reverse order: 23
Odd nos in reverse order: 21
Odd nos in reverse order: 19
Odd nos in reverse order: 17
Odd nos in reverse order: 15
Odd nos in reverse order: 13
Odd nos in reverse order: 11
Odd nos in reverse order: 9
Odd nos in reverse order: 7
Odd nos in reverse order: 5
Odd nos in reverse order: 3
Odd nos in reverse order: 1
-------------------------------------------------------------

