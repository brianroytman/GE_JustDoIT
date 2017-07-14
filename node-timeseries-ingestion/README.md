node-timeseries-ingestion
=========================

A simple ingestion tool for Predix Time Series using Node.js and the [websocket](https://www.npmjs.com/package/ws) library.

Ingests a hand-crafted payload (with as many tags and datapoints as you'd like) into Time Series.

Easily extensible to import bulk data in any format.

## Usage
+ Clone this repository
+ `npm install` to install dependencies
+ You'll need a UAA client with permission to ingest into timeseries. This means you'll have to update the client *authorities* with the correct scopes (permissions). You can find these by looking at the VCAP_SERVICES for predix-timeseries when running `cf env` on an app that timeseries is bound do.
  + Example: `uaac client update <clientName> --authorities "<oldAuthorities> timeseries.zones.<zoneId>.ingest timeseries.zones.<zoneId>.user"`
+ Configure your connection to the Time Series ingestion service in `config.js` by filling out
  + `endpoint` - ingestion URL (can also be found in VCAP_SERVICES)
  + Authorization `token` from the client with ingest permission
  + `Predix-Zone-Id` of your timeseries instance
  + `useProxy` - `true` or `false` - use system http_proxy environment variable (enables the app to work while on BLUESSO)
    + Default is `true` - If you're not using a proxy, make sure to set it to false.
+ Create your payload in `payload.js`
  + You can modify `payload.js` to create a payload in any way, as long as it exports a JSON object adhering to the correct payload format
  + The correct format is detailed in `payload.js`
  + You can also review the guidelines here: https://www.predix.io/docs/?r=266347#lZ1d8Ub
+ Run `node app.js` to send the data in `payload.js` to Time Series


Switch to the `example-bulk-import` branch for an example modification for *bulk data ingestion* in `bulk.js`

## Author
Alexander Wong (alexander.wong@ge.com)
