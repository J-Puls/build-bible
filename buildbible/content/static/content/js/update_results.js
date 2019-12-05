$(document).ready(function () {
    var v_id = $('#page-data').data('vehicle_id');
    getContent(1, v_id);
})

function getContent(category, v_id) {
    $('.posts').children().remove();
    $('.posts').append(`<div class="w-50  text-center m-center">
    <p>
        <ion-icon name="aperture" class="spinner"></ion-icon>
    </p>
    <p class="flashing">Fetching content...</p>
</div>`)
    var options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };
    $.ajax({
        type: "GET",
        url: '/utils/update_content',
        datatype: "json",
        async: true,
        data: {
            vehicle_id: v_id,
            category: category,
        },
        success: function (json) {
            $('.posts').children().remove();
            if (json.length > 0) {
                if (category > 0) {
                    for (var i = 0; i < json.length; i++) {
                        $('.posts').append(`<section class="post">
                        <header class="post-header">
                            <h2 class="post-title">
                                <a href="/post/` + json[i].id + `" aria-label="` + json[i].title + `" title="` + json[i].title + `">
                                    ` + json[i].title + `
                                </a>
                            </h2>
                            <p class="post-meta">
                                Posted on <small>
                                    ` + new Date(json[i].date_posted).toLocaleDateString("en-US", options) + `
                                </small>
                            </p>
                        </header>
                        <div class="post-description">
                            <p>` + json[i].description + `</p>
                        </div>
                    </section>`)
                    }
                } else if (category == 0) {
                    for (var i = 0; i < json.length; i++) {
                        $('.posts').append(`<section class="post">
                        <header class="post-header">
                            <h2 class="post-title">` + json[0].display_filename + `</h2>
                            <p class="post-meta">
                                Uploaded on: <small>` + new Date(json[0].date_uploaded).toLocaleDateString("en-US", options) + `</small>
                            </p>
                        </header>
                            <a href="/media/` + json[0].fsm_file + `" target="_blank" class="pure-button button-link" aria-label="View PDF" title="View PDF">View PDF</a>
                    </section>`)
                    }
                }

            } else {
                $('.posts').append(`<h3 class="text-center">We haven't added content for that yet.
                <br><small class="text-primary">Try another category or check back soon!</small></h3>
                <img class="center-block" src="` + $('#page-data').data('illurl') + `" height="250" width="500" alt="no results">`)
            }

        }
    })
}
var tabs = $('.nav-link');
$(tabs).on('click', function () {
    for (var i = 0; i < tabs.length; i++) {
        $(tabs[i]).removeClass('active');
    }
    var v_id = $('#page-data').data('vehicle_id');
    $(this).addClass('active')
    getContent(($(this).data('category')), v_id)
})