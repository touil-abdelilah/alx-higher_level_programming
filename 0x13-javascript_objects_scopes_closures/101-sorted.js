#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

Object.keys(dict).forEach(userId => {
  const occurrence = dict[userId];
  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }
  sortedDict[occurrence].push(userId);
});

console.log(sortedDict);
