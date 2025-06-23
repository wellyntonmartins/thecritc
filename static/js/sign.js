function submitSignin() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (email === "" || password === "") {
    alert("Please, fill in both email password and inputs.");
    return;
  }

  fetch("/signin", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      password: password,
    }),
  });
}

function submitSignup() {
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var repeatPassword = document.getElementById("repeat_password").value;

  if (
    username === "" ||
    email === "" ||
    password === "" ||
    repeatPassword === ""
  ) {
    alert("Please, fill in both email and password inputs.");
    return;
  }

  if (password !== repeatPassword) {
    alert("The passwords must match. Please, try again.");
    return;
  }

  fetch("/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      email: email,
      password: repeatPassword,
    }),
  })
    .then((response) => {
      if (response.ok) {
        alert("Signup successful! You can now sign in.");
        window.location.href = "/signin";
      } else {
        response.json().then((data) => {
          alert("Signup failed: " + data.error);
        });
      }
    })
    .catch((error) => {
      console.error("Error during signup:", error);
      alert("An error occurred during signup. Please try again later.");
    });
  return false;
}
