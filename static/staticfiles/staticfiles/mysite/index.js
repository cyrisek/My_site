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
        }
    });
});
