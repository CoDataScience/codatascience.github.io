---
layout: raw
title: tensorflow_example_davis_yoshida in tutorials
repository: tutorials
---
<html>
<head><meta charset="utf-8" />
<title>tensorflow_example_davis_yoshida</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.6 (http://getbootstrap.com)
 * Copyright 2011-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
@-moz-document url-prefix() {
  div.inner_cell {
    overflow-x: hidden;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 20ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">itertools</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">shutil</span>
<span class="kn">import</span> <span class="nn">tensorflow</span> <span class="k">as</span> <span class="nn">tf</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">batch_size</span> <span class="o">=</span> <span class="mi">64</span>
<span class="n">hidden_units</span> <span class="o">=</span> <span class="mi">900</span>
<span class="n">n_layers</span> <span class="o">=</span> <span class="mi">5</span>
<span class="n">logdir</span> <span class="o">=</span> <span class="s1">&#39;/tmp/tf_demo_logs&#39;</span> <span class="c1"># Be careful changing this since this directory will be purged when this notebook is run</span>
<span class="n">num_examples</span> <span class="o">=</span> <span class="mi">1000</span>
<span class="n">noise_scale</span> <span class="o">=</span> <span class="mf">0.1</span>
<span class="n">num_epochs</span> <span class="o">=</span> <span class="mi">10</span>
<span class="n">learning_rate</span> <span class="o">=</span> <span class="mf">0.0001</span>
<span class="n">init_scale</span> <span class="o">=</span> <span class="mi">6</span> <span class="o">/</span> <span class="p">(</span><span class="n">hidden_units</span> <span class="o">**</span> <span class="mf">0.5</span><span class="p">)</span>
<span class="n">nonlinearity</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Clean out old model so changes to definition won&#39;t mismatch</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">logdir</span><span class="p">):</span>
    <span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="n">logdir</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Generate some noisy training data</span>
<span class="n">x_data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="p">(</span><span class="n">num_examples</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
<span class="n">label_data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">&gt;</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span> <span class="o">*</span> <span class="n">x</span><span class="p">)</span> <span class="o">+</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="n">scale</span><span class="o">=</span><span class="n">noise_scale</span><span class="p">))</span> <span class="k">for</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="ow">in</span> <span class="n">x_data</span><span class="p">])</span> <span class="c1"># + np.random.normal(scale=noise_scale, size=num_examples)</span>

<span class="k">def</span> <span class="nf">plot</span><span class="p">(</span><span class="n">points</span><span class="p">,</span> <span class="n">labels</span><span class="p">):</span>
    <span class="n">colors</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;red&#39;</span><span class="p">,</span> <span class="s1">&#39;blue&#39;</span><span class="p">]</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="o">*</span><span class="nb">zip</span><span class="p">(</span><span class="o">*</span><span class="n">points</span><span class="p">),</span> <span class="n">color</span><span class="o">=</span><span class="p">[</span><span class="n">colors</span><span class="p">[</span><span class="n">l</span><span class="p">]</span> <span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="n">labels</span><span class="p">])</span>           

<span class="n">plot</span><span class="p">(</span><span class="n">x_data</span><span class="p">,</span> <span class="n">label_data</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1"># Grid of points for evaluating model</span>
<span class="n">holdout_x</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">itertools</span><span class="o">.</span><span class="n">product</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mf">0.03</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mf">0.03</span><span class="p">)))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
APz5z/4/TfLa/6FDsGqV/4KfNMnrTVd37Jj/6u/e3c+aFWprI53eunXrGOOX9xI9c5FmcrEIuCXH
rK+GEFZFyzQDt4UQFmet9yBwB3AW8AowJ4Swq8D7KLmoESH4Ha537vQztBMndt4z0F1Cc7O3xyn3
ltciUnFpJRepNe8NIdwG3FZkmXYpcQjhQeDBdEolnZkZXHGFP6QK1NUpsRCRnKqpK6qIiIh0AUou
REREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5E
REQkUUouREREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRE
RCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQkUUouRERE
JFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQk
UUouREREJFFKLkRERCRRSi5EREQkUUouREREJFFKLkRERCRRSi5EREQkUUoualhTU1Oli9DpKGbl
UdziU8zKo7hVh9SSCzN7wMxeNbNDZvZRiessMrOTbR7L0ypjrdOHMD7FrDyKW3yKWXkUt+pQn+K2
uwO/AVYDs2OstwK4FbDo9bFkiyUiIiJpSi25CCE8BGBms2KueiyE8GEKRRIREZEOUI1tLq40s/1m
tt3MGs2sd6ULJCIiIqVL87JIOVYAvwV2A4OA+cByM5sQQgh51ukJsG3bto4pYRdy4MAB1q1bV+li
dCqKWXkUt/gUs/IobvFkHTt7Jrldy3/MzrGw2XxgXoFFAjA0hPBm1jqzgF+EEGKfgTCzgcBbwJQQ
wst5lvlrYEncbYuIiMhnZoYQfp3UxuKeufhnYFGRZf5QZlnaCSHsNrM/AoOBnMkF8AIwE3gbOJrU
e4uIiNSAnsAF+LE0MbGSixDCn4A/JVmAQsysP3AOsLdImRLLtkRERGrMa0lvMM37XAwws5HA+UCd
mY2MHr2yltluZtdHz3uZ2U/NbLyZnW9mU4DfAW+ScEYlIiIi6UmzQeePgVuyXmda2HwVWBU9/0vg
zOh5MzAiWucsYA+eVPwohHA8xXKKiIhIgmI16BQREREpphrvcyEiIiKdmJILERERSVSnTC40KFp8
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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">build_model</span><span class="p">():</span>
    <span class="sd">&quot;&quot;&quot;Build the model. No actual computation is done here, we&#39;re just defining the structure of future computation.&quot;&quot;&quot;</span>
    <span class="c1"># These variables are used to feed data into the graph</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">placeholder</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
    <span class="n">labels</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">placeholder</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;labels&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
    
    <span class="c1"># Create a list of layer sizes for our network</span>
    <span class="n">layer_sizes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="n">hidden_units</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">n_layers</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span>
    
    <span class="c1"># For each layer except the last define an affine transformation followed by a nonlinearity</span>
    <span class="n">layer_output</span> <span class="o">=</span> <span class="n">x</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="p">(</span><span class="n">in_size</span><span class="p">,</span> <span class="n">out_size</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">layer_sizes</span><span class="p">,</span> <span class="n">layer_sizes</span><span class="p">[</span><span class="mi">1</span><span class="p">:])):</span>
        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">variable_scope</span><span class="p">(</span><span class="s1">&#39;layer&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">),</span> <span class="n">reuse</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
            <span class="n">W</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">get_variable</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;W&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">),</span> <span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="n">in_size</span><span class="p">,</span> <span class="n">out_size</span><span class="p">),</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
            <span class="n">b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">get_variable</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;b&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">),</span> <span class="n">shape</span><span class="o">=</span><span class="n">out_size</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
            <span class="n">layer_output</span> <span class="o">=</span> <span class="n">nonlinearity</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="n">layer_output</span><span class="p">,</span> <span class="n">W</span><span class="p">)</span> <span class="o">+</span> <span class="n">b</span><span class="p">)</span>
        
    <span class="c1"># Compute two logits for a softmax layer</span>
    <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">variable_scope</span><span class="p">(</span><span class="s1">&#39;softmax&#39;</span><span class="p">,</span> <span class="n">reuse</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="n">softmax_W</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">get_variable</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;softmax_W&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="n">hidden_units</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
        <span class="n">softmax_b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">get_variable</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;softmax_b&#39;</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
        <span class="n">logits</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="n">layer_output</span><span class="p">,</span> <span class="n">softmax_W</span><span class="p">)</span> <span class="o">+</span> <span class="n">softmax_b</span>
    
    <span class="c1"># Instead of explicitly computing softmax, just pass logits to this loss functions</span>
    <span class="c1"># It will one loss per example so take the mean over the batch</span>
    <span class="n">loss</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">reduce_mean</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">sparse_softmax_cross_entropy_with_logits</span><span class="p">(</span><span class="n">logits</span><span class="p">,</span> <span class="n">labels</span><span class="p">))</span>
    
    <span class="c1"># Predictions are not used during training but are used for evaluation</span>
    <span class="n">predictions</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">logits</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>

    <span class="c1"># This node is used to apply gradient information to modify variables</span>
    <span class="n">train_op</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">AdamOptimizer</span><span class="p">(</span><span class="n">learning_rate</span><span class="o">=</span><span class="n">learning_rate</span><span class="p">)</span><span class="o">.</span><span class="n">minimize</span><span class="p">(</span><span class="n">loss</span><span class="p">)</span>
    
    
    <span class="k">return</span> <span class="n">x</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">predictions</span><span class="p">,</span> <span class="n">loss</span><span class="p">,</span> <span class="n">train_op</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># All variables defined will be put into the default graph</span>
