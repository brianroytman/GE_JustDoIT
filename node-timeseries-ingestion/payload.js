/*
Payload - a set of datapoints to be ingested to Predix Timeseries
see: https://www.predix.io/docs/?r=266347#lZ1d8Ub for more info.

<MessageID> - (Required) can be string or int (between 0-2^64), and must be unique
<tagName> - (Required) Name of the tag
<Timestamp> - (Required) unix timestamp (time since epoch) in milliseconds
<Measure> - (Required) Numeric value
<Quality> - (Required) Quality of the data [0, 1, 2, 3]
  0 - Bad quality
  1 - Uncertain quality
  2 - Not applicable
  3 - Good quality (Default)
<Attribute> - (Optional) Any data associated with a tag.
  ex. "uri": "/assets/1"

You can include multiple datapoints in one payload.

*/
var payload =
{
   "messageId": "<MessageID>",
   "body":[
      {
         "name":"<tagName>",
         "datapoints":[
            [
               <Timestamp>,
               <Measure>,
               <Quality>
            ]
         ],
         "attributes":{
            "AttributeKey1": "AttributeValue1",
            "AttributeKey2": "AttributeValue2",
         }
      }
   ]
};

module.exports = payload;
