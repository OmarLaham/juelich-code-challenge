FROM node:18

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

# Set the PORT and BASE_URL environment variables to control PORT and BASE_URL.
ENV PORT="5000"
ENV BASE_URL="/conabio"

EXPOSE 5000
CMD [ "node", "index.js" ]
