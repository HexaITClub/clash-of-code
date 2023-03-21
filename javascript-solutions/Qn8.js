function checkValidName(name) {
    
    if (typeof name !== "string"){
    return -1;
  }
    
  if (typeof name !== "string" && /^[a-zA-Z]+$/.test(name)) {
    return -1;
  }

  // Check if the name consists of two or more words
  const words = name.trim().split(/\s+/);
  if (words.length < 2) {
    return -1;
  }

  return words.length;
}

console.log(checkValidName("Subedi Bibek"))
console.log(checkValidName("Unravel Subedi Bibek"))
console.log(checkValidName("00"))
console.log(checkValidName(00))

// solution by subedibibek