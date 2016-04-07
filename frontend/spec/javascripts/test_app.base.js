/*global describe, schaukasten, $, beforeEach, afterEach, it, expect */
/*jslint nomen: true, unparam: true, bitwise: true*/

describe("Schaukasten", function () {
    "use strict";

    beforeEach(function () {
        $('body').append($('<div class="content"></div>'));
        schaukasten.initialize();
    });

    afterEach(function () {
        $('.content').remove();
    });

    it("can run tests.", function () {
        expect($('.content').text()).toEqual('App is initialized');
    });
});
