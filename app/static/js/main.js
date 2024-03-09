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
                        $('#songInfo').html('<p>Title: ' + foundSong.title + '</p><p>Author: ' + foundSong.author + '</p>');
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
