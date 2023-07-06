let owl = $('.owl-carousel');
owl.owlCarousel({
    center: true,
    loop: true,
    margin: 40,
    items: 3,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});
owl.on('mousewheel wheel', '.owl-stage', function (e) {
    if (e.originalEvent.deltaY > 0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});

// education / work
$("#education-btn").click(function () {
    $(".work-item").hide();
    $(".education-item").show();
});
$("#work-btn").click(function () {
    $(".education-item").hide();
    $(".work-item").show();
});
$("button.navbar-toggler").click(function () {
    $("#navbarNav").toggleClass("collapse");
    if (!$("#navbarNav").hasClass("collapse")) {
        $(".navbar").css("border", "none");
    } else {
        $(".navbar").css("border-bottom", "1px solid #ddd");
    }
});
$("form").submit(function (event) {
    event.preventDefault();
    var form = $(this);
    var url = form.attr("action");
    var data = form.serialize();
    var csrf_token = $('meta[name="csrf-token"]').attr('content'); // retrieve CSRF token from meta tag

    // Add CSRF token to form data
    data += "&_token=" + csrf_token;

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        success: function (response) {
            // handle success response
            if (response.status === 'success') {
                $(".alert-success").removeClass("d-none").html(response.message);
                form.find('input[type="text"], input[type="email"], textarea').val('');
                setTimeout(function () {
                    $(".alert-success").addClass("d-none");
                }, 5000);
            } else {
                $(".alert-danger").removeClass("d-none").html(response.message);
                console.log(response);
                form.find('input[type="text"], input[type="email"], textarea').val('');
                setTimeout(function () {
                    $(".alert-danger").addClass("d-none");
                }, 5000);
            }
        },
        error: function (xhr, status, error) {
            // handle error response
        }
    });
});
$('#color-button').on('click', function () {
    const currentMainColor = $(':root').css('--main-color');

    if (currentMainColor === '#fafafa') {
        $(':root').css('--main-color', '#09192E');
        $(':root').css('--accent-color', '#42A2A1');
        $(':root').css('--text-color', '#CEDBF2');
        $(':root').css('--hover-color', '#05edeb');
        $(':root').css('--background-color', '#172A45');
        $(':root').css('--shadow-color', 'rgba(255, 255, 255, 0.2)');
        $(':root').css('--card-footer-color', '#13243b');
        $('nav').addClass('navbar-dark');
        $('.moon-sun-icon').removeClass('bi-moon-stars-fill').addClass('bi-sun-fill');
    } else {
        $(':root').css('--main-color', '#fafafa');
        $(':root').css('--accent-color', '#6e4fef');
        $(':root').css('--text-color', '#040307');
        $(':root').css('--hover-color', '#342570');
        $(':root').css('--background-color', '#fafafa');
        $(':root').css('--shadow-color', 'rgba(0, 0, 0, 0.2)');
        $(':root').css('--card-footer-color', '#f7f7f7');
        $('nav').removeClass('navbar-dark');
        $('.moon-sun-icon').removeClass('bi-sun-fill').addClass('bi-moon-stars-fill');
    }
});