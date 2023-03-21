const fs = require("fs");

fs.readFile("coc.txt", "utf-8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const count = (data.match(/\bthe\b/gi) || []).length;

  console.log(`The word "the" appears ${count} times in the file.`);
});


//Solution by Subedi Bibek