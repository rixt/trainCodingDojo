var onoff = require('onoff'); //  https://www.npmjs.com/package/onoff
var exec = require('child_process').exec;

var Gpio = onoff.Gpio;

// Set pins for sensors for input and interrupt
var SENSOR1 = new Gpio(20, 'in', 'both'); // Export GPIO #20 as an interrupt generating input.
var SENSOR2 = new Gpio(21, 'in', 'both'); // Export GPIO #21 as an interrupt generating input.	

// Set motor controller GPIO pins for output 
var STEPPIN_RIGHT = new Gpio(23, 'out');   // Blue 1
var STEPPIN_LEFT = new Gpio(24, 'out');    // Blue 2
var MOTORPOWER_PIN = new Gpio(25, 'out');	 // Yellow

var writeToConsole = function (error, stdout, stderr) { console.log(stdout); }

function stopMotorAfterTimeout() {
	setTimeout(function () {
		STEPPIN_RIGHT.writeSync(0);
		MOTORPOWER_PIN.writeSync(0);
	}, 300);
}

var drive_right = function () {
	STEPPIN_LEFT.writeSync(0);
	STEPPIN_RIGHT.writeSync(1);
	MOTORPOWER_PIN.writeSync(1);

	stopMotorAfterTimeout();
}

var drive_left = function () {
	STEPPIN_LEFT.writeSync(1);
	STEPPIN_RIGHT.writeSync(0);
	MOTORPOWER_PIN.writeSync(1);

	stopMotorAfterTimeout();
}

// The callback passed to watch will be called when the SENSOR1 is passed. 
var oldLargeValue = 0, numberOfPassingsLargeSensor = 0;
SENSOR1.watch(function (err, value) {
	if (err) {
		console.log(err);
		//throw err;
	}
	if (oldLargeValue != value) {
		oldLargeValue = value;
		if (value == 1) {
			console.log(numberOfPassingsLargeSensor + ' Large track sensor = ' + value);
			console.log('Changing gear');
			drive_left();
		}
		numberOfPassingsLargeSensor++;
	}
});

// The callback passed to watch will be called when the SENSOR2 is passed. 
var oldSidingsValue = 0, numberOfPassingsSidingsSensor = 0;
SENSOR2.watch(function (err, value) {
	if (err) {
		console.log(err);
		//throw err;
	}
	if (oldSidingsValue != value) {
		oldSidingsValue = value;
		if (value == 1) {
			console.log(numberOfPassingsSidingsSensor + ' Sidings sensor = ' + value);
			console.log('Changing gear');
			drive_right();
		}
		numberOfPassingsSidingsSensor++;
	}
});

var stdin = process.stdin;

// without this, we would only get streams once enter is pressed
stdin.setRawMode(true);

// resume stdin in the parent process (node app won't quit all by itself
// unless an error or process.exit() happens)
stdin.resume();

// i don't want binary, do you?
stdin.setEncoding('utf8');
var speed = 0, forward = 0, reverse = 0, irChannel = '1R';

// Controll train with keyboard
stdin.on('data', function (key) {
	// ctrl-c ( end of text )
	if (key === '\u0003') {
		cleanUp();
	}

	if (key === 'k') {
		if (reverse == 1) {
			speed--;
			if (speed == 0) {
				exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_BRAKE', writeToConsole);
				reverse = 0;
			} else {
				exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_M' + speed, writeToConsole);
			}
		} else {
			forward = 1;
			if (speed != 8) {
				speed++;
			}
			exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_' + speed, writeToConsole);
		}
		console.log(speed);
	}

	if (key === 'm') {
		if (forward == 1) {
			speed--;
			if (speed == 0) {
				exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_BRAKE', writeToConsole);
				forward = 0;
			} else {
				exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_' + speed, writeToConsole);
			}
		} else {
			reverse = 1;
			if (speed != 8) {
				speed++;
			}
			exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_M' + speed, writeToConsole);
		}
		console.log(speed);
	}

	if (key === 'a') {
		process.stdout.write(key + ' Stop Train!!');
		speed = 0;
		forward = 0;
		reverse = 0;
		exec('irsend SEND_ONCE LEGO_Single_Output ' + irChannel + '_BRAKE', writeToConsole);
	}

});

function cleanUp() {
	SENSOR1.unexport(); // Unexport GPIO and free resources
	SENSOR2.unexport();
	STEPPIN_RIGHT.writeSync(0);
	STEPPIN_RIGHT.unexport();
	STEPPIN_LEFT.writeSync(0);
	STEPPIN_LEFT.unexport();
	MOTORPOWER_PIN.writeSync(0);
	MOTORPOWER_PIN.unexport();
	process.exit();
}


process.on('SIGINT', function () {
	cleanUp();
});