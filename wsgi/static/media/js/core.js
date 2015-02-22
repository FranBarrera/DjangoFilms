var core = {
    init: function () {
        core.setImageSize();
    },
    setImageSize: function () {
        var width_el = $('.card').find('img');
        var width_login = $('.login');
        width_el.css('height', width_el.width() * 274 / 185);
        width_login.css('top', ($(window).height() - width_login.height()) / 2 - 100);
    }
};

$(document).ready(function () {
    core.init();
});


$(window).resize(function () {
    core.init();
});
