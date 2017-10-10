var codeLiteracy;

function setup() {

	codeLiteracy = new CodingClass();
	pComp = new CodingClass();

	pComp.numStudents = 100;

}

function draw() {

	print (pComp.numStudents); // 100

}

function CodingClass() {

	this.date = "tuesday";
	this.numStudents = 20;

}