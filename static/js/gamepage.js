const rateDivs = document.getElementsByClassName("rate-note");
const textRate = document.getElementById("text-rate");
const bigNumberRate = document.getElementById("bignumber-rate");

console.log(textRate);

// For all the rate-bar section (change colors)
Array.from(rateDivs).forEach((div, index) => {
  div.addEventListener("mouseenter", function () {
    bigNumberRate.style.border = "none";
    switch (index) {
      case 0:
        textRate.innerHTML = "So bad, don't play!";
        rateDivs[0].style.background = "#ff6874";
        bigNumberRate.innerHTML = "1";
        bigNumberRate.style.background = "#ff6874";
        break;
      case 1:
        textRate.innerHTML = "So bad, you mustn't play it";
        bigNumberRate.innerHTML = "2";
        bigNumberRate.style.background = "#ff6874";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ff6874";
        }
        break;
      case 2:
        textRate.innerHTML = "Bad game, don't recommend";
        bigNumberRate.innerHTML = "3";
        bigNumberRate.style.background = "#ff6874";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ff6874";
        }
        break;
      case 3:
        textRate.innerHTML = "Must be better than this";
        bigNumberRate.innerHTML = "4";
        bigNumberRate.style.background = "#ffbd3f";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ffbd3f";
        }
        break;
      case 4:
        textRate.innerHTML =
          "Must be better than this, but isn't a horrible game";
        bigNumberRate.innerHTML = "5";
        bigNumberRate.style.background = "#ffbd3f";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ffbd3f";
        }
        break;
      case 5:
        textRate.innerHTML = "Median game. Good to play for a while";
        bigNumberRate.innerHTML = "6";
        bigNumberRate.style.background = "#ffbd3f";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ffbd3f";
        }
        break;
      case 6:
        textRate.innerHTML = "Liked, the game delivers what it promises";
        bigNumberRate.innerHTML = "7";
        bigNumberRate.style.background = "#00ce7a";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#00ce7a";
        }
        break;
      case 7:
        textRate.innerHTML = "Very good game. Everyone must play it one day";
        bigNumberRate.innerHTML = "8";
        bigNumberRate.style.background = "#00ce7a";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#00ce7a";
        }
        break;
      case 8:
        textRate.innerHTML = "Without words!! This game is incredible";
        bigNumberRate.innerHTML = "9";
        bigNumberRate.style.background = "#00ce7a";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#00ce7a";
        }
        break;
      case 9:
        textRate.innerHTML = "Perfect game!!!!";
        bigNumberRate.innerHTML = "10";
        bigNumberRate.style.background = "#00ce7a";
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#00ce7a";
        }
        break;
      default:
    }
  });

  div.addEventListener("mouseleave", function () {
    textRate.innerHTML = "Hover to put your note";
    bigNumberRate.innerHTML = "";
    bigNumberRate.style.background = "#f5f5f7";
    bigNumberRate.style.border = "1.5px solid #8e8e93";
    switch (index) {
      case 0:
        rateDivs[0].style.background = "#ffc3c7";
        break;
      case 1:
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ffc3c7";
        }
        break;
      case 2:
        for (i = 0; i <= index; i++) {
          rateDivs[i].style.background = "#ffc3c7";
        }
        break;
      case 3:
        for (i = 0; i <= index; i++) {
          if (i <= 2) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i == 3) {
            rateDivs[i].style.background = "#ffe5b2";
          }
        }
        break;
      case 4:
        for (i = 0; i <= index; i++) {
          if (i <= 2 && i < 3) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i >= 3) {
            rateDivs[i].style.background = "#ffe5b2";
          }
        }
        break;
      case 5:
        for (i = 0; i <= index; i++) {
          if (i <= 2 && i < 3) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i >= 3) {
            rateDivs[i].style.background = "#ffe5b2";
          }
        }
        break;
      case 6:
        for (i = 0; i <= index; i++) {
          if (i <= 2 && i < 3) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i >= 3 && i < 6) {
            rateDivs[i].style.background = "#ffe5b2";
          } else if (i == 6) {
            rateDivs[i].style.background = "#99ebca";
          }
        }
        break;
      case 7:
        for (i = 0; i <= index; i++) {
          if (i <= 2 && i < 3) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i >= 3 && i < 6) {
            rateDivs[i].style.background = "#ffe5b2";
          } else if (i >= 6) {
            rateDivs[i].style.background = "#99ebca";
          }
        }
        break;
      case 8:
        for (i = 0; i <= index; i++) {
          if (i <= 2 && i < 3) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i >= 3 && i < 6) {
            rateDivs[i].style.background = "#ffe5b2";
          } else if (i >= 6) {
            rateDivs[i].style.background = "#99ebca";
          }
        }
        break;
      case 9:
        for (i = 0; i <= index; i++) {
          if (i <= 2 && i < 3) {
            rateDivs[i].style.background = "#ffc3c7";
          } else if (i >= 3 && i < 6) {
            rateDivs[i].style.background = "#ffe5b2";
          } else if (i >= 6) {
            rateDivs[i].style.background = "#99ebca";
          }
        }
        break;
      default:
        console.log("Índice não tratado:", index);
    }
  });
});
