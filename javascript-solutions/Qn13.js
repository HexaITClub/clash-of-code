function printWords(words) {
    if (words === "") {
      console.log("[empty]");
    } else {
      const wordstoarray = words.split(" ");
      for (let i = 0; i < wordstoarray.length; i++) {
        console.log(wordstoarray[i]);
      }
    }
  }
  
  
  printWords('Bibek')
  printWords('Subedi')
  printWords('Bibek Subedi')

// solution by subedibibek