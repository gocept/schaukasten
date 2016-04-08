/*global describe, Schaukasten, $, beforeEach, afterEach, it, expect */

describe("Schaukasten", function () {
    "use strict";

    beforeEach(function () {
        $('body').append($('<div class="content"></div>'));
        new Schaukasten('.content');
    });

    afterEach(function () {
        $('.content').remove();
    });

    it("can run tests.", function () {
        expect($('.content').text()).toEqual('App is initialized');
    });
});
