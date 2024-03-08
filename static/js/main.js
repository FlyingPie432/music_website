$(document).ready(function() {
    $('#search-form').submit(function(event) {
        event.preventDefault();
        var searchQuery = $('#search-query').val();
        $.ajax({
            type: 'POST',
            url: '/music',
            data: { search_query: searchQuery },
            success: function(response) {
                displaySongs(response);
            }
        });
    });

    function displaySongs(songs) {
        $('#song-results').empty();
        songs.forEach(function(song) {
            var songHTML = '<div>';
            songHTML += '<h3>' + song.title + '</h3>';
            songHTML += '<p>Author: ' + song.author + '</p>';
            songHTML += '</div>';
            $('#song-results').append(songHTML);
        });
    }
});
