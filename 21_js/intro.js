//Team EmptyCup - William Li, Pak Lau
//Soft Dev
//K21 -- Get Scripty
//2021-04-013

// no semi colons necessary

function factI(n){		//declare functions with function
	var total = 1		//must have a declare youre using a variable with var
	for(var i=n; i>0; i--){		//same syntax as java loops
		var total = total * i
	}
	return total
}

function factR(n){
	if(n !== 1){
		return n * factR(n-1)
	} else {
		return 1
	}
}

function fibI(n){
	var first = 0
	var second = 1
	var third = 1
	for(var i = 0; i<n-1; i++){
		first = second
		second = third
		third = first + second
	}
	return first
}

function fibR(n){
	if(n>3){
		return fibR(n-1) + fibR(n-2)
	} else if (n !== 1){
		return 1
	} else {
		return 0
	}
}
