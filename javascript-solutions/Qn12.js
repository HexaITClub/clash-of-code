function calculateProduct(num1, num2) {
    let result = 0;
    for (let i = 0; i < num2; i++) {
      result += num1;
    }
    return result;
  }
  
  console.log(calculateProduct(2, 2)); // Output: 4
  console.log(calculateProduct(4, 2)); // Output: 8