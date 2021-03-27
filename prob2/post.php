
<?php 
 session_start();include('connection.php');
 if(empty($_SESSION["username"]))
 {
 	 header("Location:index1.php");
 }
?>


<!DOCTYPE html>
<html>
<head>
	<title>
		UGAC 
	</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="https://unpkg.com/bootstrap-table@1.18.1/dist/bootstrap-table.min.css" rel="stylesheet">
	<style type="text/css">
		
	</style>
	
</head>
<body>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="margin-bottom: 30px;">
      <a class="navbar-brand" style="color: white" >UGAC Forum</a>
      <ul class="navbar-nav ml-auto">
           
            <li class="nav-item">
                <a style="color:white;" class="nav-link" href="logout.php">Logout</a>
            </li>
        </ul>
      
    </nav>
    <div style="margin-left: 20px;">
	<div style="text-align:left;">
		<button style="background-color: #343a40 ; ">
			<a style="text-decoration: none;color:white;border:none;" href="login.php">Back</a>
		</button>
	</div>
	

	<p class="heading">
		<?php 

		echo '<div style="text-align:center;font-size:2em;"><strong>' . $_SESSION["title"] . '</strong></div>';
		echo "<br>";
		echo '<div style="text-align:center;">' . $_SESSION["cont"] . '</div>';
		?>
	</p>

	<div style="margin-left:30px;margin-right: 30px;margin-top:50px;">
		
		<form formaction="post.php" method="POST">
			<textarea style="width:60%;" name="area" required></textarea>
			
			<div>
				<button name="comment">
					Add Comment
				</button>

			</div>
			<br>
		</form>
		
		<?php
			$title=$_SESSION["title"];
			$user = $_SESSION["username"];

			if(isset($_POST['comment']))
			{
  				extract($_POST);
  				$area = $_POST['area'];
  				if($area){
	  				$sql="INSERT INTO Comments(Post,writer,comment) VALUES('$title', '$user','$area')";  
	                $result=mysqli_query($con,$sql);
	                if($result){ 
	                    echo"Added comment";

	                } 
	                else {  
	                    echo "Failure!";  
	                }
            	}

			}

			?>
			<h3>Comments:</h3>
			<?php
			$sql = "select * from Comments where Post = '$title'";  
			$result = mysqli_query($con, $sql);   
			$num = mysqli_num_rows($result);  
			$row  = mysqli_fetch_all($result);
			$_SESSION["comms"]=$row;
			If($num>0){
                    $i=0;
                    while($i<$num){
                        echo "<hr><p>Writer: <strong>" . $_SESSION["comms"][$i][1] . "</strong></p>";
                        echo "<p>Comment: " . $_SESSION["comms"][$i][2] . "</p>";
                        
                        echo "<p></p>";
                        $i=$i+1;
                    }
                   echo "<hr>"; 
                }
                else{
                    echo"No Comments found";
                }

          
		?>

	</div>
</div>

</body>
</html>