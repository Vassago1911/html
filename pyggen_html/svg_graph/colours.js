function random_rgb() {
    var o = Math.round, r = Math.random, s = 32 ; offset=32;
    return 'rgba(' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) + ')';
}

function random_rgb_light() {
    var o = Math.round, r = Math.random, s = 32 ; offset=32;
    return 'rgba(' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) +
               ',' + o(r()*s + offset ) + ',.95)';
}