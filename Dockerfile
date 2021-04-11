FROM alpine:3.7

RUN apk add --no-cache curl

WORKDIR /output_data

# COPY get_toronto_covid_data_curl.sh .

RUN curl https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/e5bf35bc-e681-43da-b2ce-0242d00922ad?format=json --output /output_data/output.txt

#CMD ["sh", "get_toronto_covid_data_curl.sh"]
