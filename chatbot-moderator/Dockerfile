# Copyright 2019, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.

# build stage
FROM mhart/alpine-node:10 as build-stage
WORKDIR /app
COPY package.json package-lock.json ./
# ENV VUE_APP_DEMO_ENABLED=true
ENV VUE_APP_ROOT_API=https://localhost:9999


RUN npm install
RUN npm audit
COPY . .
RUN npm run build

# production stage
FROM nginx:1.15.8-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/project.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/project-ssl.conf /etc/nginx/conf.d/ssl.conf
COPY ./key.pem /etc/ssl/key.pem
COPY ./cert.pem /etc/ssl/certificate.pem
EXPOSE 80
EXPOSE 443

RUN apk --no-cache add curl
HEALTHCHECK --timeout=5s CMD curl -k --fail https://client/status || exit 1

CMD ["nginx", "-g", "daemon off;"]
