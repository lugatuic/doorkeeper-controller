<?php

    function verifyUser()
    {
        $uin = $_POST['UIN'];
        $servername = "localhost";
        $username = "";
        $password = "";
        $dbname = "";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        } 
    
        //query the SQL DB for the users uin, and check if they're allowed in.
        $sql = "SELECT uin, status FROM user WHERE uin=$uin AND status=1";
        $result = $conn->query($sql);

        // if the user is allowed in.
        if($result->num_rows >=1){
            return 1;
        }
        return 0;
}

echo verifyUser();
?>
