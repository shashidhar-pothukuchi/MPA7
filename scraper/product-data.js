const Scraper = require("@jonstuebe/scraper");
var fs = require('fs');
let url = process.argv[2];
// run inside of an async function


async function con (){
  const data = await Scraper.scrapeAndDetect(
    url,
  );
  console.log(data);
  let json = JSON.stringify(data);
  fs.writeFile('scraper/data/prodata.json',json,'utf8',function(err) {
    if (err) throw err;
        //console.log(result.reviews.length)
        })
}
con().then(
  
);