---
layout: raw
title: odc_vowpalwabbit_nehal_kamat in tutorials
repository: tutorials
---
<html>
<head><meta charset="utf-8" />
<title>odc_vowpalwabbit_nehal_kamat</title>

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
<div class=" highlight hl-ipython2"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">vowpalwabbit</span> <span class="kn">import</span> <span class="n">pyvw</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">datasets</span>
<span class="kn">from</span> <span class="nn">sklearn.cross_validation</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="kn">from</span> <span class="nn">vowpalwabbit.sklearn_vw</span> <span class="kn">import</span> <span class="n">VWClassifier</span>
<span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">itertools</span>
<span class="kn">from</span> <span class="nn">operator</span> <span class="kn">import</span> <span class="n">itemgetter</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">pickle</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/home/nehal/.virtenvs/odc-challenge/local/lib/python2.7/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  warnings.warn(&#39;Matplotlib is building the font cache using fc-list. This may take a moment.&#39;)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="o">%</span><span class="k">matplotlib</span> inline
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
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">DIR</span> <span class="o">=</span> <span class="s2">&quot;./data/&quot;</span>
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
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">X</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">datasets</span><span class="o">.</span><span class="n">make_hastie_10_2</span><span class="p">(</span><span class="n">n_samples</span><span class="o">=</span><span class="mi">10000</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">X</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">256</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">VWClassifier</span><span class="p">()</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
<span class="n">model</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
<span class="n">model</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_test</span><span class="p">,</span> <span class="n">y_test</span><span class="p">)</span>
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
<div class=" highlight hl-ipython2"><pre><span></span><span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">ast</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>
<span class="n">feature_dict</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
<span class="n">regex</span> <span class="o">=</span> <span class="s2">r&quot;\(\d+, \d+.[\de-]+\)&quot;</span>
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
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">vw_compatible_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;./vw_compatible_file.vw&quot;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;total_spend.txt&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">train_data</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">islice</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mi">600000</span><span class="p">):</span>
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
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">total_spend_df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s1">&#39;total_spend.txt&#39;</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="s2">&quot;,&quot;</span><span class="p">,</span> <span class="n">header</span> <span class="o">=</span> <span class="bp">None</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="nb">len</span><span class="p">(</span><span class="n">total_spend_df</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[32]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>12440009</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">total_spend_df</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Household ID&quot;</span><span class="p">,</span> <span class="s2">&quot;Total Expenditure&quot;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">common_50</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">(</span><span class="n">total_spend_df</span><span class="p">[</span><span class="s2">&quot;Total Expenditure&quot;</span><span class="p">])</span><span class="o">.</span><span class="n">most_common</span><span class="p">(</span><span class="mi">50</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">common_50_x</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">common_50_y</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">common_50</span><span class="p">:</span>
    <span class="n">common_50_x</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="n">common_50_y</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[50]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">common_50_x</span><span class="p">,</span> <span class="n">common_50_y</span><span class="p">,</span> <span class="s1">&#39;-o&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;$ Spend&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of Households&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[50]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x7f2ae82adb38&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">cutoff_total_spend_df</span> <span class="o">=</span> <span class="n">total_spend_df</span><span class="p">[(</span><span class="n">total_spend_df</span><span class="p">[</span><span class="s1">&#39;Total Expenditure&#39;</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">500</span><span class="p">)</span> <span class="o">&amp;</span> <span class="n">total_spend_df</span><span class="p">[</span><span class="s1">&#39;Total Expenditure&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">upper_limit_total_spend_df</span> <span class="o">=</span> <span class="n">total_spend_df</span><span class="p">[(</span><span class="n">total_spend_df</span><span class="p">[</span><span class="s2">&quot;Total Expenditure&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">500</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">total_spend_df</span><span class="p">[</span><span class="s2">&quot;Total Expenditure&quot;</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">10000</span><span class="p">)]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">cutoff_total_spend_df</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[20]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Household ID</th>
      <th>Total Expenditure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2964841</td>
      <td>126.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>31389918</td>
      <td>365.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>31390092</td>
      <td>344.25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>31390102</td>
      <td>60.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>31390134</td>
      <td>179.00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>31390210</td>
      <td>229.99</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31390279</td>
      <td>179.94</td>
    </tr>
    <tr>
      <th>10</th>
      <td>31390294</td>
      <td>14.99</td>
    </tr>
    <tr>
      <th>11</th>
      <td>31390306</td>
      <td>94.49</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2964853</td>
      <td>216.23</td>
    </tr>
    <tr>
      <th>15</th>
      <td>31390346</td>
      <td>49.50</td>
    </tr>
    <tr>
      <th>16</th>
      <td>485583</td>
      <td>44.50</td>
    </tr>
    <tr>
      <th>18</th>
      <td>31390388</td>
      <td>170.00</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31390444</td>
      <td>43.18</td>
    </tr>
    <tr>
      <th>20</th>
      <td>31390470</td>
      <td>417.42</td>
    </tr>
    <tr>
      <th>21</th>
      <td>31390501</td>
      <td>397.85</td>
    </tr>
    <tr>
      <th>22</th>
      <td>31390502</td>
      <td>434.87</td>
    </tr>
    <tr>
      <th>23</th>
      <td>31390515</td>
      <td>65.97</td>
    </tr>
    <tr>
      <th>24</th>
      <td>31390566</td>
      <td>304.84</td>
    </tr>
    <tr>
      <th>25</th>
      <td>31390592</td>
      <td>287.96</td>
    </tr>
    <tr>
      <th>27</th>
      <td>31390624</td>
      <td>186.00</td>
    </tr>
    <tr>
      <th>28</th>
      <td>485590</td>
      <td>22.98</td>
    </tr>
    <tr>
      <th>29</th>
      <td>31390636</td>
      <td>87.50</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31390673</td>
      <td>34.50</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31390679</td>
      <td>183.09</td>
    </tr>
    <tr>
      <th>32</th>
      <td>31390820</td>
      <td>33.98</td>
    </tr>
    <tr>
      <th>33</th>
      <td>31390822</td>
      <td>229.85</td>
    </tr>
    <tr>
      <th>36</th>
      <td>485599</td>
      <td>209.40</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2964861</td>
      <td>230.32</td>
    </tr>
    <tr>
      <th>39</th>
      <td>31390934</td>
      <td>13.99</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>12439975</th>
      <td>31388979</td>
      <td>378.00</td>
    </tr>
    <tr>
      <th>12439976</th>
      <td>31389000</td>
      <td>368.64</td>
    </tr>
    <tr>
      <th>12439977</th>
      <td>31389052</td>
      <td>29.99</td>
    </tr>
    <tr>
      <th>12439978</th>
      <td>31389072</td>
      <td>111.97</td>
    </tr>
    <tr>
      <th>12439979</th>
      <td>485552</td>
      <td>39.98</td>
    </tr>
    <tr>
      <th>12439980</th>
      <td>31389087</td>
      <td>257.08</td>
    </tr>
    <tr>
      <th>12439981</th>
      <td>31389100</td>
      <td>213.75</td>
    </tr>
    <tr>
      <th>12439983</th>
      <td>31389168</td>
      <td>39.16</td>
    </tr>
    <tr>
      <th>12439984</th>
      <td>31389232</td>
      <td>259.80</td>
    </tr>
    <tr>
      <th>12439986</th>
      <td>31389257</td>
      <td>74.00</td>
    </tr>
    <tr>
      <th>12439987</th>
      <td>31389271</td>
      <td>61.20</td>
    </tr>
    <tr>
      <th>12439988</th>
      <td>31389299</td>
      <td>49.99</td>
    </tr>
    <tr>
      <th>12439990</th>
      <td>31389326</td>
      <td>179.41</td>
    </tr>
    <tr>
      <th>12439992</th>
      <td>31389359</td>
      <td>74.99</td>
    </tr>
    <tr>
      <th>12439993</th>
      <td>31389365</td>
      <td>144.16</td>
    </tr>
    <tr>
      <th>12439994</th>
      <td>31389434</td>
      <td>487.01</td>
    </tr>
    <tr>
      <th>12439995</th>
      <td>31389438</td>
      <td>69.98</td>
    </tr>
    <tr>
      <th>12439996</th>
      <td>485561</td>
      <td>498.80</td>
    </tr>
    <tr>
      <th>12439997</th>
      <td>31389468</td>
      <td>497.25</td>
    </tr>
    <tr>
      <th>12439998</th>
      <td>31389478</td>
      <td>246.90</td>
    </tr>
    <tr>
      <th>12439999</th>
      <td>31389506</td>
      <td>188.74</td>
    </tr>
    <tr>
      <th>12440000</th>
      <td>31389509</td>
      <td>84.97</td>
    </tr>
    <tr>
      <th>12440001</th>
      <td>31389599</td>
      <td>252.69</td>
    </tr>
    <tr>
      <th>12440002</th>
      <td>31389641</td>
      <td>449.83</td>
    </tr>
    <tr>
      <th>12440003</th>
      <td>31389652</td>
      <td>37.97</td>
    </tr>
    <tr>
      <th>12440004</th>
      <td>31389655</td>
      <td>239.94</td>
    </tr>
    <tr>
      <th>12440005</th>
      <td>31389673</td>
      <td>277.24</td>
    </tr>
    <tr>
      <th>12440006</th>
      <td>31389710</td>
      <td>174.00</td>
    </tr>
    <tr>
      <th>12440007</th>
      <td>31389733</td>
      <td>19.99</td>
    </tr>
    <tr>
      <th>12440008</th>
      <td>2964839</td>
      <td>59.99</td>
    </tr>
  </tbody>
</table>
<p>9069132 rows × 2 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">upper_limit_total_spend_df</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[27]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Household ID</th>
      <th>Total Expenditure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>31390077</td>
      <td>2138.49</td>
    </tr>
    <tr>
      <th>6</th>
      <td>31390208</td>
      <td>5831.89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>31390260</td>
      <td>1472.04</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2964852</td>
      <td>2420.45</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31390343</td>
      <td>659.87</td>
    </tr>
    <tr>
      <th>17</th>
      <td>31390372</td>
      <td>593.85</td>
    </tr>
    <tr>
      <th>26</th>
      <td>31390605</td>
      <td>4902.59</td>
    </tr>
    <tr>
      <th>34</th>
      <td>485597</td>
      <td>594.95</td>
    </tr>
    <tr>
      <th>35</th>
      <td>31390877</td>
      <td>1465.11</td>
    </tr>
    <tr>
      <th>38</th>
      <td>31390923</td>
      <td>3145.63</td>
    </tr>
    <tr>
      <th>41</th>
      <td>31391000</td>
      <td>2139.35</td>
    </tr>
    <tr>
      <th>43</th>
      <td>31391100</td>
      <td>5011.30</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2964865</td>
      <td>726.80</td>
    </tr>
    <tr>
      <th>49</th>
      <td>31391248</td>
      <td>3005.52</td>
    </tr>
    <tr>
      <th>57</th>
      <td>31391438</td>
      <td>1837.67</td>
    </tr>
    <tr>
      <th>59</th>
      <td>31391457</td>
      <td>1216.98</td>
    </tr>
    <tr>
      <th>60</th>
      <td>485614</td>
      <td>5041.55</td>
    </tr>
    <tr>
      <th>63</th>
      <td>31391644</td>
      <td>722.67</td>
    </tr>
    <tr>
      <th>65</th>
      <td>31391660</td>
      <td>518.41</td>
    </tr>
    <tr>
      <th>67</th>
      <td>31391837</td>
      <td>3839.46</td>
    </tr>
    <tr>
      <th>68</th>
      <td>485622</td>
      <td>2955.95</td>
    </tr>
    <tr>
      <th>69</th>
      <td>31391930</td>
      <td>573.34</td>
    </tr>
    <tr>
      <th>78</th>
      <td>31392134</td>
      <td>2109.02</td>
    </tr>
    <tr>
      <th>82</th>
      <td>31392210</td>
      <td>569.82</td>
    </tr>
    <tr>
      <th>84</th>
      <td>31392247</td>
      <td>925.76</td>
    </tr>
    <tr>
      <th>87</th>
      <td>485633</td>
      <td>2633.61</td>
    </tr>
    <tr>
      <th>89</th>
      <td>31392362</td>
      <td>2179.97</td>
    </tr>
    <tr>
      <th>92</th>
      <td>31392451</td>
      <td>635.70</td>
    </tr>
    <tr>
      <th>93</th>
      <td>31392496</td>
      <td>2552.98</td>
    </tr>
    <tr>
      <th>98</th>
      <td>31392699</td>
      <td>688.92</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>12439894</th>
      <td>31386848</td>
      <td>3228.40</td>
    </tr>
    <tr>
      <th>12439895</th>
      <td>31386878</td>
      <td>507.60</td>
    </tr>
    <tr>
      <th>12439897</th>
      <td>485484</td>
      <td>3827.59</td>
    </tr>
    <tr>
      <th>12439898</th>
      <td>31386971</td>
      <td>540.38</td>
    </tr>
    <tr>
      <th>12439900</th>
      <td>2964703</td>
      <td>727.76</td>
    </tr>
    <tr>
      <th>12439902</th>
      <td>2964707</td>
      <td>1007.43</td>
    </tr>
    <tr>
      <th>12439908</th>
      <td>31387415</td>
      <td>2895.50</td>
    </tr>
    <tr>
      <th>12439909</th>
      <td>31387445</td>
      <td>524.80</td>
    </tr>
    <tr>
      <th>12439910</th>
      <td>2964735</td>
      <td>1533.16</td>
    </tr>
    <tr>
      <th>12439917</th>
      <td>31387557</td>
      <td>724.84</td>
    </tr>
    <tr>
      <th>12439919</th>
      <td>31387587</td>
      <td>5271.92</td>
    </tr>
    <tr>
      <th>12439922</th>
      <td>31387658</td>
      <td>543.54</td>
    </tr>
    <tr>
      <th>12439923</th>
      <td>31387704</td>
      <td>906.06</td>
    </tr>
    <tr>
      <th>12439925</th>
      <td>31387742</td>
      <td>16963.16</td>
    </tr>
    <tr>
      <th>12439926</th>
      <td>485513</td>
      <td>2210.42</td>
    </tr>
    <tr>
      <th>12439934</th>
      <td>31387834</td>
      <td>1450.96</td>
    </tr>
    <tr>
      <th>12439935</th>
      <td>31387874</td>
      <td>1547.55</td>
    </tr>
    <tr>
      <th>12439937</th>
      <td>31387890</td>
      <td>823.64</td>
    </tr>
    <tr>
      <th>12439942</th>
      <td>31388164</td>
      <td>723.44</td>
    </tr>
    <tr>
      <th>12439944</th>
      <td>2964781</td>
      <td>1945.55</td>
    </tr>
    <tr>
      <th>12439950</th>
      <td>31388266</td>
      <td>545.41</td>
    </tr>
    <tr>
      <th>12439958</th>
      <td>31388562</td>
      <td>2237.57</td>
    </tr>
    <tr>
      <th>12439960</th>
      <td>46748</td>
      <td>830.56</td>
    </tr>
    <tr>
      <th>12439966</th>
      <td>31388741</td>
      <td>763.15</td>
    </tr>
    <tr>
      <th>12439971</th>
      <td>31388870</td>
      <td>1818.45</td>
    </tr>
    <tr>
      <th>12439973</th>
      <td>31388962</td>
      <td>1116.90</td>
    </tr>
    <tr>
      <th>12439982</th>
      <td>31389105</td>
      <td>7221.62</td>
    </tr>
    <tr>
      <th>12439985</th>
      <td>31389256</td>
      <td>670.75</td>
    </tr>
    <tr>
      <th>12439989</th>
      <td>485558</td>
      <td>2343.14</td>
    </tr>
    <tr>
      <th>12439991</th>
      <td>31389334</td>
      <td>875.75</td>
    </tr>
  </tbody>
</table>
<p>3370510 rows × 2 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">cutoff_total_spend_df</span><span class="p">[</span><span class="s2">&quot;Total Expenditure&quot;</span><span class="p">],</span> <span class="n">bins</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;$ expenditure in (0,500)&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of Households&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Spend trend of households&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[30]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x7f2ae808e898&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
0Vb8zAefn/ng8zMfXJ2dnUyfPh0KawrWU0skQpJEGqp+YaT1Z4rOAk6S9CDpIZxGmkX2KkidpyXN
Ac6UtJg0XfzZwC2Rp/yPiAckzQXOyyO/1gHOAToKzXDXkRKei/OQ/U3ytWZHxMs55lLSwoUXSPoW
aaHBo4G+OrwuB5g8eTJTpkzp17Ox2o0ZM8bPe5D5mQ8+P/PB52feNA3pWtISiRCpSWwzXrsOExFx
Rl676YekRR5vBvaNiBWFsBmkqdsvJy3Ady1pXaOig4HZpNFiq3PsKwlMRKyWtB/wfdJqzcuACyks
TpiTrr1JtVF3AN3AzIiYU+uNm5mZWfO0RCIUEb8ByldNLh6fyZqLUJYff4m00nH5KtTFmOeA6X2U
43Fgvz5i7iOteWRmZmZDXKsNnzczMzMbNE6EbNiaNm1as4vQdvzMB5+f+eDzMx9eWm6JjeFI0hTg
zjvvvNMd7MzMzPph/vz5TJ06FdIyWfPrfX7XCJmZmVnbciJkZmZmbcuJkJmZmbUtJ0JmZmbWtpwI
mZmZWdtyImRmZmZty4mQmZmZtS0nQmZmZta2nAiZmZlZ23IiZGZmZm3LiZCZmZm1LSdCZmZm1rac
CJmZmVnbciJkZmZmbcuJkJmZmbUtJ0JmZmbWtpwImZmZWdtyImRmZmZty4mQmZmZtS0nQmZmZta2
nAiZmZlZ23IiZGZmZm3LiZCZmZm1LSdCZmZm1racCJmZmVnbciJkZmZmbcuJkJmZmbUtJ0JmZmbW
tpwImZmZWdtyImRmZmZta61mFwBA0qbAt4B9gdHAn4FDI2J+IeZU4HBgLHALcEREPFg4Pgo4EzgQ
GAXMBT4fEU8XYjYEZgP7AauBK4BjImJZIWYz4AfAHsDzwEXAiRGxuhCzdT7P9sDTwOyI+HadHkdF
XV1ddHd39xk3btw4Jk6cOAglMjMzG7qanghJKiU2NwD7AN3AlsDiQswJwJHAIcCjwNeBuZImR8SK
HHYWKZE6AFgKnEtKdHYtXO5SYDywF7AOcCHwQ2B6vs4I4BrgSWAnYFPgYmAFcFKOWZ+UZF0HfBbY
CvixpMURcX5dHkovurq6mDRpMsuXv9Bn7LrrjmbBgk4nQ2ZmZhU0PRECTgS6IuLwwr7HymKOAU6L
iF8BSDoEWATsD1wmaQPgMOCgiLgxxxwKdEraISLmSZpMSrSmRsRdOeYo4GpJx0XEwnz8bcCeEdEN
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
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">upper_limit_total_spend_df</span><span class="p">[</span><span class="s2">&quot;Total Expenditure&quot;</span><span class="p">],</span> <span class="n">bins</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;$ expenditure in (500:)&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of Households&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Spend trend of households&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[31]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x7f2ae89c5ef0&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkoAAAGHCAYAAABPvX1uAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzs3XmcXFWZ//HPN4EEgxDASAIjURwUIoKSsATRIEZBRlQE
HWgmsv8YHbYJwoAOSAZUMDMSZJFRCMPI0g6CCgoSFh1AQDIQZJEmCoRNTKAlJDEQluT5/XFOkZtL
VS/V1V2Vzvf9etWr+5771L3n3upOPznbVURgZmZmZm82pNkVMDMzM2tVTpTMzMzManCiZGZmZlaD
EyUzMzOzGpwomZmZmdXgRMnMzMysBidKZmZmZjU4UTIzMzOrwYmSmZmZWQ1OlMzsDZL+V9Kvml2P
vpL0hKSLG3i8oZKmS3pK0nJJP+nm3Nc26tzNkn8WHmjwMVdI+noP4qZJWtHIc5vVy4mSWYNJ2kbS
VfkP5suSnpF0o6Sjml23HujRM40kfVXSZ/u7Mn3Q6GczHQYcD1wJHAjMGMBzN0szryOafH6zN6zV
7AqYDSaSPgT8CngS+AEwH9gMmAgcA5zXvNo11NeAHwPXNLsiA2Q34JmIOL7ZFTGzgeVEyayx/hV4
Edg+IpYUd0ga1ZwqNZekERHxUrPr0Ucbkz5XM1vDuOvNrLHeDfy+nCQBRERncTuP1zhH0gGSHsnd
dPdI+kj5vZI2lXSxpPmSlkl6SNIhpZhd8zG/IOlfJT2dj3mzpL+tcswjJD0q6SVJv5X04Z5cYB47
MgI4OJ9vRWU8UGVsiaRxkq6Q9AJwe+G9W+Zuyb/kuv2fpE+Xjn9QPsaHJJ0l6TlJf5X0E0lvq1Kf
k/O1LpV0i6T39eQ68ntHSPpOHnu0LH8OXynsf2e+3o8C78/1Wi5pUg+OvYuku/N1Pibpi1ViNpf0
43w/lkq6S9LflWIq93lsqbzyeU8qlG0h6WpJf87nfVpSu6T1Su+dkn/WXsrnbpf0jhrXMU7Sr3P9
npF0QpWYt0uamX8+X5b0O0kHdneP8ns/nH8OXpb0R0lH1Ij7hKTbJS2UtCR/Vt/syTnM+sItSmaN
9SQwUdLWEfH7HsR/FNgPOAd4Bfgn4JeSdoyIhwEkbQzcDSzPcZ3AnsBMSetFxDmlY56UY/8dGAmc
CFwG7FwJkHQY8J/Ab0jjbd4NXAu8ADzVTZ2nADNznX6Qyx7LXyvjSn4M/AH4KqB8zq3z+Z4BzgCW
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
AAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[86]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">ast</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>
<span class="n">feature_dict</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
<span class="n">regex</span> <span class="o">=</span> <span class="s2">r&quot;\(\d+, \d+.[\de-]+\)&quot;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[88]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">DIR</span> <span class="o">+</span> <span class="s2">&quot;train.txt&quot;</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">islice</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100000</span><span class="p">):</span>
        <span class="n">features_tuples</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">regex</span><span class="p">,</span> <span class="n">line</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">&quot;utf-8&quot;</span><span class="p">),</span> <span class="n">flags</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
        <span class="n">store_features</span> <span class="o">=</span> <span class="p">[</span><span class="n">ast</span><span class="o">.</span><span class="n">literal_eval</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">features_tuples</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">pair</span> <span class="ow">in</span> <span class="n">store_features</span><span class="p">:</span>
            <span class="n">feature_dict</span><span class="p">[</span><span class="n">pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pair</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[108]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># del feature_dict</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[92]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># len(feature_dict)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s1">&#39;feature_dict_100000_hp.pickle&#39;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">handle</span><span class="p">:</span>
  <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">feature_dict</span><span class="p">,</span> <span class="n">handle</span><span class="p">,</span> <span class="n">protocol</span><span class="o">=</span><span class="n">pickle</span><span class="o">.</span><span class="n">HIGHEST_PROTOCOL</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
