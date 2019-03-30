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


//
 socket.onopen = function(e){
        console.log('open',e)
          form.submit(function(event){
            // event.preventDefault();
            var final_data
            <!--var result = document.myform.PCA_Status_Choice.value-->
            <!--alert(result)-->
             <!--var bridgeStatus = '{{obj.Bridge_Status_Choice}}'-->
                    <!--var pcaStatus = '{{obj.PCA_Status_Choice}}'-->
                    <!--var gpuStatus = '{{obj.GPU_Status_Choice}}'-->

            // if updating bridge table
            if ( '{{path}}' === 'fromBridgeTable' ){
                    var bridgeTableID = {{obj.bridgeTableID}}
                    var bridgeStatus = document.myform.Bridge_Status_Choice.value
                    var pcaStatus = document.myform.PCA_Status_Choice.value
                    var gpuStatus = document.myform.GPU_Status_Choice.value
                     final_data = {
                        'bridgeTableID': bridgeTableID,
                        'bridgeStat':bridgeStatus,
                        'pcaStat': pcaStatus,
                        'gpuStat': gpuStatus,
                    }
                    <!--socket.send(JSON.stringify(final_data));-->
                 }
             else ('{{path}}' === 'fromElevator'){

                    var elevatorID = {{obj.elevatorID}}
                    var elevatorStatus = document.myform.Escalator_Status_Choice.value
                      final_data = {
                        'elevatorID': elevatorID,
                        'elevatorStat':elevatorStatus,
                    }

                    console.log('sent from form')
             }
             socket.send(JSON.stringify(final_data));
        });
    }