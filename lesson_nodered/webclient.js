require('http').get({host:'localhost',port:1880,path:'/mine'}, function(response) {
        // Continuously update stream with data
        var body = 'Initial';
        var WebSocket=require('ws');
        var ws=new WebSocket('ws://127.0.0.1:1880/ws/mine');
        response.on('data', function(d) {
//            document.body.innerHTML += "343243";

        });
    });

