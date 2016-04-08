'use strict';

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

/*global $, document */

var Schaukasten = function Schaukasten(selector) {
  _classCallCheck(this, Schaukasten);

  this.node = $(selector);
  $(selector).text('App is initialized');
};

$(document).ready(function () {
  new Schaukasten('.content');
});
//# sourceMappingURL=app.base.js.map
