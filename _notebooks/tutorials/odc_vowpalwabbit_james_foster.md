---
layout: raw
title: odc_vowpalwabbit_james_foster in tutorials
repository: tutorials
---
<html>
<head><meta charset="utf-8" />
<title>odc_vowpalwabbit_james_foster</title>

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

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Tutorial-on-using-Vowpal-Wabbit-and-R-Magic-for-the-Oracle-Data-Challenge">Tutorial on using Vowpal Wabbit and R Magic for the Oracle Data Challenge<a class="anchor-link" href="#Tutorial-on-using-Vowpal-Wabbit-and-R-Magic-for-the-Oracle-Data-Challenge">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-1:-Get-Data">Step 1: Get Data<a class="anchor-link" href="#Step-1:-Get-Data">&#182;</a></h2><h3 id="A.-Download-full-compressed-data-sets">A. Download full compressed data sets<a class="anchor-link" href="#A.-Download-full-compressed-data-sets">&#182;</a></h3><p>links on slack general channel</p>
<h3 id="B.-Download-sampled-data">B. Download sampled data<a class="anchor-link" href="#B.-Download-sampled-data">&#182;</a></h3><p>links on slack general channel</p>
<h3 id="C.-Create-your-own-sample-from-downloaded-full-data-sets">C. Create your own sample from downloaded full data sets<a class="anchor-link" href="#C.-Create-your-own-sample-from-downloaded-full-data-sets">&#182;</a></h3><p>Download and install odc from <a href="https://github.com/CoDataScience/oracle-audience">https://github.com/CoDataScience/oracle-audience</a></p>
<p>also see Pedro's posts on slack competition channel</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash
<span class="c1">#sample from full data sets</span>
python3 /Users/jmf/workspace/Jupyter/odc/oracle-audience-master/odc.py sample <span class="m">10000</span> data/train data/sampled_train.txt  <span class="c1">#but this only sampled negative examples?</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Single file detected
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>Traceback (most recent call last):
  File &#34;/Users/jmf/workspace/Jupyter/odc/oracle-audience-master/odc.py&#34;, line 173, in &lt;module&gt;
    cli()
  File &#34;/usr/local/lib/python3.5/site-packages/click-6.6-py3.5.egg/click/core.py&#34;, line 716, in __call__
    return self.main(*args, **kwargs)
  File &#34;/usr/local/lib/python3.5/site-packages/click-6.6-py3.5.egg/click/core.py&#34;, line 696, in main
    rv = self.invoke(ctx)
  File &#34;/usr/local/lib/python3.5/site-packages/click-6.6-py3.5.egg/click/core.py&#34;, line 1060, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File &#34;/usr/local/lib/python3.5/site-packages/click-6.6-py3.5.egg/click/core.py&#34;, line 889, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File &#34;/usr/local/lib/python3.5/site-packages/click-6.6-py3.5.egg/click/core.py&#34;, line 534, in invoke
    return callback(*args, **kwargs)
  File &#34;/Users/jmf/workspace/Jupyter/odc/oracle-audience-master/odc.py&#34;, line 128, in sample
    files = [smart_open.smart_open(input_path)]
  File &#34;/usr/local/lib/python3.5/site-packages/smart_open-1.3.5-py3.5.egg/smart_open/smart_open_lib.py&#34;, line 127, in smart_open
    return file_smart_open(parsed_uri.uri_path, mode)
  File &#34;/usr/local/lib/python3.5/site-packages/smart_open-1.3.5-py3.5.egg/smart_open/smart_open_lib.py&#34;, line 558, in file_smart_open
    return open(fname, mode)
FileNotFoundError: [Errno 2] No such file or directory: &#39;data/train&#39;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-2:-[If-you-are-running-on-the-full-data-set]-Decompress-Data">Step 2: [If you are running on the full data set] Decompress Data<a class="anchor-link" href="#Step-2:-[If-you-are-running-on-the-full-data-set]-Decompress-Data">&#182;</a></h2><p>see <a href="http://codata.colorado.edu/competitions/oracle/">http://codata.colorado.edu/competitions/oracle/</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

