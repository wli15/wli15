from random import choice
JobClass = {
	
}
x=randint(0,99.8)
for key, value in JobClass.items():
	x=x-value
	if x<0:
		print(key)
		break
