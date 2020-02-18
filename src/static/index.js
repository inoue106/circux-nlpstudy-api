$(document).ready(function() {
    $('.js-recognize').on('click', function() {
        $.ajax({
            type: "POST",
            url: "/recognize",
            data: {w: $('.js-word').val()},
            dataType: "json"
        })
        .done(function(res) {
            $('.js-result').html('<ul></ul>');
            res.data.forEach(function (t) {
                $('.js-result ul').append(`<li>${t.i} ${t.orth} ${t.lemma} ${t.pos} ${t.tag} ${t.dep} ${t.head}</li>`);
            });
        });
    });
    $('.js-similarity').on('click', function() {
        $.ajax({
            type: "POST",
            url: "/similarity",
            data: {w1: $('.js-word1').val(), w2: $('.js-word2').val()},
            dataType: "json"
        })
        .done(function(res) {
            $('.js-result').html('<ul></ul>');
            $('.js-result ul').append(`<li>${res.similarity}</li>`);
        });
    });
    $('.js-most-similar').on('click', function() {
        $.ajax({
            type: "POST",
            url: "/most-similar",
            data: {w: $('.js-word1').val(), n: 5},
            dataType: "json"
        })
        .done(function(res) {
            $('.js-result').html('<ul></ul>');
            res.similarity.forEach(function (s) {
                $('.js-result ul').append(`<li>${s[0]}(${s[1]})</li>`);
            });
        });
    });
});
