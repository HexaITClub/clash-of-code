function isPalindrome(word) {
    const reversed = word.split("").reverse().join("");
    return word === reversed;
  }
  
  
  console.log(isPalindrome("ear")); 
  console.log(isPalindrome("noon")); 


  // solution by subedibibek