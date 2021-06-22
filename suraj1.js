const { Console } = require("console")
const fs =require("fs")
const s= fs.readFileSync("suraj/content1.json","utf8")
// const y = s.toString
console.log(s)
// for(j in y){
//     console.log(j);
//     for(i in j){
//         console.log(i)
//     }
// }