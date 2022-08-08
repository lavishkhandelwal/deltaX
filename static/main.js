$("#saveArtist").click(function (){
    output = "";
    let artist = $('#artist').val();
    let dob = $('#dob').val();
    let bio = $('#bio').val();
    let csrf = $('input[name=csrfmiddlewaretoken]').val();
    data = {name: artist, dob : dob, bio : bio, csrfmiddlewaretoken: csrf};
    $.ajax({
        url: 'ajax_artists/',
        method: 'POST',
        data : data,
        success: function (data) {
            x = data.artists_data;
            if(data.msg == "Save"){
                for(i = 0; i < x.length; i++){
                    output += '<li class="dropdown-item"><input type = "checkbox" value = ' + x[i].name + '>&nbsp;&nbsp;' + x[i].name + '</li>'
                }
                alert("Success! Artist Saved.")
                $("#post-form").trigger("reset");
                $("#artist-drop-down").html(output);
            }
            if(data.msg == "0"){
                alert("Artist Already Exits.")
                $("#post-form").trigger("reset");
            }
            if(data.msg == "fill all fields"){
                alert("All fields are required.")
            }
        },
    });
});

$("#saveSong").click(function (){
    var data = new FormData($('#post-form').get(0));
    $.ajax({
        url: './',
        method: 'POST',
        data : data,
        processData: false,
        contentType: false,
        success: function (data) {
            if(data.msg == "Save"){
                alert("Success! Song Saved.")
                $("#post-form").trigger("reset");
                $("#artist-drop-down").html(output);
            }
            if(data.msg == "0"){
                alert("Song Already Exits.")
                $("#post-form").trigger("reset");
            }
            if(data.msg == "fill all fields"){
                alert("All fields are required.")
            }
        },
    });
});

$("#cancelArtist").click(function (){
    $("#post-form").trigger("reset");
});

$("#cancelSong").click(function (){
    $("#post-form").trigger("reset");
});

