$(document).ready(function() {
    $('#searchForm').submit(function(event) {
        event.preventDefault();
        var searchQuery = $('#searchQuery').val();
        $.ajax({
            url: '/music',
            type: 'POST',
            data: {search_query: searchQuery},
            success: function(response) {
                console.log(response); // Добавлено для проверки
                if (response.length > 0) {
                    var foundSong = response.find(song => song.title.toLowerCase() === searchQuery.toLowerCase());
                    if (foundSong) {
                        var audioHtml = foundSong.audio_link ? '<a href="' + foundSong.audio_link + '" download>Download Audio</a>' : 'No audio available';
                        $('#songInfo').html('<p>Song Name : ' + foundSong.title + '</p><p>Author: ' + foundSong.author + '</p>' + '<p>Audio: ' + audioHtml + '</p>');
                    } else {
                        $('#songInfo').html('<p>No such song found</p>');
                    }
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
