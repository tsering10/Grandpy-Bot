// script called when page has been loaded

//get the dialogue ID
var dialogue = document.getElementById("dialogue");
var form = document.querySelector("form");
var query_text = form.query;
//create a div with ID(text_answer)  tag element
var text_answer = document.createElement("div");
text_answer.id = "text_answer";

// create a div with ID(global_gp_answer) tag element
var global_gp_answer = document.createElement("div");
global_gp_answer.id = "global_gp_answer";

// create a figure element
var figure_Gp = document.createElement("figure");
// create a image tag element
var Gp_icon = document.createElement("img");
Gp_icon.src = "/static/img/answer_robot.png";
Gp_icon.alt = "answer_grandpy";
Gp_icon.title = "answer_grandpy";

// create a p tag element
var Gp_answer = document.createElement("p");
Gp_answer.textContent = "Salut, je suis GrandPy, mets-moi à l'épreuve !";

text_answer.appendChild(Gp_answer);
figure_Gp.appendChild(Gp_icon);
global_gp_answer.appendChild(figure_Gp);
global_gp_answer.appendChild(text_answer);
dialogue.appendChild(global_gp_answer);

// Add event on form
form.addEventListener("submit", function(e){
	e.preventDefault();

	if (form.elements.query.value.length > 2){
		button_papy_link();
	}
	else {
		noQuery();
	}

});


