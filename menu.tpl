<html>
<body>
<h1>Adressaparken demo</h1>

<button onmousedown="httpGetAsync('sound/1')" href="#">Sound speaker 1</button>
<button onmousedown="httpGetAsync('sound/2')" href="#">Sound speaker 2</button>
<button onmousedown="httpGetAsync('sound/3')" href="#">Sound speaker 3</button>
<button onmousedown="httpGetAsync('sound/4')" href="#">Sound speaker 4</button>
<button onmousedown="httpGetAsync('sound/5')" href="#">Sound speaker 5</button>
<button onmousedown="httpGetAsync('sound/6')" href="#">Sound speaker 6</button>
<button onmousedown="httpGetAsync('light/1')" href="#">LED 1</button>
<button onmousedown="httpGetAsync('light/11')" href="#">LED 11</button>
<button onmousedown="httpGetAsync('light/21')" href="#">LED 21</button>
<button onmousedown="httpGetAsync('light/31')" href="#">LED 31</button>
<button onmousedown="httpGetAsync('light/41')" href="#">LED 41</button>
<button onmousedown="httpGetAsync('light/51')" href="#">LED 51</button>
<button onmousedown="httpGetAsync('light/61')" href="#">LED 61</button>
<button onmousedown="httpGetAsync('light/71')" href="#">LED 71</button>
<button onmousedown="httpGetAsync('light/81')" href="#">LED 81</button>
<button onmousedown="httpGetAsync('light/91')" href="#">LED 91</button>


<style>
    button {
      background: #34d97b;
      background-image: -webkit-linear-gradient(top, #34d97b, #32b82b);
      background-image: -moz-linear-gradient(top, #34d97b, #32b82b);
      background-image: -ms-linear-gradient(top, #34d97b, #32b82b);
      background-image: -o-linear-gradient(top, #34d97b, #32b82b);
      background-image: linear-gradient(to bottom, #34d97b, #32b82b);
      -webkit-border-radius: 28;
      -moz-border-radius: 28;
      border-radius: 28px;
      font-family: Arial;
      color: #ffffff;
      font-size: 20px;
      padding: 10px 20px 10px 20px;
      text-decoration: none;
    }

    button:hover {
      background: #3cb0fd;
      background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);
      background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);
      background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);
      background-image: -o-linear-gradient(top, #3cb0fd, #3498db);
      background-image: linear-gradient(to bottom, #3cb0fd, #3498db);
      text-decoration: none;
    }
</style>
    <script>
    function httpGetAsync(theUrl, callback)
    {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() { 
            if (callback!=null && xmlHttp.readyState == 4 && xmlHttp.status == 200)
                callback(xmlHttp.responseText);
        }
        xmlHttp.open("GET", theUrl, true); // true for asynchronous 
        xmlHttp.send(null);
    }
    </script>
</body>
</html>