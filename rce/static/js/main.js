$('#mylink a').on('click', function (event) {
    event.preventDefault()
    console.log("click")
    $('#mylink a').removeClass('active');
    $(this).addClass('active');
})