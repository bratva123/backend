#!/usr/bin/python

import commands,cgi


print "Content-Type:text/html"
print ""
mem='50'

print """<html>
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title></title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/simple-sidebar.css" rel="stylesheet">
</head>
<style>
#myProgress {
  width: 100%;
  background-color: #ddd;
}

#myBar {
"""
print "width: "+mem+"%;"
print """
  height: 30px;
  background-color: #4CAF50;
  text-align: center;
  line-height: 30px;
  color: white;
}
* {
    box-sizing: border-box;
}

body {
  margin: 0;
}

/* Style the header */
.header {
    background-color:skyblue;
    padding: 3px;
    text-align: center;
}

/* Style the top navigation bar */
.topnav {
    overflow: hidden;
    background-color:gray;
}

/* Style the topnav links */
.topnav a {
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
    background-color: #ddd;
    color: black;
}

/* Create three equal columns that floats next to each other */
.column {
    float: right;
    width: 33.33%;
    padding: 15px;
}

/* Clear floats after the columns */
.row:after {
    content: "";
    display: table;
    clear: both;
}

/* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media (max-width:600px) {
    .column {
        width: 100%;
    }
}
</style>
<body>

<div class="header">
  <font color="green" size="5px"><h1>YOUR ONLINE DRIVE</h1></font>
  
</div>

<div class="topnav">
  <a href="home.html" name="images">| IMAGES |</a>
  <a href="login.html" name="txt">| TEXT OR DOC |</a>
  <a href="upload.html" name="uploads">| UPLOADS |</a>
</div>

<div class="row">
 <div class="column">
  <h2>| USED |</h2>
<div id="myProgress">
 
"""
web='<div id="myBar">'
print web+""+mem+"</div>"
print """
</div>
</div>
</div>
</body>
</html>"""