<span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span><span class="o">.</span><span class="n">as_default</span><span class="p">():</span>
    <span class="c1"># Set a default name prefix and initializer for all variables</span>
    <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">variable_scope</span><span class="p">(</span><span class="s1">&#39;model&#39;</span><span class="p">,</span> <span class="n">reuse</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">initializer</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">random_uniform_initializer</span><span class="p">(</span><span class="n">minval</span><span class="o">=-</span><span class="n">init_scale</span><span class="p">,</span> <span class="n">maxval</span><span class="o">=</span><span class="n">init_scale</span><span class="p">)):</span>
        <span class="n">x_placeholder</span><span class="p">,</span> <span class="n">label_placeholder</span><span class="p">,</span> <span class="n">predictions</span><span class="p">,</span> <span class="n">loss</span><span class="p">,</span> <span class="n">train_op</span> <span class="o">=</span> <span class="n">build_model</span><span class="p">()</span>
    
    <span class="c1"># List of indices which will be shuffled for each epoch</span>
    <span class="n">example_order</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="n">num_examples</span><span class="p">))</span>
    
    <span class="c1"># The supervisor automatically saves variable state, and ensures that variables are initialized/loaded</span>
    <span class="n">supervisor</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">Supervisor</span><span class="p">(</span><span class="n">logdir</span><span class="o">=</span><span class="n">logdir</span><span class="p">)</span>
    <span class="k">with</span> <span class="n">supervisor</span><span class="o">.</span><span class="n">managed_session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="c1"># Plot the initial (random) decision boundary</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Initial decision boundary:&#39;</span><span class="p">)</span>
        <span class="n">feed_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">x_placeholder</span><span class="p">:</span> <span class="n">holdout_x</span><span class="p">}</span>
        <span class="n">prediction_vals</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">predictions</span><span class="p">,</span> <span class="n">feed_dict</span><span class="o">=</span><span class="n">feed_dict</span><span class="p">)</span>
        <span class="n">plot</span><span class="p">(</span><span class="n">holdout_x</span><span class="p">,</span> <span class="n">prediction_vals</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
        
        
        <span class="k">for</span> <span class="n">epoch</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_epochs</span><span class="p">):</span>
            <span class="c1"># Shuffle the order of examples</span>
            <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">shuffle</span><span class="p">(</span><span class="n">example_order</span><span class="p">)</span>
            <span class="n">steps</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="n">total_loss</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_examples</span> <span class="o">//</span> <span class="n">batch_size</span><span class="p">):</span>
                <span class="c1"># Get the indices for this minibatch</span>
                <span class="n">indices</span> <span class="o">=</span> <span class="n">example_order</span><span class="p">[</span><span class="n">i</span> <span class="o">*</span> <span class="n">batch_size</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="n">batch_size</span><span class="p">]</span>
                <span class="c1"># Fetches defines what values in the graph we want to compute</span>
                <span class="n">fetches</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;loss&#39;</span><span class="p">:</span> <span class="n">loss</span><span class="p">,</span> <span class="s1">&#39;train_op&#39;</span><span class="p">:</span> <span class="n">train_op</span><span class="p">}</span>
                <span class="c1"># A feed_dict defines the values we will insert into the graph</span>
                <span class="n">feed_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">x_placeholder</span><span class="p">:</span> <span class="n">x_data</span><span class="p">[</span><span class="n">indices</span><span class="p">],</span> <span class="n">label_placeholder</span><span class="p">:</span> <span class="n">label_data</span><span class="p">[</span><span class="n">indices</span><span class="p">]}</span>
                <span class="c1"># This is where all the actual computation happens</span>
                <span class="n">output</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">fetches</span><span class="o">=</span><span class="n">fetches</span><span class="p">,</span> <span class="n">feed_dict</span><span class="o">=</span><span class="n">feed_dict</span><span class="p">)</span>
                
                <span class="n">steps</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">total_loss</span> <span class="o">+=</span> <span class="n">output</span><span class="p">[</span><span class="s1">&#39;loss&#39;</span><span class="p">]</span>
            <span class="n">avg_loss</span> <span class="o">=</span> <span class="n">total_loss</span> <span class="o">/</span> <span class="n">steps</span>
            <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Epoch: </span><span class="si">{}</span><span class="s1"> Average Loss: </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">epoch</span><span class="p">,</span> <span class="n">avg_loss</span><span class="p">))</span>
                
            <span class="c1"># Plot the predicted curve</span>
            <span class="n">feed_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">x_placeholder</span><span class="p">:</span> <span class="n">holdout_x</span><span class="p">}</span>
            <span class="c1"># By not passing train_op in as a fetch, we can run the model without modifying weights</span>
            <span class="n">prediction_vals</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">predictions</span><span class="p">,</span> <span class="n">feed_dict</span><span class="o">=</span><span class="n">feed_dict</span><span class="p">)</span>
            <span class="n">plot</span><span class="p">(</span><span class="n">holdout_x</span><span class="p">,</span> <span class="n">prediction_vals</span><span class="p">)</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Initial decision boundary:
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xt8VeWd7/HPb+dCQrgFYhIFRBSLSCtKQKGotVKPbadq
W6tOqujUjr3odBzaHnvG10xtPefo6cXSy4yt1qlW0Yxap61trdfa6pRLSyJVEaGiqBACASJJIEAu
z/ljbcJOIFfW2s/ee33fr9d+yV57rb2/edzZ+e3nWet5zDmHiIiISFgSvgOIiIhIblFxISIiIqFS
cSEiIiKhUnEhIiIioVJxISIiIqFScSEiIiKhUnEhIiIioVJxISIiIqFScSEiIiKhUnEhIiIioYq0
uDCzs8zsUTPbbGZdZnbhAPu/L7lf6q3TzMqjzCkiIiLhibrnogRYDVwHDHYREwecCFQmb0c757ZF
E09ERETClh/lkzvnHgceBzAzG8Khjc655mhSiYiISJQy8ZwLA1abWb2ZPWlm7/UdSERERAYv0p6L
YdgCfBZYBYwArgF+b2anO+dWH+4AM5sAnA9sBPamKaeIiEguKAKOA55wzu0I60kzqrhwzq0H1qds
WmFmJwCLgav6OOx84P6os4mIiOSwy4EHwnqyjCou+vAnYEE/j28EWLp0KTNmzEhLoFyxePFilixZ
4jtGVlGbDY/abejUZsOjdhuatWvXcsUVV0Dyb2lYsqG4OJVguKQvewFmzJjB7Nmz05MoR4wdO1Zt
NkRqs+FRuw2d2mx41G7DFuppBZEWF2ZWAkwjOEkT4HgzmwXsdM69bWa3Asc4565K7n898AawhmAc
6Brg/cB5UeYUERGR8ETdczEHeJZg7goH3Jbc/lPgaoJ5LCan7F+Y3OcYYA/wIrDQOfdcxDlFREQk
JFHPc/EH+rnc1Tn3qV73vwV8K8pMIiIiEq1MnOdC0qS6utp3hKyjNhsetdvQqc2GR+2WGcy5wc7K
nZnMbDZQW1tbq5N4REREhqCuro6qqiqAKudcXVjPq54LERERCZWKCxEREQmVigsREREJlYoLERER
CZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJ
lYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmV
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
fPCDwTG/+13w4VNdHZwpvnQpvPZa8NqXXw5vvQUPPghtbXDeeXDuuUHG554LrqL55CeD/y5dChs3
wsyZwbb164O22r8fPvxhWLAAfvnL4GcsKwsyFRUFbbd5c7DU82WXBW38858HPUQXXhi06SOPqM3V
5mrzqNv8qKO8fbxKL5EPi0RNwyIiIiLDk3XDIiIiIhJPKi5EREQkVCouREREJFQqLkRERCRUKi5E
REQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRE
RCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouRERE
JFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQk
VCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRU
Ki5EREQkVCouREREJFQqLkRERCRUKi5irKamxneErKM2Gx6129CpzYZH7ZYZIisuzOxGM/ujme02
s52DPOZuM+vqdXssqoxxp1/CoVObDY/abejUZsOjdssM+RE+dwHwELAcuHoIx/0W+DvAkvf3hRtL
REREohRZceGc+zqAmV01xEP3OecaI4gkIiIiaZCJ51ycY2ZbzexVM7vdzMb7DiQiIiKDF+WwyHD8
FngEeAM4AbgVeMzM5jvnXB/HFAGsXbs2PQlzyK5du6irq/MdI6uozYZH7TZ0arPhUbsNTcrfzqIw
n9f6/pt9mJ3NbgW+0s8uDpjhnFufcsxVwBLn3JB7IMxsKrABWOice7aPfT4J3D/U5xYREZFulzvn
HgjryYbac/Ft4O4B9nl9mFkO4Zx7w8y2A9OAwxYXwBPA5cBGYG9Yry0iIhIDRcBxBH9LQzOk4sI5
twPYEWaA/pjZJGACsGWATKFVWyIiIjGzLOwnjHKei8lmNguYAuSZ2azkrSRln1fN7KLkv0vM7Jtm
doaZTTGzhcAvgPWEXFGJiIhIdKI8ofNm4MqU+wfOsHk/8Fzy3ycCY5P/7gROSR4zDqgnKCq+6pxr
jzCniIiIhGhIJ3SKiIiIDCQT57kQERGRLKbiQkREREKVlcWFFkUbuuG0WfK4m82s3sz2mNlTZjYt
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
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 0 Average Loss: 0.6958528945843379
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xt8XFW9///XJ/f0njY0oaWUcitQoJC0QKkgV/HCVRF+
oVwV0SN6OEWP/vSoR/0e5adHKaKieKoglOYoIgVE7hTway/ShEIpvUhpC21JryFN2vSSZP3+2JM0
SZPm0r1nzcx+Px+PedDZs3fmPYvJzCdr7bW2OecQERERCUuW7wAiIiKSWVRciIiISKhUXIiIiEio
VFyIiIhIqFRciIiISKhUXIiIiEioVFyIiIhIqFRciIiISKhUXIiIiEioVFyIiIhIqCItLszsLDN7
3MzWm1mLmV3aw/4fTuzX/tZsZiOjzCkiIiLhibrnYiCwGLgV6O1FTBxwDFCauB3qnNsUTTwREREJ
W06UP9w59zTwNICZWR8O3eyc2x5NKhEREYlSKp5zYcBiM9tgZs+a2Zm+A4mIiEjvRdpz0Q/vA58H
FgH5wOeAl8zsNOfc4q4OMLMRwEXAGmBXknKKiIhkggLgCOAZ59zWsH5oShUXzrmVwMp2mxaY2VHA
dOCGbg67CHgo6mwiIiIZbBowO6wfllLFRTf+AUw9wONrAGbNmsXxxx+flECZYvr06cyYMcN3jLSi
NusftVvfqc36R+3WN8uWLePaa6+FxHdpWNKhuDiFYLikO7sAjj/+eMrKypKTKEMMHTpUbdZHarP+
Ubv1ndqsf9Ru/RbqaQWRFhdmNhA4muAkTYAjzWwisM05956Z3QGMcs7dkNj/NmA1sJRgHOhzwLnA
hVHmFBERkfBE3XMxCZhLsHaFA36a2P574DME61iMabd/XmKfUcBO4A3gfOfcKxHnFBERkZBEvc7F
yxxguqtz7qZO9/8b+O8oM4mIiEi0UnGdC0mSiooK3xHSjtqsf9Rufac26x+1W2ow53q7KndqMrMy
oKqqqkon8YiIiPRBdXU15eXlAOXOueqwfq56LkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5E
REQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRE
RCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouRERE
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
0MfiwszuMLOWA9yazezYkDMaQdEhB6OmBnbs8J1CRCRaCxb4TiBAX6cP/AS4r4d93ulnlhqCQqKE
jr0XI4HXejp4+vTpDB06tMO2iooKKioq+hknwwwaFKx10dLiO4mISHSKinwnSFmVlZVUVlZ22FZX
VxfJc5lz0XYKmNkNwAzn3PBe7LsB+G/n3IzE/SEEhcb1zrmHuzmmDKiqqqqirKwsxOQZ6Ior4Ikn
dI0REck8WVlBYbF+PeTn+06TNqqrqykvLwcod86FdjZslOtcjDGzicBYINvMJiZuA9vts9zMLmt3
2F3At8zsEjM7CXgAWAc8FlXOWPnlL/eNR+bmBid4tr+1TlUdNCj4b07OvrUxBg7cd1xWVrA9K6vn
4wYMCFYGbT0uNze43/64wYP3P66wcN9xZvs+LLo6Ljd333H5+R2PKyzc/2e3P671JNe8vH35WnP3
dJzZvnZoPa61ndof19ouanO1udo8ujYvKICHH1ZhkSKiXFXp+wRTSVu1VkTnAq8k/n0M0DaW4Zz7
sZkNAO4FhgF/Az7mnNsTYc74GDUKliyBP/0JFi0KLsN+3XXBL+iDDwbnZUyaBJ/6FFRVweOPB49d
cQWcdFLwi7t4MYweHRy3ezfMmgWbN8OUKXD55TBvHjz5ZPALf+WVwTr/lZXw5pvB4jbXXQd1dTB7
NtTWwoc+BJdcAnPnwrPPBh+SV10FRxwBDz0Ey5fDUUfBtdcGq4xWVkJ9PZxzDnz0o8ExL74YfPhU
VARnis+aBW+/HTz3tGnw7rvwhz8EU3EvvBDOOy/I+MorwSyaa64J/jtrFqxZAxMmBNtWrgzaas8e
+PjHYepUeOyx4DUWFweZCgqCtlu/PrjU89VXB2386KNBD9GllwZt+sgjanO1udo86jY/5BBvH6/S
UeTDIlHTsIiIiEj/pN2wiIiIiMSTigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWK
CxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoL
ERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsR
EREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxEREQmVigsREREJlYoLERERCZWKCxER
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
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 1 Average Loss: 0.24844461282094318
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xl8VdW9///XJxMJCZBAJBFUBlFAVDSBVsS2DrWTFetQ
vQGVagdva3sttrXfb7+9tfq7t95qrdZ7a2u1dQJz1bYOVVvrgNrK0JKIVWRQEC1gmAkBwpBk/f7Y
h5CEBJKw91nnnP1+Ph7nAWefvXPeWTnJ+Zy19lrbnHOIiIiIhCXLdwARERHJLCouREREJFQqLkRE
RCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVCouREREJFQqLkRERCRUKi5EREQkVJEWF2b2
ETN70sxWm1mLmU05yP4fS+zX9tZsZoOjzCkiIiLhibrnohBYCFwNdPciJg44BihP3A53zq2LJp6I
iIiELSfKL+6c+xPwJwAzsx4cut45tzWaVCIiIhKlVDznwoCFZrbGzP5sZqf6DiQiIiLdF2nPRS98
AFwFLAD6AF8GXjKzDznnFnZ2gJkNAj4JrAR2JimniIhIJsgHhgPPOuc2hvVFU6q4cM4tA5a12TTP
zI4GZgDTuzjsk8CsqLOJiIhksGnAQ2F9sZQqLrrwN2DyAR5fCTBz5kzGjh2blECZYsaMGdx2222+
Y6QVtVnvqN16Tm3WO2q3nlm8eDGXXnopJN5Lw5IOxcVJBMMlXdkJMHbsWCoqKpKTKEMMGDBAbdZD
arPeUbv1nNqsd9RuvRbqaQWRFhdmVgiMIjhJE2CkmY0HNjnn/mlmNwFDnHPTE/tfA7wLLCIYB/oy
cAZwdpQ5RUREJDxR91xMAGYTrF3hgFsT2+8HriRYx+LINvvnJfYZAuwA/gGc5Zx7JeKcIiIiEpKo
17l4mQNMd3XOXdHh/i3ALVFmEhERkWil4joXkiRVVVW+I6QdtVnvqN16Tm3WO2q31GDOdXdV7tRk
ZhVATU1NjU7iERER6YHa2loqKysBKp1ztWF9XfVciIiISKhUXIiIiEioVFyIiIhIqFRciIiISKhU
XIiIiEioVFyIiIhIqFRciIiISKhUXIiIiEioVFyIiIhIqFRciIiISKhUXIiIiEioVFyIiIhIqFRc
iIiISKhUXIiIiEioVFyIiIhIqFRciIiISKhUXIiIiEioVFyIiIhIqFRciIiISKhUXIiIiEioVFyI
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
VhmtroaGBjj9dPjUp4JjXnwx+ONTVRWcKT5zJrzzTvDc06bB++/Dww8HU3HPPhvOPDPI+MorwSya
qVODf2fOhJUrYdy4YNuyZUFb7d4Nn/kMTJ4MTzwRfI+lpUGm/Pyg7VavDi71fMklQRs/9ljQQzRl
StCmv/ud2lxtrjaPus0PO8zbn1dpL/JhkahpWERERKR30m5YREREROJJxYWIiIiESsWFiIiIhErF
hYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWF
iIiIhErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWI
iIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiI
iIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxYWIiIiESsWFiIiI
hErFhYiIiIRKxYWIiIiESsWFiIiIhErFhYiIiIRKxUWMVVdX+46QdtRmvaN26zm1We+o3VJDZMWF
mX3PzF41s+1mtqmbx9xrZi0dbs9ElTHu9EvYc2qz3lG79ZzarHfUbqkhJ8KvnQs8AswFruzBcX8E
vgBY4v6ucGOJiIhIlCIrLpxzNwCY2fQeHrrLObc+gkgiIiKSBKl4zsXpZrbWzJaY2Z1mNtB3IBER
Eem+KIdFeuOPwO+Ad4GjgZuAZ8xsknPOdXFMPsDixYuTkzCD1NfXU1tb6ztGWlGb9Y7arefUZr2j
duuZNu+d+WF+Xev6PbuTnc1uAr57gF0cMNY5t6zNMdOB25xzPe6BMLMRwHLgLOfc7C72mQrM6unX
FhERkVbTnHMPhfXFetpz8RPg3oPss6KXWfbjnHvXzDYAo4BOiwvgWWAasBLYGdZzi4iIxEA+MJzg
vTQ0PSounHMbgY1hBjgQMzsCGAR8cJBMoVVbIiIiMTMn7C8Y5ToXR5rZeGAYkG1m4xO3wjb7LDGz
8xL/LzSzm83sw2Y2zMzOAh4HlhFyRSUiIiLRifKEzhuBy9vc33uGzRnAK4n/HwMMSPy/GTgxcUwx
sIagqPiBc25PhDlFREQkRD06oVNERETkYFJxnQsRERFJYyouREREJFRpWVzoomg915s2Sxx3o5mt
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
YII=
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 2 Average Loss: 0.12675620168447493
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xl8XXWd//HXJ3vStE3akARoaQvFClVLN2wtyiaKCxUU
YSKbMiPooOPUcXR+/pxxxvmNjBt1GRlZHoBsGUQFQUAWBXHoIiSUpZQWW1poS9I9S7c0yff3x7lt
b9IkTdJz7vfce97Px+M+2nvuOfd87jfn3vu539Wcc4iIiIiEJc93ACIiIpJblFyIiIhIqJRciIiI
SKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEioIk0uzOy9
ZvaAmW0ws24zm3+Y/U9P7Zd+6zKz6ijjFBERkfBEXXMxAlgGXAMMdhETB5wI1KZuRzvnNkUTnoiI
iIStIMond879DvgdgJnZEA7d7JxrjSYqERERiVIc+1wYsMzMNprZY2b2Ht8BiYiIyOBFWnMxDG8B
VwPPAcXAZ4GnzOxU59yyvg4ws7HAB4G1wJ4MxSkiIpILSoCJwKPOua1hPWmskgvn3CpgVdqmJWZ2
ArAAuKKfwz4I3BV1bCIiIjnsEuDusJ4sVslFP/4MzBvg8bUAd955JyeddFJGAsoVCxYsYOHChb7D
yCoqs+FRuQ2dymx4VG5Ds2LFCi699FJIfZeGJRuSi1MImkv6swfgpJNOYsaMGZmJKEeMHj1aZTZE
KrPhUbkNncpseFRuwxZqt4JIkwszGwFMJuikCXC8mU0Dtjnn3jSza4FjnHNXpPb/EvA6sJygHeiz
wJnAOVHGKSIiIuGJuuZiFvAkwdwVDvhBavvPgSsJ5rEYn7Z/UWqfY4BdwIvA2c65pyOOU0REREIS
9TwXf2SA4a7Ouc/0uv894HtRxiQiIiLRiuM8F5IhdXV1vkPIOiqz4VG5DZ3KbHhUbvFgzg12Vu54
MrMZQENDQ4M68YiIiAxBY2MjM2fOBJjpnGsM63lVcyEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKh
UnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFS
ciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJy
ISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIh
IiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEi
IiKhUnIhIiIioVJyISIiIqGKNLkws/ea2QNmtsHMus1s/iCOOcPMGsxsj5mtMrMrooxRREREwhV1
zcUIYBlwDeAOt7OZTQR+C/wemAb8CLjZzM6JLkQREREJU0GUT+6c+x3wOwAzs0Ec8nlgjXPuq6n7
K83sNGAB8Hg0UYqIiEiYIk0uhmEO8ESvbY8CCz3EkpPa2+Guu+C556CmBq64AszgttuguRlmzoS6
Oli0CH772+Cx88+HWbPgzjth2TI49lj49Kdhzx64/XbYsgXmzIGLLoInn4RHHoHCQvjEJ+Ad74A7
7oCXX4bjjoPPfAa2bw+ea8cOOO00+PjH4dFH4fHHoaQELr4YJk8OYlq5Eo4/Pjhu40a4+25oa4Mz
z4TzzgtifPJJKC8P4j722OC41athypTg9a1ZA/fcA7t3w/vfD+eeC/fdB3/6E1RUwCWXwNixcOut
sG4dTJ0Kl10GK1bAL38JHR3BMWedBffeC4sXB/tffjmUlQXnW78epk2DSy+Fxka4/37o6oKPfjR4
jfX1KvNcKfO6i7ooe/KhRBX62rKTs+I6Hz8+4x+p0h/nXEZuQDcw/zD7rAS+1mvbh4AuoLifY2YA
rqGhwcnA1q51bvx458ycKyhwLj8/+L9Z8P+CAufAuZKS4N+Cgp7b0o/Lyzt0n9LSQ7cVFwf77j8u
P39wxxUVHTxu/7+99ykrO3RbYWHP44qKBne+/fEVFASvc7DH5eX1LLvi4r6PU5nnRpkXscf9sfQD
iSr0X3OBK8zrjP11XlTk3MMP+/6UzT4NDQ2OoNvCDBfid745d9iuEKEws27gfOfcAwPssxK4xTn3
nbRtHwYeBEqdcx19HDMDaHjf+97H6NGjezxWV1dHXV1dWC8h6330o/C73wW/NERk6BZwHd/nK+Qd
vgtZTmijnFreYhdlxH1woRmMHh1U/JSW+o4mnurr66mvr++xraWlhaeffhpgpnOuMaxzxa1ZpAmo
6bWtGmjtK7FIt3DhQmbMmBFZYNmupQUefhgylEuK5KQr+DmD6JueM37LR9lFue8wBsW5oAXqscfg
Yx/zHU089fWDu7GxkZkzZ4Z+rriloouBs3tt+0BquxyBXbuUWIgcqZG0xu5DM0ptjCTbkqm2Nt8R
CEQ/z8UIM5tmZqekNh2fuj8+9fi1ZvbztEN+BpxgZt8xsylm9rfAhcB1UcaZBLW1QV8wERm+9YzP
sq/aIzOHxcBgBvrFx9y5viMQiL7mYhbwPNBAkP7+AGgE/i31eC1woH+vc24t8BHg/QTzYywA/to5
13sEiQxRe3tQeyEiw1fBDt8hZNQqpvgOYchWrfIdgUD081z8kQESGOfcZ/o5JvwGoIRra4Pubt9R
iGSbbtI/wkbSmmW/44/MVsYS/C7Mnle9ZYvvCATi1+dCIlJTE8wPICKDU8pOen9Ermecn2A8mcMS
simxAJg923cEAkouEmPv3uAmIoNzCXcxm6Xk03lgWxk7E9XnYhovMp/fkEf6+PV4l8DGjb4jEFBy
kRjbt2t+C5GhGM96HuIjfIZbKGYPALVsyrLf8Ufuf/gr/p4fMoJ2AIoYcFYA79av9x2BgJKLxKip
CWYcFpHBWcFJHMVWbuJqWhnFdio4huT9LC5lDz/gK+yggu1UcD73Eefai2nTfEcgEL9JtCQinZ2q
uRAZilJ2HejKWMQ+imjxHZJXBXRRQQudFPoOZUDt7b4jEFDNRWJs3Qr79vmOQiR7TGQdneT7DiN2
3qKWOHfyXL3adwQCSi4So6oKiop8RyESXwX0zL5XcwKFqLqvt6BpKL7NIlOyb2qOnKTkIiHy8oKF
fUTkUGXs5Cpu6DEqQrUWfcsj3hPmFKixPxaUXCTEpk0aiirSn/G8yXX8A1dyy4Ghp1NYRac+Ig8R
zPUR318qy5f7jkBAyUVijBmjjF6kP03UUkAnN3EV6xnHE5zN33AjBTH/le5DDZuIc7PIhAm+IxDQ
aJHEKCqCwsJg1IiI9LSbUjrJJ59uammmlmbfIcVWCXuIc83F2LG+IxBQzUViNDXB7t2+oxCJp0m8
TjEaTjUYbx5cazKWGht9RyCg5CIxKiogX/3TRPq0hSq6Y/xrPE6O5i3yY5yI1db6jkBAyUVilJZq
hk6R/rQwmo6YTw4VF5/lJrpiXFaTJvmOQEDJRWI0NcHOnb6jEImn41lDSczXzIiLD/A4/843MLrJ
owuL2VwgS5b4jkBAyUVilJdrnguR/Qrp6PGl2MJoj9Fkn2/wH6zmBBaygP/g/2IxGlVTWek7AgEl
F4kxciSMGOE7CpF4OI8HcGmTZG2imt0Ux3iAZfxMYi1/x0/4J76TWjE1HqU3darvCASUXCRGc7MW
9BHZ7+t8m0u5Awim/Z7Cq5SyV106h6GZGtoZRVyGpy5a5DsCAc1zkRjFxb4jEImPTgr5OZdzNTfw
APOpYIfvkLJWMfGa+re01HcEAkouEqOyEkaNgtZW35GI+NdMNQacxjOcxjO+w8lqlexgFC20xqT2
YtYs3xEIqFkkMTZvVmIhst+xbPAdQs7YTBWtjCYOiQWoWSQulFwkhEaKiBzk9NEXGotJR8798vSn
jQX9GRKiqipoFhER2MjRvkPIGVVsZRQtxGW0yNy5viMQUHKRGNu2qVlEZL8amnyHkDO2URmrZpGl
S31HIKDkIjH2xXcpAJEM6PmruojOmHwVZr99MZsKvEMTrcaCkouEqK4OJtISSZoKttP7V/V6xsWk
Ej/7VbOJkbQSl2aRefN8RyCg5CIxWluhrc13FCKZ90nu5Rr+C4C81JTfR7HJZ0g5pZVRtFFOXJpF
li3zHYGAkovE2LXLdwQifpTTzg/5ErfwGWbxHON5g1qaYvJVmP12UUacvkr0Iyoe4nNFSKRqa4PF
y0SS5llmUUA3n+E2ljKHN5jARN7wHVbOqKWJctqIS7OIRovEg5KLhGhvV+2FJNMJrInJ115uaqc8
VXsRj7qgVat8RyCg5CIx2tqgOz6rIotkTBVb6I7JF18uamMk3WkrzPq2ZYvvCASUXCRGTQ2UlfmO
QiR6weiQg3UVzzOdfNVdRKaGZspitOT67Nm+IxBQcpEYe/cGN5FcVsou/pOvEVTRB1V11TR7jSnX
7aWYvRQTl2aRjRt9RyCg5CIxtm+Hri7fUYhEq5LtXM1N3MYVTGQdAJN4HbUIRmc7lXTFaCKt9et9
RyCgJdcTo6YGSkpgzx7fkYhEp5kadlHCFdzO5dxOC6Mpp02/oiJUQzNj2cJWqnyHAsC0ab4jEFDN
RWJ0dqrmQnJfAZ3kpybKMqCCFgpUbxGpArr4P1zrO4wD2tt9RyCg5CIxtm7V+iKS+8aylWJ0oWfa
l7mOa/mn1OqoEPR38ZPUrV7t5bTSi5KLhKiqgqIi31GIRGsLVexBF3qmGfBPfIdmaljOydzKp/H1
9TJlipfTSi9KLhIiLw8sHp25RSLTTR4uJqMWkqiEvZzMCqrY6i2GAvUkjAUlFwmxaZOGokruq2YT
pehC920FJ5NHp5dzL1/u5bTSS0aSCzO7xsxeN7PdZrbEzPqd5sTMrjCzbjPrSv3bbWaauPoIjRmj
jF5yTxntFKT1sdjGGPZpEJx3x7GObk9/hwkTvJxWeok8uTCzi4EfAN8EpgMvAI+a2UDjllqA2rSb
LpcjVFQEhfEZii4Siiu5lc60ORY6KKIjRnMuJFUlO7yde+xYb6eWNJmouVgA3OCcu9059yrwOWAX
cOUAxzjn3Gbn3KbUbXMG4sxpTU2we7fvKETCdTH3cCOfpYTg4q6liRHoQvftRd7lrVmksdHLaaWX
SOutzKwQmAl8e/8255wzsyeAgRbGLTeztQTJTyPwdefcK1HGmusqKiA/X3NdSG7ZRiV/w818knt5
nHMwunHEZSLq5Kqh2dtiZrW1Xk4rvUTdKFYF5MMhk/s3A/0NGFpJUKvxIjAa+EdgkZlNdc5tiCrQ
XFdaGszQuXOn70hEwtPGyAOTZX2SX/oOR1Iu4D5G0Uo75RlPMiZNyujppB++RosY/Syh55xb4py7
0zn3onPuT8DHgc3AVZkMMNc0NSmxkNxzHG/6DkH6UM5OHmA+5anVUvMz2ESyZEnGTiUDiLrmYgvQ
BdT02l7NobUZfXLOdZrZ88DkgfZbsGABo0eP7rGtrq6Ourq6wUebw8rLg3kuXDxWRRYJRRvlagaJ
qdN5mvWM4z4uoIlafs7lvMJUov5rVVZG+vRZrb6+nvr6+h7bWlpa+tn7yJiL+NvGzJYAS51zX0rd
N+AN4MfOue8N4vg84GXgYefcV/p4fAbQ0NDQwIwZM8INPoc4B6NGad59yS13cCmXcpfvMGQQzuMB
fst5kZ9nzRo1jQxFY2MjM2fOBJjpnAutO2wmmkWuA64ys8vN7O3Az4Ay4DYAM7vdzA50+DSzfzaz
c8xskplNB+4iGIp6cwZizVnNzUosJPeM542+21cldt5kXEbOs2hRRk4jhxH5LCfOuV+k5rT4FkHz
yDLgg2nDS8dBjwa5SuBGgvkttgMNwNzUMFYZpuJi3xGIhG8vurCzRRm7CBYzi/Y3bWlppE8vg5SR
KdScc9cD1/fz2Fm97n8Z+HIm4kqSysqgWaS11XckIsNTw1u0UMEeitn/BdVMjfpbZIlLuJslzI28
pmnWrIhPIIOitUUSYvNmJRaS3T7MI9zM35CHo4B95NHFONarWSRLfJabOJsnAMink7y0advDpGaR
eNAk/AmhFVEl23WTxyXczSks42b+hg0cy0TW+g5LBqmIfTzCh/k1H+cB5rOTMu7n46GfJ08/mWNB
yUVCVFWpWUSy22Lm4ICpvMJCtZxmpQK6uIh7uYh7ccA7eYkVnBTqRFtzB5r7WTJGOV5CbNumxEKy
27v5s/pX5BADfsbnKKLjwMq2xpGvT7B06RE/hYRAyUVC7IumeVMkY4ro8B2ChOw0nuEFpvE5fsYc
FnEyr/Sx4Fn3kJ6zQ5dJLCi5SIjqahg50ncUIsP3DO9R580c9DZe4yf8HYuZx218hu5erfUzeL6f
6cP7vhrmzYsgSBkyJRcJ0doKbW2+oxAZvlN4Qc0iOW4WDVzOzwGHpWosvss/UkNzHwlG31fDsmXR
xiiDo+QiIXbt8h2ByJEZSZtqLhLgFq7kZ3yOGTRyHOt4Jy/xHLP4O37M8axmAq8PeLx+RMWDkouE
qK0NFi8TyRbjeJO8tA5+i5mjmosEyKebq7mR55jNOiZSzRaOponr+AdWM5mVvJ0KtvV5rNHN++aq
g1kcKLlIiPZ21V5I9ihgH9fzeYAD1eFTWOUzJImJYjq4lq8D6aNLugHHF/gJx616wltscpCSi4Ro
a4PuoXW6FvGmhD2cx0P8nrM5jf+lmD0cz2o1iwgAn+MG7uEipvEiRezlBNbwI77ED1kAW7b4Dk/Q
JFqJUVMDZWWqvZDs0E4526jgdP7IU5zpOxyJof2TcR1i9uzMByOHUM1FQuzdG9xEskE+XZSyW30s
ZOg2bvQdgaDkIjG2b4euI5/8TiQjythFKcqGZRjWr/cdgaDkIjFqaqCkxHcUIoPTxkh2MEp9LGTo
pk3zHYGg5CIxOjtVcyHZw3AU0qlmERm69nbfEQhKLhJj61atLyLZo5x2RqDexzIMq1f7jkBQcpEY
VVVQVOQ7CpG+jaKlx/TO7ZTThmZ9k2GYMsV3BIKSi8TIywNTHbPE1FXcQB7dPZbcdpj6XMjQFWiG
hThQcpEQmzZpKKrE1xk8xW/5KLU0A0GzyCja1OdChm75ct8RCJpEKzHGjAkS+s6+Vi4W8Wwz1VzB
z3mD43iW2XRQiKO/dS9FBjBhgu8IBCUXiVFUBIWFSi4knnYTjJMuoIu5LPEcjWS1sWN9RyCoWSQx
mppg927fUYj0bTxvqpZCwtHY6DsCQclFYlRUQH6+7yhE+raDSnXelHDU1vqOQFBykRilpZqhU+Kr
hVGquZBwTJrkOwJByUViNDXBzp2+oxDp23G8oZoLCccS9dmJAyUXCVFernkuJL7aGek7BMkVlZW+
IxCUXCTGyJEwYoTvKESgmiaq2Exe2oRZWxirZhEJx9SpviMQlFwkRnOz1vOReDiTp/glF1LCHvLo
opAOjmOdmkUkHIsW+Y5A0DwXiVFc7DsCkcBuSjmdp1nLRO7kUtYykXeiWRUlJKWlviMQlFwkRmUl
jBoFra2+I5Gke46ZOOAotrCAH/oOR3LNrFm+IxDULJIYmzcrsZB4eA+L1b9CoqNmkVhQcpEQGiki
cdGtjx2JUp6urzjQXyEhqqqCZhER3xYzR503JTpz5/qOQFBykRjbtqlZROLh3fxZzSISnaVLfUcg
KLlIjH37fEcgydWznqKIDk9xSCJ06PqKAyUXCVFdHUykJZJpU1lOPp0H7i9irppFJDrz5vmOQFBy
kRitrdDW5jsKSR7Hzfw1xeylgKD67BSeV7OIRGfZMt8RCEouEmPXLt8RSBIZjlN5lgZmcil3MIG1
TOUV32FJLtOvqFjQJFoJUVsbLF6mKcAlkxx5bOAYprCSW/lr3+FIEmi0SCyo5iIh2ttVeyE+OCrY
oWYQyZxVq3xHIGQouTCza8zsdTPbbWZLzGz2Yfb/pJmtSO3/gpl9KBNx5rK2Nuju9h2FJI3hGMlO
32FIkmzZ4jsCIQPJhZldDPwA+CYwHXgBeNTMqvrZfy5wN3ATcApwP3C/mZ0cday5rKYGysp8RyFJ
48hjI0drdIhkzuwBf7tKhmSi5mIBcINz7nbn3KvA54BdwJX97P8l4BHn3HXOuZXOuW8CjcAXMhBr
ztq7N7iJZFoZO9UsIpmzcaPvCISIkwszKwRmAr/fv80554AngP563cxNPZ7u0QH2l0HYvh26unxH
IUmTRxcVaGpYyaD1631HIERfc1EF5APNvbY3A7X9HFM7xP1lEGpqoKTEdxSSNN3k00SNmkUkc6ZN
8x2B4G8oqtF7TuAj3H/BggWMHj26x7a6ujrq6uqGHl0O6uxUzYX4Ucg+NYtI5mi8fb/q6+upr6/v
sa2lpSWSc0WdXGwBuoCaXturObR2Yr+mIe4PwMKFC5kxY8ZwYkyErVu1vohkioNUOmF0M5ZtfsOR
ZFm9WlOA96OvH9yNjY3MnDkz9HNF2izinNsHNABn799mZpa6v6ifwxan759yTmq7DFNVFRQV+Y5C
ct0I2sjnYBWZI4/NjPUYkSTOlCm+IxAyM1rkOuAqM7vczN4O/AwoA24DMLPbzezbafv/CPiQmX3Z
zKaY2b8SdAr9rwzEmrPy8sBUNy0Ru5JbKKSDvLQEo1tz9UkmFWji6TiI/F3vnPsF8A/At4DngXcB
H3TObU7tMo60zprOucVAHXAVsAz4OPAx55wWJDgCmzZpKKpE7z0s5mE+zDiCHvtGNzVsPsxRIiFa
vtx3BEKGOnQ6564Hru/nsbP62PYr4FdRx5UkY8YECX1n5+H3FRmuZqq5mHt4nUk8y2x2U5rWA0Mk
AyZM8B2BoIXLEqOoCAoLlVxItHYRTAObh+Pd/NlzNJJIY9XHJw7UGJoQTU2we7fvKCTXTWIt3aqn
EJ8aG31HICi5SIyKCsjP9x2F5LptjCFPU2aJT7WabzEOlFwkRGmpZuiU6G2nwncIknSTJvmOQFBy
kRhNTbBTK19LxI7ndTWLiF9LlviOQFBykRjl5ZrnQqLXxkhMzSLiU2Wl7wgEJReJMXIkjBjhOwrJ
JaPYwXjeII+DQ5CaqNGHivg1darvCAQlF4nR3Kz1fCRcp/EMv+RCytmJ0U0hHZzAarrULCI+Lepv
ZQnJJM1zkRDFxb4jkFyzm1JO5VnWMpE7uZS/MJkZPK/RIuJXaanvCAQlF4lRWQmjRkFrq+9IJFc0
Mp1uoIIdfFFL/0hczJrlOwJBzSKJsXmzEgsJ1xyWkoem9paYUbNILCi5SAiNFJGwabVTiaU8XZdx
oL9CQlRVBc0iImFZyql0g3pYSLzMnes7AkHJRWJs26ZmEQnXbJ5Ts4jEz9KlviMQlFwkxr59viOQ
7NezjqKIDk9xiAygQ9dlHCi5SIjq6mAiLZHhmsYL5HMwS13MHDWJSPzMm+c7AkHJRWK0tkJbm+8o
JJtdz+cpZycFqQRjGsvUJCLxs2yZ7wgEJReJsWuX7wgk203jRRqYyZXcwgTWMpVXfIckcij9iooF
TaKVELW1weJlmgJchms9x/I2XuMGPuc7FJH+abRILKjmIiHa21V7IUemgh1qBpH4W7XKdwSCkovE
aGuD7m7fUUg2G4WqmyULbNniOwJByUVi1NTAsWXb0ZRHMlzrOVZXj8Tf7Nm+IxCUXCRG/t5dfGvv
1wimPFIVhgxdGWpXkyywcaPvCAQlF8mxfTtXdt3EbVzBRNYBUEAHSjRksMawXX0uJP7Wr/cdgaDk
IjlqaqCkhCu4nTUcz3YqeID56BKQwdrI0b5DEDm8adN8RyDomyU5OjuhqwsIGkYqaOGDPMYpNJJP
p9/YJCsUojnkJQtovH0sKLlIiq1bD1lgJA/HY3yQj/JbLNU8kkeXj+gklno2mR2FeuFLFli92ncE
gpKL5KiqgqKiQzYfxRbu5wKaqWE5J3MBvz4wvbMkVym7yOs1NmQT1Z6iERmCKVN8RyAouUiOvDyw
/rvjHcUWTmYFX2YhXeTT81erBiAmzaXcwQh29mgy61Z3TskGBZp4Og6UXCTFpk2wd+9hd3sPi7mb
T1HJjrSt+lJJmtk8x+84lwmpkUUAR/OWx4hEBmn5ct8RCEoukmPMmEFn9H/FPbzF0TzNe3mYc9VM
kkBN1DKXxbzGiTzLLP7AmRTpOpBsMGGC7wgELVyWHEVFUFgYjBoZhGI6eC//C8Al3MWdXEqXLpfE
aGcEEHT6nUWD52hEhmDsWN8RCKq5SI6mJti9e1iH/oQvcg6P9dqqfhi5bDKr6dLHg2SjxkbfEQhK
LpKjogLy84d16EjaeYSP8ALv4nYu44v8MOTgJG62MpZ8zd4q2ai21ncEgpKL5CgthZKSI3qKd/ES
l3EnZ/IU6uSZ2zZTpb+wZKdJk3xHICi5SI6mJti5M5SneoFTyNOsnjltCqvo1MeDZKMlS3xHICi5
SI7y8gHnuRiK0eygm+E1sUh2aGXUIZNoiWSFykrfEQhKLpJj5EgYMSKUpzqR11CzSG7bwDFKLiQ7
TZ3qOwJByUVyNDeHtqBPIzMxNYvkNDWLSNZatMh3BIKSi+QoLg7tqUrYg6nmIqftoUQ1F5KdSkt9
RyAouUiOykoYNSqUp/ok9+L6TC70ZZSNCuhgPG/0WBF3LROUXEh2mjXLdwRCxMmFmVWa2V1m1mJm
283sZjMbsOHfzJ4ys+60W5eZXR9lnImweTO0tobyVJNYy/f5CgAF7Et9KTnUDyM7ncqz3MmlFLOX
fDrJo4u3sYou/T0lG6lZJBains/5bqAGOBsoAm4DbgAuHeAYB9wI/DMHv612RRdiQoQ0UmS/L7OQ
9/InbuPTbKGKP3AmW7Qkd1ZyGO/jT6xkCjdyFSuZwiksU82FZKc8VcjHQWTJhZm9HfggMNM593xq
2xeBh8zsK865pgEO3+Wc2xxVbIlUVRU0i4RUewHBypmzeQ6AM3iSP3IUqr3IPg3MoIs8xrGef+df
fIcjcmTmzvUdgRBts8hcYPv+xCLlCYKaiXcf5thLzGyzmb1kZt82M/XQOVLbtoWaWPT2FjUoschO
01lGPt2OpO50AAAXcklEQVT660luWLrUdwRCtM0itcCm9A3OuS4z25Z6rD93AeuAjcC7gO8CbwMu
jCjOZNgX7XLZnRRF+vwSnUItpS65pKPDdwTCMJILM7sW+NoAuzjgpIGeggGGFTjnbk67u9zMmoAn
zGySc+71/o5bsGABo0eP7rGtrq6Ourq6AUJJkOrqYCKttrZInn4cb7KG41HtRfZ5lll0kUeeai8k
F8yb5zuC2Kqvr6e+vr7HtpaWlkjONZyai+8Dtx5mnzVAE/Ts4Wdm+UAl0DyE8y0l+MaaDPSbXCxc
uJAZM2YM4WkTprU1ssQCYDNHRfbcEq2pvKIVUCV3LFsGEyb4jiKW+vrB3djYyMyZM0M/15CTC+fc
VmDr4fYzs8VAhZlNT+t3cTZBojCURrHpBDUdbw01VkmzK9oBN7spRbUW2aLnsOFywpm5VSQWIvwR
JYMXWYdO59yrwKPATWY228zmAT8B6vePFDGzY8xshZnNSt0/3sy+YWYzzGyCmc0Hfg780Tn3clSx
JkJtbbB4WUTGsx5NopUd3s6rFKT1s2hkuua0kNyh0SKxEPWA4E8BrxKMEvkt8DRwddrjhQSdNctS
9zuA9xMkJSuA7wH3AvMjjjP3tbdHWnuxg4rInlvC9T2+QhEd5KfWh5nIOvKVGEquWLXKdwRCxJNo
Oed2MMCEWc65dXBw7W7n3HrgjChjSqy2NuiOrl29lZGoWSQ7zGEpS5jDv/BvPMq5TGKN75BEwrNl
i+8IhOhn6JS4qKmBsrLIai/GsZ51TIrkuSVc6xnHKbzAfXzCdygi4Zs923cEghYuS469e4NbRHZR
hvpcZIcyduovJblr40bfEQhKLpJj+3bo6jr8fsO0lbGoWSQ7jGWb/lKSu9av9x2BoOQiOWpqoKQk
sqefSQP5mukxK2zgGN8hiERn2jTfEQhKLpKjszPSmouv8j3AsB6TManyPY4K6dRfRnJXu+ZtiQMl
F0mxdWuk64vMYSn3cz4TWJe2VZXv8dAzlahmk/4ykrtWr/YdgaDkIjmqqqAo2sXFPspDrOYEVnEi
DUzvVYshPhSyF+uVXDRT4ykakQyYMsV3BIKSi+TIywOL/vdqHo4T+QsTWYeaRfy7mHuoZNuBCbMA
uvW2l1xWoBkW4kCfMkmxaVOkQ1F7W80JuIPzo4kn01nGY3yAE3ntwLajtUyP5LLly31HIGgSreQY
MybI6Ds7D79vCMYdWGtErfs+beQYZvA8r3AyyziF7VRSwQ7fYYlERyuixoKSi6QoKoLCwowlF+W0
k0c33aq98KqNkQfSu+ks8xqLSEaMHes7AkHNIsnR1AS7d2fsdCuZosQiBqawkn36O0iSNDb6jkBQ
cpEcFRWQn7kvmWo2Zexc0r/NHEUB0c1vIhI7tbW+IxCUXCRHaWmkM3T2dhSbNWNnhpWwm9N5ioK0
cm+mWr1eJFkmaQHFOFBykRRNTbBzZ8ZO9won00Vhxs4ncDKvcBeXMJm/AJBPJ1N5hU69zSVJlizx
HYGgDp3JUV4ezHPhMjP3hEYkZN4OKjiWjbzMO/gd5/Iy7+ADPEq+JjOTJKms9B2BoOQiOUaOhBEj
Mjbv/gmsYTZLaWQmXbrMMuINjmMfBRTQyUd4mI/wsO+QRDJv6lTfEQhqFkmO5uaML+hzB5dTxRaM
bgrpALrRrJ3ReQcvU0in+lhIsi1a5DsCQTUXyVFcnPFTTmEVf2Ey9dTxMu/gFU7i97wfp6+/SOwh
cx12RWKrtNR3BIKSi+SorIRRo6C1NaOnLWcnn+VmAO7gEp7gAxk9f5Ks4sQDzSJK3ySxZs3yHYGg
ZpHk2Lw544lFb8t5B3macyEyU3lFzSIiahaJBSUXSZGBFVEPJ49u8jRyITTWK1FTc5MIwQrQ4p3+
CklRVRU0i3h0PvfT2efcF+rkORzzWNRjKfXlnMw+ClSakmxz5/qOQFBykRzbtnlvFjmVZ/kc1wOk
fSlq5dTh+i5f4URWpZqaHCerWUQEli71HYGgDp3JsS8eU3FfzzW8n99zG1ewjbEs4xR2McJ3WFmi
m/TfA9VsYSlzuJGreIDzOIkV/kITiYuODt8RCKq5SI7q6mAiLc8M+AS/5kE+xjOcxhReRc0ih1dN
E73frm8yjpG08RV+wNOcwQ183k9wInEyb57vCAQlF8nR2gptbb6jOMRmqlCzyOFdyl1cxu0E3TaD
TrFaeVakD8uW+Y5AUHKRHLt2+Y6gT3so8x1CViinnZv4a37G55hBI8exLjX7qYj0EMMfUUmk5CIp
amuDxctiZhxvomaRQ1WylfRyWcY0iunkam7kOWazjolUs8VfgCJxpdEisaDkIina22NZe7GDCt8h
xM5RbOKH/D1gByYdO451SsFEBmPVKt8RCEoukqOtDbrjN4FVG6NQn4ueKtnO5dzJb5jPTBooZg+T
WaPkQmQwtqhGLw40FDUpamqgrCx2tRfzeIaH+DBdfU6ulUyvM4m9FDGfB5nPg77DEckus2f7jkBQ
zUVy7N0b3GLm//IfGGjNkTTltFNAPOYlEck6Gzf6jkBQcpEc27dDV/y+wE/lWZ7g/cykATh0vYwk
qmYT+WoEERme9et9RyAouUiOmhooKfEdRZ9O52n+zLtpZSRrOL7HehlJUENTj5qKdUygQy2WIsMz
bZrvCAQlF8nR2RnLmot0I2lnIm9wJbf00UySu7/k/5HvYLgDr7mQfVo9VmS42tt9RyAouUiOrVtj
s77I4fwXX+Aa/oti9gCkZqTMpeSi52v5AE/wMB/mBFYDcAwbKVByITI8q1f7jkBQcpEcVVVQVOQ7
ikEpYh8/5u/ZRDXLOZmv8Z9k63DVInp2og36lPR8LW9Ry9n8npVM4TUm8zAfyqlUSiSjpkzxHYGg
5CI58vLAsusLehRtnMwKRrDTdyjDUsA+vsiPD6wFAnAOj3M8q3v0sehOvQ0NmMxqjmdtlqZSIjFQ
oP5KcaDkIik2bYrlUNTBWMdE8mM5imTg+oVqNvGf/B+u4acHkol38RKP8gFO4fkD+41jg5IJkbAs
X+47AiHC5MLMvm5mz5jZTjPbNoTjvmVmG81sl5k9bmaTo4oxUcaMydqM/jje6OcR340HPVOCsl7z
U2xjDA7jJ/wdGzmGJzibL/IjJrOGZ3k3LzOVJzibt7Ey04GL5K4JE3xHIERbc1EI/AL478EeYGZf
A74AXA2cCuwEHjWz7OgsEGdFRVCYnbNgfoZbKaAzVnNgTKeBCawlPy2ZuJJb6UybabSDIjpS949i
C2fzB45jw4HHp/IKZ/MHihI29FYkUmPH+o5AiDC5cM79m3PuR8BLQzjsS8C/O+cedM69DFwOHAOc
H0WMidLUBLt3+45iWMaxgfs5n9G0pm11DK6TZzS1G6fyLI9wLhNZd2DbxdzDjXyWEoJyrqWJEWRn
mYtkrcZG3xEIMVpbxMwmAbXA7/dvc861mtlSYC5BLYgMV0UF5OfHfq6L/pzLo2zkGB7nHNoYydf4
Dhs4loESjAI6UrNHDO0yL2IvXeT3OC6PLrrJP3C/mRpOYiWreBtPcQYbOJZ38iKn8Qyf5F4e5xyM
7kGnQCISktpa3xEI8erQWUvwM7O51/bm1GNyJEpLYztD52CVsof5PMgl3M01/BRLq5U4imbezis9
miku4L4DIzF6OnjccazlONb1mBX0Qu7tlZA4LuZ/euyzhkkA5OE4iye5jDsZTRsAFbTwSX7Jhfxa
iYVIpk2a5DsCYYjJhZlda2bdA9y6zOxtIcdo+O+5l/2ammBndg7p7MtX+D4Xci8Q1CrMYQn38XFq
U7lpPp1cwP1cz9+STydGd1qfjYNf+fNYxAPMZyxbDhz3V/wPP2ABeXRhdDOKFm7kat7Lnw7sM5fF
uihF4mjJEt8RCENvFvk+cOth9lkzzFiaCD71a+hZe1ENaeP2+rFgwQJGjx7dY1tdXR11dXXDDCfH
lJcHc11058bMj4V08gv+iga+y5OcyWRe4+2sZA3H8yDn8RcmM4clTGQtH+M33McF7KKUb/ItdjHi
wPPsoIJpvMg6JvIbPsZaJjKdZXyUh7iIe7mf8+kknxHs5A+cxf9yGouZy2z+rFoJkTiqrPQdQWzV
19dTX1/fY1tLS0sk5zLnov39ZWZXAAudc2MGse9G4HvOuYWp+6MIEo3LnXP39nPMDKChoaGBGTNm
hBh5DrrgAnjwwaztdxGGL/Jj/pvPH2j2KKSD9RzLWLaRrym3RbJXXl6QWGzYAMXFvqPJGo2Njcyc
ORNgpnMutN6wUc5zMd7MpgETgHwzm5a6jUjb51Uz+1jaYT8EvmFm55nZO4HbgfXAb6KKM1F++tOD
7ZGFhUEHz/Tb/qGq5eXBvwUFB+fGGDHi4HF5ecH2vLzDH1dWFswMuv+4wsLgfvpxI0ceelxp6cHj
zA5+WPR1XGHhweOKi3seV1ra47n/H99g+sjVBw7rzi/iIn5Jd1HJwfj2x907pvTz5ecHz7+/HPYf
t7+c0o/bXy4JLfM+yw6C4dEqc5V5WGVeUgL33qvEIiaiHC3yLYKhpPvtz4jOBJ5O/f9E4EBbhnPu
u2ZWBtwAVAB/Aj7knOuIMM7kOOYYeOkl+OUv4bnngmXYL7sseIPecUfQL2PWLPjEJ6ChAR54IHjs
ggvgne8M3rjLlsGxxwbH7d0Ld94JmzfD3Llw/vmwaBE89FDwhr/wwmCe//p6ePnlYHKbyy6Dlha4
+27Yvh1OOw3OOw+efBIeeyz4kLzoIpg4Ee66C159FU44AS69NJhltL4e2trgjDPg3HODY/7wh+DD
p64u6Cl+553wl78E577kEnjjDbjnHti9m9HnnMPis07kwYfg6aeDQTSf+tTpFFasDY5buxamToVP
fQpWrQrKqqMDPvxhmDcPfvOb4DVWVQUxlZQEZbdhQ7DU88UXB2V8331BDdH8+UGZ/upXiS1zzjkH
zjoriPFgoQf/qsxV5mGW+VFH+fp0lV4ibxaJmppFREREhifrmkVEREQkmZRciIiISKiUXIiIiEio
lFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiU
XIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRc
iIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyI
iIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiI
iEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRcJFh9fb3vELKOymx4VG5DpzIbHpVbPESW
XJjZ183sGTPbaWbbBnnMrWbW3ev2cFQxJp3ehEOnMhseldvQqcyGR+UWDwURPnch8AtgMXDlEI57
BPg0YKn7e8MNS0RERKIUWXLhnPs3ADO7YoiH7nXObY4gJBEREcmAOPa5OMPMms3sVTO73szG+A5I
REREBi/KZpHheAT4FfA6cAJwLfCwmc11zrl+jikBWLFiRWYizCEtLS00Njb6DiOrqMyGR+U2dCqz
4VG5DU3ad2dJmM9r/X9n97Gz2bXA1wbYxQEnOedWpR1zBbDQOTfkGggzmwSsBs52zj3Zzz6fAu4a
6nOLiIjIAZc45+4O68mGWnPxfeDWw+yzZpixHMI597qZbQEmA30mF8CjwCXAWmBPWOcWERFJgBJg
IsF3aWiGlFw457YCW8MMYCBmNg4YC7x1mJhCy7ZEREQSZlHYTxjlPBfjzWwaMAHIN7NpqduItH1e
NbOPpf4/wsy+a2bvNrMJZnY2cD+wipAzKhEREYlOlB06vwVcnnZ/fw+bM4GnU/8/ERid+n8X8K7U
MRXARoKk4l+cc/sijFNERERCNKQOnSIiIiKHE8d5LkRERCSLKbkQERGRUGVlcqFF0YZuOGWWOu5b
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
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 3 Average Loss: 0.11852103223403294
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xt83HWd7/HXJ/e06SVtaEIvlNJCKQUKvQihgFzEK1dB
OOEq7IqeRddTd9Vdj55dPXtkhZUurrILckCwEAVdEBREUATWXjgkVGjtBdtCSUPSW0iTpk2b5Hv+
+E3bJG2azPT3m+/M/N7Px2Me7fzm9/vNZ775zcxnvldzziEiIiISljzfAYiIiEhuUXIhIiIioVJy
ISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhijS5
MLNzzOwpM9tkZj1mdukg+38wsV/vW7eZjYsyThEREQlP1DUXw4HlwG3AUBcxccDxQFXidrRzbnM0
4YmIiEjYCqI8uXPu18CvAczMkjh0i3NuRzRRiYiISJQysc+FAcvNrNHMfmNmZ/kOSERERIYu0pqL
FLwHfBZ4DSgGPgP83sw+4JxbfqgDzGws8BHgbWB3muIUERHJBSXAscBzzrltYZ00o5IL59xaYG2v
TUvNbCqwALhpgMM+AjwSdWwiIiI57Drg0bBOllHJxQBeBeYf5vG3ARYtWsSMGTPSElCuWLBgAQsX
LvQdRlZRmaVG5ZY8lVlqVG7JWbVqFddffz0kvkvDkg3JxWkEzSUD2Q0wY8YMZs+enZ6IcsSoUaNU
ZklSmaVG5ZY8lVlqVG4pC7VbQaTJhZkNB6YRdNIEOM7MZgHbnXPvmtntwHjn3E2J/b8IbABWErQD
fQY4H7goyjhFREQkPFHXXMwFXiSYu8IB301sfwi4hWAei0m99i9K7DMe6ADeAC50zr0ccZwiIiIS
kqjnuXiJwwx3dc7d3O/+ncCdUcYkIiIi0crEeS4kTWpqanyHkHVUZqlRuSVPZZYalVtmMOeGOit3
ZjKz2UBdXV2dOvGIiIgkob6+njlz5gDMcc7Vh3Ve1VyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhI
qJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEio
lFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiU
XIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRc
iIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyI
iIhIqJRciIiISKiUXIiIiEioIk0uzOwcM3vKzDaZWY+ZXTqEY84zszoz221ma83spihjFBERkXBF
XXMxHFgO3Aa4wXY2s2OBXwK/BWYBdwP3m9lF0YUoIiIiYSqI8uTOuV8DvwYwMxvCIf8dWO+c+0ri
/hozOxtYADwfTZQiIiISpkiTixScCbzQb9tzwEIPseSk9nZ45BF47TWorISbbgIz+NGPoLkZ5syB
mhpYvBh++cvgscsvh7lzYdEiWL4cJkyAT38adu+Ghx+GrVvhzDPh6qvhxRfh2WehsBCuvBJOPhl+
/GNYsQKOOQZuvhlaWoJzvf8+nH02fPKT8Nxz8PzzUFIC11wD06YFMa1ZA8cdFxzX2AiPPgptbXD+
+XDJJUGML74IZWVB3BMmBMetWwfTpwevb/16+OlPYdcu+NCH4KMfhSeegFdegdGj4brrYOxYePBB
eOcdmDkTbrgBVq2Cn/0M9uwJjrngAnj8cViyJNj/xhth2LDg+RoaYNYsuP56qK+HJ5+E7m64+OLg
NdbWqsyzocwvnNuKLfqxCj2iQu+puY7nFo+I7DqfNCntH6kyEOdcWm5AD3DpIPusAb7ab9vHgG6g
eIBjZgOurq7OyeG9/bZzkyY5Z+ZcQYFz+fnB/82C/xcUOAfOlZQE/xYU9N3W+7i8vIP3KS09eFtx
cbDvvuPy84d2XFHRgeP2/dt/n2HDDt5WWNj3uKKioT3fvvgKCoLXOdTj8vL6ll1x8aGPU5lnfpkf
zxrXUlLpelTokRT6XgrcFSXPRHadFxU598wzvj9ls09dXZ0j6LYw24X4nW/ODdoVIhRm1gNc7px7
6jD7rAEecM59p9e2jwNPA6XOuT2HOGY2UHfuuecyatSoPo/V1NRQU1MT1kvIehdfDL/+dfBDQ0T6
eolzOYvFFKA3SBR+yF9yK/cBQ2khT54ZjBoVVPyUlkbyFFmvtraW2traPttaW1t5+eWXAeY45+rD
eq5MSy5eAuqcc1/qte3TwELnXPkAx8wG6urq6pg9e3bIUeeO1lYoL4c0/blFssrRNNLIBN9h5LRz
eJk/cBaO/Eif58kn4bLLIn2KnFJfX8+cOXMg5OQi0+a5WAJc2G/bhxPb5Qh0dCixEBlIGe2+Q8h5
OxgZeWIBQVcV8S/qeS6Gm9ksMzstsem4xP1JicdvN7OHeh3yH8BUM/uOmU03s78CrgLuijLOOKiq
CvqCicjB1jGV3RQPPl5eUjaJd9PyPNXVaXkaGUTUNRdzgdeBOoIOI98F6oFvJh6vAvb373XOvQ18
AvgQwfwYC4C/cM71H0EiSWpvD2ovRORgY9lGEZ0R9QYQgPcZxRCmOzpia9dG/hQyBFHPc/ESh0lg
nHM3D3DMnCjjiqO2Nujp8R2FSGYqpyXj2ohzzQ5GEVVnzt62bo38KWQI9H6KicrKYKi6iBxsA1Po
pMh3GDntbP6LAvZG/jzz5kX+FDIESi5iorMzuInIwcpoT8sXX5x9ibsoppN8unptDb+ZpLEx9FNK
CpRcxERLi+a3EBnIODaTr+6ckZrGOl7hHM7hlV5bw28maWgI/ZSSAiUXMVFZGcw4LCJQSVOfmop3
mMyejFsNIfecznJe5ALaGc4WxlLAQfMiHrFZs0I/paRAyUVMdHWp5kJkny/zHQxHXmI2zkL2kod6
PKfLcDooYi89EXwFtWvKkoyg5CImtm2DvWpSFgHgw7zAM3ycqawDYDyNFCi5SKtGxtMTQW3RunWh
n1JSoHrAmKiogKKiYOFDkbh7jyou4gXWMJ11TCWPbhzpGCgp+0xgE/l00R3y19D06aGeTlKk5CIm
8vKChX1EhP3V8UbQ0VDSL2iGCr8TbYG+1TKCmkViYvNmDUUV2WcCjaql8OxdJtFNYejnXbky9FNK
CpRcxMSYMcroRfbZQoUGnnpWRdP+DrVhmjw59FNKCpRcxERRERSG/yNBJCvtokQ1F56VsqvfhFrh
GDs29FNKCpRcxERTE+za5TsKEV/61lMcg2Za8m0DU9hLcejnra8P/ZSSAiUXMTF6NOTn+45CxIeD
G0BaKFeziGcVbMUiGP5bVRX6KSUFSi5iorRUM3RKPM2mjpHs6NO+v4MRahbxbBStFEYwQ+eUKaGf
UlKg5CImmppg507fUYik33m8xBNcThntgCOfLo5ho++wYm89x7GH8H/xLF0a+iklBRo/EBNlZcE8
F051wRIz7zOa8/k9DUzkCa6giSqOYaMmzfJsFK2RnLe8PJLTSpKUXMTEiBEwfLjm3Zf4WcWJGDCC
dm7kx77DkYRxbKaYXXRSQphp3syZoZ1KjoCaRWKiuVmJhcTTGbxKt+ooMs46ptJJKWHXHy1eHOrp
JEVKLmKiOPwRXyJZYTcl5GlsSMYpJZqx8aWlkZxWkqTkIibKy2HkSN9RiKRfPaer3iIDTWATJewi
7PVF5s4N9XSSIiUXMbFlC+zY4TsKkfQ7g1fpUXqRcTYwhd1qFslZSi5iQiuiSlw5JRYZKS+CCbQg
WAFa/NOfISYqKtQsIvG0jA9g6nORcSbzTiTNItXVoZ5OUqTkIia2b1eziMTTPF5TapGB3mVSJM0i
y5aFejpJkZKLmNi713cEIn4UshdNl5V59lAUzXnDn1FcUqDkIibGjQsm0hLJdZPZ0GcdkaWcoaGo
Geg41lMcQbPI/Pmhnk5SpOQiJnbsgLY231GIRGskrfxf/oI8esgnqK47jT8qtchATVRFMonW8uWh
nk5SpOQiJjo6fEcgEr1hdHAhL7KUM/kkTzCJjZzIat9hySG0UxbJefUjKjNobZGYqKoKFi/TFOCS
y5qooo0yZlPPY1zjOxw5jKmso5jddFJMmLUXGi2SGVRzERPt7aq9kNxXRjvD6FD3zSywjbF0UkTY
zSJr14Z6OkmRkouYaGuDnmjmrBHJGCNoIz+iyZkkXC2UE8VX0NatoZ9SUqDkIiYqK2HYMN9RiESr
mUraGaYOnFlgChsoojP0886bF/opJQVKLmKiszO4ieSyYjopplPNIlmgnTL2RtDtr7Ex9FNKCpRc
xERLC3R3D76fSDYrp4VCdKFng82Mw5Ef+nkbGkI/paRAyUVMVFZCSYnvKETCdRTNFHBg+tlmKulA
F3o2mMw7FBD+dJqzZoV+SkmBkouY6OpSzYXkni+xkAK69s/IWUAX+aq5yAp7KaQngq8gDbfPDEou
YmLbNq0vIrnnHF7mBT60f6KssWyjGF3o2aCR8fRE0Odi3brQTykp0CRaMVFRAUVFWtRHcksj47mK
n7OCk9nAFHoSi6urQ2fmm8AmStiVWBk1PNOnh3o6SZFqLmIiLw9Mn7iSY/ZVqxtwHBuYxnolFlli
BO3cyr19FpkLQ4F+MmcEJRcxsXmzhqJK7plIg5KJLHYHX+UWHiCfrl5bj2wStJUrjywmCUdakgsz
u83MNpjZLjNbamYDTnNiZjeZWY+ZdSf+7TEzTVx9hMaMUUYvuWczlZowK4sVs4cfcisNTOQFLuSb
fIMjbdSaPDmc2OTIRP51Y2bXAN8FbgVeBRYAz5nZCc65gSZqbQVO4MBVps+PI1RUBIWFwagRkVyx
mxLVXOSAKpqpopmtjOVIk4uxY8OJSY5MOmouFgD3Ouceds6tBj4HdAC3HOYY55zb4pzbnLhtSUOc
Oa2pCXbt8h2FyJHq+ztjEu96ikOi8Cdm9msiSV59fUjByBGJNLkws0JgDvDbfduccw54ATjcwrhl
Zva2mW00syfN7KQo44yD0aMhP/zJ8ETSrO+v2u2Uq1ozh4yjme4jnLWzqiqkYOSIRF1zUQHkA839
tjcDA10CawhqNS4FriOIcbGZTYgqyDgoLdUMnZLdprOKo2gmr9cv2zZGqFkkh4ynkSNtFpkyJZxY
5Mj4Gi1iDNCPwjm31Dm3yDn3hnPuFeCTwBaCPhuSoqYm2LnTdxQiqfsgL/MUlzKaVgDy6eIYNYvk
lD9yWp/kMRVLl4YUjByRqDt0bgW6gcp+28dxcG3GITnnuszsdWDa4fZbsGABo0aN6rOtpqaGmpqa
oUebw8rKgnkunOqQJUu9z2jO5FXeZRJPcAWbmMCJrNKkWTlkNO9zpH/N8vJwYslFtbW11NbW9tnW
2toayXOZi/jbxsyWAsucc19M3DdgI/A959ydQzg+D1gBPOOc+9tDPD4bqKurq2P27NnhBp9DnIOR
IzXvvmSvGaxkJScrkchh71HFMWykiwL6JhlDTyHXr1fTSDLq6+uZM2cOwBznXGjdYdPRLHIXcKuZ
3WhmJwL/AQwDfgRgZg+b2bf37Wxm3zCzi8xsipmdDjwCTAbuT0OsOau5WYmFZLf5LFZikeOOpokH
uZl8usmni8L9q6YO/S+/eHE0sUlyIp/nwjn3mJlVAN8iaB5ZDnyk1/DSidCnka0cuI+gw2cLUAdU
J4axSoqKi31HIHJkdoW8BoVkput5hHN4hUVczxaO4nGuopEJDDXBKNVlkhHSMmejc+4e4J4BHrug
3/0vAV9KR1xxUl4eNIvs2OE7EpHUvMYc9a+Iicls5H8SVGgv57REcjE0c+dGFZUkQ2uLxMSWLUos
JLudxRIlFjHUkEStBahZJFMouYgJrYgq2advZ/MefVzFUl6SC5nl6TLJCPozxERFRdAsIpItTuf1
PlNBL+FMzcYZQ+N5j2SWl6o+3NzPkjZKLmJi+3Y1i0j2KGY3D3EjI2jbn2BUq1kklt6jkmSaRZYt
iy4WGTotwh0Te/f6jkBk6PLo4RRW8gan8n0+zyucw1xe8x2WeNBNYVL779kz+D4SPSUXMTFuHIwY
AW1tviMRGdwuhrGZCibSwHf4O9/hiEeX8hTf46/pPujr6tBjh+bPT0tYMgg1i8TEjh1KLCR7FLKH
MbSoGUT4MndSSfMhlmI/9NWxfHn0McnglFzEREeH7whEhq6IPRTQ7TsMyQBH08RrzOWv+R7HsY7J
bDjs/voRlRmUXMREVVWweJlINthJGVsZo9EhAgQJxl38DeuYxhpOZDTbD7mf0cO51epglgmUXMRE
e7tqLyR7FLCXEbSpWUQOUswebudrANj+2q0ewPF5/o1j1r7gLTY5QMlFTLS1QU9yc9GIpNmBeooS
dlOMfoHKoX2Oe/kpVzOLNyiik6ms526+yL+yALZu9R2eoNEisVFZCcOGqfZCMtN4NtFEFT3kA9BO
GdsZTTnvq/ZCDulqHudqHj/4gXnz0h+MHEQ1FzHR2RncRDLRAu5iLNv2jwjIp5tSdimxkOQ1NvqO
QFByERstLdCtzveSoWawisWcxcd4ljy6GUYHpSgblhQ0NPiOQFByERuVlVBS4jsKkUNrYBJTWcfT
XEo7ZWxivO+QJFvNmuU7AkF9LmKjq0s1F5K5CjkwZ3Mpuz1GIlmvvd13BIJqLmJj2zatLyKZq5Jm
9a+QcKxb5zsCQclFbFRUQFGR7yhEDu09jtaEWRKO6dN9RyAouYiNvDww/TSUDHAqy6lmMQW95rHo
0UeRhKVArf2ZQO/omNi8WUNRJTOczEqe5HI+yEv7t01kk5pFJBwrV/qOQFCHztgYMyZI6Lv6Lywo
kmYbOYZxbOEFLuItpvEOk6lmse+wJFdMnuw7AkHJRWwUFUFhoZIL8W8LFfv/fzx/5nj+7DEayTlj
x/qOQFCzSGw0NcGuXb6jEIE51PsOQXJZva6vTKDkIiZGj4b8fN9RiEAzlb5DkFxWVeU7AkHJRWyU
lmqGTskM65miYacSnSlTfEcgKLmIjaYm2LnTdxQicCbLNDJEorN0qe8IBCUXsVFWpnkuxI88+s47
/z6jPUUisVBe7jsCQclFbIwYAcOH+45C4uhint6/lDrAm5ysZhGJzsyZviMQlFzERnOz1vOR9DN6
eJCbOZ3XgWCBsnN4Rc0iEp3FmjMlE2iei5goLvYdgcSRwxhGB0uo5mku4WXO5QyW+Q5Lcllpqe8I
BCUXsVFeDiNHwo4dviOReDGaqeQY3uUKnuQKnvQdkOS6uXN9RyCoWSQ2tmxRYiHpZ/QwnkY1g0j6
qFkkIyi5iAmNFBEfHAZKLSSd8vS1lgn0V4iJioqgWUQkvYxNjNfoEEmf6mrfEQhKLmJj+3Y1i4gP
jqN5T3UXkj7L1GE4Eyi5iIm9e31HIPFxYNIsw1HQbxItkUjt2eM7AkHJRWyMGxdMpCUSpemsAg6s
kOfIo4EJahaR9Jk/33cEgpKL2NixA9rafEchue4L/BvVLE5M+e0Axzg2q1lE0mf5ct8RCEouYqOj
w3cEEgflvM9zXMQ/8XVO4k9MYT0ldPoOS+JEv6IygpKLmKiqChYvE4nSeqYwgg7+nn9mJSeznmmq
tZD00miRjKDkIiba21V7IdGrYKv6V4hfa9f6jkBIU3JhZreZ2QYz22VmS81s3iD7f8rMViX2/6OZ
fSwdceaytjbo6fEdheS6UexQciF+bd3qOwIhDcmFmV0DfBf4B+B04I/Ac2ZWMcD+1cCjwA+B04An
gSfN7KSoY81llZUwbJjvKCTXbeBYNYOIX/MO+9tV0iQdNRcLgHudcw8751YDnwM6gFsG2P+LwLPO
ubucc2ucc/8A1AOfT0OsOauzM7iJRGkE6kwnnjU2+o5AiDi5MLNCYA7w233bnHMOeAEYqNdNdeLx
3p47zP4yBC0t0K25jCRiR7EVtb6JVw0NviMQoq+5qCCYUae53/ZmoGqAY6qS3F+GoLISSkp8RyG5
p28Pi40co17i4tesWb4jEKDA0/Ma/T+VjnD/BQsWMGrUqD7bampqqKmpST66HNTVpZoLCddMVnAy
K3icT9GTmJWzEE29LJ61t/uOIGPV1tZSW1vbZ1tra2skzxV1crGVYKGByn7bx3Fw7cQ+TUnuD8DC
hQuZPXt2KjHGwrZtWl9EwnUc63mQmxlFKw9yM3spYgKbcGiRdfFo3TpNAT6AQ/3grq+vZ86cOaE/
V6Q1mM65vUAdcOG+bWZmifuLBzhsSe/9Ey5KbJcUVVRAUZHvKCSXrOUEStnNvXyOzYxjJSdxGb9Q
s4j4NX267wiE9DSL3AU8ZGZ1wKsEo0eGAT8CMLOHgQbn3NcS+98NvGRmXwJ+BdQQdAr9TBpizVl5
eWD6OSkh6ur18TGaVkYTTfWqSFIKfLX2S2+R/8hwzj0G/A3wLeB14FTgI865LYldJtKrs6ZzbglB
QnErsBz4JHCZc+5PUceayzZv1lBUCddJ6C0pGWjlSt8RCGnq0Omcuwe4Z4DHLjjEtp8DP486rjgZ
MyZI6Lu6fEciuWIjx/gOQeRgkyf7jkDQ2iKxUVQEhYW+o5Bcso0xmupbMs/Ysb4jEJRcxEZTE+za
5TsKySWns1yjQiTz1Nf7jkBQchEbo0dDfr7vKCSbFdFJ7+lmmg8aMS6SAao032ImUHIRE6WlmqFT
jsy1PIr1Si7eZrKaRSTzTJniOwJByUVsNDXBzp2+o5Bs9q98kat4HIA8ujmDZWoWkcyzdKnvCAR/
039LmpWVBfNcOP3UlBTtoYjH+G/UcQcvcj7TeMt3SCIHKy/3HYGg5CI2RoyA4cM17b6kbhsVVLCN
OdQzB3Wakww1c6bvCAQ1i8RGc7MSCzkyE3lXzSCS+RYPtLKEpJOSi5goLvYdgWS7vWhxGskCpaW+
IxCUXMRGeTmMHOk7Cslm71Gl0SGS+ebO9R2BoOQiNrZsgR07fEch2aVvKjGRBjWLSOZTs0hGUHIR
E1oRVZLjMHr6bdNFJFkgT19rmUB/hZioqFCziAzdyazA0XdK1wYmqFlEMl91te8IBCUXsbF9u5pF
ZOj+gvu5lkeAYMIsgPE0qu5CMt+yZb4jEDTPRWzs3TvQIw5Vd0t/xezhR9zEJ/gVi7iOHYxiGFr5
TrLAnj2+IxBUcxEb48bBKSM27P8VCjCaFg6dWKjyO+7WcjyFdHMttTzDxfwX51DEgBmqSOaYP993
BIKSi9iwHa3c3fYX5NFDfuJL4hp+ym18H6BX0tG/E5/E0STe1ZUg2Wn5ct8RCEou4qOjg/N5kaWc
ySd5gkls5ERW8z2+wAPczFxeYxIbGcUO1Ewiw+mgR9eBZKO2Nt8RCEou4qOqCsrKmEM9j3ENG5nM
/+Bu8oCb+RHLOJONTOYvuZ98ug5xAjWVxMlajqdAf3PJRhotkhGUXMRFezt0dAy62wIWUk4LBX3a
19XpM27GsVnNIpKd1q71HYGg5CI+2tqgZ/Cviwk0sowzuIafUEYbw2lHiUX8lPM+Pfp4kGy0davv
CAQlF/FRWQnDhg1p1+PYwCJupI2RbGcM5WyPODjxraDfSJA/M5V81V1INpo3z3cEgpKL+OjsDG5J
KmIv/8A3E/d6t8GrPT5XnMAa/obv0vtvGnTsFclCjY2+IxCUXMRHSwt0dw++3yH8Nd/jP/gsE2kA
oJA9h1h3QrLVBDbxbb7GP/N3VLAFgIkaiirZqqHBdwSCkov4qKyEkpKUDjXgs9zHRo6hhdEs4tqD
1p2Q7PUnTgIcX+UOmqlkO+XcwI/1F5bsNGuW7wgEJRfx0dWVcs3FPgaMppUr+AUnsGb/ZFyS3UrY
vf+DIA9HOe/rg0GyV3u77wgEJRfxsW3b4RYYSUohXbzI+XyY5/c3jxhHlriIP8ex3ncIIuFZt853
BIKSi/ioqICiotBON573eIZP8B5H8ydmMIc61MkzO73F8frLSe6YPt13BIJWRY2PvDyw8OerqGQz
lWymgG40H0Z26lbvCsklBfpaywSquYiLzZtTGoo6VI0cHdm5JVonslppoeSOlSt9RyAouYiPMWMi
zegr2IqaRbLTRo7xHYJIeCZP9h2BoOQiPoqKoLAwstOXshs1i2SnVkZpTgvJHWPH+o5AUHIRH01N
sGtXZKdvYGJk55ZoncwKfRBI7qiv9x2BoOQiPkaPhvzoOu6N5n3ULJIditndZ4bVZio9RiMSsqoq
3xEISi7io7Q05Rk6h2IEO1CzSHa4lkf63N/EBLr1t5NcMWWK7wgEJRfx0dQEO3dGdvp3mRTZuSVc
t/P33MRDAOTRzWzqyFetk+SKpUt9RyBonov4KCsL5rlw0XyJlNFO0CyiX8CZbhelPMAtLGAhz3MR
E3nXd0gi4Skv9x2BoOQiPkaMgOHDI5t3fyzbIjmvhG8rFUxmI6fyJqfypu9wRMI1c6bvCAQ1i8RH
c3OkC/oEzSKqtcgGx7BRfynJXYsX+45AUHIRH8XFkZ5+OB1otEh22EO014KIV6WlviMQlFzER3k5
jBwZ2emv4xHyNBVTVmiiUmmg5K65c31HIEScXJhZuZk9YmatZtZiZveb2fBBjvm9mfX0unWb2T1R
xhkLW7bAjh2Rnf6L3E01SwDIp4t8wlneXcI3kQY1i0juUrNIRoi6Q+ejQCVwIVAE/Ai4F7j+MMc4
4D7gGxxoxO+ILsSYiGBF1N5K2c3vuIDH+RTP8HHaGc5TXB7pc0pqelRhKbksT9d3JogsuTCzE4GP
AHOcc68ntn0B+JWZ/a1zrukwh3c457ZEFVssVVQEzSIR1l4UsZfreJTreJRujBI66aIAdfTMLI1M
4Gia9FeR3FRd7TsCIdpmkWqgZV9ikfACQc3EGYMce52ZbTGzN83s22amHjpHavv2SBOL/lYzgy4K
UWKReY6mUX8VyV3LlvmOQIi2WaQK2Nx7g3Ou28y2Jx4byCPAO0AjcCpwB3ACcFVEccbD3vT2gdhL
dCuwSnIdDf0LAAAWuUlEQVSMbhwH1pUpoMtjNCIR27PHdwRCCsmFmd0OfPUwuzhgxuFOwWHGLDrn
7u91d6WZNQEvmNkU59yGgY5bsGABo0aN6rOtpqaGmpqaw4QSI+PGBRNptbWl5elmsoIC9qpZxLOJ
bKSBY/psa2Ai49iiv4rkpvnzfUeQsWpra6mtre2zrbW1NZLnSqXm4l+ABwfZZz3QBIzrvdHM8oFy
oDmJ51tG8O00DRgwuVi4cCGzZ89O4rQxs2NH2hILgA0cl2gWEZ9u4QHeYBa/4LJERp/HUUosJJct
Xw6TJ/uOIiMd6gd3fX09c+bMCf25kk4unHPbYPC5ns1sCTDazE7v1e/iQoJEIZlGsdMJajreSzZW
6aUjvQNu2ilL6/PJoY2gnUep4X4+wwPcwnbGUM77vsMSiU4af0TJwCLr0OmcWw08B/zQzOaZ2Xzg
34DafSNFzGy8ma0ys7mJ+8eZ2dfNbLaZTTazS4GHgJeccyuiijUWqqqCxcvSZCYrKdBcF96t5CRK
6eQLfJ/Xmc07HMsIopsGXsQ7jRbJCFEPCL4WWE0wSuSXwMvAZ3s9XkjQWXNY4v4e4EMESckq4E7g
ceDSiOPMfe3taa29eI+j1SySAcbTqHlTJV7WrvUdgRDxJFrOufc5zIRZzrl34EA3dudcA3BelDHF
Vlsb9KTva2YrFWl7LhnYGFroJk9Ts0t8bN3qOwJBa4vER2UlDBs2+H4hmcEq8jXk0bvVTKdQiYXE
ybx5viMQlFzER2dncEuT9xlNty4v78pp0SJlEi+Njb4jEJRcxEdLC3R3p+3pGhmPLi//qmimq9cE
WiI5r6HBdwSCPv3jo7ISSkrS9nQnsJY80pfMSKD/CJ23mEaB/g4SJ7Nm+Y5AUHIRH11daa256KSY
Hk3VlFZHsZkv8D2sVx+LEnZ7jEjEg3YNtc4ESi7iYtu2tK4v8g6T0eWVXpN5hzv4Kl/mTkrpSGzb
SLeSPImTdet8RyDo0z8+KiqgqChtTzeFDX1+QUv0NjCFPHr4Dn/HZsaxkpP4DPdRoC6dEifTp/uO
QIh4ngvJIHl5YOn7BRvMq6AvtXTqIW9/iZexk5NY5TUeES8K9LWWCVRzERebN6d1KOo6pvZZ5lui
N5V15Cuhk7hbudJ3BIKSi/gYMyatGf1EGlDNRXo1MFElLqIVUTOCkou4KCqCwvSt9VFGu6acTrN2
yujRW1ribuxY3xEISi7io6kJdu1K29OtYTo9ahZJq+msIV8JncRdfb3vCAQlF/ExejTkp+/Lfhyb
0/ZccVXCrj4TlW1mnMdoRDJEVZXvCAQlF/FRWprWGTqP4V0u5IWDZoyU8NTwaJ/aoS0cxV7VFknc
TZniOwJByUV8NDXBzp1pfcqHuIlp/Bmg1wqp6nIYlq/zT/wV3wcgj25O5k0KNdW3xN3Spb4jEDTP
RXyUlQXzXLj0fblPoJEVnMyv+SgrOJnXmMPP+FTanj/X7WQ43+cLfJ4f8CwfYyxbfYck4l95ue8I
BCUX8TFiBAwfnvZ59/Pp4RM8wyd4hoe4gZ9xdVqfP5dtI+gVP4PVzGC152hEMsTMmb4jENQsEh/N
zd4X9FnBKeTtbx6R5PWtdZrEu1o1RKS/xYt9RyAouYiP4mLfEVDCLpwuuZRZv+RiD8XqwSLSX2mp
7wgEJRfxUV4OI0d6DeEE1iq5SNGJh1gnpJlKD5GIZLi5c31HICi5iI8tW2DHDq8hrOTkPvMyyNB9
kv/kO3wFgAL2kkc3E2hQs4hIf2oWyQjq0BkXaVwRdSB59JBHj2buTIHD+Bvu4jxe4kd8mq1UUME2
32GJZJ48/WbOBEou4qKiImgW8Vh7cTlPcjtfO8QjDvQb/LBe53TycMzjNebxmu9wRDJXdbXvCAQ1
i8TH9u3em0U+wP/jc9wD9J9US4nFYGbxR3pUTiKDW7bMdwSCkov42JsZ03Dfw238jCv5GM9wFn9g
GB2+Q8oKhezVyBCRodizx3cEgpKL+Bg3LphIyzMDruQ/eZrL+ANnM53VaErwgx1NI9ZrhdN6Tidf
5SQyuPnzfUcgKLmIjx07oK3NdxQH2UIFahbp62gauY9bMdz+hd9msEqLqYsMxfLlviMQlFzER0dm
Nj/sZpjvEDJA3xqJMtq5mF/xX5zNxTzNJDZyoqb3FhmaDPwRFUdKLuKiqipYvCzDXMRvYr8s+3RW
9+rgCuuYym6KOZOlPMGVbGQyf8kDerOKDIVGi2QEfV7FRXt7RtZefJ3/QxF7+ny5xs0/8o+U07I/
yRrLNoroVGORSCrWrvUdgaDkIj7a2qAn81rtT2IVSzmTS3iKUjoow+9wWR9OYhXLOINr+AlltDGR
d/XGFEnV1q2+IxA0iVZ8VFbCsGEZWXtxCit4gisB2E45R/Mee/C/0Fq6vMtEPsGzLOJG36GIZL95
83xHIKjmIj46O4NbhhtDCwtYyMHDU3N3GOYwOnL41YmkWWOj7wgEJRfx0dIC3dmxaNi3+Rr/zN9R
wRaARP+D7Ih9aPqmEhVsU/8KkbA0NPiOQFByER+VlVBS4juKIcnD8VXuoJlKtlPOnfwtuXKp5rOX
/vN6NDDBTzAiuWjWLN8RCLnyiS2D6+rKmpqLffJwlPM+N/Ew49jcb0RJdjYkXMLTnEZ9n9dSoKm9
RcLT3u47AkHJRXxs25Yx64skaxQ7eJlzqWaJ71CO2DTW8Qwf52J+uX967wm8p2YRkbCsW+c7AkHJ
RXxUVEBRke8oUnYCb/EK5/IuE1nFiZzMm1nRD6OIvp1o3+J4jqaZJ7mCZipZyUmJ9VVEJBTTp/uO
QFByER95eWDZ//t4Ips4kTV8hTtx5PsO57AK2MsX+F6fBcj29hr9fRRbOYlVWpBMJEwFmmEhEyi5
iIvNm7NiKOpQXc8i7uDLlA66ZHuUX9yHP/c4NvPP/D238YP9s2+exCq61QgiEp2VK31HIESYXJjZ
18zsD2a208y2J3Hct8ys0cw6zOx5M5sWVYyxMmZMTmX0BnyZf6GZSn7H+SziuoP2KWYX+f2aTorZ
HXIUBwyjvc86KdsZg8P4N/6aRsbzAhfyBe5WTYVIlCZP9h2BEG3NRSHwGPDvQz3AzL4KfB74LPAB
YCfwnJllb2eBTFFUBIWFvqMI3QjaOZ/fcy2PMo9X+3y5X8ujGK5Ps8St3NvnfqpOp47JvJ0YWhq4
hQfp4kAZ76GIPYn7R7GVC/kdx7DpiJ9bRA5j7FjfEQgRJhfOuW865+4G3kzisC8C/9s597RzbgVw
IzAeuDyKGGOlqQl27fIdRWQMeIIrOJkV+7d9mOf5CddQRntinx4W8iX+kvuPOMH4AP+PZ/kox/LO
/m3X8FPu4zOUEJRzFU0MJ3fLXCQj1df7jkDIoLVFzGwKUAX8dt8259wOM1sGVBPUgkiqRo+G/Pys
m+siGRNopJ7ZLKGadUzlfF5kHJv5KM/xGz7MLkowHPfxWf6e21nMWWzgWL7B/+lzniI66Saf7l5v
jzy66enVgbSZSmawhrWcwO85j01M4BTe4Gz+wKd4nOe5CKMHR//GExGJVFWV7wiEDEouCBILBzT3
296ceEyORGlpMEPnzp2+I4mUAWexhLN6zYkxnA6u4Mk++03hbabwNt3k8UNuZRMT9icTV/E4j3J9
r70d1/ATHuOa/fusZwoQTPR1AS/2OfdoWvkUPwv/xYnI4KZM8R2BkGSziJndbmY9h7l1m9kJIcdo
ZOt0jJmkqSnnE4tU5NPDU1zKWLYm7nfx3/gJ32UBeXRj9DCSVu7js5zDK/v3qWaJLkqRTLR0qe8I
hORrLv4FeHCQfdanGEsTQSJRSd/ai3HA64MdvGDBAkaNGtVnW01NDTU1NSmGk2PKyoK5LnqOvDNj
rpnFG7zDsfyCy3ibYzmd5VzMr7iax3mSy+kin+Hs5HdcwH9xNkuoZh6vqrlDJBOVl/uOIGPV1tZS
W1vbZ1tra2skz2XORfv7y8xuAhY658YMYd9G4E7n3MLE/ZEEicaNzrnHBzhmNlBXV1fH7NmzQ4w8
B11xBTz9dE73uxCRmMrLCxKLTZuguNh3NFmjvr6eOXPmAMxxzoXWGzbKeS4mmdksYDKQb2azErfh
vfZZbWaX9TrsX4Gvm9klZnYK8DDQAPwiqjhj5Qc/ONAeWVgYdPDsfds3VLWsLPi3oODA3BjDhx84
Li8v2J6XN/hxw4YFM4PuO66wMLjf+7gRIw4+rrT0wHFmBz4sDnVcYeGB44qL+x5XWnrwuXsfl5/o
pFlUdCC+fXEPdpzZgXLYd9y+cup93L5yUZmrzFXm0ZV5SQk8/rgSiwwRZYfObxEMJd1nX0Z0PvBy
4v/HA/vbMpxzd5jZMOBeYDTwCvAx59yeCOOMj/Hj4c034Wc/g9deC5Zhv+GG4A364x8H/TLmzoUr
r4S6OnjqqeCxK66AU04J3rjLl8OECcFxnZ2waBFs2QLV1XD55bB4MfzqV8Eb/qqrgnn+a2thxYpg
cpsbboDWVnj0UWhpgbPPhksugRdfhN/8JviQvPpqOPZYeOQRWL0apk6F668PZhmtrYW2NjjvPPjo
R4Njfve74MOnpiboKb5oEfz5z8FzX3cdbNwIP/1pMBT3oovggguCGF9+ORhFc+21wb+LFsHbb8PM
mcG2tWuDstqzBz7+cZg/H37xi+A1VlQEMZWUBGW3aVOw1PM11wRl/MQTQQ3RpZcGZfrzn6vMVeYq
86jL/KijvH28Sl+RN4tETc0iIiIiqcm6ZhERERGJJyUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIi
EiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiIS
KiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIq
JRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiol
FyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUX
IiIiEiolFyIiIhIqJRciIiISKiUXMVZbW+s7hKyjMkuNyi15KrPUqNwyQ2TJhZl9zcz+YGY7zWz7
EI950Mx6+t2eiSrGuNObMHkqs9So3JKnMkuNyi0zFER47kLgMWAJcEsSxz0LfBqwxP3OcMMSERGR
KEWWXDjnvglgZjcleWinc25LBCGJiIhIGmRin4vzzKzZzFab2T1mNsZ3QCIiIjJ0UTaLpOJZ4OfA
BmAqcDvwjJlVO+fcAMeUAKxatSo9EeaQ1tZW6uvrfYeRVVRmqVG5JU9llhqVW3J6fXeWhHleG/g7
+xA7m90OfPUwuzhghnNuba9jbgIWOueSroEwsynAOuBC59yLA+xzLfBIsucWERGR/a5zzj0a1smS
rbn4F+DBQfZZn2IsB3HObTCzrcA04JDJBfAccB3wNrA7rOcWERGJgRLgWILv0tAklVw457YB28IM
4HDMbCIwFnhvkJhCy7ZERERiZnHYJ4xynotJZjYLmAzkm9msxG14r31Wm9llif8PN7M7zOwMM5ts
ZhcCTwJrCTmjEhERkehE2aHzW8CNve7v62FzPvBy4v/HA6MS/+8GTk0cMxpoJEgq/pdzbm+EcYqI
iEiIkurQKSIiIjKYTJznQkRERLKYkgsREREJVVYmF1oULXmplFniuG+ZWaOZdZjZ82Y2Lco4M42Z
lZvZI2bWamYtZnZ/707JAxzz+37XWbeZ3ZOumH0ws9vMbIOZ7TKzpWY2b5D9P2VmqxL7/9HMPpau
WDNFMmVmZjf1upb2XVcd6YzXNzM7x8yeMrNNidd/6RCOOc/M6sxst5mtTWE5iqyXbLmZ2QcP8V3Z
bWbjknnerEwuOLAo2r8nedyzQCVQlbjVhBxXJku6zMzsq8Dngc8CHwB2As+ZWVEkEWamR4EZwIXA
J4BzgXsHOcYB93HgWjsa+EqEMXplZtcA3wX+ATgd+CPBdVIxwP7VBOX6Q+A0glFhT5rZSemJ2L9k
yyyhlQOfXVUEI/HiZDiwHLiN4D12WGZ2LPBL4LfALOBu4H4zuyi6EDNSUuWW4AgGXOy71o52zm1O
6lmdc1l7A24Ctg9x3weB//Qds+9bkmXWCCzodX8ksAu42vfrSFNZnQj0AKf32vYRoAuoOsxxLwJ3
+Y4/jeW0FLi7130DGoCvDLD/T4Cn+m1bAtzj+7VkcJkN+X0bh1vifXnpIPt8B3ij37Za4Bnf8Wd4
uX2QYPTmyCN5rmytuUiVFkUbosTU61UEWT8AzrkdwDKg2ldcaVYNtDjnXu+17QWCrP6MQY69zsy2
mNmbZvZtMyuNLEqPzKwQmEPf68QRlNNA10l14vHenjvM/jklxTIDKDOzt81so5nFqqYnRWcS4+vs
CBmwPNEk/hszOyvZE2TawmVRSmVRtDirIvgSbe63vTnxWBxUAX2qAp1z3Yk+K4crg0eAdwhqfk4F
7gBOAK6KKE6fKoB8Dn2dTB/gmKoB9o/LdZVKma0BbgHeIJgb6MvAYjOb6ZzbFFWgWW6g62ykmRU7
5zo9xJQN3iNoCn8NKAY+A/zezD7gnFs+1JNkTHKRyqJoyXDOPdbr7koze5NgUbTzGHjdkowWdZkN
9LQMvd0uIw213A53Cg5TBs65+3vdXWlmTcALZjbFObchqWCzV7LXSdZfVyEYsAycc0sJmlKCHc2W
AKuAWwn6bcjQWOLfuF9rA0p8X/T+zlhqZlOBBQTNc0OSMckFmbkoWqaLssyaCN6IlfTN/scBrx/y
iOwx1HJrIni9+5lZPlDOwb+IDmcZQVlOI6g5yyVbCdpnK/ttH8fAZdSU5P65JpUy68M512VmrxNc
U3JoA11nO5xzezzEk81eBeYnc0DGJBcuAxdFy3RRllki+WoiGCXxBoCZjSToa/CDKJ4zXYZabolf
h6PN7PRe/S4uJEgUliXxlKcT/FLK2mttIM65vWZWR1AuTwGYmSXuf2+Aw5Yc4vGLEttzXopl1oeZ
5QEnA7EZTp+CJUD/Ic4fJibXWchOI9nPL9+9V1Ps8TqJYGjR/yIYnjUrcRvea5/VwGWJ/w8naPc+
g2D41oUE7UmrgELfrycTyyxx/ysEX8KXAKcQDBl8Cyjy/XrSWG7PJK6VeQSZ+xrgx70eH5+4juYm
7h8HfB2YnbjWLgX+DPzO92uJsIyuJhhFdCPBCJt7E9fNUYnHHwa+3Wv/amAP8CWCPgb/COwGTvL9
WjK4zL5BkIBNIUhWawmGhp/o+7WkscyGJz6zTiMY9fA/EvcnJR6/HXio1/7HAu0Eo0amA3+VuO4+
5Pu1ZHi5fTHxuTUVmAn8K7AXOC+p5/X9wlMsrAcJqhX7387ttU83cGPi/yXArwmqyXYTVHn/+743
chxuyZZZr23/SNAxsYOgp/U0368lzeU2GlhEkJC1EMzNMKzX45N7lyMwEfg9sCVRZmsSb94y368l
4nL6K+DtxBfmEhLJVuKx3wEP9Nv/SoJkdhdBzdhHfL+GTC4z4C6CJrVdiffj08Cpvl9Dmsvrg4kv
x/6fYQ8kHn+Qfkl84pi6RLm9Bdzg+3VkerkRdBZ+iyB53UIwquncZJ9XC5eJiIhIqOI2z4WIiIhE
TMmFiIiIhErJhYiIiIRKyYWIiIiESsmFiIiIhErJhYiIiIRKyYWIiIiESsmFiIiIhErJhYiIiIRK
yYWIiIiESsmFiIiIhOr/A58OfkQJ9BPiAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 4 Average Loss: 0.1277194768190384
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xl8XXWd//HXJ3vSNEsbmtCFUrYCRQpdhFKUXVwAEREm
sgm/kXHjp3Vm1J+DjtvIKCNVRxkZHdkKETdQFESRdeyCNJSlthQKhS4kTbc0adOmSb6/P85te5M2
zdJz7vfce97Px+M+2nvuOfd88s3JPZ/7Xc05h4iIiEhY8nwHICIiIrlFyYWIiIiESsmFiIiIhErJ
hYiIiIRKyYWIiIiESsmFiIiIhErJhYiIiIRKyYWIiIiESsmFiIiIhErJhYiIiIQq0uTCzN5hZr81
s7Vm1mNmFw2w/xmp/dIf3WY2Jso4RUREJDxR11yMAJYAnwQGu4iJA44G6lKPQ51z66MJT0RERMJW
EOWbO+f+APwBwMxsCIe2OOe2RhOViIiIRCmOfS4MWGJm68zsj2Z2mu+AREREZPAirbkYhreAfwCe
BYqBjwJPmNnbnXNL9neAmY0GzgdWATsyFKeIiEguKAEOBx5xzm0M601jlVw451YAK9I2LTSzI4E5
wDX9HHY+cE/UsYmIiOSwK4B7w3qzWCUX/XgGmH2A11cBzJs3j+OOOy4jAeWKOXPmMHfuXN9hZBWV
2fCo3IZOZTY8KrehWbZsGVdeeSWk7qVhyYbk4iSC5pL+7AA47rjjmDZtWmYiyhGVlZUqsyFSmQ2P
ym3oVGbDo3IbtlC7FUSaXJjZCOAogk6aAEeY2VRgk3NutZndBIx1zl2T2v/TwOvAUoJ2oI8CZwHn
RRmniIiIhCfqmosZwOMEc1c44Dup7XcC1xHMYzEhbf+i1D5jge3AC8A5zrmnIo5TREREQhL1PBdP
coDhrs65a/s8vxm4OcqYREREJFpxnOdCMqS+vt53CFlHZTY8KrehU5kNj8otHsy5wc7KHU9mNg1Y
vHjxYnXiERERGYLGxkamT58OMN051xjW+6rmQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJE
RERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkRE
REKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCRERE
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
pJe8vCCxWLsWiot9R5M1ohqKGlmfCzObYGZTgYlAvplNTT1GpO2z3Mzen3bYd4EbzexCM3sbcBew
BvhNVHEmyg9/uLc9srAw6OCZ/igsDF4rLw/+LSjYO9vdiBF7j8vLC7bn5Q18XFlZMDPo7uMKC4Pn
6ceNHLnvcaWle48z2/thsb/jCgv3Hldc3Pu40tJ93zv9uN2dXIuK9sa3O+6BjjPbWw67j9tdTunH
7S4XlbnKXGUeXZmXlMAvfqHEIiainOfiawRDSXfbnRGdBTyV+v/RwJ62DOfct82sDLiNYBKtp4H3
aI6LkIwdCy++CL/8JTz7bLAM+1VXBX+gd98d9MuYMQM++EFYvBh++9vgtQ98AN72tuAPd8kSGDcu
OG7nTpg3D1paYNYsuPhimD8ffv/74A/+0kuDef4bGuCll2DixOC41la4917YvBlOPx0uvBAefxz+
+MfgQ/Kyy+Dww+Gee2D5cjjySLjyymCW0YYGaGuDM8+Ed787OOaxx4IPn/r6oKf4vHnw6qvBua+4
At58E+67LxiKe955cPbZQYxPPRWMovnwh4N/582DVatgypRg24oVQVl1dsJ73wuzZ8NvfhP8jDU1
QUwlJUHZrV0bLPV8+eVBGd9/f1BDdNFFQZn+6lcqc5W5yjzqMj/kEG8fr9Jb5M0iUVOziIiIyPBk
XbOIiIiIJJOSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmV
kgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWS
CxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZIL
ERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsR
EREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSiwRr
aGjwHULWUZkNj8pt6FRmw6Nyi4fIkgsz+6KZ/cXMtpnZpkEec7uZ9fR5PBRVjEmnP8KhU5kNj8pt
6FRmw6Nyi4eCCN+7EPg5sAC4bgjHPQx8BLDU853hhiUiIiJRiiy5cM59FcDMrhnioTudcy0RhCQi
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
79uMz6UAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 5 Average Loss: 0.09163083682457605
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xl8XHW9//HXJ1uTNm2SNjShC6VQKFC10LRCKSirqFcQ
UdGwKgq4XK/W+1Pu9bpcuVe5yFXEBUVQtkIuroiKsi9CF21CVWqhUCilrWnTNs3SpkuS7++PM20n
adIsPWe+Z+a8n4/HPJI5c86Zz3xzMvOZ72rOOURERETCkuc7ABEREcktSi5EREQkVEouREREJFRK
LkRERCRUSi5EREQkVEouREREJFRKLkRERCRUSi5EREQkVEouREREJFRKLkRERCRUkSYXZnaqmT1g
ZuvMrNvMzhtg/7em9ku/dZnZ+CjjFBERkfBEXXMxClgGfBIY7CImDjgKqE7dDnXObYwmPBEREQlb
QZQnd879AfgDgJnZEA5tcs61RhOViIiIRCmOfS4MWGZm683sYTM72XdAIiIiMniR1lwMwz+Aq4Gl
wAjgSuBJM3uzc25ZXweY2TjgHGA1sCNDcYqIiOSCYuBw4CHn3OawThqr5MI5txJYmbZpsZkdCcwH
Lu/nsHOAe6KOTUREJIddDNwb1slilVz040/AvAM8vhpgwYIFHHvssRkJKFfMnz+fG2+80XcYWUVl
Njwqt6FTmQ2Pym1oVqxYwSWXXAKpz9KwZENycTxBc0l/dgAce+yxzJo1KzMR5YiysjKV2RCpzIZH
5TZ0KrPhUbkNW6jdCiJNLsxsFDCNoJMmwBFmNhPY4px73cyuAyY45y5P7f9p4FVgOUE70JXA6cDZ
UcYpIiIi4Ym65mI28ATB3BUO+GZq+53AFQTzWExO278otc8EYDvwV+BM59zTEccpIiIiIYl6noun
OMBwV+fch3vdvwG4IcqYREREJFpxnOdCMqS2ttZ3CFlHZTY8KrehU5kNj8otHsy5wc7KHU9mNguo
r6+vVyceERGRIWhoaKCmpgagxjnXENZ5VXMhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIi
IqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIi
oVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKhUnIhIiIioVJyISIiIqFSciEiIiKh
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
e/LygsRi3ToYMcJ3NFkjqoXLopznYrKZzQSmAPlmNjN1G5W2zwtm9u60w74NfNHMzjWzNwJ3AWuB
X0cVZ6J8//v72iMLC4MOnum3PUNVS0uDnwUF++bGGDVq33F5ecH2vLyBjxs5MpgZdM9xhYXB/fTj
Ro/e/7iSkn3Hme17s+jruMLCfceNGNHzuJKS/c+dftyeTq5FRfvi2xP3QMeZ7SuHPcftKaf04/aU
i8pcZa4yj67Mi4vhZz9TYhETUc6qdC3BUNI99mREpwNPp34/CtjbluGc+4aZjQRuAcqBPwLvcM7t
ijDO5JgwAf72N/j5z2HpUqiqgksvDf5B77476Jcxeza8971QXw8PPBA89p73wBvfGPzjLlsGEycG
x+3cCQsWQFMTzJ0L558PCxfC734X/MO/733BPP91dfD888HkNpdeCi0tcO+90NwMp5wC554LTzwB
Dz8cvEleeCEcfjjccw+88AIceSRcckkwy2hdHbS1wWmnwdvfHhzz+OPBm09tbdBTfMECePnl4Lkv
vhjWrIH77guG4p59NpxxRhDj008Ho2guuij4uWABrF4NM2YE21auDMpq1y545zth3jz49a+D11hZ
GcRUXByU3bp1wTLPH/hAUMa/+lVQQ3TeeUGZ/uIXKnOVuco86jI/5BBvb6/SU+TNIlFTs4iIiMjw
ZF2ziIiIiCSTkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJ
lZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmV
kgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWS
CxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZIL
ERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkosE
q6ur8x1C1lGZDY/KbehUZsOjcouHyJILM/uCmT1rZtvMbMsgj7ndzLp73R6MKsak0z/h0KnMhkfl
NnQqs+FRucVDQYTnLgR+CiwCrhjCcb8HPgRY6v7OcMMSERGRKEWWXDjnvgpgZpcP8dCdzrmmCEIS
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
ejKQMhMAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 6 Average Loss: 0.09302352716525396
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xl8XHW9//HXJ3u6JWlDE1ra0gUKFCk0rViKihYEFxDR
izdSQFxARa+/Xq/i9Xqvy1X5ISLXDRdQWQr5KXpBRJRNFLWLNqEgpaXS0pY2JN3SJG3TJcn398eZ
tknaNNs58z0z5/18PObRzJlzZj7z7ZmZz/mu5pxDREREJCw5vgMQERGR7KLkQkREREKl5EJERERC
peRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQhVpcmFmrzez
h8xss5l1mtklfez/xtR+XW8dZjY2yjhFREQkPFHXXAwHVgDXA/1dxMQBJwGVqdvxzrkt0YQnIiIi
YcuL8smdc78DfgdgZjaAQ7c651qiiUpERESiFMc+FwasMLN6M3vMzM7xHZCIiIj0X6Q1F4PwKnAd
sBwoBD4M/MHMXuucW3G0A8xsDHAhsB7Ym6Y4RUREskERcCLwqHNue1hPGqvkwjm3BljTZdNSM5sK
LASu7uWwC4F7o45NREQki10B3BfWk8UquejFX4F5x3h8PcCiRYs49dRT0xJQtli4cCG33nqr7zAy
ispscFRuA6cyGxyV28CsWrWKBQsWQOq3NCyZkFycSdBc0pu9AKeeeiqzZs1KT0RZoqSkRGU2QCqz
wVG5DZzKbHBUboMWareCSJMLMxsOTCPopAkwxcxmAjucc6+Y2Y3AOOfc1an9Pwm8DKwkaAf6MPAm
4IIo4xQREZHwRF1zMRt4imDuCgfcktp+F/ABgnksJnTZvyC1zzhgD/AcMN8593TEcYqIiEhIop7n
4o8cY7irc+6aHvdvBm6OMiYRERGJVhznuZA0qa6u9h1CxlGZDY7KbeBUZoOjcosHc66/s3LHk5nN
Ampra2vViUdERGQA6urqqKqqAqhyztWF9byquRAREZFQKbkQERGRUCm5EBERkVApuRAREZFQKbkQ
ERGRUCm5EBERkVApuRAREZFQKbkQERGRUCm5EBERkVApuRAREZFQKbkQERGRUCm5EBERkVApuRAR
EZFQKbkQERGRUCm5EBERkVApuRAREZFQKbkQERGRUCm5EBERkVApuRAREZFQKbkQERGRUCm5EBER
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
wQf0nnuCfhmzZ8O73w21tfDQQ8Fj73oXvOY1wQd3xQoYPz44bt8+WLQItm6FuXPh0kth8WL4zW+C
D/x73hPM819TA88/H0xuc+WV0NwM990HTU1w7rlw8cXw1FPw2GPBl+Tll8OJJ8K998Lq1TB1KixY
EMwyWlMDra1w3nlw0UXBMb//ffDlU10d9BRftAheeil47SuugI0b4Wc/C4biXnABvPnNQYxPPx2M
onnf+4J/Fy2C9ethxoxg25o1QVnt3w9vexvMmwe/+lXwHsvLg5iKioKy27w5WOr5ve8NyviBB4Ia
oksuCcr0l79UmavMVeZRl/lxx3n7epXuIm8WiZqaRURERAYn45pFREREJJmUXIiIiEiolFyIiIhI
qJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEio
lFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiU
XIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRc
iIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyI
iIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXCRYTU2N7xAyjspscFRuA6cyGxyVWzxE
llyY2efM7C9mttvMdvTzmJ+aWWeP2yNRxZh0+hAOnMpscFRuA6cyGxyVWzzkRfjc+cDPgSXABwZw
3G+B9wOWur8v3LBEREQkSpElF865LwGY2dUDPHSfc25rBCGJiIhIGsSxz8V5ZtZoZqvN7DYzG+07
IBEREem/KJtFBuO3wC+Bl4GpwI3AI2Y21znnejmmCGDVqlXpiTCLNDc3U1dX5zuMjKIyGxyV28Cp
zAZH5TYwXX47i8J8Xuv9N/soO5vdCNxwjF0ccKpzbk2XY64GbnXODbgGwswmA2uB+c65p3rZ533A
vQN9bhERETnkCufcfWE92UBrLr4B/LSPfdYNMpYjOOdeNrNtwDTgqMkF8ChwBbAe2BvWa4uIiCRA
EXAiwW9paAaUXDjntgPbwwzgWMzsBGAM8GofMYWWbYmIiCTM4rCfMMp5LiaY2UxgEpBrZjNTt+Fd
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
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 7 Average Loss: 0.10572540462017059
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
QkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRC
REREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJE
RERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkRE
REKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCREREQqXkQkREREKl5EJERERCpeRCRERE
QqXkQkREREKl5CLB6uvrfYeQc1RmQ6Nyy5zKbGhUbvEQWXJhZl82s7+a2Q4z2zLIY24xs65et/uj
ijHp9CbMnMpsaFRumVOZDY3KLR6KInzuYuBXwGLgAxkc9wfgfYCl7reHG5aIiIhEKbLkwjn3DQAz
uyLDQ9udcxsjCElERESyII59Lk43s/Vm9oKZ3WhmY3wHJCIiIoMXZbPIUPwB+A3wEjAVuAa438zm
OudcP8eUAaxYsSI7EeaRlpYWGhsbfYeRU1RmQ6Nyy5zKbGhUbplJ++4sC/N5rf/v7D52NrsGuOog
uzjgOOfcqrRjrgBucM5lXANhZlOA1cBZzrlH+9nnvcDtmT63iIiIdLvEOXdHWE+Wac3Fd4BbBtjn
xSHGcgDn3Etmtgk4GugzuQAeBC4B1gC7wzq3iIhIApQBRxJ8l4Ymo+TCObcZ2BxmAAdjZhOBscBr
A8QUWrYlIiKSMIvCfsIo57mYZGYzgclAoZnNTN2Gp+3zgpldkPp7uJl9y8zeYGaTzews4G5gFSFn
VCIiIhKdKDt0fhO4PO3+vh42ZwCPp/4+BhiV+rsTODF1zGigiSCp+Kpzbm+EcYqIiEiIMurQKSIi
IjKQOM5zISIiIjlMyYWIiIiEKieTCy2KlrmhlFnquG+aWZOZ7TSzh8zs6CjjjBszqzSz282sxcy2
mtnN6Z2S+znmsV7XWaeZ3ZitmH0ws0+Y2UtmtsvMlpjZnAH2f7eZrUjt/7SZvS1bscZFJmVmZlek
XUv7rqud2YzXNzN7k5ndY2brUq9//iCOOd3MGsxst5mtGsJyFDkv03Izszf38V3ZaWbjMjlvTiYX
7F8U7ccZHvcHoBqoSd3qQo4rzjIuMzO7Cvgk8FHg9cAO4EEzK4kkwni6AzgOOAv4F+A04KcDHOOA
m9h/rY0HrowwRq/M7GLgOuBrwMnA0wTXSVU/+88lKNf/AU4iGBV2t5kdn52I/cu0zFJa2P/ZVUMw
Ei9JhgPLgE8QvMcOysyOBH4P/AmYCXwPuNnMzokuxFjKqNxSHMGAi33X2njn3IaMzuqcy9kbcAWw
ZZD73gL81nfMvm8ZllkTsCDt/khgF/Ae368jS2U1HegCTk7bdi7QAdQc5LhHget9x5/FcloCfC/t
vgFrgSv72f8XwD29ti0GbvT9WmJcZoN+3ybhlnpfzh9gn2uBZ3ptqwfu9x1/zMvtzQSjN0ceyrly
teZiqLQo2iClpl6vIcj6AXDObQeWAnN9xZVlc4Gtzrmn0rY9TJDVv2GAYy8xs41m9qyZXW1m5ZFF
6ZGZFQO19LxOHEE59XedzE09nu7Bg+yfV4ZYZgAVZrbGzF4xs0TV9AzRKST4OjtEBixLNYn/0cze
mOkTxG3hsigNZVG0JKsh+BJd32v7+tRjSVAD9KgKdM51pvqsHKwMbgdeJqj5ORH4FnAs8K6I4vSp
Ciik7+tkWj/H1PSzf1Kuq6GU2UrgA8AzBHMDfRFYZGYznHProgo0x/V3nY00s1LnXLuHmHLBawRN
4U8CpcCHgcfM7PXOuWWDfZLYJBdDWRQtE865X6XdXW5mzxIsinY6/a9bEmtRl1l/p2Xw7XaxNNhy
O9hTcJAycM7dnHZ3uZk1Aw+b2RTn3EsZBZu7Mr1Ocv66CkG/ZeCcW0LQlBLsaLYYWAF8hKDfhgyO
pf5N+rXWr9T3Rfp3xhIzmwosIGieG5TYJBfEc1G0uIuyzJoJ3ojV9Mz+xwFP9XlE7hhsuTUTvN5u
ZlYIVHLgL6KDWUpQlkcT1Jzlk00E7bPVvbaPo/8yas5w/3wzlDLrwTnXYWZPEVxT0rf+rrPtzrk9
HuLJZX8D5mVyQGySCxfDRdHiLsoySyVfzQSjJJ4BMLORBH0NfhTFObNlsOWW+nU42sxOTut3cRZB
orA0g1OeTPBLKWevtf445/aaWQNBudwDYGaWuv/9fg5b3Mfj56S2570hllkPZlYAvA5IzHD6IVgM
9B7i/BYScp2F7CQy/fzy3Xt1iD1eJxEMLfoqwfCsmanb8LR9XgAuSP09nKDd+w0Ew7fOImhPWgEU
+349cSyz1P0rCb6EzwdOIBgy+A+gxPfryWK53Z+6VuYQZO4rgZ+nPX546jqanbp/FPAVYFbqWpsP
/BN4xPdribCM3kMwiuhyghE2P01dN4elHr8NuDpt/7nAHuBzBH0Mvg7sBo73/VpiXGb/QZCATSFI
VusJhoZP9/1aslhmw1OfWScRjHr4bOr+pNTj1wA/S9v/SKCNYNTINODjqevubN+vJebl9pnU59ZU
YAbwXWAvcHpG5/X9wodYWLcQVCv2vp2Wtk8ncHnq7zLgAYJqst0EVd4/3vdGTsIt0zJL2/Z1go6J
Owl6Wh/t+7VkudxGAwsJErKtBHMzDEt7fHJ6OQITgceAjakyW5l681b4fi0Rl9PHgTWpL8zFpJKt
1GOPAP/ba/93EiSzuwhqxs71/RriXGbA9QRNartS78d7gRN9v4Ysl9ebU1+OvT/D/jf1+C30SuJT
xzSkyu0fwGW+X0fcy42gs/A/CJLXjQSjmk7L9LxauExERERClbR5LkRERCRiSi5EREQkVEouRERE
JFRKLkRERCRUSi5EREQkVEouREREJFRKLkRERCRUSi5EREQkVEouREREJFRKLkRERCRUSi5EREQk
VP8f8rXDk6Bw0rgAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 8 Average Loss: 0.08927668581406276
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xl8nGW9///XJ1uTbkna0ATaUkqBAkVKF5aeIrIKKqug
nAgFweMual1/X4/H7XyP/hQREUVRj2yFqMgRAdmR7VhabUJZShcolFJK2nRL0zZdklzfP+5pOkmT
JpPe91z3zP1+Ph7zaOee+577M1fumfnMtZpzDhEREZGwFPgOQERERPKLkgsREREJlZILERERCZWS
CxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQlVpMmFmb3bzO4z
s7fNrMPMzu9j//ek9ku/tZvZqCjjFBERkfBEXXMxBFgIfBbo7yImDjgcqEndDnTOrY0mPBEREQlb
UZRP7px7GHgYwMwsg0ObnHObo4lKREREohTHPhcGLDSz1Wb2qJn9i++AREREpP8irbkYgHeATwIL
gEHAx4GnzOwE59zCng4ws5HA2cAKYHuW4hQREckHpcAhwCPOufVhPWmskgvn3DJgWdqmeWY2AZgN
XNnLYWcDd0Ydm4iISB67DLgrrCeLVXLRi38AM/fx+AqAOXPmcNRRR2UloHwxe/Zsrr/+et9h5BSV
2cCo3DKnMhsYlVtmFi9ezOWXXw6p79Kw5EJycRxBc0lvtgMcddRRTJ06NTsR5Yny8nKVWYZUZgOj
csucymxgVG4DFmq3gkiTCzMbAhxG0EkT4FAzmwxscM69ZWY/AA5yzl2Z2v8LwBvAIoJ2oI8DpwFn
RRmniIiIhCfqmovpwJMEc1c44LrU9tuAqwnmsRibtn9Jap+DgG3Ai8AZzrlnIo5TREREQhL1PBdP
s4/hrs65q7rdvxa4NsqYREREJFpxnOdCsqS2ttZ3CDlHZTYwKrfMqcwGRuUWD+Zcf2fljiczmwrU
19fXqxOPiIhIBhoaGpg2bRrANOdcQ1jPq5oLERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxER
EQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERER
CZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJ
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
SKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhI
qJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEio
lFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiU
XIiIiEiolFyIiIhIqJRcJFhdXZ3vEHKOymxgVG6ZU5kNjMotHiJLLszsG2b2dzPbamYb+nnMLWbW
0e32YFQxJp3ehJlTmQ2Myi1zKrOBUbnFQ1GEz10M/BF4Drg6g+MeAj4KWOr+jnDDEhERkShFllw4
574LYGZXZnjoDudcUwQhiYiISBbEsc/FqWa2xsyWmNlNZjbCd0AiIiLSf1E2iwzEQ8A9wBvABOAH
wINmNsM553o5phRg8eLF2YkwjzQ3N9PQ0OA7jJyiMhsYlVvmVGYDo3LLTNp3Z2mYz2u9f2f3sLPZ
D4Cv72MXBxzlnFuWdsyVwPXOuYxrIMxsPLAcOMM592Qv+3wEuDPT5xYREZFOlznn7grryTKtufgx
cEsf+7w+wFj24px7w8zWAYcBPSYXwCPAZcAKYHtY5xYREUmAUuAQgu/S0GSUXDjn1gPrwwxgX8xs
DDASeKePmELLtkRERBJmbthPGOU8F2PNbDIwDig0s8mp25C0fZaY2QWp/w8xsx+Z2YlmNs7MzgDu
BZYRckYlIiIi0YmyQ+f3gCvS7u/uYXMa8Ezq/4cD5an/twPHpo6pAFYTJBXfcs7tijBOERERCVFG
HTpFRERE+hLHeS5EREQkhym5EBERkVDlZHKhRdEyN5AySx33PTNbbWbbzOwxMzssyjjjxswqzexO
M2s2s41m9tv0Tsm9HPNUt+us3cxuylbMPpjZZ83sDTNrNbN5ZnZ8H/t/yMwWp/Z/wczel61Y4yKT
MjOzK9Oupd3X1bZsxuubmb3bzO4zs7dTr//8fhxzqpnVm9l2M1s2gOUocl6m5WZm7+nhu7LdzEZl
ct6cTC7YsyjaLzM87iGgGqhJ3WpDjivOMi4zM/s68Dngk8AJwFbgETMriSTCeLoLOAo4A/gAcApw
cx/HOODX7LnWDgS+FmGMXpnZpcB1wLeBKcALBNdJVS/7zyAo198AxxGMCrvXzI7OTsT+ZVpmKc3s
+eyqIRiJlyRDgIXAZwneY/tkZocADwBPAJOBG4DfmtlZ0YUYSxmVW4ojGHCx+1o70Dm3NqOzOudy
9gZcCWzo5763AP/jO2bftwzLbDUwO+3+cKAV+LDv15GlsjoS6ACmpG07G2gDavZx3JPAT3zHn8Vy
mgfckHbfgFXA13rZ//fAfd22PQfc5Pu1xLjM+v2+TcIt9b48v499fgi82G1bHfCg7/hjXm7vIRi9
OXx/zpWrNRcDpUXR+ik19XoNQdYPgHNuMzAfmOErriybAWx0zj2ftu1xgqz+xD6OvczMmszsJTP7
vpmVRRalR2ZWDEyj63XiCMqpt+tkRurxdI/sY/+8MsAyAxhqZivMbKWZJaqmZ4BOIsHX2X4yYGGq
SfxRM/uXTJ8gbguXRWkgi6IlWQ3Bl+iabtvXpB5LghqgS1Wgc6491WdlX2VwJ/AmQc3PscCPgCOA
SyKK06cqoJCer5OJvRxT08v+SbmuBlJmS4GrgRcJ5gb6KjDXzCY5596OKtAc19t1NtzMBjnndniI
KRe8Q9AUvgAYBHwceMrMTnDOLezvk8QmuRjIomiZcM79Me3uIjN7iWBRtFPpfd2SWIu6zHo7Lf1v
t4ul/pbbvp6CfZSBc+63aXcXmVkj8LiZjXfOvZFRsLkr0+sk56+rEPRaBs65eQRNKcGOZs8Bi4FP
EPTbkP6x1L9Jv9Z6lfq+SP/OmGdmE4DZBM1z/RKb5IJ4LooWd1GWWSPBG7Gartn/KOD5Ho/IHf0t
t0aC19vJzAqBSvb+RbQv8wnK8jCCmrN8so6gfba62/ZR9F5GjRnun28GUmZdOOfazOx5gmtKetbb
dbbZObfTQzy57B/AzEwOiE1y4WK4KFrcRVlmqeSrkWCUxIsAZjacoK/BL6I4Z7b0t9xSvw4rzGxK
Wr+LMwgShfkZnHIKwS+lnL3WeuOc22Vm9QTlch+AmVnq/s96Oey5Hh4/K7U97w2wzLowswLgGCAx
w+kH4Dmg+xDn95KQ6yxkx5Hp55fv3qsD7PE6lmBo0bcIhmdNTt2GpO2zBLgg9f8hBO3eJxIM3zqD
oD1pMVDs+/XEscxS979G8CV8HvAugiGDrwIlvl9PFsvtwdS1cjxB5r4UuCPt8YNS19H01P1DgW8C
U1PX2vnAa8DffL+WCMvowwSjiK4gGGFzc+q6OSD1+O3A99P2nwHsBL5E0MfgO8B24GjfryXGZfYf
BAnYeIJktY5gaPiRvl9LFstsSOoz6ziCUQ9fTN0fm3r8B8BtafsfAmwhGDUyEfhM6ro70/driXm5
fSH1uTUBmAT8FNgFnJrReX2/8AEW1i0E1Yrdb6ek7dMOXJH6fynwMEE12XaCKu9f7n4jJ+GWaZml
bfsOQcfEbQQ9rQ/z/VqyXG4VwByChGwjwdwMg9MeH5dejsAY4CmgKVVmS1Nv3qG+X0vE5fQZYEXq
C/M5UslW6rG/Ab/rtv/FBMlsK0HN2Nm+X0Ocywz4CUGTWmvq/Xg/cKzv15Dl8npP6sux+2fY71KP
30K3JD51TH2q3F4FZvl+HXEvN4LOwq8SJK9NBKOaTsn0vFq4TEREREKVtHkuREREJGJKLkRERCRU
Si5EREQkVEouREREJFRKLkRERCRUSi5EREQkVEouREREJFRKLkRERCRUSi5EREQkVEouREREJFRK
LkRERCRU/w8tc+8HnHYS6wAAAABJRU5ErkJggg==
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch: 9 Average Loss: 0.07391997848947843
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzt3Xt8XHWd//HXJ9emTS+hIQktpYSLLRQoJK3QrQKCIIpU
1xvGclFR2RWVrT9/uOt6xV35iYvg/caKYiEiuiJgBUFA0NK6JJRLKa20FGjTNL036TWX7++PM20n
aZJm0nPme2bO+/l4zKOZM+fM+cy3M3M+872acw4RERGRsBT4DkBERETyi5ILERERCZWSCxEREQmV
kgsREREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsREREJVaTJhZm90czu
NbO1ZtZjZnMOsf85qf3Sb91mVhVlnCIiIhKeqGsuRgFLgGuAoS5i4oATgZrU7SjnXFs04YmIiEjY
iqJ8cufcA8ADAGZmGRy6wTm3PZqoREREJEpx7HNhwBIzazGzP5rZP/gOSERERIYu0pqLYVgHXA08
BZQCHwUeM7PXO+eW9HeAmY0H3gKsBnZnKU4REZF8MAI4FnjQObcprCeNVXLhnFsBrEjbtMjMjgfm
AVcOcNhbgDuijk1ERCSPzQXuDOvJYpVcDOBvwOxBHl8NMH/+fE466aSsBJQv5s2bx8033+w7jJyi
MhselVvmVGbDo3LLzLJly7jssssgdS0NSy4kF6cTNJcMZDfASSedRF1dXXYiyhNjx45VmWVIZTY8
KrfMqcyGR+U2bKF2K4g0uTCzUcAJBJ00AY4zs+nAZufca2Z2AzDBOXdlav9rgZeBpQTtQB8F3gRc
EGWcIiIiEp6oay5mAI8SzF3hgJtS238OfJhgHotJafuXpPaZAOwEngXOd849HnGcIiIiEpKo57n4
M4MMd3XOfajP/W8A34gyJhEREYlWHOe5kCxpaGjwHULOUZkNj8otcyqz4VG5xYM5N9RZuePJzOqA
pqamJnXiERERyUBzczP19fUA9c655rCeVzUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIi
IhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIi
EiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiIS
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
iIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiI
iEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiI
SKiUXIiIiEiolFyIiIhIqJRciIiISKiUXIiIiEiolFyIiIhIqJRciIiISKiUXCRYY2Oj7xByjsps
eFRumVOZDY/KLR4iSy7M7HNm9lcz22Fmm4d4zG1m1tPntiCqGJNOH8LMqcyGR+WWOZXZ8Kjc4qEo
wucuBn4FPAl8OIPj/gB8ELDU/T3hhiUiIiJRiiy5cM59BcDMrszw0D3OuQ0RhCQiIiJZEMc+F+ea
2Xoze9HMvm9mR/gOSERERIYuymaR4fgD8BvgZeB44AZggZnNcs65AY4ZAbBs2bLsRJhHtm3bRnNz
s+8wcorKbHhUbplTmQ2Pyi0zadfOEWE+rw18ze5nZ7MbgM8OsosDTnLOrUg75krgZudcxjUQZlYL
rATOd849OsA+HwDuyPS5RUREZL+5zrk7w3qyTGsu/gu47RD7rBpmLAdxzr1sZhuBE4B+kwvgQWAu
sBrYHda5RUREEmAEcCzBtTQ0GSUXzrlNwKYwAxiMmR0NjAfWHSKm0LItERGRhFkY9hNGOc/FJDOb
DkwGCs1seuo2Km2fF83sHam/R5nZjWZ2pplNNrPzgXuAFYScUYmIiEh0ouzQeT1wRdr9fT1s3gQ8
nvr7RGBs6u9u4LTUMeOAFoKk4ovOuc4I4xQREZEQZdShU0RERORQ4jjPhYiIiOQwJRciIiISqpxM
LrQoWuaGU2ap4643sxYz22lmD5nZCVHGGTdmVmFmd5jZNjPbYma3pndKHuCYx/q8z7rN7PvZitkH
M7vGzF42s11mtsjMZh5i//ea2bLU/s+Y2VuzFWtcZFJmZnZl2ntp3/tqZzbj9c3M3mhm95rZ2tTr
nzOEY841syYz221mK4axHEXOy7TczOycfq6V3WZWlcl5czK54MCiaD/I8Lg/ANVATerWEHJccZZx
mZnZZ4FPAFcDrwd2AA+aWUkkEcbTncBJwPnAxcDZwI8OcYwDfsyB99pRwHURxuiVmV0K3AR8CTgD
eIbgfVI5wP6zCMr1J8DpBKPC7jGzk7MTsX+ZllnKNg58d9UQjMRLklHAEuAags/YoMzsWOB+4E/A
dOBbwK1mdkF0IcZSRuWW4ggGXOx7rx3lnGvL6KzOuZy9AVcCm4e4723A//iO2fctwzJrAeal3R8D
7ALe5/t1ZKmspgI9wBlp294CdAE1gxz3KPBN3/FnsZwWAd9Ku2/AGuC6Afb/JXBvn21PAt/3/Vpi
XGZD/twm4Zb6XM45xD5fB57ts60RWOA7/piX2zkEozfHHM65crXmYri0KNoQpaZeryHI+gFwzm0H
FgOzfMWVZbOALc65p9O2PUyQ1Z95iGPnmtkGM3vOzL5mZmWRRemRmRUD9fR+nziCchrofTIr9Xi6
BwfZP68Ms8wAys1stZm9amaJqukZprNI8PvsMBmwJNUk/kcz+4dMnyBuC5dFaTiLoiVZDcFFdH2f
7etTjyVBDdCrKtA5153qszJYGdwBvEJQ83MacCPwOuA9EcXpUyVQSP/vkykDHFMzwP5JeV8Np8yW
Ax8GniWYG+j/AgvNbJpzbm1Ugea4gd5nY8ys1Dm3x0NMuWAdQVP4U0Ap8FHgMTN7vXNuyVCfJDbJ
xXAWRcuEc+5XaXeXmtlzBIuincvA65bEWtRlNtBpGXq7XSwNtdwGewoGKQPn3K1pd5eaWSvwsJnV
OudezijY3JXp+yTn31chGLAMnHOLCJpSgh3NngSWAR8j6LchQ2Opf5P+XhtQ6nqRfs1YZGbHA/MI
mueGJDbJBfFcFC3uoiyzVoIPYjW9s/8q4Ol+j8gdQy23VoLXu5+ZFQIVHPyLaDCLCcryBIKas3yy
kaB9trrP9ioGLqPWDPfPN8Mps16cc11m9jTBe0r6N9D7bLtzbq+HeHLZ34DZmRwQm+TCxXBRtLiL
ssxSyVcrwSiJZwHMbAxBX4PvRXHObBlquaV+HY4zszPS+l2cT5AoLM7glGcQ/FLK2ffaQJxznWbW
RFAu9wKYmaXuf3uAw57s5/ELUtvz3jDLrBczKwBOARIznH4YngT6DnG+kIS8z0J2Opl+f/nuvTrM
Hq+TCIYWfZFgeNb01G1U2j4vAu9I/T2KoN37TILhW+cTtCctA4p9v544llnq/nUEF+FLgFMJhgz+
HSjx/XqyWG4LUu+VmQSZ+3LgF2mPT0i9j2ak7h8HfB6oS73X5gAvAY/4fi0RltH7CEYRXUEwwuZH
qffNkanHbwe+lrb/LGAv8GmCPgZfBnYDJ/t+LTEusy8QJGC1BMlqI8HQ8Km+X0sWy2xU6jvrdIJR
D/+Suj8p9fgNwM/T9j8W6CAYNTIF+Hjqffdm368l5uV2bep763hgGnAL0Amcm9F5fb/wYRbWbQTV
in1vZ6ft0w1ckfp7BPAAQTXZboIq7x/s+yAn4ZZpmaVt+zJBx8SdBD2tT/D9WrJcbuOA+QQJ2RaC
uRlGpj0+Ob0cgaOBx4ANqTJbnvrwlvt+LRGX08eB1akL5pOkkq3UY48AP+2z/7sJktldBDVjb/H9
GuJcZsA3CZrUdqU+j/cBp/l+DVkur3NSF8e+32E/TT1+G32S+NQxTaly+ztwue/XEfdyI+gs/HeC
5HUDwaimszM9rxYuExERkVAlbZ4LERERiZiSCxEREQmVkgsREREJlZILERERCZWSCxEREQmVkgsR
EREJlZILERERCZWSCxEREQmVkgsREREJlZILERERCZWSCxEREQnV/weuUcU9aNZU/AAAAABJRU5E
rkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