<span class="c1">#decompress and merge train data</span>
tar -xzvf data/train_set.tar.gz
bzip2 -d data/train/*.bz2
cat data/train/* &gt; data/train.txt
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

<span class="c1">#decompress and merge validation data</span>
tar -xzvf data/val_set.tar.gz
bzip2 -d data/val/*.bz2
cat data/val/* &gt; data/val.txt
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

<span class="c1">#decompress and merge contest data</span>
tar -xzvf data/contest_set.tar.gz
bzip2 -d data/contest/*.bz2
cat data/contest/* &gt; data/contest.txt
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-3:-Install-Vowpal-Wabbit">Step 3: Install Vowpal Wabbit<a class="anchor-link" href="#Step-3:-Install-Vowpal-Wabbit">&#182;</a></h2><p>see <a href="https://github.com/JohnLangford/vowpal_wabbit/wiki/Download">https://github.com/JohnLangford/vowpal_wabbit/wiki/Download</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-4:-Convert-training-and-validation-data-to-Vowpal-Wabbit-format">Step 4: Convert training and validation data to Vowpal Wabbit format<a class="anchor-link" href="#Step-4:-Convert-training-and-validation-data-to-Vowpal-Wabbit-format">&#182;</a></h2><p>code adapted from tutorial at <a href="http://codata.colorado.edu/notebooks/tutorials/odc_vowpalwabbit_nehal_kamat/">http://codata.colorado.edu/notebooks/tutorials/odc_vowpalwabbit_nehal_kamat/</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="kn">import</span> <span class="nn">itertools</span>
<span class="n">DIR</span> <span class="o">=</span> <span class="s2">&quot;./data/&quot;</span>

<span class="k">def</span> <span class="nf">file_len</span><span class="p">(</span><span class="n">fname</span><span class="p">):</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">fname</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">l</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">f</span><span class="p">):</span>
            <span class="k">pass</span>
    <span class="k">return</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[103]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># convert training data to VW format</span>

<span class="n">vw_compatible_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s2">&quot;./sampled_10000-train-vw_compatible_file.vw&quot;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;sampled_10000-train.txt&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">train_data</span><span class="p">:</span>
    <span class="n">nRows</span> <span class="o">=</span> <span class="n">file_len</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s1">&#39;sampled_10000-train.txt&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">islice</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">nRows</span><span class="p">):</span>
        <span class="n">el</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
        <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; &#39;&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; | &quot;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
            <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot;:&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[106]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># convert validation data to VW format</span>

<span class="n">vw_compatible_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s2">&quot;./sampled_10000-val-vw_compatible_file.vw&quot;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;sampled_10000-val.txt&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">val_data</span><span class="p">:</span>
    <span class="n">nRows</span> <span class="o">=</span> <span class="n">file_len</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s1">&#39;sampled_10000-val.txt&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">islice</span><span class="p">(</span><span class="n">val_data</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">nRows</span><span class="p">):</span>
        <span class="n">el</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
        <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; &#39;&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; | &quot;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
            <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot;:&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-5:-Train-Vowpal-Wabbit-model(s)">Step 5: Train Vowpal Wabbit model(s)<a class="anchor-link" href="#Step-5:-Train-Vowpal-Wabbit-model(s)">&#182;</a></h2><p>see <a href="https://github.com/JohnLangford/vowpal_wabbit/wiki/Tutorial">https://github.com/JohnLangford/vowpal_wabbit/wiki/Tutorial</a></p>
<p>Note: vw-varinfo is just a wrapper around vw that allows human-readable output of feature weights. see <a href="https://github.com/JohnLangford/vowpal_wabbit/wiki/using-vw-varinfo">https://github.com/JohnLangford/vowpal_wabbit/wiki/using-vw-varinfo</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Default-Model">Default Model<a class="anchor-link" href="#Default-Model">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[284]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

vw-varinfo -f data/model.vw -d data/sampled_10000-train-vw_compatible_file.vw &gt; feature_weights.txt
<span class="c1">#  -f says write the final model here</span>
<span class="c1">#  --loss_function logistic makes this binary classification</span>
<span class="c1">#  -d says use this training data</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Lasso-Regression">Lasso Regression<a class="anchor-link" href="#Lasso-Regression">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[122]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

vw-varinfo --l1 1e-7 -f data/model.vw -d data/sampled_10000-train-vw_compatible_file.vw &gt; feature_weights.txt
<span class="c1"># --l1 is lasso regression</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Neural-network-model">Neural network model<a class="anchor-link" href="#Neural-network-model">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[139]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

vw-varinfo --nn <span class="m">10</span> -f data/model.vw -d data/sampled_10000-train-vw_compatible_file.vw &gt; feature_weights.txt
<span class="c1">#  --nn is neural network model with X number of hidden units</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-6:-Run-Vowpal-Wabbit-model-on-Validation-Set">Step 6: Run Vowpal Wabbit model on Validation Set<a class="anchor-link" href="#Step-6:-Run-Vowpal-Wabbit-model-on-Validation-Set">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[285]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

<span class="c1">#example</span>
vw -i data/model.vw -t data/sampled_10000-val-vw_compatible_file.vw -p predictions.txt
<span class="c1">#  -t says, don`t learn, just score</span>
<span class="c1">#  -i says use this model to score</span>
<span class="c1">#  -p says output predictions to this file</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>only testing
predictions = predictions.txt
Num weight bits = 18
learning rate = 0.5
initial_t = 0
power_t = 0.5
using no cache
Reading datafile = data/sampled_10000-val-vw_compatible_file.vw
num sources = 1
average  since         example        example  current  current  current
loss     last          counter         weight    label  predict features
126.284500 126.284500            1            1.0   0.0000  11.2376      346
139.537628 152.790756            2            2.0   0.0000  12.3609      171
287.765436 435.993244            4            4.0  84.9700  57.2009     4396
322.304579 356.843722            8            8.0   0.0000   3.0295       69
241.897910 161.491241           16           16.0   0.0000  21.8121      841
391.066750 540.235590           32           32.0   0.0000   0.6538       49
346.160955 301.255160           64           64.0   0.0000   7.1842      111
1054.787658 1763.414360          128          128.0   0.0000   1.5063       57
1095.489470 1136.191283          256          256.0   0.0000   2.9224      464
7020.840507 12946.191544          512          512.0   0.0000  65.4305     6204
5337.910548 3654.980590         1024         1024.0   0.0000   9.7615      267
5415.389770 5492.868991         2048         2048.0   0.0000  18.0220      735
4276.943999 3138.498227         4096         4096.0   0.0000   5.8025      235
3832.083136 3387.222273         8192         8192.0   0.0000  30.6766     1879

finished run
number of examples per pass = 10000
passes used = 1
weighted example sum = 10000.000000
weighted label sum = 139006.738209
average loss = 4090.008185
best constant = 13.900674
total feature number = 10495922
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-7:-Convert-VW-predictions.txt-file-to-submission-format">Step 7: Convert VW predictions.txt file to submission format<a class="anchor-link" href="#Step-7:-Convert-VW-predictions.txt-file-to-submission-format">&#182;</a></h2><p>see Pedro's posts on slack</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#nBuyers = 100000</span>
<span class="n">nBuyers</span> <span class="o">=</span> <span class="mi">1000</span>

<span class="kn">import</span> <span class="nn">sys</span>
<span class="k">def</span> <span class="nf">parse_lines</span><span class="p">(</span><span class="nb">file</span><span class="p">):</span>
    <span class="n">lines</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">score</span><span class="p">,</span> <span class="n">hhid</span> <span class="o">=</span> <span class="n">l</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
            <span class="n">score</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
            <span class="n">hhid</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">hhid</span><span class="p">)</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">score</span><span class="p">,</span> <span class="n">hhid</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">lines</span>

<span class="k">def</span> <span class="nf">write_submission</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span> <span class="n">output</span><span class="p">):</span>
    <span class="n">sorted_predictions</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;household_id,advertise</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sorted_predictions</span><span class="p">)):</span>
            <span class="n">_</span><span class="p">,</span> <span class="n">hhid</span> <span class="o">=</span> <span class="n">sorted_predictions</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nBuyers</span><span class="p">:</span>
                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;{},1</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">hhid</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;{},0</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">hhid</span><span class="p">))</span>
                
                
<span class="k">def</span> <span class="nf">write_submission_ordered</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span> <span class="n">output</span><span class="p">):</span>
    <span class="n">sorted_predictions</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;household_id</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sorted_predictions</span><span class="p">)):</span>
            <span class="n">_</span><span class="p">,</span> <span class="n">hhid</span> <span class="o">=</span> <span class="n">sorted_predictions</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nBuyers</span><span class="p">:</span>
                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;{}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">hhid</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;{}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">hhid</span><span class="p">))</span>

<span class="c1">#if __name__ == &#39;__main__&#39;:</span>
<span class="c1">#    lines = parse_lines(sys.argv[1])</span>
<span class="c1">#    write_submission(lines, sys.argv[2])</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[286]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">lines</span> <span class="o">=</span> <span class="n">parse_lines</span><span class="p">(</span><span class="s1">&#39;predictions.txt&#39;</span><span class="p">)</span>
<span class="n">write_submission</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span><span class="s1">&#39;submission.csv&#39;</span><span class="p">)</span>
<span class="n">write_submission_ordered</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span> <span class="s1">&#39;submission_ordered.csv&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-8:-[If-you-are-using-sample-validation-data]-Create-sample_val_spend-file-for-scoring">Step 8: [If you are using sample validation data] Create sample_val_spend file for scoring<a class="anchor-link" href="#Step-8:-[If-you-are-using-sample-validation-data]-Create-sample_val_spend-file-for-scoring">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">sample_val_spend_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s2">&quot;./sample_val_spend.csv&quot;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;sampled_10000-val.txt&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">sample_val_spend_data</span><span class="p">:</span>
    <span class="n">nRows</span> <span class="o">=</span> <span class="n">file_len</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s1">&#39;sampled_10000-val.txt&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">islice</span><span class="p">(</span><span class="n">sample_val_spend_data</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">nRows</span><span class="p">):</span>
        <span class="n">el</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
        <span class="n">sample_val_spend_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot;,&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
        <span class="n">sample_val_spend_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="n">sample_val_spend_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-9:-Run-scoring-script-on-validation-data">Step 9: Run scoring script on validation data<a class="anchor-link" href="#Step-9:-Run-scoring-script-on-validation-data">&#182;</a></h2><p>see <a href="https://github.com/CoDataScience/oracle-audience">https://github.com/CoDataScience/oracle-audience</a> and Pedro's posts on slack</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Ratio-Scoring">Ratio Scoring<a class="anchor-link" href="#Ratio-Scoring">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[287]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

python3 /Users/jmf/workspace/Jupyter/odc/oracle-audience-master/odc.py score --ratio data/all_val_spend.csv submission.csv

<span class="c1">#0.45 default VW settings</span>
<span class="c1">#0.45 L1 (lasso regression) at 1e-7</span>
<span class="c1">#0.40 L1 (lasso regression) at 1e-4</span>
<span class="c1">#0.27 L1 (lasso regression) at .01</span>

<span class="c1">#0.44 neural network w/ 5 hidden units</span>
<span class="c1">#0.44 neural network w/ 10 hidden units</span>
<span class="c1">#0.28 neural network w/ 100 hidden units</span>

<span class="c1">#0.05 logistic loss function (on unmodified data sets)</span>

<span class="c1">#.44 default VW with interaction terms of top 79 features</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Scoring Options
ratio: True
ordered: False
spend_file: data/all_val_spend.csv
submission_file: submission.csv
Revenue: 68285.85000000003
Possible Revenue: 139006.7400000001
Fraction of Possible Revenue: 0.49124128801236533
Number of Responders: 410
Possible Number of Responders: 909
Fraction of Possible Responders 0.45104510451045104
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Ordered-Scoring-[must-use-full-data-set-to-be-accurate?]">Ordered Scoring [must use full data set to be accurate?]<a class="anchor-link" href="#Ordered-Scoring-[must-use-full-data-set-to-be-accurate?]">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[111]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash 

python3 /Users/jmf/workspace/Jupyter/odc/oracle-audience-master/odc.py score --ordered --ratio data/all_val_spend.csv submission_ordered.csv
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Scoring Options
ratio: True
ordered: True
spend_file: data/all_val_spend.csv
submission_file: submission_ordered.csv
Revenue: 72796.56000000003
Possible Revenue: 139006.7400000001
Fraction of Possible Revenue: 0.5236908656371624
Number of Responders: 432
Possible Number of Responders: 909
Fraction of Possible Responders 0.4752475247524752
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-10:-Convert-Contest-Set-data-to-Vowpal-Wabbit-format">Step 10: Convert Contest Set data to Vowpal Wabbit format<a class="anchor-link" href="#Step-10:-Convert-Contest-Set-data-to-Vowpal-Wabbit-format">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># convert validation data to VW format</span>

<span class="n">vw_compatible_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s2">&quot;./contest.vw&quot;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;contest.txt&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">val_data</span><span class="p">:</span>
    <span class="n">nRows</span> <span class="o">=</span> <span class="n">file_len</span><span class="p">(</span><span class="n">DIR</span><span class="o">+</span><span class="s1">&#39;contest.vw&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">islice</span><span class="p">(</span><span class="n">val_data</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">nRows</span><span class="p">):</span>
        <span class="n">el</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
        <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; &#39;&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; | &quot;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
            <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot;:&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="n">vw_compatible_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-10:-Run-Vowpal-Wabbit-model-on-Contest-Set">Step 10: Run Vowpal Wabbit model on Contest Set<a class="anchor-link" href="#Step-10:-Run-Vowpal-Wabbit-model-on-Contest-Set">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span>%%bash

<span class="c1">#example</span>
vw -i data/model.vw -t data/contest-vw_compatible_file.vw -p predictions_contest.txt
<span class="c1">#  -t says, don`t learn, just score</span>
<span class="c1">#  -i says use this model to score</span>
<span class="c1">#  -p says output predictions to this file</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-11:-Convert-VW's-contest-set-output-to-submission-format">Step 11: Convert VW's contest set output to submission format<a class="anchor-link" href="#Step-11:-Convert-VW's-contest-set-output-to-submission-format">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[64]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">lines</span> <span class="o">=</span> <span class="n">parse_lines</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;predictions_contest.txt&#39;</span><span class="p">)</span>
<span class="n">write_submission</span><span class="p">(</span><span class="n">lines</span><span class="p">,</span> <span class="n">DIR</span> <span class="o">+</span><span class="s1">&#39;submission_contest.csv&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">------------------------------------------------------------</span>
<span class="ansi-red-fg">IOError</span>                    Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-64-efbed775f5d1&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span><span class="ansi-blue-fg">()</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-fg"> </span>lines <span class="ansi-blue-fg">=</span> parse_lines<span class="ansi-blue-fg">(</span>DIR <span class="ansi-blue-fg">+</span> <span class="ansi-blue-fg">&#39;predictions_contest.txt&#39;</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span> write_submission<span class="ansi-blue-fg">(</span>lines<span class="ansi-blue-fg">,</span> DIR <span class="ansi-blue-fg">+</span><span class="ansi-blue-fg">&#39;submission_contest.csv&#39;</span><span class="ansi-blue-fg">)</span>

<span class="ansi-green-fg">&lt;ipython-input-61-04f26cf8fb94&gt;</span> in <span class="ansi-cyan-fg">parse_lines</span><span class="ansi-blue-fg">(file)</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span> <span class="ansi-green-fg">def</span> parse_lines<span class="ansi-blue-fg">(</span>file<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      6</span>     lines <span class="ansi-blue-fg">=</span> <span class="ansi-blue-fg">[</span><span class="ansi-blue-fg">]</span>
<span class="ansi-green-fg">----&gt; 7</span><span class="ansi-red-fg">     </span><span class="ansi-green-fg">with</span> open<span class="ansi-blue-fg">(</span>file<span class="ansi-blue-fg">)</span> <span class="ansi-green-fg">as</span> f<span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      8</span>         <span class="ansi-green-fg">for</span> l <span class="ansi-green-fg">in</span> f<span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      9</span>             score<span class="ansi-blue-fg">,</span> hhid <span class="ansi-blue-fg">=</span> l<span class="ansi-blue-fg">.</span>strip<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">.</span>split<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">)</span>

<span class="ansi-red-fg">IOError</span>: [Errno 2] No such file or directory: &#39;./data/predictions_contest.txt&#39;</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Model-Introspection">Model Introspection<a class="anchor-link" href="#Model-Introspection">&#182;</a></h1><p>see <a href="https://github.com/JohnLangford/vowpal_wabbit/wiki/using-vw-varinfo">https://github.com/JohnLangford/vowpal_wabbit/wiki/using-vw-varinfo</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-R-Magic">Install R Magic<a class="anchor-link" href="#Install-R-Magic">&#182;</a></h3><p><a href="http://rpy.sourceforge.net/rpy2/doc-dev/html/overview.html">http://rpy.sourceforge.net/rpy2/doc-dev/html/overview.html</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="o">%</span><span class="k">load_ext</span> rpy2.ipython
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
<div class=" highlight hl-ipython2"><pre><span></span><span class="o">%%</span>R
f <span class="o">=</span> read.table<span class="p">(</span><span class="s">&#39;feature_weights.txt&#39;</span><span class="p">,</span> header<span class="o">=</span><span class="bp">T</span><span class="p">)</span>
<span class="kp">print</span><span class="p">(</span><span class="kp">dim</span><span class="p">(</span>f<span class="p">))</span>
<span class="kp">print</span><span class="p">(</span><span class="kp">head</span><span class="p">(</span>f<span class="p">))</span>
f<span class="o">$</span>RelScore <span class="o">=</span> <span class="kp">as.numeric</span><span class="p">(</span><span class="kp">sub</span><span class="p">(</span><span class="s">&quot;%&quot;</span><span class="p">,</span><span class="s">&quot;&quot;</span><span class="p">,</span>f<span class="o">$</span>RelScore<span class="p">))</span>
<span class="kp">summary</span><span class="p">(</span>f<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_text output_subarea ">
<pre>[1] 130086      6
  FeatureName HashVal MinVal MaxVal  Weight RelScore
1       35875   35875      0      0 5996.03   17.65%
2       39858   39858      0      0 5177.77   15.24%
3        7208    7208      0      0 4508.64   13.27%
4      110472  110472      0      0 1889.09    5.56%
5       66485   66485      0      0 1889.09    5.56%
6       12654   12654      0      0 1750.51    5.15%
  FeatureName        HashVal           MinVal      MaxVal      Weight         
 0      :     1   Min.   :     0   Min.   :0   Min.   :0   Min.   :-33980.20  
 10     :     1   1st Qu.: 33359   1st Qu.:0   1st Qu.:0   1st Qu.:    -0.22  
 100    :     1   Median : 66742   Median :0   Median :0   Median :    -0.03  
 1000   :     1   Mean   : 66745   Mean   :0   Mean   :0   Mean   :    -0.19  
 10000  :     1   3rd Qu.:100107   3rd Qu.:0   3rd Qu.:0   3rd Qu.:     0.12  
 100000 :     1   Max.   :133530   Max.   :0   Max.   :0   Max.   :  5996.03  
 (Other):130080                                                               
    RelScore         
 Min.   :-100.00000  
 1st Qu.:   0.00000  
 Median :   0.00000  
 Mean   :  -0.00044  
 3rd Qu.:   0.00000  
 Max.   :  17.65000  
                     
</pre>
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
<div class=" highlight hl-ipython2"><pre><span></span><span class="o">%%</span>R
f<span class="o">$</span>absRelScore <span class="o">=</span> <span class="kp">abs</span><span class="p">(</span>f<span class="o">$</span>RelScore<span class="p">)</span>
hist<span class="p">(</span>f<span class="o">$</span>absRelScore<span class="p">[</span>f<span class="o">$</span>absRelScore<span class="o">&gt;</span><span class="m">1</span><span class="p">],</span> breaks<span class="o">=</span><span class="m">15</span><span class="p">)</span>
hist<span class="p">(</span>f<span class="o">$</span>RelScore<span class="p">[</span><span class="kp">abs</span><span class="p">(</span>f<span class="o">$</span>RelScore<span class="p">)</span><span class="o">&gt;=</span><span class="m">1</span><span class="p">],</span> breaks<span class="o">=</span><span class="m">15</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
k3S9J9ikZ2brvk2YMEFq164tp59+ui2XngP1XKipcuXKcsYZZ9jXWfnLHOSkQhIwgcIxB5lz0kkn
5drizz//bKebE3Bo+tVXX22n/fOf/wxNi/di+/btzp133uk888wz8RYL3Lz27dtbJ3Vt165d1P2L
XGbp0qWOOYmG1jMnfadXr15R1402sUOHDnbdGTNmRJud1LQbbrghtH0te/iPuYhwtmzZklQ+kyZN
suteeumloeWHDRvm6D6F51mxYkXHnAhDyxTVi/fffz9XucxFgrNq1Srn8MMPD01//vnnHS/UkZqF
G7qv1VaNk02Rn2WtW3NBlCfv448/3lm7dm2y2fpiuZ49e9r97Nq1a6i85kIjtO8mKIemZ+OL7LlV
Mp8eP6WLLrpIBgwYIOZDmVSxH3jgAXs3t3///qSWD8JCenfyySefSIkSJUTv+N599908uxVtmRde
eEGWLFki/fv3t3cz9erVk2effVb+7//+L8/6mZ5wwQUXyBNPPGHrbuDAgVKtWjW7T48//niBNq37
cN9990nVqlXlsccek/fee0+uvPJK2blzp1xzzTXy+++/FyjfdK9kLhjk008/tXd+ekdsLiDtXbq2
LPTo0UO8VEfqqXWkdXLTTTfZu3Sd9v333xeI5amnnhJz8SZnnnmmvP766/Lyyy9LkyZNZNGiRdKn
T58C5ZnJlbSlx9wI5GoNSLS9Xbt2yT333CPmhiDPomqpxyVJhCZojx4F2hxprsBtcNEiapOVfgi0
2apkyZLSsmVLMXd8tglHp2kzpCb9YGuzjp7ENK1YsUKmTZsmCxculGOPPVauuuoqe3K2M80vbZ4d
NWqUbQLUE0Lz5s1tk9Hf/vY3adu2rW0i06Y43da///1v22yqJyENWrrdzz77zG5D89Zg4jbl6onF
XM3LrbfeKq+++qr8+OOP9gR78cUXy6xZs8TcCdnmVg0KRx11lFucPH9jld/cRcjTTz9tTwoVKlSQ
d955R84//3w54ogjQnnEWkZP/IcddphdXr20LNpUpk21boq3b+4yerFj7tasrbpdd911thtB58er
L3d9/avNcn//+99DkzRwmrsG21XhTtQuipdeesmeoOvWrSvdu3e3du788L9abk3adeGezDt27Ch7
9+61gUObrDUPTdoMqHWjzb+nnHKKmJaCXN0dv/32mz12vvjiC9tMrL4tWrSw66qXNt9rk7keC+PH
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
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
53phAndx44+31C7jcBv9n/w+SM5Tznqfu3kMgbs48Xkmr9fjDh06+OV0Qf9/GU1kIJWTQHiSSD7A
kx9nCsB9+vTxB7Lr/vIlV/B2V7GBu8v0byA3acSvd5N9Andn6peFJ06NC7u70ECvdXfVfrzG3RX5
fNwkJP86ndB1QnFX7/65ypQcgPXc3VUE7i4kcJOK/H7dXY7fXhk9+eST/nXuytznGwZgN5kmcJOa
/P7DeupE6O6kguOPP96/xnUV+tek/lNc+d2dVhCOncvVdS8XOilr3E8BUft2d0yJcV6NHYbBxE02
Ci688EIfTFSGMADrYkUBWuvDE6pOsO4uJVFU1wPh89YynezdJBT/XI5KqQFYJ6twm9BD+9F4p8qv
FAZPN/nOX1y5O25/8bPPPvv4AKt21Gtdj4JvD3cX54OvlrlhiwJ5qNyqt+YUKBVX3tQArAstHZMK
Orow0HN5aF8KvmEA1vPrr7/eH0O6UNBzBSvVt6hj1xfK/eN6E3zQ0XPtx92l+zzkLRfZKpCFJ3Tl
rwuoRx55JMwiCN9buhhQuym4hhcv7m7UW2rj6667zuettlG+rqfBP3dd14m8UgOwjJPHn7V/vZd0
MRpeCITBU2PZuhByd/H+IvnKK6/0+RZ3PGujMA/XpRy4O/Zg6tSpgZtc5uvhJmj6Ouj95yYT+nbQ
e0tJFxUqk7v798+L+sdN7vTtKSe9xk1C9OcMN5ExSPen7YtLBODihP7/esaA3VFX3kmzXm+88cbE
3xFHHFFkkdR1qHTccceZup3VLecCmO9idIHEdwFrvbrJ1OWlrshw7FPjYJpVqm5BdQm7E4bvnnSH
hO+e1Osuvvhic29I382qrtd0yQVO362oLil1bWocVd2j7oSWGD9Vd11y0iza+vXr+/27E6Jfpe5L
Fxh8F50WaPZkalLZiiu/ZumGXVzKW+V2J9wCWambWCZKmsWsbngljcWqa1avV7eqZkJrzD05aZ26
1ZW3Cwq+e1ldi+G4vMaD3cQgP2apbtexY8cm2sFdICVnlXiscUONrao7XOOImtmr9lNd3cnXb6ex
MyV1JWpWvGbLq1tWs3xVFnWbK6nbUd28muF7xRVX+GWavZuc5K+ZvBoX3ZzyykzDG+qylJkLpt5L
+1DXdJjkrm5eHUMuEPqZ4iqzC5q+21vbpTt2tVzDJupGV12V5KFjRknHsdrVBUTbeeed/VDKHXfc
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
jct0v1HdWaXApagWnnIjgAACCBQWePzxx23ZsmXWsmXLwitLccmKFSvs+++/txtuuKEU9xKfrLkD
jk9bUhMEEEAgIVC/fn079thjE8/L4sFrr71m8+fPL4tdxWIfjAHHohmpBAIIIIBA1AQIwFFrMcqL
AAIIIBALAQJwLJqRSiCAAAIIRE2AABy1FqO8CCCAAAKxECAAx6IZqQQCCCCAQNQECMBRazHKiwAC
CCAQCwECcCyakUoggAACCERNgAActRajvAgggAACsRAgAMeiGakEAggggEDUBAjAUWsxyosAAggg
EAsBAnAsmpFKIIAAAghETYAAHLUWo7wIIIAAArEQIADHohmpBAIIIIBA1AQIwFFrMcqLAAIIIBAL
AQJwLJqRSiCAAAIIRE2AABy1FqO8CCCAAAKxECAAx6IZqQQCCCCAQNQECMBRazHKiwACCCAQCwEC
cCyakUoggAACCERNgAActRajvAgggAACsRAgAMeiGakEAggggEDUBAjAUWsxyosAAgggEAsBAnAs
mpFKIIAAAghETYAAHLUWo7wIIIAAArEQIADHohmpBAIIIIBA1AQIwFFrMcqLAAIIIBALAQJwLJqR
SiCAAAIIRE2AABy1FqO8CCCAAAKxECAAx6IZqQQCCCCAQNQECMBRazHKiwACCCAQCwECcCyakUog
gAACCERNgAActRajvAgggAACsRAgAMeiGakEAggggEDUBAjAUWsxyosAAgggEAsBAnAsmpFKIIAA
AghETYAAHLUWo7wIIIAAArEQIADHohmpBAIIIIBA1AQIwFFrMcqLAAIIIBALAQJwLJqRSiCAAAII
RE2AABy1FqO8CCCAAAKxECAAx6IZqQQCCCCAQNQECMBRazHKiwACCCAQCwECcCyakUoggAACCERN
gAActRajvAgggAACsRAgAMeiGakEAggggEDUBPIuAG/YsMFWrFgRNUfKiwACCCCAQIkE8iIAr1u3
zgYOHGjNmjWzrbfe2urWrWs1a9a01q1b22OPPVaiCrExAggggAACURCokg+F7Nu3ry1evNgmTJhg
u+66qw++q1atspkzZ1q/fv1s7dq1dtFFF+VDUSkDAggggAACORHIizvgV155xR566CFr06aN1apV
yypVqmR16tSxDh062LBhw+z555/PSWXJBAEEEEAAgXwRyIsArK7myZMnpzUZP368NWjQIO06FiKA
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
YHTvvffa1Vdf7buEk7tQhw4daoccckjaslWtWtV0V7x27Vr7/fff/TZvvvmm7bPPPrbddtvZCSec
4INs6otXr15tlSpVsipVqvhVu+++uw/yO+64o3++cuVKO+mkk/yd6tFHH22ffPKJX75gwQJ/odCk
SRNr06ZN4s77008/tbPOOsuOOuooa9WqlSn/bMqhTJ944gnbc889rVatWrbvvvv6ixC/M/fPnDlz
/B2+7tTVG7Bx40a/atSoUbbTTjtZvXr1fDkVGJQUCLS8Zs2aVhFd1d66uEpNcpLzHnvsYffcc4+t
WrUqscn7779vuoNN/XvvvfcS24QPXn/9ddtmm218XuEy/kegJAIE4JJosW2pC+huQt3B6r5Tl6vu
MJ588km7/vrrberUqfbrr78WKMPs2bPttdde83/a7owzzrDjjz/eB52lS5faMccc44PVrFmzrE6d
OnbrrbcWeL2eKJjphNy6dWsbOHCgqdtWwU9d0Uq9e/e2GjVq2GeffWZHHnmkXXLJJX657syXLVvm
g6TK+ac//ckWLlxoa9as8WU+4IADTBcMv/32W1bl+Oqrr3zeo0eP9nf07dq1M3VRh2n8+PHeRCf+
F1980ZdZFxu62/rXv/5l33zzjQ/2Dz74oH+J7uS7dOniH1dE165du/rejNAv/L958+b23HPP2cSJ
E03HT8uWLf1drC70dKGmi6nUPy1PTeppueOOO/yxkbqO5whkJeC6TkgI5JWAu3sMXNdzokxLliwJ
zj333MCN9wburjRwd4J+3eGHHx64u8/ABU6/zt3pBU899VTg7gz9eheIgvbt2wfuDtb/uQAXuDtS
v84FpMCNESb24QJn4IKl336rrbYKunfvHrg7o8DdSQfuzjhwAdxv67otAzcZLJg7d676HIP58+cn
8vjjH/8YuPHWYNq0aYHKEqaiynHttdcGV111ld9U5fz888/9459//jm4++67g7333ts/dxckwbHH
HhtmGdx4442BuxgIXAAO3F1Y4LrnAxdAfHnDjQ488MDABevwaVCRXMNKV69ePZBlpuSGKgLX2xJU
rlw5cMMAmTYrcvnkyZMDd8FWYBvX9R9cfvnlBZbxBIFUAe6As7pMYaPyFNAkpUMPPdTU1aqxveS7
WN0hzpgxw9QdrAlYr776qrkA6ovrgqNfp65G/R188MHmTsZ+2+T6qItZE7h01+2Cp7+TXLRokakb
/LvvvvN3OOpKVlJXtbq5lbcmfzVt2jSRlQv2/g5YC8Luaz3OthzbbrutjR071pdV+3v22WcLjFMq
/zCprrrbrlatmu+y1x28yqLegy+//NJv5i4SfLd5+JrU/yuCq7rr5ZCa1CuhyWm6+9X4u3oQNMyg
oQLdOaf+TZkyJTULniOwxQIE4C0mJIPSFPjzn//sg6L2oTHeww47zHf7pu5TXcQa89THldxdsF+t
LmB3F2gKpuHfRx99ZBqzDZPGivVcgTZMu+yyi51++um+e1KzrH/55Rf/+nD9o48+6oOyAqACepjc
3aupe1PJ3VGFiy2bcmhjlf+ZZ57xgVflVde4u2JO5KOLjDBplq+6yDWRSN3lGnfWX+3atRNd5Br/
VT7pUkVwlY0+yiaH5KSLrJ133tl3QevCRZP6NF6vtOuuu9oFF1xQ6E+T9EgI5FqAAJxrUfLLqYDG
U4cNG2b6nKX+NHZ33HHHpd2HTqoaK9adrCbW6K5Zk2emT5/ut9cYsetaLnBXqTtILXNd3IkZsxqL
VTDs1q2bv4PUeKDuvhUMdbK+6667/Bihgu0jjzzil2tiloJ78l1qWMhsyqFt9dlV3ZFpLFr7evzx
x32dw3x0d68xcAV93R0raGjmtrbXXbY+rqUx6jCp3KpLulQRXDUrXnf5uohKTuppkKXGgNUrkpzU
q3HKKacU+tNyEgK5FvjPtM9c50p+CORIQJ/lVKB56aWXzI3n+QDTs2fPjLn379/f/v73v5sbI/Uf
W9LHlHSSVfes7pI1QSn57lQZ6S7IjY+aG2/1gU932n379vXLtF756XO6DzzwgOnkrQCsGdMK0pqI
pa5qTYYaMWKED4bvvvuuXpZI2m825VBeukjQrG1dbGhCmQKFukuV1C3txpl9ANZMcN2p6QJC3fDq
mtdsZwVo3UUrKR/dKadLFcFVdddFSGrSBQsJgXwQqKRB4XwoCGVAoCiBhx56yHe5aqZxSZM+rqO7
Rn38pKikLks34cvvR2O9qUl3m/Xr109d7Ls5NdaY7jXJG6crh4Kngu3tt9+e2FQzq3XXFo5lJ1a4
B9pWH2tKNytXs75VjjDpue7INXtbwTldiqur6qrZ8PqMtZu8lq7qpbpMF4DqhdFn10kIZBKgCzqT
DMvzSkB3vZ07d96sMumOt7jgq4wV8DQZK1MgTRd89Tp1c2Z6jdaHKVM59PEqdWWHSWVNF3y1Xnfn
6YKv1iUH3/C5PjKlMetMKa6u6npXz0F5BF8NHWgyFwmB4gTogi5OiPV5IZAp+OVF4bagELpL08Sf
bC4QNmc36kpXV3mmFFdXjYlr7kB5JF0IafiAru7y0I/WPumCjlZ7UVoEEEAAgZgI0AUdk4akGggg
gAAC0RIgAEervSgtAggggEBMBAjAMWlIqoEAAgggEC0BAnC02ovSIoAAAgjERIAAHJOGpBoIIIAA
AtESIABHq70oLQIIIIBATAQIwDFpSKqBAAIIIBAtAQJwtNqL0iKAAAIIxESAAByThqQaCCCAAALR
EiAAR6u9KC0CCCCAQEwECMAxaUiqgQACCCAQLQECcLTai9IigAACCMREgAAck4akGggggAAC0RIg
AEervSgtAggggEBMBP4fWbdJug4OH+gAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="o">%%</span>R
topFeatures <span class="o">=</span> f<span class="p">[</span><span class="kp">order</span><span class="p">(</span><span class="o">-</span>f<span class="o">$</span>absRelScore<span class="p">),]</span>
<span class="kp">print</span><span class="p">(</span><span class="kp">nrow</span><span class="p">(</span>topFeatures<span class="p">))</span>
<span class="c1">#topFeatures = topFeatures[order(-topFeatures$absRelScore),]</span>
topFeatures<span class="p">[</span><span class="m">1</span><span class="o">:</span><span class="m">100</span><span class="p">,]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_text output_subarea ">
<pre>[1] 130086
       FeatureName HashVal MinVal MaxVal     Weight RelScore absRelScore
130086       78025   78025      0      0 -33980.200  -100.00      100.00
1            35875   35875      0      0   5996.030    17.65       17.65
2            39858   39858      0      0   5177.770    15.24       15.24
3             7208    7208      0      0   4508.640    13.27       13.27
130085       13930   13930      0      0  -3128.130    -9.21        9.21
4           110472  110472      0      0   1889.090     5.56        5.56
5            66485   66485      0      0   1889.090     5.56        5.56
6            12654   12654      0      0   1750.510     5.15        5.15
7            15330   15330      0      0   1716.390     5.05        5.05
8            53200   53200      0      0   1601.740     4.71        4.71
130084       35139   35139      0      0  -1504.100    -4.43        4.43
9            97998   97998      0      0   1474.850     4.34        4.34
130083      104584  104584      0      0  -1256.530    -3.70        3.70
10           89909   89909      0      0   1188.030     3.50        3.50
11           24090   24090      0      0    981.228     2.89        2.89
12           40883   40883      0      0    906.858     2.67        2.67
13           29339   29339      0      0    871.751     2.57        2.57
14          123831  123831      0      0    729.806     2.15        2.15
130082        2460    2460      0      0   -726.053    -2.14        2.14
15           13675   13675      0      0    700.632     2.06        2.06
16           75887   75887      0      0    647.230     1.90        1.90
130081       96609   96609      0      0   -570.376    -1.68        1.68
17          132020  132020      0      0    564.235     1.66        1.66
18          113689  113689      0      0    548.918     1.62        1.62
130080        2769    2769      0      0   -538.172    -1.58        1.58
130079       13188   13188      0      0   -497.602    -1.46        1.46
130078      118386  118386      0      0   -464.157    -1.37        1.37
19          110394  110394      0      0    463.707     1.36        1.36
20           57070   57070      0      0    463.707     1.36        1.36
21          112669  112669      0      0    462.643     1.36        1.36
22             158     158      0      0    462.643     1.36        1.36
130077      108839  108839      0      0   -448.514    -1.32        1.32
130076       77849   77849      0      0   -441.237    -1.30        1.30
130075       11601   11601      0      0   -433.235    -1.27        1.27
23           55881   55881      0      0    428.961     1.26        1.26
130074       71374   71374      0      0   -404.756    -1.19        1.19
24           15580   15580      0      0    374.565     1.10        1.10
25          111537  111537      0      0    368.788     1.09        1.09
26           83177   83177      0      0    368.620     1.08        1.08
130073       19556   19556      0      0   -359.455    -1.06        1.06
27           84417   84417      0      0    358.088     1.05        1.05
130072      127527  127527      0      0   -346.891    -1.02        1.02
130071       24268   24268      0      0   -334.316    -0.98        0.98
130070       17874   17874      0      0   -328.244    -0.97        0.97
28           44440   44440      0      0    326.484     0.96        0.96
130068       65460   65460      0      0   -321.337    -0.95        0.95
130069       34370   34370      0      0   -322.602    -0.95        0.95
130065      114878  114878      0      0   -319.911    -0.94        0.94
130066       10686   10686      0      0   -320.925    -0.94        0.94
130067       38885   38885      0      0   -321.062    -0.94        0.94
29           55133   55133      0      0    312.607     0.92        0.92
130064       32330   32330      0      0   -299.904    -0.88        0.88
130062       94312   94312      0      0   -288.496    -0.85        0.85
130063       64412   64412      0      0   -289.259    -0.85        0.85
130061       80783   80783      0      0   -273.671    -0.81        0.81
130060      117923  117923      0      0   -267.721    -0.79        0.79
130059      110696  110696      0      0   -260.236    -0.77        0.77
30          115049  115049      0      0    251.424     0.74        0.74
130058       28373   28373      0      0   -239.144    -0.70        0.70
31           54332   54332      0      0    224.978     0.66        0.66
32           32477   32477      0      0    224.901     0.66        0.66
130057       42413   42413      0      0   -209.135    -0.62        0.62
33           28677   28677      0      0    204.781     0.60        0.60
34           13054   13054      0      0    201.646     0.59        0.59
130056       68904   68904      0      0   -199.098    -0.59        0.59
130055       49835   49835      0      0   -196.616    -0.58        0.58
35           34791   34791      0      0    189.236     0.56        0.56
130054      122914  122914      0      0   -189.534    -0.56        0.56
130053      121268  121268      0      0   -183.706    -0.54        0.54
36           94689   94689      0      0    179.752     0.53        0.53
130052       62369   62369      0      0   -181.773    -0.53        0.53
37           69561   69561      0      0    162.146     0.48        0.48
38           98657   98657      0      0    161.584     0.48        0.48
130049       57947   57947      0      0   -162.636    -0.48        0.48
130050       94635   94635      0      0   -163.295    -0.48        0.48
130051       70162   70162      0      0   -164.569    -0.48        0.48
39           78553   78553      0      0    160.475     0.47        0.47
130046       94249   94249      0      0   -151.709    -0.45        0.45
130047       14676   14676      0      0   -152.356    -0.45        0.45
130048       38735   38735      0      0   -154.583    -0.45        0.45
40           21800   21800      0      0    148.688     0.44        0.44
130043       26448   26448      0      0   -149.624    -0.44        0.44
130044      129933  129933      0      0   -150.317    -0.44        0.44
130045      120246  120246      0      0   -150.514    -0.44        0.44
41            3566    3566      0      0    146.185     0.43        0.43
130042       77584   77584      0      0   -147.687    -0.43        0.43
130041       54275   54275      0      0   -141.398    -0.42        0.42
42           54795   54795      0      0    138.091     0.41        0.41
130040      119756  119756      0      0   -140.315    -0.41        0.41
130039       41106   41106      0      0   -134.787    -0.40        0.40
43           67944   67944      0      0    133.864     0.39        0.39
44           29023   29023      0      0    130.056     0.38        0.38
45           15953   15953      0      0    129.827     0.38        0.38
130037       24259   24259      0      0   -128.626    -0.38        0.38
130038       59065   59065      0      0   -129.770    -0.38        0.38
130035       54642   54642      0      0   -124.115    -0.37        0.37
130036       74968   74968      0      0   -126.765    -0.37        0.37
46           10681   10681      0      0    119.820     0.35        0.35
130034       68021   68021      0      0   -116.651    -0.34        0.34
47            1786    1786      0      0    110.523     0.33        0.33
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="o">%</span><span class="k">Rpull</span> topFeatureNames
<span class="c1">#sends topFeatureNames variable and data from R to python</span>
<span class="n">topFeatureNames</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">------------------------------------------------------------</span>
<span class="ansi-red-fg">LookupError</span>                Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-7-5d9fe6c92f6a&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span><span class="ansi-blue-fg">()</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-fg"> </span>get_ipython<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">.</span>magic<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">u&#39;Rpull topFeatureNames&#39;</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span> <span class="ansi-red-fg">#sends topFeatureNames variable and data from R to python</span>

<span class="ansi-green-fg">//anaconda/lib/python2.7/site-packages/IPython/core/interactiveshell.pyc</span> in <span class="ansi-cyan-fg">magic</span><span class="ansi-blue-fg">(self, arg_s)</span>
<span class="ansi-green-intense-fg ansi-bold">   2161</span>         magic_name<span class="ansi-blue-fg">,</span> _<span class="ansi-blue-fg">,</span> magic_arg_s <span class="ansi-blue-fg">=</span> arg_s<span class="ansi-blue-fg">.</span>partition<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">&#39; &#39;</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   2162</span>         magic_name <span class="ansi-blue-fg">=</span> magic_name<span class="ansi-blue-fg">.</span>lstrip<span class="ansi-blue-fg">(</span>prefilter<span class="ansi-blue-fg">.</span>ESC_MAGIC<span class="ansi-blue-fg">)</span>
<span class="ansi-green-fg">-&gt; 2163</span><span class="ansi-red-fg">         </span><span class="ansi-green-fg">return</span> self<span class="ansi-blue-fg">.</span>run_line_magic<span class="ansi-blue-fg">(</span>magic_name<span class="ansi-blue-fg">,</span> magic_arg_s<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   2164</span> 
<span class="ansi-green-intense-fg ansi-bold">   2165</span>     <span class="ansi-red-fg">#-------------------------------------------------------------------------</span>

<span class="ansi-green-fg">//anaconda/lib/python2.7/site-packages/IPython/core/interactiveshell.pyc</span> in <span class="ansi-cyan-fg">run_line_magic</span><span class="ansi-blue-fg">(self, magic_name, line)</span>
<span class="ansi-green-intense-fg ansi-bold">   2082</span>                 kwargs<span class="ansi-blue-fg">[</span><span class="ansi-blue-fg">&#39;local_ns&#39;</span><span class="ansi-blue-fg">]</span> <span class="ansi-blue-fg">=</span> sys<span class="ansi-blue-fg">.</span>_getframe<span class="ansi-blue-fg">(</span>stack_depth<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">.</span>f_locals
<span class="ansi-green-intense-fg ansi-bold">   2083</span>             <span class="ansi-green-fg">with</span> self<span class="ansi-blue-fg">.</span>builtin_trap<span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">-&gt; 2084</span><span class="ansi-red-fg">                 </span>result <span class="ansi-blue-fg">=</span> fn<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">*</span>args<span class="ansi-blue-fg">,</span><span class="ansi-blue-fg">**</span>kwargs<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   2085</span>             <span class="ansi-green-fg">return</span> result
<span class="ansi-green-intense-fg ansi-bold">   2086</span> 

<span class="ansi-green-fg">&lt;decorator-gen-126&gt;</span> in <span class="ansi-cyan-fg">Rpull</span><span class="ansi-blue-fg">(self, line)</span>

<span class="ansi-green-fg">//anaconda/lib/python2.7/site-packages/IPython/core/magic.pyc</span> in <span class="ansi-cyan-fg">&lt;lambda&gt;</span><span class="ansi-blue-fg">(f, *a, **k)</span>
<span class="ansi-green-intense-fg ansi-bold">    191</span>     <span class="ansi-red-fg"># but it&#39;s overkill for just that one bit of state.</span>
<span class="ansi-green-intense-fg ansi-bold">    192</span>     <span class="ansi-green-fg">def</span> magic_deco<span class="ansi-blue-fg">(</span>arg<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">--&gt; 193</span><span class="ansi-red-fg">         </span>call <span class="ansi-blue-fg">=</span> <span class="ansi-green-fg">lambda</span> f<span class="ansi-blue-fg">,</span> <span class="ansi-blue-fg">*</span>a<span class="ansi-blue-fg">,</span> <span class="ansi-blue-fg">**</span>k<span class="ansi-blue-fg">:</span> f<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">*</span>a<span class="ansi-blue-fg">,</span> <span class="ansi-blue-fg">**</span>k<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">    194</span> 
<span class="ansi-green-intense-fg ansi-bold">    195</span>         <span class="ansi-green-fg">if</span> callable<span class="ansi-blue-fg">(</span>arg<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>

<span class="ansi-green-fg">//anaconda/lib/python2.7/site-packages/rpy2-2.8.3-py2.7-macosx-10.6-x86_64.egg/rpy2/ipython/rmagic.pyc</span> in <span class="ansi-cyan-fg">Rpull</span><span class="ansi-blue-fg">(self, line)</span>
<span class="ansi-green-intense-fg ansi-bold">    346</span>         outputs <span class="ansi-blue-fg">=</span> args<span class="ansi-blue-fg">.</span>outputs
<span class="ansi-green-intense-fg ansi-bold">    347</span>         <span class="ansi-green-fg">for</span> output <span class="ansi-green-fg">in</span> outputs<span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">--&gt; 348</span><span class="ansi-red-fg">             </span>robj <span class="ansi-blue-fg">=</span> ri<span class="ansi-blue-fg">.</span>globalenv<span class="ansi-blue-fg">.</span>get<span class="ansi-blue-fg">(</span>output<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">    349</span>             self<span class="ansi-blue-fg">.</span>shell<span class="ansi-blue-fg">.</span>push<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">{</span>output<span class="ansi-blue-fg">:</span> converter<span class="ansi-blue-fg">.</span>ri2py<span class="ansi-blue-fg">(</span>robj<span class="ansi-blue-fg">)</span> <span class="ansi-blue-fg">}</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">    350</span> 

<span class="ansi-red-fg">LookupError</span>: &#39;topFeatureNames&#39; not found</pre>
</div>
</div>

</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
