FROM node:15

ENV HOST 0.0.0.0

# Create app directory
RUN mkdir -p /usr/src/me
WORKDIR /usr/src/me

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package.json yarn.lock ./

RUN yarn install

COPY . ./

# for developpement
# CMD yarn dev

# for production
RUN yarn build
CMD yarn start