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
    $.post($(this).attr("action"), $(this).serialize(), function (response) {
        // update the HTML of a div with the response from the server
        if (response.status === 'success') {
            $(".alert-success").removeClass("d-none").html(response.message);
            $('#myForm').find('input[type="text"], input[type="email"], textarea').val('');
            setTimeout(function () {
                $(".alert-success").addClass("d-none");
            }, 5000);
        } else {
            $(".alert-danger").removeClass("d-none").html(response.message);
            console.log(response);
            $('#myForm').find('input[type="text"], input[type="email"], textarea').val('');
            setTimeout(function () {
                $(".alert-danger").addClass("d-none");
            }, 5000);
        }
    });
});
$('#color-button').on('click', function () {
    const currentMainColor = $(':root').css('--main-color');
    const currentAccentColor = $(':root').css('--accent-color');

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