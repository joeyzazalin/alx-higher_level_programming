#!/usr/bin/node
const x = math.floor(number(process.argv[2]));
if (isNaN(x)) {
	console.log('missing number of occurrences');
} else {
	for (let i = 0; i < x; i++) {
		console.log('C is fun');
	}
}
