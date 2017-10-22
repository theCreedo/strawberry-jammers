var counter = 0;
var song_count = 0;
var song_name = ["a", "b", "c", "d", "e", "f"]
var lyrics = []
var lyrics_counter = 0;

function populate_search_results() {
	// song_name = document.getElementById('user-input').value;

	document.getElementById('search_results').classList.remove('hide');

	for (var i = 1; i < 6; i++) {
		var song_item = '<a id="song' 
		+ i.toString()
		+ '" href="#" class="list-group-item" onclick="addSong()">'																
		+ song_name[i]
		+ '<span class="glyphicon glyphicon glyphicon-plus" style="float: right;"></span>'
		+ '</a>'
		$(song_item).appendTo("#search-results")

		var id = "song" + i.toString();

		$('#'+id).click(addEventListener);
	}
};

function addEventListener() {
	if (counter > 0) {
		var id = $(this).attr('id')+ 0;
		console.log('triggered');

		var string = '<li><a data-toggle="tab" href="#' + id + '">'
		+ $(this).text()
		+ '</a></li>';

		$(string).appendTo("#song-list");

		var tab_item = '<div id="' + id + '" class="tab-pane fade in">'
		+ '<div>';

		//tab_item += // lyrics here
		tab_item = tab_item + '</div>';

		var new_id = "song" + (song_count+2) + '0';

		$(tab_item).appendTo('#tab-master');

		if (counter == 1) {
			var newBody = document.getElementById("songListActual").innerHTML;
			document.getElementById("songListContainer").innerHTML = newBody;

			var toAdd = '<p><a id ="' + new_id + '" href="#' + id + '" class="list-group-item active">' + $(this).text() + '</a></p>';
			$(toAdd).appendTo('#songListContainer');
		}

		else {
			var toAdd = '<p><a id="' + new_id + '"href="#' + id + '" class="list-group-item">' + $(this).text() + '</a></p>';
			$(toAdd).appendTo('#songListContainer');
		}

		$('#'+new_id).click(addEventListenerForSongView);


		song_count++;
	}


	counter++;

};

function addEventListenerForSongView() {
	$(this).addClass('active')}
	