 const manufacturer = $('#id_manufacturer'),
            vehicle = $('#id_vehicle');

manufacturer.on('change', function(){
    updateChoices();
})


function updateChoices(){
    csrf = $('input[name="csrfmiddlewaretoken"]')
    $.ajax({
        type: "GET",
        url: '/utils/get_choices',
        datatype: "json",
        async: true,
        data: {csrfmiddlewaretoken: $(csrf).val(),
                manufacturer: $(manufacturer).val()},
        success: function(json){
            $(vehicle).children().remove();
            for(var i = 0; i < json.choices.length; i++){
                $(vehicle).append(
                    new Option(json.choices[i][1], json.choices[i][0]));
            }
        }
    })
}
