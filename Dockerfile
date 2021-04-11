FROM alpine:3.7

RUN apk add --no-cache curl

RUN apk add --no-cache python3

WORKDIR /output_data

# COPY get_toronto_covid_data_curl.sh .

COPY main.py .


RUN curl https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/e5bf35bc-e681-43da-b2ce-0242d00922ad?format=json --output /output_data/output_curl.txt

RUN python3 main.py

#CMD ["sh", "get_toronto_covid_data_curl.sh"]
