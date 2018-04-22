from file_process import pi


def calc_area_of_circle(r):
	return pi*pow(r,2)


def main():
	print 'please input the radius:'
	r=input()
	print calc_area_of_circle(r)

main()




