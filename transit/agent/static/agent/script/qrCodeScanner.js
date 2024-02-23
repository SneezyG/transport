

const qrCode = window.qrcode;

const video = document.createElement("video");
const canvasElement = document.getElementById("qr-canvas");
const canvas = canvasElement.getContext("2d");

let scanning = false;

const body = document.querySelector("body");
const dialog = document.querySelector("dialog");
const button = document.querySelector("#draw > button");
const backdrop = document.querySelector("#backdrop");
const scanLine = document.querySelector("#scanning");

/*
// set trip sn in local-storage for testing purpose.
localStorage.setItem("sn", "fa814af1-6daf-47fb-910e-20b3b50e6678");
*/

  
button.addEventListener("click", () => {
    let sn = localStorage.getItem("sn"); 
    if (sn) {
      setTimeout(() => {
        location.assign(`/agent/report/${sn}/`);
      }, 8000)
    }
    dialog.open = true;
    backdrop.style.visibility = 'visible';
    body.style.overflow = 'hidden';
    dialog.style.animationPlayState = "running";
    dialog.addEventListener("animationend", stream)
});

backdrop.addEventListener('click', resetDom)
function resetDom() {
    dialog.open = false;
    backdrop.style.visibility = 'hidden';
    body.style.overflow = 'visible';
    scanLine.style.visibility = "hidden";
    scanLine.style.animationPlayState = "paused";
    // reset dialog animation.
    dialog.style.animation = "none";
    dialog.offsetWidth;
    dialog.style.animation = null;
    
    scanning = false;
    video.srcObject.getTracks().forEach(track => {
      track.stop();
    });
}



function stream() {
  navigator.mediaDevices
    .getUserMedia({ video: { facingMode: "environment"}})
    .then(function(stream) {
      scanning = true;
      scanLine.style.visibility = "visible";
      scanLine.style.animationPlayState = "running";
      video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
      video.srcObject = stream;
      video.play();
      tick();
      scan();
    });
}


function tick() {
  canvasElement.height = video.videoHeight;
  canvasElement.width = video.videoWidth;
  canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);

  scanning && requestAnimationFrame(tick);
}



function scan() {
  try {
    qrcode.decode();
  } catch (e) {
    setTimeout(scan, 300);
  }
}



qrCode.callback = (res) => {
  if (res) {
    console.log(res);
    localStorage.setItem("sn", res);
    location.assign(`/agent/report/${res}/`);
    resetDom();
  }
}

