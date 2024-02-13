// 1번 별
for (i = 0; i < 5; i++) {
    let stars = "";
  
    for (j = 0; j <= i; j++) {
      stars += "*";
    }
  
    console.log(stars);
  }
  
  // 2번 별
  for (i = 0; i < 5; i++) {
    let stars = "";
  
    for (j = 0; j <= i; j++) {
      stars += "*";
    }
  
    console.log(stars);
  }
  for (i = 4; i >= 0; i--) {
    let stars = "";
  
    for (j = 0; j <= i; j++) {
      stars += "*";
    }
  
    console.log(stars);
  }
  
  // // 3번 별
  for (i = 0; i < 5; i++) {
    let stars = "";
  
    for (j = 5; j > i; j--) {
      stars += " ";
    }
    for (k = 0; k < 2 * i + 1; k++) {
      stars += "*";
    }
    console.log(stars);
  }
  for (i = 5; i >= 0; i--) {
    let stars = "";
  
    for (j = 5; j > i; j--) {
      stars += " ";
    }
    for (k = 0; k < 2 * i + 1; k++) {
      stars += "*";
    }
    console.log(stars);
  }