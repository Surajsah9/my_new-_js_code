// const fetch = require('node-fetch');

const getReddit = async () => {
	const response = await fetch('https://saral.navgurukul.org/api/courses/74/exercises');
	const body = await response.json();
	console.log(body); // prints a chock full of HTML richness
	return body;};

// const fetch = require('node-fetch');
// const cheerio = require('cheerio');

// const getReddit = async () => {
//   // get html text from reddit
//   const response = await fetch('https://www.imdb.com/chart/top/');
//   // using await to ensure that the promise resolves
//   const body = await response.text();

//   // parse the html text and extract titles
//   const s = cheerio.load(body);
//   const titleList = [];
    
//   // using CSS selector  
//   s('._eYtD2XCVieq6emjKBH3m').each((i, title) => {
//     const titleNode = s(title);
//     const titleText = titleNode.text();
    
//     titleList.push(titleText);
//   });

//   console.log(titleList);
// };

// getReddit();

