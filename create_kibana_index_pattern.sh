#!/bin/bash
curl -X POST "localhost:5601/api/saved_objects/index-pattern/filebeat"  -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '
{
  "attributes": {
    "title": "filebeat-*",
    "timeFieldName": "@timestamp"
  }
}'