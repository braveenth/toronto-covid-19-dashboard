#!/bin/bash
curl -X POST http://localhost:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@export.ndjson