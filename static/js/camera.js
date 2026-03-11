const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const capture = document.getElementById("capture");

navigator.mediaDevices.getUserMedia({video:true})
.then(stream=>{
video.srcObject=stream;
})
.catch(err=>{
console.log("Camera error:",err);
});

capture.addEventListener("click",function(){

const context = canvas.getContext("2d");

context.drawImage(video,0,0,320,240);

const image = canvas.toDataURL("image/png");

document.getElementById("captured_image").value=image;

alert("Face Captured");

});