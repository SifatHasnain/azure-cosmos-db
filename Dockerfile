FROM python:3.7-alpine
# RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY dotnet-install.sh dotnet-install.sh
RUN ["chmod", "+x", "./dotnet-install.sh"] 
RUN apk add bash icu-libs krb5-libs libgcc libintl libssl1.1 libstdc++ zlib && \
    apk add libgdiplus --repository https://dl-3.alpinelinux.org/alpine/edge/testing/ && \
    ./dotnet-install.sh -c Current --runtime aspnetcore 

COPY . .

RUN ["chmod", "+x", "./bulk_insert_app/mockDatagen"]
RUN ["chmod", "+x", "./run.sh"]