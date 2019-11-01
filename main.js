my_word = mais

function ask_for_data() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "https://eae84c8226604a85a54cdddcb25bc5fa.vfs.cloud9.us-east-1.amazonaws.com/checkword/api/v1/task?word=" + my_word, true);
  xhttp.send();
}