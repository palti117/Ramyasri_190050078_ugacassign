<?php session_start();include('connection.php');
?>
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link href="https://unpkg.com/bootstrap-table@1.18.1/dist/bootstrap-table.min.css" rel="stylesheet">
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
<?php      
    

 
     // if(!isset($_POST['login']))

     // {        

     //    header("Location:index1.php");
        
     // }
     // else if(empty($_SESSION["username"])){
     //     header("Location:index1.php");
     // }
    
     

    $sql2 = "select * from posts";  
    $result2 = mysqli_query($con, $sql2);  
    $row2  = mysqli_fetch_all($result2); 
    $num = mysqli_num_rows($result2);
    if(isset($_POST['login'])){
    $username = $_POST['user'];  
    $password = $_POST['pass'];  
      
        //to prevent from mysqli injection  
        $username = stripcslashes($username);  
        $password = stripcslashes($password);  
        $username = mysqli_real_escape_string($con, $username);  
        $password = mysqli_real_escape_string($con, $password);  
      
        $sql = "select * from login where username = '$username' and password = '$password'";  
        $result = mysqli_query($con, $sql);   
        $count = mysqli_num_rows($result);  
        $row  = mysqli_fetch_array($result);

        if($count == 1){  
            
            $_SESSION["username"] = $row['username'];
            $_SESSION["name"]=$row['name']; 
             $_SESSION["posts"]=$row2;
            //header("Location: home.php");
        } 


        else{  
              
            //unset($_SESSION["username"]);
            //unset($_SESSION["name"]);
            
            header("Location:index1.php");
        
        } 
    }
        
            
      if(empty($_SESSION["username"])){
        header("Location:index1.php");
    }  
           
?>
        
       <div style="margin-left: 20px;">
        <p><b>Welcome </b><?php echo $_SESSION["username"] ?></p>
        <hr>
        <?php
            if($result2){
               
                If($num>0){
                    $i=0;
                    while($i<$num){
                        echo "Post name: <strong>" . $_SESSION["posts"][$i][0] . "</strong><br>";
                        $page = strval($i) . ".php";
                        echo "<span>Content: " . $_SESSION["posts"][$i][1] . "</span>";
                        
                       
                        ?>
                        <div style="margin-top: 5px;">
                            <form action="login.php" method="POST">
                                <input type="submit" name="Read" value="Read:<?php echo $i+1;?>">
                            </form>
                            <hr>
                           <?php 
                                if(isset($_POST['Read']))
                                {
                                    extract($_POST);
                                    $val = $_POST['Read']; 
                                    $val = (int) substr($val, 5); 
                                    $val = $val -1;
                                    $_SESSION["posts"]=$row2;
                                    $_SESSION["title"]=$_SESSION["posts"][$val][0];
                                    $_SESSION["cont"]=$_SESSION["posts"][$val][1];
                                    header("Location:post.php");

                                }
                           ?>
                        </div>
                        <?php
                        
                        echo "<p></p>";
                        $i=$i+1;
                    }
                    
                }
                else{
                    echo"no results found";
                }

            }

        ?>
    </div>

        
</body>
</html>