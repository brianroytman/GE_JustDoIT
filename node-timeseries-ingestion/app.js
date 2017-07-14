var WebSocket = require('ws');
var url = require('url');
var HttpsProxyAgent = require('https-proxy-agent');

var payload = require('./payload');
var config = require('./config');

// WebSocket endpoint for the proxy to connect to
var endpoint = config.predix.timeseries.endpoint;
console.log('[INFO] attempting to connect to WebSocket %j', endpoint);

var headers = {
  'Authorization': 'Bearer ' + config.predix.timeseries.authToken,
  'Predix-Zone-Id': config.predix.timeseries.zoneId,
  'Origin': 'http://localhost'
};

// finally, initiate the WebSocket connection
if (config.useProxy) {
  // create an instance of the `HttpsProxyAgent` class with the proxy server information
  var opts = url.parse(config.proxy);
  var agent = new HttpsProxyAgent(opts);
  var socket = new WebSocket(endpoint, { agent: agent, headers: headers });
} else {
  var socket = new WebSocket(endpoint, { headers: headers });
}

// Send the payload upon opening a valid connecion to the ingestion socket
socket.on('open', function open() {
  console.log("[INFO] sending payload...");
  socket.send(JSON.stringify(payload), function ack(error) {
    if (error) {
      console.log("[INFO] Error sending payload.");
    } else {
      console.log("[INFO] payload sent." );
    }
  });
});

// Upon response from the websocket
socket.on('message', function(data, flags) {
  /* Print response
  {
    "statusCode": <AcknowledgementStatusCode>,
    "messageId": <MessageID>
  }
  Status codes:
    202 Accepted successfully
    200 Bad Request
    401 Unauthorized
    413 Request entity too large (payload cannot exceed 512KB)
    503 Failed to ingest data
  */
  console.log("[INFO] Acknowledgement Message:");
  console.log(JSON.stringify(JSON.parse(data), null, 2));
  // Exit after we received a reponse
  process.exit();
});
