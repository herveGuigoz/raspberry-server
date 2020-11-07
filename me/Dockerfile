FROM node:15.1.0-buster

ENV HOST 0.0.0.0

# Create app directory
RUN mkdir -p /usr/src/me
WORKDIR /usr/src/me

# Prevent the reinstallation of node modules at every changes in the source code.
COPY package.json yarn.lock ./

RUN yarn install

COPY . ./

# for production
RUN yarn build
CMD [ "yarn", "start" ]

# for developpement
# CMD yarn dev

