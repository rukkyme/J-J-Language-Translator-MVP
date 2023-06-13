$(document).ready(function () {
    // Populate language dropdowns
    $.each(LANGUAGES, function (code, language) {
        $('#source-lang').append($('<option>').val(code).text(language));
        $('#target-lang').append($('<option>').val(code).text(language));
    });

    // Translate button click event
    $('#translate-btn').click(function () {
        var text = $('#text-input').val();
        var sourceLang = $('#source-lang').val();
        var targetLang = $('#target-lang').val();

        if (text && sourceLang && targetLang) {
            // Translate text
            $.ajax({
                url: '/translate',
                type: 'POST',
                dataType: 'json',
                data: {
                    text: text,
                    sourceLang: sourceLang,
                    targetLang: targetLang
                },
                success: function (response) {
                    $('#output').text(response.translatedText);
                },
                error: function () {
                    alert('An error occurred during translation.');
                }
            });
        } else {
            alert('Please enter text and select source/target languages.');
        }
    });
});

