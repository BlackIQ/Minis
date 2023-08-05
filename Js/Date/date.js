/* JavaScript By Amir */
function startTime() {
	// Start Clock
	var today = new Date();
	// Date
	var d = today.getDay();
	var M = today.getMonth();
	var y = today.getFullYear();
	// Date
	d = checkTime(d);
	M = checkTime(M);
	y = checkTime(y);
	// Outputs Variables
	var date = y + " / " + M + " / " + d;
	// Outputs
	document.getElementById('date').innerHTML = date;
	t = setTimeout(function() {startTime()} ,500);
}
function checkTime(i) {
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}