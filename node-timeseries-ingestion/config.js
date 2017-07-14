var config = {};
config.predix = {};
config.predix.timeseries = {};

// * Time Series config *
// endpoint - ingestion WebSocket url for your instance of Time Series.
//   ex. wss://gateway-predix-data-services.run.asv-pr.ice.predix.io/v1/stream/messages
// <token> - token received from UAA instance connected with Time Series, must include ingestion scope
// <Predix-Zone-Id> - Predix-Zone-Id
config.predix.timeseries.endpoint = '<your ingestion url>';
config.predix.timeseries.authToken = '<your authorization token>';
config.predix.timeseries.zoneId = '<Predix-Zone-Id>';

// * Proxy config *
// Set the following to true if you want to use your system http_proxy
config.useProxy = true;
// HTTP/HTTPS proxy to connect to
// Default uses environment variable
if (process.env.http_proxy){
  config.proxy = process.env.http_proxy;
} else {
  config.proxy = "<other proxy>";
}
if (config.useProxy){
  console.log('[INFO] Using proxy server %j', config.proxy);
}

module.exports = config;
