var js = document.createElement("script");
js.src = 'https://cdn.pubnub.com/sdk/javascript/pubnub.4.0.6.js';
//js.src = 'https://cdn.pubnub.com/pubnub-dev.js';
document.body.appendChild(js);
//var pubnub=PUBNUB({publish_key:'demo',subscribe_key:'demo'});
var pubnub=PUBNUB({publish_key: 'pub-c-44487f29-cca6-4a4b-9a6a-6e91cf733868', subscribe_key: 'sub-c-faae2814-66fd-11e6-9d44-02ee2ddab7fe'}); // always required
pubnub.publish({channel:'demo_echiu',message:'From Javascript'});
pubnub.subscribe({channel:'demo_echiu',message: function(m){console.log(m)} });

/*
Exception: ReferenceError: PUBNUB is not defined
@Scratchpad/1:6:5
*/
/*
Exception: TypeError: Cannot call a class as a function
_classCallCheck@https://cdn.pubnub.com/sdk/javascript/pubnub.4.0.6.js:72:100
_class@https://cdn.pubnub.com/sdk/javascript/pubnub.4.0.6.js:99:6
@Scratchpad/1:6:12
*/
/*
Exception: ReferenceError: PUBNUB is not defined
@Scratchpad/1:6:5
*/