<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="UTF-8">
  <style>

    /*  -------------------------------------------------------
      :: Colour definition
      -------------------------------------------------------*/
    :root {
        --light-color: red;
        --sound-color: green;
        --video-color: blue;
      }
    /* -------------------------------------------------------*/

    * {
      margin: 0;
      -webkit-transition: .3s;
      transition: .3s ease 0s;
      color: black;
      background-color: #FFF;
    }

    .header {
      margin: 12px auto;
    }

    h1 {
      font: 20px Helvetica, sans-serif;
      font-weight: lighter;
      text-align: center;
    }

    h1 > #bold {
      font-weight: bold;
    }

    .tabs > button.active {
      border-bottom: medium solid rgba(255,100,0,.3);
      font-size: 14px;
      color: #111;
    }

    .tablink {
        display:table-row-group;
        border: none;
        outline: none;
        cursor: pointer;
        padding: 8px 16px;
        font-size: 13px;
        width: 25%;
        color: #666;
    }

    .tabs {
      width: 100%;
      margin: auto;
      text-align: center;
      position: fixed;
      bottom: 0px;
      padding-bottom: 10px;
    }

    .container > .tabcontent {
      display: none;
      padding: 20px;
      text-align: center;
      height: 100%;
      width: 100%;
      margin-bottom: 30px;
    }

    #light, #light > * {
      color: var(--light-color);
    }
    #sound, #sound > * {
      color: var(--sound-color);
    }
    #video, #video > * {
      color: var(--video-color);
    }

    #light > button {
      border-color: var(--light-color);
    }

    #sound > button {
      border-color: var(--sound-color);
    }

    #video > button {
      border-color: var(--video-color);
    }

    .container{
      overflow: scroll;
      display: flex;
      flex-flow: row wrap;
      justify-content: flex-end;
      align-items: center;
    }

    .container > * {
      margin: auto;
    }

    .tabcontent > button {
      width: 120px;
      height: 45px;
      margin: 5px 5px;
      border: .5px solid white;
      border-radius: 2px;
    }

    .tabcontent > button:active {
      color: #FFF;
      border-top-width: 6px;
      border-bottom-width: 6px;
      -webkit-transition: .1s;
      transition: .1s ease 0s;
    }

    *:focus { outline:0 !important; }
    /*  -------------------------------------------------------
      :: Mobile Specific Styling
      -------------------------------------------------------*/


    /*  -------------------------------------------------------
        :: Desktop Specific Styling
        -------------------------------------------------------*/
    @media screen and (min-width: 1000px) {

      .tabcontent > button{
        width: 200px;
      }

      .tabs {
        position: fixed;
        bottom: 2px;
      }
    }
  </style>
  <title>Adressaparken Demo</title>
</head>
<body>
  <div class="header">
    <h1>ADRESSA<span id="bold">PARKEN</span> DEMO</h1>
  </div>
  <div class="container">
    <div id="light" class="tabcontent">
      <button onmousedown="httpGetAsync('lightrandom/1')">LED 1</button>
      <button onmousedown="httpGetAsync('lightrandom/11')">LED 11</button>
      <button onmousedown="httpGetAsync('lightrandom/21')">LED 21</button>
      <button onmousedown="httpGetAsync('lightrandom/31')">LED 31</button>
      <button onmousedown="httpGetAsync('lightrandom/41')">LED 41</button>
      <button onmousedown="httpGetAsync('lightrandom/51')">LED 51</button>
      <button onmousedown="httpGetAsync('lightrandom/61')">LED 61</button>
      <button onmousedown="httpGetAsync('lightrandom/71')">LED 71</button>
      <button onmousedown="httpGetAsync('lightrandom/81')">LED 81</button>
      <button onmousedown="httpGetAsync('lightrandom/91')">LED 91</button>
      <button onmousedown="httpGetAsync('lightall/0/0/40')">LED all blue</button>
      <button onmousedown="httpGetAsync('lightall/255/255/255')">LED all white</button>
      <button onmousedown="httpGetAsync('lightallrandom')">LED all random</button>
    </div>
    <div id="sound" class="tabcontent">
        <button onmousedown="httpGetAsync('sound/3')">Speaker 1</button>
        <button onmousedown="httpGetAsync('sound/4')">Speaker 2</button>
        <button onmousedown="httpGetAsync('sound/5')">Speaker 3</button>
        <button onmousedown="httpGetAsync('sound/6')">Speaker 4</button>
        <button onmousedown="httpGetAsync('sound/7')">Speaker 5</button>
        <button onmousedown="httpGetAsync('sound/8')">Speaker 6</button>
      </div>
      <div id="video" class="tabcontent">
          <p> nothing yet </p>
      </div>
    </div>
  <div class='tabs'>
    <button class="tablink" onclick="openTab('light', event)" id="defaultOpen">Light</button>
    <button class="tablink" onclick="openTab('sound', event)">Sound</button>
    <button class="tablink" onclick="openTab('video', event)">Video</button>
  </div>
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

        function openTab(name, evt) {
            // Declare all variables
            var i, tabcontent, tablinks;

            // Get all elements with class="tabcontent" and hide them
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
            }

            // Get all elements with class="tablinks" and remove the class "active"
            tablinks = document.getElementsByClassName("tablink");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }

            // Show the current tab, and add an "active" class to the button that opened the tab
            document.getElementById(name).style.display = "block";
            evt.currentTarget.className += " active";
        }
        // Get the element with id="defaultOpen" and click on it
        document.getElementById("defaultOpen").click();
      </script>
  </body>
</html>
