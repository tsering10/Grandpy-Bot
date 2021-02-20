
function chatBox(response, global_response) {
    // create DOM objects
	var global_gp_answer = document.createElement("div");
	global_gp_answer.id = "global_gp_answer";
	var figure_Gp = document.createElement("figure");
	var Gp_answer_gmap = document.createElement("p");
	var answer_gmap = document.createElement("p");
	var Gp_answer_wiki = document.createElement("p");
	var answer_wiki = document.createElement("p");
	var text_answer = document.createElement("div");
	text_answer.id = "text_answer";
	Gp_answer_gmap.id = 'Gp_answer';
    Gp_answer_wiki.id = 'Wiki_answer';
	var Gp_icon = document.createElement("img");

	Gp_icon.src = "/static/img/answer_robot.png";
	Gp_icon.alt = "answer_grandpy";
	Gp_icon.title = "answer_grandpy";
	global_gp_answer.appendChild(figure_Gp);
	figure_Gp.appendChild(Gp_icon);
	global_gp_answer.appendChild(text_answer);
	dialogue.appendChild(global_gp_answer);

	// If Mediawiki and Google map return  values
	if (response.wiki !== "NO_RESULT") {
	Gp_answer_gmap.textContent = response.Gp_answer_gmap+" "+response.gmap;
	Gp_answer_wiki.textContent = response.Gp_answer_wiki;

	source_url = document.createElement("a");
	source_url.href = "https://fr.wikipedia.org/?curid="+response.wiki_id
	source_url.textContent = "Lire la suite";
	answer_wiki.textContent = response.wiki+" ";
	answer_wiki.appendChild(source_url);

	text_answer.appendChild(Gp_answer_gmap);
	text_answer.appendChild(Gp_answer_wiki);
	text_answer.appendChild(answer_wiki);

    // calling the updateMap function to update new coordinates
	updateMap(response.latitude, response.longitude, response.gmap);

	grandpyLoad("off")
	query_text.disabled = false;
	}
	// if gmap returns nothing
	else {
		if (response.gmap === "NO_RESULT"){
			var Gp_answer = document.createElement("p");
			Gp_answer.textContent = response.Gp_answer;
			text_answer.appendChild(Gp_answer);
			grandpyLoad("off")
			query_text.disabled = false;
			}

		// if only wikimedia returns nothing
		else {
			Gp_answer_gmap.textContent = response.Gp_answer_gmap+" "+response.gmap;;
			Gp_answer_wiki.textContent = response.Gp_answer_wiki;
			text_answer.appendChild(Gp_answer_gmap);
			text_answer.appendChild(Gp_answer_wiki);
			grandpyLoad("off")
			query_text.disabled = false;
			}
	}
}

// GrandPy thinking animation
function grandpyLoad(state) {
	var Gp_loading_pict = document.getElementById("search_img");

	if (state === "on") {
		var papy_gif = document.createElement("img");
		papy_gif.src = "/static/img/robo_search.gif";
		papy_gif.alt = "robot_searching"
		papy_gif.title = "Je cherche..."
		papy_gif.id = "gif_search"
		Gp_loading_pict.replaceChild(papy_gif, document.getElementById("search_img_gif"))

	} else {
		var search_img_gif = document.createElement("img")
		search_img_gif.src = "/static/img/search_image.png";
		search_img_gif.alt = "search_image";
		search_img_gif.id = "search_img_gif";
		search_img_gif.addEventListener("click", user_request_analyse);
		Gp_loading_pict.replaceChild(search_img_gif, document.getElementById("gif_search"))
	}
}


// if the query has more than 2 characters
function user_request_analyse()
{
	if (form.elements.query.value.length > 2) {
			button_papy_link();
					}
	else 	{
			noQuery();
					}
}

/// Main function called when the client ask a question to GrandPy
function button_papy_link() {
	grandpyLoad("on");
	query_text.disabled = true;
	var request = form.elements.query.value;
	form.elements.query.value="";
	var global_user_request = document.createElement("div");
	global_user_request.id = "global_user_request";
	var figure_user = document.createElement("figure");
	var user_icon = document.createElement("img");
	user_icon.src = "/static/img/robots-typing.png";
	user_icon.alt = "search_grandpy";
	user_icon.title = "search_grandpy";
	figure_user.appendChild(user_icon);
	var user_request = document.createElement("p");
	user_request.textContent = request;
	user_request.id = "user_request_query";
	global_user_request.appendChild(figure_user);
	global_user_request.appendChild(user_request);
	dialogue.appendChild(global_user_request);
	var url = encodeURI("https://tashi-grandpy.herokuapp.com//results/?query="+request);
	// var url = encodeURI("http://127.0.0.1:5000/results/?query="+request);

	ajaxGet(url, chatBox);

}

// If the query less than 2 characters we give a response
function noQuery()
{
	var text_answer = document.createElement("div");
	text_answer.id = "text_answer";

	var global_gp_answer = document.createElement("div");
	global_gp_answer.id = "global_gp_answer";

	var figure_Gp = document.createElement("figure");
	var Gp_icon = document.createElement("img");
	Gp_icon.src = "/static/img/answer_robot.png";
	Gp_icon.alt = "answer_grandpy";
	Gp_icon.title = "answer_grandpy";

	var Gp_answer = document.createElement("p");
	Gp_answer.textContent = "Si tu ne me demandes rien, je ne peux pas y réfléchir !";

	text_answer.appendChild(Gp_answer);
	figure_Gp.appendChild(Gp_icon);
	global_gp_answer.appendChild(figure_Gp);
	global_gp_answer.appendChild(text_answer);
	dialogue.appendChild(global_gp_answer);
}

// AJAX request using build-in XMLHttpRequest object
function ajaxGet(url, callback) {
	// Creates a new XMLHttpRequest object
	var req = new XMLHttpRequest();
	req.open("GET", url);
	req.addEventListener("load", function() {
		// Everything is good, the response was received.
        if (req.readyState === XMLHttpRequest.DONE) {
            if (req.status === 200) {
                 global_response = JSON.parse(req.responseText)
                response = global_response.response
                callback(response, global_response);
          }}
          else {
			console.error(req.status + " " + req.statusText + " " + url);
		}
	});
	req.addEventListener("error", function() {
		console.error("There was a problem with the request : " + url);
	});
	req.send(null);
}