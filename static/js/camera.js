const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({ video: true })
.then(function(stream) {
    video.srcObject = stream;
})
.catch(function(error) {
    console.log("Camera error:", error);
});
function capture(){

const video = document.getElementById("video");
const canvas = document.getElementById("canvas");

canvas.width = video.videoWidth;
canvas.height = video.videoHeight;

const ctx = canvas.getContext("2d");

ctx.drawImage(video,0,0);

const image = canvas.toDataURL("image/png");

fetch("/voting/verify/",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({image:image})
})
.then(res=>res.json())
.then(data=>{
alert(data.message);
});

}