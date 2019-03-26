// handling websocket for airline employees

 //console.log(window.location)
var loc = window.location
//var form = $('#formData')
var wsStart = 'ws://'
if (loc.protocol == 'https:'){
    wsStart = 'wss://'
}
var endpoint = wsStart + loc.host + loc.pathname
console.log(loc.host)
console.log(loc.pathname)

 var socket = new WebSocket(endpoint)
//
//   socket.onmessage = function(e){
//     console.log('messageeeeeeeeee',e)
//        var data = JSON.parse(e.data)
//        var bridgeTableId =  data.bridgeTableID
//	    //var new_status = data.new_bridgeStatus
//    console.log(bridgeTableId)
//
//    var bridgeStat = 'bridge ' + bridgeTableId
//      console.log(bridgeStat)
//    bridgeStat = bridgeStat.toString()
//   var index = document.getElementsByClassName(bridgeStat)[0]
//   //$('.bridge ' + bridgeStat)
//   index.setAttribute("src","{% static "systems/green.png"%}")
//   console.log(index)
//  //var index = $('#newTing')
//  //  index.attr("src",'{% static "systems/green.png" %}')
//
//    }
    socket.onopen = function(e){
        console.log('opennnnnnnnnnnnn',e)
        }
//
//     socket.onerror = function(e){
//        console.log('error',e)
//    }
//    socket.onclose = function(e){
//        console.log('closedddddddddddddddddd',e)
//    }
