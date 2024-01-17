// static/clipboard.js
function copyToClipboard() {
  /* Get the text field */
  var passwordField = document.getElementById("password");

  /* Create a range and select the text field */
  var range = document.createRange();
  range.selectNode(passwordField);

  try {
    /* Use the Clipboard API to copy the text inside the text field */
    navigator.clipboard.writeText(passwordField.innerText);

    /* Change the icon and text */
    var copyButton = document.querySelector(".copy-btn");
    copyButton.innerHTML = '<i class="fas fa-check"></i> Copied!';

    /* Disable further clicks on the button */
    copyButton.disabled = true;

    /* Optionally: Automatically revert the button state after a few seconds */
    setTimeout(function () {
      copyButton.innerHTML = '<i class="fas fa-copy"></i> Copy to Clipboard';
      copyButton.disabled = false;
    }, 3000); // Revert after 3 seconds (adjust as needed)
  } catch (err) {
    console.error("Unable to copy to clipboard:", err);
    /* Handle the error here, e.g., show an error message to the user */
  }
}
