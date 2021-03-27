
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
    
    <div style="margin-left:30px;">
        <h1>Login Here</h1>
        <form name="f1" action = "login.php" method = "POST">
            <div>
                <strong>Username:</strong>
                <input style="margin-left: 20px;" type="text" name="user" placeholder ="Enter Username" required>
            </div>
            
            <div style="margin-top:20px;">
                <strong>Password:</strong>
                <input style="margin-left: 24px;" type="password" name="pass" placeholder="Enter Password" required>
            </div>
            
            <div style="margin-top:10px;margin-left: 200px;margin-bottom: 20px;">
                <input style="background-color: #343a40;color:white; " type="submit" name="login" value="Login">
            </div>
            
            
            <h5>Don't have an account? <button style="background-color: #343a40; "><a style="text-decoration: none;color:white;border:none;" href="signup.php">Signup</a></button></h5>
        </form>
        <?php
            if(!empty($_SESSION["message"])){
                echo $_SESSION["message"];
            }
        ?>
        
    </div>

</body>
</head>
</html>