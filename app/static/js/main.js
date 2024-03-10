$(document).ready(function() {
    $('#searchForm').submit(function(event) {
        event.preventDefault();

        var searchQuery = $('#searchQuery').val();
        $.ajax({
            url: '/music',
            type: 'POST',
            data: {search_query: searchQuery},
            success: function(response) {
                if (response.length > 0) {
                    $('#songInfo').empty();
                    response.forEach(function(song) {
                        var songBlock = $('<div class="song-block"></div>');
                        songBlock.append('<p>Title: ' + song.title + '</p>');
                        songBlock.append('<p>Author: ' + song.author + '</p>');
                        songBlock.append('<a href="' + song.audio_link + '">Listen</a>');
                        $('#songInfo').append(songBlock); // Добавляем блок на страницу
                    });
                } else {
                    $('#songInfo').html('<p>No songs found</p>');
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
