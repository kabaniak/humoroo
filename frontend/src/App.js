import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {

        var xhr = null;
    function getXmlHttpRequestObject() {
        if (!xhr) {
            // Create a new XMLHttpRequest object 
            xhr = new XMLHttpRequest();
        }
        return xhr;
    };

    function dataCallback() {
        // Check response is ready or not
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log("Word data received!");
            
            console.log(xhr.responseText);
        }
    }

    function getWords() {
        console.log("Get words...");
        xhr = getXmlHttpRequestObject();
        xhr.onreadystatechange = dataCallback;
        // asynchronous requests
        xhr.open("GET", "http://localhost:5000/users", true);
        // Send the request over the network
        xhr.send(null);
    }

    const sendDataCallback = () => {
        // Check response is ready or not
        if (xhr.readyState == 4 && xhr.status == 201) {
            console.log("Data creation response received!");
            console.log(xhr.responseText);
        }
    }

    const sendData = () => {
        var noun1 = document.getElementById('noun-1').value;
        var noun2 = document.getElementById('noun-2').value;

        if (!noun1 || !noun2) {
            console.log("Data is empty.");
            return;
        }
        console.log("Sending data: " + noun1 +" and "+noun2);
        xhr = getXmlHttpRequestObject();
        xhr.onreadystatechange = sendDataCallback;
        // asynchronous requests
        xhr.open("POST", "http://localhost:5000/users", true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        // Send the request over the network
        xhr.send(JSON.stringify({"data": {"noun1": noun1, "noun2": noun2}}));
    }

    return (
        <div className="App">
        <img src="/humoroo_logo_hires.jpeg" alt="header" width="50%"/>
        <form>
            <div className="form-group" id="word-input">
            <div className="row">
                <div className="col-sm"></div>
                <div className="col-sm">
                <input type="text" className="form-control" id="noun-1" placeholder="Noun #1"></input>
                </div>
                <div className="col-sm">
                <input type="text" className="form-control" id="noun-2" placeholder="Noun #2"></input>
                </div>
                <div className="col-sm" id="shuffle-button">
                </div>
            </div>
            </div>

            <div className="form-group">
            <div className="row">
                <div className="col-sm"></div>
                <div className="col-sm">
                <select class="custom-select my-2" id="selectNounType">
                    <option selected>Choose type...</option>
                    <option value="1">Person</option>
                    <option value="2">Place</option>
                    <option value="3">Event</option>
                    <option value="4">Thing</option>
                </select>
                </div>
                <div className="col-sm">
                <select class="custom-select my-2" id="selectNounType">
                    <option selected>Choose type...</option>
                    <option value="1">Person</option>
                    <option value="2">Place</option>
                    <option value="3">Event</option>
                    <option value="4">Thing</option>
                </select>
                </div>
                <div className="col-sm"></div>
            </div>
            </div>
        </form>
        <button type="button" className="btn btn-info" id="generate" onClick={()=> sendData()} >Generate</button>
        <p></p>
        <img src="/comicpictures.jpg" alt="comic" width="50%" id="comicImage"/>
        </div>
    );
}


export default App;
