#!/usr/bin/node

const args = process.argv.slice(2); //Gets the command line args, excluding the forst two (node and script filename)


if (args.length === 0) {
	console.log("No argument");
	}else if (args.lenght === 1) {
	console.log("Argument found");
	}else {
	console.log("Arguments found");
	}

