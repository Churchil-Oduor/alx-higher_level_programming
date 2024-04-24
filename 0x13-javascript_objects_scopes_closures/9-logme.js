#!/usr/bin/node

exports.logMe = function (item) {

  let count = 0; 
  function increase () {
    count++;
  }
  
  increase();
  console.log(`${count}: ${item}`);
} ();

