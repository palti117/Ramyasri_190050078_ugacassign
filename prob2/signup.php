<!DOCTYPE html>
<html>
<head>
    <title>UGAC</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="https://unpkg.com/bootstrap-table@1.18.1/dist/bootstrap-table.min.css" rel="stylesheet">
</head>
<body>
     <nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="margin-bottom: 30px;">
      <a class="navbar-brand" style="color: white" >UGAC Forum</a>
      
      
    </nav>
    
    <div style="margin-left: 20px;">
        <h1>SignUp Here!</h1>
        <form method="POST" action="">
            <div  style="margin-top:20px;">
                <strong>Name:</strong>
                <input style="margin-left: 40px;" type="text" name="name" placeholder ="Enter Name" required>
            </div>
            <div  style="margin-top:20px;">
               <strong>Username:</strong>
               <input style="margin-left: 10px;" type="text" name="user" placeholder ="Enter Username" required>
                
            </div>
            <div  style="margin-top:20px;">
                <strong>Password:</strong>
                <input style="margin-left: 15px;" type="password" name="pass" placeholder="Enter Password" required>
            </div>
            
            <div style="margin-top:10px;margin-left: 200px;margin-bottom: 10px;">               
                <input style="background-color: #343a40;color:white; "  type="submit" name="submit" value="SignUp">
            </div>
        </form>
        <br>
        <p>Already have account? <button style="background-color: #343a40 ; "><a style="text-decoration: none;color:white;border:none;" href="index1.php">Login</a></button></p>
    </div>
   
    <?php 

    if(isset($_POST["submit"])){  
        if(!empty($_POST['user']) && !empty($_POST['pass'])) {  
            $user=$_POST['user'];  
            $pass=$_POST['pass'];  
            $name = $_POST['name'];
            $con=mysqli_connect('localhost:3306','root','','users') or die(mysqli_error());  
           
            $query="SELECT * FROM login WHERE username='".$user."'"; 
            $answer=mysqli_query($con,$query);
            $numrows=mysqli_num_rows($answer);  
            if($numrows==0){  
                $sql="INSERT INTO login(name,username,password) VALUES('$name', '$user','$pass')";  
                $result=mysqli_query($con,$sql);  
                if($result){ 
                    echo"Registered successfully with username $user, Login for home page";

                } 
                else {  
                    echo "Failure!";  
                }  
          
            }
            else {  
                echo "That username already exists! Please try again with another.";  
            }  
          
        }
        else {  
            echo "All fields are required!";  
        }  
    }  
    ?>  

</body>  
</html> 