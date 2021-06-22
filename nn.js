// const http = require('http'),
//     fs = require('fs');
// fs.readFile('./page.html', function (err, html) {
//     if (err) {
//         throw err; 
//     }       
//     http.createServer(function(request, response) {  
//         response.writeHeader(200, {"Content-Type": "text/html"});  
//         response.write(html);  
//         response.end();  
//     }).listen(80);
// });

// const express = require('express');
// const app = new express();

// app.get('/', function(request, response){
//     response.sendFile('absolutePathToYour/htmlPage.html');
// });

// You can echo files manually using the fs object, but I'd recommend using the ExpressJS framework to make your life much easier.

// ...But if you insist on doing it the hard way:

// var http = require('http');
// const fs = require('fs');
// const url =require("url")
// var data=fs.readFileSync('page.html','utf8')
// var y= http.createServer((req, res)=>{
//     if (req.url=="/"){
//     res.writeHead(200, {'Content-Type': 'text/html'})
//     res.write(data)}
//     else if(req.url=="/about"){
//         res.write("hello to about");
//     }
//     else if(req.url=="/contact"){
//         res.write("hello to contact page");
//     }
// });
// y.listen((8082),()=>{ 
//     console.log("yes")
// });

// const reads=fs.readFileSync("page.html")

// var server=http.createServer((req,res)=>{
//     res.writeHead(200,{"content-type":"text/html"})
//     res.write(reads)
// }).listen(8080,()=>{
// console.log("listioning")
// })























fetch()