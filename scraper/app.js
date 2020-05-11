var reviewsCrawler = require('amazon-reviews-crawler')
var fs = require('fs')
let rev = []
let itr = process.argv[2].slice(0,process.argv[2].indexOf('.'));
let id = process.argv[2].slice(process.argv[2].indexOf('.')+1)
console.log(id+' '+itr);
reviewsCrawler(id, {
    page: 'https://www.amazon.com/product-reviews/{{asin}}/?pageNumber='+itr,
    userAgent: 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0',
    elements: {
        // Searches whole page
        productTitle: '.product-title',
        reviewBlock: '.review',

        // Searches within elements.reviewBloc
        review_header: '.review-title',
        review_rating: '.review-rating',
        ratingPattern: 'a-star-',
        review_text: '.review-text',
        review_author: '.review-byline a',
        review_posted_date: '.review-date'
    },

    // Stops crawling when it hits a particular review ID
    // Useful for only crawling new reviews
    stopAtReviewId: false
})
.then(function(result){
    //console.log(result.reviews);
    console.log(result.reviews.length);
    var json = JSON.stringify(result);
    fs.writeFile('scraper/data/datatemp.json',json,'utf8',function(err) {
        if (err) throw err;
            //console.log(result.reviews.length)
            });
})
.catch(console.error);


