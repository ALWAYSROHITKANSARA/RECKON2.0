<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/webcamjs/1.0.25/webcam.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" />

<link href="style/style.css" rel="stylesheet" />
</head>
<body>
<div class="center">
<div class="slider">TALKING HAND</div>
<form method="post" action="storeimage.php">
<div class="box">
<div id="my_camera"></div>
<br>
<input type=button value="Click" onClick="take_snapshot()" class="buttom">
<input type="hidden" name="image" class="image-tag">
</div>
<div class="box2">
<div id="results">Your captured image will appear here...</div>
</div>
<input type="text" class="text" >
</div>

<script language="JavaScript">
Webcam.set({
width: 500,
height: 400,
image_format: 'jpeg',
jpeg_quality: 90
});
Webcam.attach( '#my_camera' );
function take_snapshot() {
Webcam.snap( function(data_uri) {
$(".image-tag").val(data_uri);
document.getElementById('results').innerHTML = '<img src="'+data_uri+'"/>';
} );
}
</script>
</body>
</html>
