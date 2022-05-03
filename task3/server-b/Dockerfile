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


# Set the HOSTs and PORTs environment variables for Server-A and Server-B.
ENV SERVER_A_HOST="172.24.24.3"
ENV SERVER_A_PORT="2000"
ENV SERVER_B_HOST="127.0.0.1"
ENV SERVER_B_PORT="3000"

EXPOSE 3000
CMD [ "node", "index.js" ]
