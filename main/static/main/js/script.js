
function details_project() {
	document.querySelector("#details-project").classList.toggle("active");
	document.querySelector("#create").classList.toggle("active");

};

function details_task() {
	document.querySelector("#details-task").classList.toggle("active");
	document.querySelector("#add-file").classList.toggle("active");
};

// let projects = document.querySelector("#projects");
// let task = document.querySelector("#task");
// let persons = document.querySelector("#persons");

// let projectsBtn = document.querySelector("#projects-btn");
// let taskBtn = document.querySelector("#task-btn");
// let personsBtn = document.querySelector("#persons-btn");

function projectsFunc() {
	document.querySelector("#task-btn").classList.remove("active");
	document.querySelector("#task").classList.add("active");

	document.querySelector("#persons-btn").classList.remove("active");
	document.querySelector("#persons").classList.add("active");

	document.querySelector("#projects-btn").classList.add("active")
	document.querySelector("#projects").classList.remove("active")
}


function taskFunc() {
	document.querySelector("#persons-btn").classList.remove("active");
	document.querySelector("#persons").classList.add("active");
	
	document.querySelector("#projects-btn").classList.remove("active")
	document.querySelector("#projects").classList.add("active")

	document.querySelector("#task-btn").classList.add("active");
	document.querySelector("#task").classList.remove("active");
}


function personsFunc() {
	document.querySelector("#projects-btn").classList.remove("active")
	document.querySelector("#projects").classList.add("active")
	
	document.querySelector("#task-btn").classList.remove("active");
	document.querySelector("#task").classList.add("active");

	document.querySelector("#persons-btn").classList.add("active");
	document.querySelector("#persons").classList.remove("active");
}
