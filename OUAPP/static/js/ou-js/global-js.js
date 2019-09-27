'use strict';

const offnone = document.getElementById('bs');
const search_on = document.getElementById('fun_search');
const search_results = document.getElementById('search_results');
const icon_slash = document.getElementById('i_slash');


search_on.addEventListener('click', function() {	
	search_results.style.display = 'block';
});

offnone.addEventListener('click', function() {
	search_results.style.display = '';
	
});

$('#fun_search').click(function() {
	
	
	search_results.style.display = 'block';
	
});

$(document).keydown(function(e){
    if (e.which == 191) {
		icon_slash.style.display = 'none';
		search_on.style
		search_results.style.display = 'block';
        return false;
	}
	if(e.which == 27) {
		icon_slash.style.display = 'block';
		search_results.style.display = '';
		return false;
	}
});

alert('Js ok');