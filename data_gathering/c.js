const req = require('request');
const fs = require('fs');
const async = require('async');

var is = [];
for(var i = 0; i < 1000; i++)
    is.push(i);


async.eachLimit(is, 5, (i, cb) => {
    var p = fs.createWriteStream('captcha/out' + i + '.jpg');
    p.on('close', x => {
        console.log('done');
        cb();
    });
    req('https://projecteuler.net/captcha/show_captcha.php').pipe(p);
});
