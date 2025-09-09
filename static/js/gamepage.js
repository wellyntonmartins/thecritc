const rateDivs = document.getElementsByClassName("rate-note");
const textRate = document.getElementById("text-rate");
const bigNumberRate = document.getElementById("bignumber-rate");
const userRate = document.getElementById("user-rate");
const avgBigNumberRate = document.getElementById("avg-bignumber-rate");
const rateCommentSquare = document.getElementsByClassName("rate-square");
let hasRated = false;
let loadedRate = false;
let currentRating = -1;

function applyRatingVisuals(index) {
  bigNumberRate.style.border = "none";

  let color;

  if (index <= 2) {
    color = "#ff6874";
  } else if (index <= 5) {
    color = "#ffbd3f";
  } else {
    color = "#00ce7a";
  }

  for (let i = 0; i <= index; i++) {
    rateDivs[i].style.background = color;
  }

  if (hasRated) {
    for (let i = index + 1; i < rateDivs.length; i++) {
      if (i <= 2) {
        rateDivs[i].style.background = "#ffc3c7";
      } else if (i <= 5) {
        rateDivs[i].style.background = "#ffe5b2";
      } else {
        rateDivs[i].style.background = "#99ebca";
      }
    }
  }

  switch (index) {
    case 0:
      textRate.innerHTML = "So bad, don't play!";
      bigNumberRate.innerHTML = "1";
      bigNumberRate.style.background = "#ff6874";
      break;
    case 1:
      textRate.innerHTML = "So bad, you mustn't play it";
      bigNumberRate.innerHTML = "2";
      bigNumberRate.style.background = "#ff6874";
      break;
    case 2:
      textRate.innerHTML = "Bad game, don't recommend";
      bigNumberRate.innerHTML = "3";
      bigNumberRate.style.background = "#ff6874";
      break;
    case 3:
      textRate.innerHTML = "Must be better than this";
      bigNumberRate.innerHTML = "4";
      bigNumberRate.style.background = "#ffbd3f";
      break;
    case 4:
      textRate.innerHTML =
        "Must be better than this, but isn't a horrible game";
      bigNumberRate.innerHTML = "5";
      bigNumberRate.style.background = "#ffbd3f";
      break;
    case 5:
      textRate.innerHTML = "Median game. Good to play for a while";
      bigNumberRate.innerHTML = "6";
      bigNumberRate.style.background = "#ffbd3f";
      break;
    case 6:
      textRate.innerHTML = "Liked, the game delivers what it promises";
      bigNumberRate.innerHTML = "7";
      bigNumberRate.style.background = "#00ce7a";
      break;
    case 7:
      textRate.innerHTML = "Very good game. Everyone must play it one day";
      bigNumberRate.innerHTML = "8";
      bigNumberRate.style.background = "#00ce7a";
      break;
    case 8:
      textRate.innerHTML = "Without words!! This game is incredible";
      bigNumberRate.innerHTML = "9";
      bigNumberRate.style.background = "#00ce7a";
      break;
    case 9:
      textRate.innerHTML = "Perfect game!!!!";
      bigNumberRate.innerHTML = "10";
      bigNumberRate.style.background = "#00ce7a";
      break;
    default:
  }
}

function resetRatingVisuals() {
  if (hasRated) return; // Não resetar se já avaliou

  textRate.innerHTML = "Hover to put your note";
  bigNumberRate.innerHTML = "";
  bigNumberRate.style.background = "#f5f5f7";
  bigNumberRate.style.border = "1.5px solid #8e8e93";

  // Resetar cores conforme sua lógica original
  for (let i = 0; i < rateDivs.length; i++) {
    if (i <= 2) {
      rateDivs[i].style.background = "#ffc3c7";
    } else if (i <= 5) {
      rateDivs[i].style.background = "#ffe5b2";
    } else {
      rateDivs[i].style.background = "#99ebca";
    }
  }
}

document.addEventListener("DOMContentLoaded", function (event) {
  if (avgBigNumberRate.innerHTML <= 30) {
    avgBigNumberRate.style.background = "#ff6874";
  } else if (avgBigNumberRate.innerHTML <= 60) {
    avgBigNumberRate.style.background = "#ffbd3f";
  } else {
    avgBigNumberRate.style.background = "#00ce7a";
  }

  Array.from(rateCommentSquare).forEach((square) => {
    if (square.innerHTML <= 3) {
      square.style.background = "#ff6874";
    } else if (square.innerHTML <= 6) {
      square.style.background = "#ffbd3f";
    } else {
      square.style.background = "#00ce7a";
    }
  });

  if (userRate && userRate.value != "") {
    loadedRate = true;
    rateDivs[userRate.value - 1].click();
  }
});

Array.from(rateDivs).forEach((div, index) => {
  div.addEventListener("click", function () {
    hasRated = true;
    currentRating = index;
    const idGame = document.getElementById("id-game").value;

    applyRatingVisuals(index);

    if (!loadedRate == true) {
      fetch(`/register_rate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id_game: idGame,
          rating: bigNumberRate.innerHTML,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log("Rate successfuly registered!");
          } else {
            alert("Error registering rate");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("Error registering rate");
        });
    }

    loadedRate = false;
  });

  div.addEventListener("mouseenter", function () {
    if (!hasRated) {
      applyRatingVisuals(index);
    }
  });

  div.addEventListener("mouseleave", function () {
    if (!hasRated) {
      resetRatingVisuals();
    }
  });
});
