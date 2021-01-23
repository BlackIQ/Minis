/* JavaScript By Amir */
function startTime() {
	// Start Clock
	var today = new Date();
	// Time
	var h = today.getHours();
	var m = today.getMinutes();
	var s = today.getSeconds();
	// Time
	h = checkTime(h);
	m = checkTime(m);
	s = checkTime(s);
	// Outputs Variables
	var time = h + " : " + m + " : " + s;
	// Outputs
	document.getElementById('time').innerHTML = time;
	t = setTimeout(function(){startTime()} ,500);
}
function checkTime(i) {
	if (i < 10) {
	  i = "0" + i;
	}
	return i;
}