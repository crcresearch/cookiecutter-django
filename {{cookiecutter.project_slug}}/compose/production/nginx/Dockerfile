FROM node:lts-alpine as build-stage

# Make sure to include the variables from NGINX.
ARG BASE_URL
ARG VUE_APP_API_PATH
ARG VUE_APP_BACKEND_PATH

# Copy build files.
COPY ./{{cookiecutter.VUE_APP_DIR}} /app

# make the 'app' folder the current working directory
WORKDIR /app

# Install and build.
RUN npm install && npm run build && npm run generate

# PRODUCTION-STAGE
FROM nginx:stable-alpine as production-stage

# Copy the dist folder from the build-stage into app.
COPY --from=build-stage /app/dist /app

# Copy a default nginx.conf with all the necessary configurations.
COPY ./compose/production/nginx/nginx.conf /etc/nginx/nginx.conf