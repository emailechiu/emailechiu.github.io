/*
 * This is a JavaScript Scratchpad.
 *
 * Enter some JavaScript, then Right Click or choose from the Execute Menu:
 * 1. Run to evaluate the selected text (Ctrl+R),
 * 2. Inspect to bring up an Object Inspector on the result (Ctrl+I), or,
 * 3. Display to insert the result in a comment after the selection. (Ctrl+L)
 */
navigator.mediaDevices.getUserMedia({
  video: true,
  audio: false
}, function (stream) {
  if (navigator.mozGetUserMedia) {
    video.mozSrcObject = stream;
  } else {
    var url = window.URL || window.webkitURL;
    video.src = url ? url.createObjectURL(stream)  : stream;
  }
  mediaStream = stream;
  video.play();
}, function (error) {
  console.log('ERROR: ' + error);
}
);
/*
Promise (pending)
*/
