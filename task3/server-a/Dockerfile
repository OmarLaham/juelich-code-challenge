# Pull node:10-alpine image
FROM node:10-alpine

# Create node_modules directory and apply needed changes to permissions
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

# Create app directory
WORKDIR /home/node/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

USER node

RUN npm install

# Bundle app source and copy so files are owned by user node from group node
COPY --chown=node:node . .

# Set the PORT and BASE_URL environment variables to control PORT and BASE_URL.
# PG_DATABASE and PG_USER are exported as environment variables by the db server
ENV PORT="2000"
ENV PG_HOST="172.24.24.2"
ENV PG_PORT="5432"
ENV PG_USER="postgres"
ENV PG_PASSWORD="kC6FM,{36k%{9t#9"
ENV PG_DATABASE="initdb"

EXPOSE 2000
CMD [ "node", "index.js" ]
