#!/usr/bin/node
const size = math.floor(number(process.argv[2]));
if (isNaN(size)) {
} else {
	for (let r = 0; r < size; r++) {
		let row = '';
		for (let c = 0; c < size; c++) row += 'X';
		console.log(row);
	}
}
