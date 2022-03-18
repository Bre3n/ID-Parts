$(document).ready(function () {

    var form = $('#form'),
        email = $('#email'),
        subject = "a",
        message = $('#message'),
        info = $('#info'),
        loader = $('#loader'),
        submit = $("#submit");

    $("#download").on('click', function () {
        window.open("https://github.com/Bre3n/ID-Parts/raw/master/dist/PartsID.exe", '_blank');
    })

    $("#documentation").on('click', function () {
        window.open("https://id-parts.readthedocs.io/pl/latest/", '_blank');
    })

    form.on('input', '#email, #subject, #message', function () {
        $(this).css('border-color', '');
        info.html('').slideUp();
    });

    submit.on('click', function (e) {
        info.html('Wysyłanie...').css('color', 'red').slideDown();
        e.preventDefault();
        if (validate()) {
            $.ajax({
                type: "POST",
                url: "mailer.php",
                data: form.serialize(),
                dataType: "json"
            }).done(function (data) {
                if (data.success) {
                    email.val('');
                    message.val('');
                    info.html('Wiadomość wysłana!').css('color', 'green').slideDown();
                } else {
                    info.html('Nieststy nie udało się wysłać wiadomości! Wyślij wiadomość ręcznie na report@partsid.cba.pl!').css('color', 'red').slideDown();
                }
            });
        }
        else {
            info.html('Uzupełnij pola...').css('color', 'red').slideDown();
        }
    });

    function validate() {
        var valid = true;
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

        if (!regex.test(email.val())) {
            email.css('border-color', 'red');
            valid = false;
        }
        if ($.trim(message.val()) === "") {
            message.css('border-color', 'red');
            valid = false;
        }

        return valid;
    }

});