//console.log(window.location)
var loc = window.location
var form = $('#formData')
var wsStart = 'ws://'
if (loc.protocol == 'https:'){
    wsStart = 'wss://'
}
var endpoint = wsStart + loc.host + loc.pathname
console.log(loc.host)
console.log(loc.pathname)

 var socket = new WebSocket(endpoint)

//    socket.onmessage = function(e){
//     console.log('message',e)
//      console.log('in msg yeeamdosnfi' )
//        var data = JSON.parse(e.data)
//        var bridgeTableId = data.bridgeTableID
//	    var new_status = data.new_bridgeStatus
//
//	    var bstat = $('#bstat')
//	    bstat.html = bridgeTableId
//    }
    socket.onopen = function(e){
        console.log('open',e)
          form.submit(function(event){

            if ( sysName == 'fromBridgeTable' ){
                    event.preventDefault();
                    var bridgeTableID = {{obj.bridgeTableID}}
                    var bridgeStatus = {{obj.Bridge_Status_Choice}}
                   // console.log('sending bridge ID ' + bridgeTableID)
                    //bridgeStatus = bridgeStatus.val()

                    var final_data = {
                        'bridgeTable_ID': bridgeTableID,
                       // 'yes':bridgeStatus
                    }
                    socket.send(JSON.stringify(final_data));
                    }
             else if (sysName == 'fromElevator'){
             }
        });
    }
    socket.onerror = function(e){
        console.log('errorrrrrrrr',e)
    }
    socket.onclose = function(e){
        console.log('socket closing from form.html',e)
    }
