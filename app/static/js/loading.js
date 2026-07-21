const messages = [
    "Checking phishing patterns...",
    "Scanning scam keywords...",
    "Analyzing financial fraud...",
    "Calculating risk score...",
    "Generating AI report..."
];

let currentMessage = 0;
let interval;

function showLoading(){

    document.getElementById("loadingOverlay").style.display="flex";

    currentMessage=0;

    document.getElementById("loadingStatus").innerHTML=messages[0];

    interval=setInterval(function(){

        currentMessage++;

        if(currentMessage<messages.length){

            document.getElementById("loadingStatus").innerHTML=messages[currentMessage];

        }

    },900);

}

function hideLoading(){

    clearInterval(interval);

    document.getElementById("loadingOverlay").style.display="none";

}