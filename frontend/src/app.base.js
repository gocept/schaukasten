/*global $, document */

class Schaukasten {
  constructor(selector) {
    this.node = $(selector);
    $(selector).text('App is initialized');
  }
}

$(document).ready(function () {
    new Schaukasten('.content');
});
