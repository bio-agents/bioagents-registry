FROM node:11.15.0
#FROM node:14.15.4
#FROM node:4.7.2

LABEL maintainer="chen xingqiang <hans@bioagents.tech>"

RUN useradd --user-group --create-home bioagents

ENV HOME=/home/bioagents

WORKDIR $HOME/frontend

RUN mkdir components/ css/ dist/ images/ img/ js/ json/ lib/ partials/ resources/ static/
COPY components components/
COPY css css/
COPY dist dist/
COPY images images/
COPY img img/
COPY js js/
COPY json json/
COPY lib lib/
COPY partials partials/
COPY resources resources/
COPY static static/
COPY bower.json gulpfile.js index-async.html index.html package.json package-lock.json /home/bioagents/frontend/

RUN chown -R bioagents:bioagents $HOME/*
USER bioagents

RUN npm config set prefix /usr/local && npm install && export PATH="./node_modules/.bin:$PATH" && bower install

# Required to work on Linux, otherwise there are permission errors
USER root
RUN chown -R bioagents:bioagents $HOME/*

CMD ["node_modules/.bin/gulp"]